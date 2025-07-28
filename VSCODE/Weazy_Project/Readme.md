# Smart Image Updater

A web-based tool to fetch, crop, and update product images for an e-commerce catalog.

## Features
- List products missing images
- Search and preview images from Unsplash
- Select and crop to 500x500 px
- Save locally and update database

## Setup
1. Install dependencies  
   `pip install -r requirements.txt`

2. Set your Unsplash API key in `app.py`

3. Run the app  
   `python app.py`

4. Open `http://localhost:5000`

## Folder Structure
- `app.py` – Flask app
- `static/uploads/` – Saved images
- `db/products.db` – SQLite sample DB
- `utils/image_utils.py` – Image resizing
