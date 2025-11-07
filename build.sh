#!/bin/bash
pip install -r requirements.txt
python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netball_system.settings'); print('Dependencies installed')"
python manage.py collectstatic --noinput
