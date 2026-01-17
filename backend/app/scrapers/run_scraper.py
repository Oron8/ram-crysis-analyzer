import sys
from pathlib import Path

# Agrega /backend al path para que funcionen los imports
BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from app.db import SessionLocal
from app.models import Product, PriceEntry
from app.scrapers.ram_scraper import scrape_demo
from datetime import datetime

def ensure_product(db, item):
    p = db.query(Product).filter(Product.name == item['name']).first()
    if not p:
        p = Product(
            name=item['name'],
            brand=item.get('brand',''),
            type=item.get('type',''),
            size=item.get('size',''),
            image=item.get('image','')
        )
        db.add(p)
        db.commit()
        db.refresh(p)
    return p

def save_data(data):
    db = SessionLocal()
    try:
        for item in data.get('ram', []):
            p = ensure_product(db, item)
            for price in item.get('prices', []):
                entry = PriceEntry(
                    product_id=p.id,
                    site=price.get('site'),
                    price=price.get('price'),
                    date=datetime.utcnow()
                )
                db.add(entry)
        db.commit()
        print("Scrape guardado OK")
    finally:
        db.close()

if __name__ == "__main__":
    data = scrape_demo()
    save_data(data)
