# Akai manager - python

## How to install

1. Download repo,
2. Initialize virtual environment in it: `python -m venv venv`,
3. Run that venv: `source venv/bin/activate`,
4. Install dependencies: `pip install -r requirements.txt`,
5. Install frontend dependencies: `npm install`
6. Compile frontend assets: `npm run dev`,
7. Copy akai_manager_python/.settings.py to akai_manager_python/settings.py and fill missing fields
8. (optional) Change database settings in settings.py if you want to use different db backend,
9. Migrate database: `python manage.py migrate`,
10. To run dev server: `python manage.py runserver`

## Fields in .settings.py

- SECRET_KEY
- SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
- SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
- DATABASES
  - PASSWORD
  - USER
