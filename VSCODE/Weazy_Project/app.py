from flask import Flask, render_template, request, jsonify
import sqlite3
import requests
import os
from utils.image_utils import make_square

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

UNSPLASH_API_KEY = 'xsdj44454emq3q3q7w4346efewd90'

def get_db_connection():
    conn = sqlite3.connect('db/products.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products WHERE image_url IS NULL").fetchall()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/search_images', methods=['POST'])
def search_images():
    product_name = request.json.get('product_name')
    url = f'https://api.unsplash.com/search/photos?query={product_name}&client_id={UNSPLASH_API_KEY}'
    res = requests.get(url).json()
    image_urls = [img['urls']['small'] for img in res.get('results', [])[:5]]
    return jsonify({'images': image_urls})

@app.route('/save_image', methods=['POST'])
def save_image():
    image_url = request.json['image_url']
    product_id = request.json['product_id']

    # Download image
    img_data = requests.get(image_url).content
    raw_path = os.path.join(UPLOAD_FOLDER, f'{product_id}_raw.jpg')
    with open(raw_path, 'wb') as f:
        f.write(img_data)

    # Make square and save
    final_path = os.path.join(UPLOAD_FOLDER, f'{product_id}.jpg')
    make_square(raw_path, final_path)

    # Update DB
    conn = get_db_connection()
    conn.execute("UPDATE products SET image_url = ? WHERE id = ?", (final_path, product_id))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success', 'image_path': final_path})

if __name__ == '__main__':
    app.run(debug=True)
