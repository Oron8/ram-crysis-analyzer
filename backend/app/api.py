
from fastapi import APIRouter, Depends
from .db import SessionLocal
from .models import Product, PriceEntry
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/products')
def list_products(db: Session = Depends(get_db)):
    prods = db.query(Product).all()
    out = []
    for p in prods:
        # aggregate prices by last entries per site
        site_map = {}
        for e in p.entries:
            site_map.setdefault(e.site, []).append({'date': e.date.strftime('%Y-%m-%d'), 'price': e.price})
        # transform to a recharts-friendly array merging dates (simple approach)
        prices = []
        # for demo, just return site_map directly
        out.append({
            'id': p.id,
            'name': p.name,
            'brand': p.brand,
            'type': p.type,
            'size': p.size,
            'image': p.image,
            'prices_by_site': site_map
        })
    return out
