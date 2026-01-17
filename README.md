
# RAM Crysis Analyzer - Local Scaffold (RAM-only)

Este repositorio es un *scaffold* listo para usar que crea:
- Frontend (React + Vite) - minimal, listo para desarrollo.
- Backend (FastAPI) - incluye API, modelos SQLite y un scraper simple "RAM-only".
- GitHub Actions workflow que ejecuta el scraper diariamente y sube resultados a Cloudflare KV (ejemplo).
- Instrucciones para ejecutar localmente y desplegar.

**Nota:** El scraper incluido es un ejemplo sencillo que toma datos "demo" o intenta hacer scraping básico.
Para scraping real (Amazon, Newegg, MercadoLibre) necesitás adaptar selectores, usar Playwright y respetar términos de uso.

---

## Estructura creada

```
ram-crysis-analyzer/
├─ frontend/
│  ├─ package.json
│  ├─ index.html
│  └─ src/
│     ├─ main.jsx
│     ├─ App.jsx
│     └─ components/
│        ├─ ProductCard.jsx
│        └─ ProductDetail.jsx
├─ backend/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ api.py
│  │  ├─ db.py
│  │  ├─ models.py
│  │  ├─ scrapers/
│  │  │  └─ ram_scraper.py
│  │  └─ tasks.py
│  └─ requirements.txt
├─ .github/
│  └─ workflows/
│     └─ daily_scrape.yml
└─ README.md
```

## Qué hace ya implementado
- Backend FastAPI con endpoint `/api/products` que devuelve productos RAM desde la base SQLite.
- `backend/app/scrapers/ram_scraper.py` contiene:
  - `scrape_demo()` que genera datos demo.
  - `scrape_from_url(url)` ejemplo de scraping con BeautifulSoup (válido para páginas simples).
- Workflow de GitHub Actions que ejecuta `python backend/app/scrapers/run_scraper.py` (script incluido) diariamente y sube a Cloudflare KV si configurás secretos.

## Cómo usar localmente (resumen rápido)

### Backend
```bash
cd ram-crysis-analyzer/backend
python -m venv .venv
source .venv/bin/activate    # o .venv\Scripts\activate en Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
# API: http://127.0.0.1:8000/api/products
```

### Frontend (dev)
```bash
cd ram-crysis-analyzer/frontend
npm ci
npm run dev
# Frontend en http://localhost:5173 (Vite)
```

### Ejecutar scraper localmente (demo)
```bash
cd ram-crysis-analyzer/backend/app/scrapers
python run_scraper.py
# Esto crea/actualiza la DB local y muestra lo subido (demo).
```

---

## Siguientes pasos sugeridos
1. Adaptar `scrapers/ram_scraper.py` para cada tienda (selectores correctos / Playwright).
2. Configurar Cloudflare y guardar `CF_ACCOUNT_ID`, `CF_KV_NAMESPACE`, `CF_API_TOKEN` como secrets en GitHub.
3. Revisar limites y legalidad de scraping para cada sitio.
