
# Script to run the RAM scraper and store results in the local DB (sqlite).
# Usage: python run_scraper.py
import os
import json
from ..db import SessionLocal, engine
from ..models import Product, PriceEntry
from ramcrysis.app.scrapers.ram_scraper import scrape_demo
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# Note: module path adjustments for direct run
try:
    from app.scrapers.ram_scraper import scrape_demo as sd
except Exception:
    from ramcrysis.app.scrapers.ram_scraper import scrape_demo as sd

def ensure_product(db: Session, item):
    # find existing by name+brand+size
    p = db.query(Product).filter(Product.name==item['name']).first()
    if p is None:
        p = Product(name=item['name'], brand=item.get('brand',''), type=item.get('type',''), size=item.get('size',''), image=item.get('image',''))
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
                pe = PriceEntry(product_id=p.id, site=price.get('site'), price=price.get('price'), date=datetime.utcnow())
                db.add(pe)
        db.commit()
        print('Scrape saved to DB.')
    finally:
        db.close()

if __name__ == '__main__':
    data = sd()
    save_data(data)
    print('Done.')
