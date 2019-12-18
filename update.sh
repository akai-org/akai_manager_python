virtualenv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python manage.py migrate
npm install
npm run update
./venv/bin/python manage.py collectstatic --noinput --link
./venv/bin/python manage.py import_permissions
