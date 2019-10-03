# Akai manager - python

## How to install
1. Download repo, 
2. Initialize virtual environment in it: `python -m venv venv`,
3. Run that venv: `source venv/bin/activate`,
4. Install dependencies: `pip install -r requirements.txt`,
5. Install frontend dependencies: `npm install`
6. Compile frontend assets: `npm run dev`,
7. (optional) Change database settings in settings.py if you want to use different db backend, 
8. Migrate database: `python manage.py migrate`,
9. To run dev server: `python manage.py runserver`
