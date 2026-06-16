# ElectroShop — Django Ecommerce (Learning Project)

Lightweight Django-based ecommerce demo used for learning and demonstrations.

## Features
- Product listing, detail, create, update and delete views
- Simple product reviews
- Admin site for managing models
- Templates under `products/templates/products`

## Prerequisites
- Python 3.10+ (you are using 3.14 in this environment)
- pip
- virtualenv (recommended)

## Quickstart
1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies. If a `requirements.txt` exists, use it; otherwise install Django:

```bash
pip install -r requirements.txt  # if present
pip install Django==6.0.6         # fallback if no requirements file
```

3. Apply migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/products/ to view the product list and http://127.0.0.1:8000/admin/ for the admin site.

## Templates and Static files
- Project-level templates are in the `templates/` folder; app templates live under `products/templates/products/`.
- Static assets are served from `static/` during development (see `STATICFILES_DIRS` in settings).

## Useful commands
- Run Django system checks:

```bash
python manage.py check
```

- Create migrations (after changing models):

```bash
python manage.py makemigrations
python manage.py migrate
```

## Project Structure (selected)
- `manage.py` — Django CLI entry
- `ecommerce/` — project settings and URL config
- `products/` — app with models, views, templates
- `templates/` — base templates (e.g., `base.html`)

## Notes
- Debug is enabled in settings for development. Set `DEBUG = False` and configure `ALLOWED_HOSTS` before deploying.
- Media file serving is configured for development only. For production, use proper storage/backends.

## Contributing
Feel free to open issues or submit pull requests for improvements.

## License
This repository does not include a license file. Add one if you plan to publish or share publicly.
