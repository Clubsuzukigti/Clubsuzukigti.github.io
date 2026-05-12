# Suzuki GTi Car Club — Sitio Web

[![Deploy](https://github.com/Clubsuzukigti/suzukigti.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/Clubsuzukigti/suzukigti.github.io/actions/workflows/deploy.yml)

**Sitio en vivo:** https://suzukigti.github.io

Archivo técnico, repuestos y comunidad mundial del Suzuki Swift GTi / Cultus GTi / Forsa GTi / Swift GT.

> Preservando el legado del Suzuki Swift GTi · Preserving the Suzuki Swift GTi legacy

## 📁 Estructura

```
sitio-web/
├── docs/                       # Contenido Markdown (ES + EN)
│   ├── index.md                # Landing en español
│   ├── index.en.md             # Landing en inglés
│   ├── historia/               # Historia del modelo
│   ├── reparaciones/           # Guías de reparación
│   ├── modificaciones/         # Modificaciones y tuning
│   ├── manuales/               # Manuales con gating
│   ├── repuestos/              # Repuestos mundiales
│   ├── garage/                 # Autos del club
│   ├── comunidad/              # Comunidad Facebook/YouTube/Telegram
│   ├── blog/                   # Blog del club
│   └── assets/                 # Imágenes, logos, CSS
├── overrides/                  # Customizaciones tema
├── mkdocs.yml                  # Config principal
├── requirements.txt            # Dependencias Python
└── .github/workflows/deploy.yml # Deploy automático a GitHub Pages
```

## 🚀 Desarrollo local

### Setup (una sola vez)
```bash
python -m venv .venv
.venv\Scripts\activate         # Windows
# o: source .venv/bin/activate # Mac/Linux
pip install -r requirements.txt
```

### Servidor con live reload
```bash
mkdocs serve
```
Abre http://127.0.0.1:8000

### Build de producción (para verificar antes de push)
```bash
mkdocs build --clean --strict
```

## 🌐 Idiomas

Bilingüe **Español (default) + Inglés** usando `mkdocs-static-i18n` en modo `suffix`:
- `historia/index.md` (español)
- `historia/index.en.md` (inglés)

Si una página `.en.md` no existe, el sitio muestra el fallback en español con un aviso.

## ✏ Cómo contribuir

### Si sabes Git
1. Fork del repo
2. Crea tu rama: `git checkout -b mi-aporte`
3. Edita archivos Markdown
4. `mkdocs serve` para preview
5. Commit + push + Pull Request

### Si no sabes Git
- Postea en el [grupo Telegram](https://t.me/suzukigti) (link próximamente)
- Un admin convertirá tu aporte en página

## 📦 Stack técnico

- **Generator:** [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- **i18n:** [mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n)
- **Lightbox:** [mkdocs-glightbox](https://github.com/blueswen/mkdocs-glightbox)
- **Hosting:** GitHub Pages (gratis ilimitado)
- **CI/CD:** GitHub Actions (deploy automático en push a main)
- **Dominio:** suzukigti.github.io

## 📄 Licencia

- **Código fuente:** MIT License
- **Contenido (texto + imágenes originales):** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Manuales originales Suzuki:** Copyright Suzuki Motor Corporation 1990-2003 — preservados para uso histórico y restauración

## 👥 Admins

- **Fernando** (admin principal) — ferpezlro@gmail.com
- Más admins se agregarán conforme crezca el club

## 🔗 Enlaces

- 🌐 [Sitio web](https://suzukigti.github.io)
- 📘 [Facebook: Suzuki Lifestyle](https://www.facebook.com/suzukilifestyle)
- 💬 [Telegram del Club](https://t.me/suzukigti) (próximamente)
- 🐙 [GitHub Org](https://github.com/Clubsuzukigti)
