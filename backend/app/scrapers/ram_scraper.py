
# Simple RAM-only scraper example.
# It includes:
# - scrape_demo(): produces demo data
# - scrape_from_url(url): example of extracting title/price/img from a simple page
#
# For real stores (Amazon, Newegg, MercadoLibre) you'll need to adapt selectors
# and probably use Playwright to avoid blocks.

import requests
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)'}

def scrape_demo():
    """Return demo RAM product list."""
    now = datetime.utcnow().isoformat()
    data = {
        'updated': now,
        'ram': [
            {
                'name': 'Corsair Vengeance DDR5 32GB 6000MHz',
                'brand': 'Corsair',
                'type': 'DDR5',
                'size': '32GB',
                'image': 'https://via.placeholder.com/600x300.png?text=Corsair+VENGEANCE+DDR5',
                'prices': [
                    {'site':'Amazon','price':210.0,'date':now},
                    {'site':'Newegg','price':205.0,'date':now}
                ]
            },
            {
                'name': 'Kingston FURY Beast DDR4 16GB 3200MHz',
                'brand': 'Kingston',
                'type': 'DDR4',
                'size': '16GB',
                'image': 'https://via.placeholder.com/600x300.png?text=Kingston+FURY+DDR4',
                'prices': [
                    {'site':'Amazon','price':70.0,'date':now},
                    {'site':'Newegg','price':68.0,'date':now}
                ]
            }
        ]
    }
    return data

def scrape_from_url(url):
    """Basic example: try to fetch title, first price-like number, image from a generic page.
    This will *not* work for complex JS-rendered pages; it's a simple example.
    """
    r = requests.get(url, headers=HEADERS, timeout=15)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    # Try common patterns
    title = soup.find('h1') or soup.select_one('#productTitle')
    title_text = title.get_text(strip=True) if title else 'unknown'
    # price heuristics: find first element with $ and digits
    price = None
    for el in soup.find_all(text=True):
        if '$' in el and any(ch.isdigit() for ch in el):
            txt = el.strip()
            # crude parse
            num = ''.join([c for c in txt if c.isdigit() or c=='.'])
            try:
                price = float(num)
                break
            except:
                continue
    img = soup.find('img')
    img_src = img['src'] if img and img.has_attr('src') else None
    return {'name': title_text, 'price': price, 'image': img_src}
