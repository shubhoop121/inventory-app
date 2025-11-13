import sqlite3
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'inventory.db') # Saves DB inside the mounted Docker volume

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists('/data'):
        os.makedirs('/data')
    conn = get_db_connection()
    # Create tables if they don't exist
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            threshold INTEGER DEFAULT 10
        );
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS inventory (
            product_id INTEGER,
            location_id INTEGER,
            quantity INTEGER DEFAULT 0,
            PRIMARY KEY (product_id, location_id),
            FOREIGN KEY(product_id) REFERENCES products(id),
            FOREIGN KEY(location_id) REFERENCES locations(id)
        );
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            location_id INTEGER,
            type TEXT,
            qty_change INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    
    # Seed Initial Data (Only if empty)
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM products")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO products (sku, name, threshold) VALUES ('TS-RED', 'Red T-Shirt', 10), ('MUG-01', 'Office Mug', 25)")
        cur.execute("INSERT INTO locations (name) VALUES ('Main Warehouse'), ('Storefront')")
        cur.execute("INSERT INTO inventory (product_id, location_id, quantity) VALUES (1, 1, 100), (2, 1, 50)")
        conn.commit()
    conn.close()

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dashboard')
def get_dashboard():
    conn = get_db_connection()
    # Get simplified inventory list
    inventory = conn.execute('''
        SELECT p.sku, p.name as product, l.name as location, i.quantity, p.threshold 
        FROM inventory i
        JOIN products p ON i.product_id = p.id
        JOIN locations l ON i.location_id = l.id
    ''').fetchall()
    
    # Get master lists for dropdowns
    products = conn.execute('SELECT * FROM products').fetchall()
    locations = conn.execute('SELECT * FROM locations').fetchall()
    
    conn.close()
    return jsonify({
        'inventory': [dict(ix) for ix in inventory],
        'products': [dict(p) for p in products],
        'locations': [dict(l) for l in locations]
    })

@app.route('/api/transaction', methods=['POST'])
def add_transaction():
    data = request.json
    pid = data['product_id']
    lid = data['location_id']
    qty = int(data['quantity'])
    t_type = data['type'] # 'IN' or 'OUT'

    conn = get_db_connection()
    try:
        # Check current stock
        cur = conn.cursor()
        cur.execute("SELECT quantity FROM inventory WHERE product_id = ? AND location_id = ?", (pid, lid))
        row = cur.fetchone()
        current_qty = row['quantity'] if row else 0

        # Calculate new quantity
        change = qty if t_type == 'IN' else -qty
        new_qty = current_qty + change

        if new_qty < 0:
            return jsonify({'error': 'Insufficient stock'}), 400

        # Update or Insert Inventory
        cur.execute("""
            INSERT INTO inventory (product_id, location_id, quantity) 
            VALUES (?, ?, ?) 
            ON CONFLICT(product_id, location_id) 
            DO UPDATE SET quantity = ?
        """, (pid, lid, new_qty, new_qty))

        # Log Transaction
        cur.execute("INSERT INTO transactions (product_id, location_id, type, qty_change) VALUES (?, ?, ?, ?)",
                    (pid, lid, t_type, change))
        
        conn.commit()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)