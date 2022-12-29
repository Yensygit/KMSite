import os
import sys
import platform
#путь к проекту, там где manage.py
sys.path.insert(0, '/home/c/cx71361/KMgroup/public_html/KMgroup')
#путь к фреймворку, там где settings.py
sys.path.insert(0, '/home/c/cx71361/KMgroup/public_html/KMgroup/KMgroup')
#путь к виртуальному окружению myenv
sys.path.insert(0, '/home/c/cx71361/KMgroup/venv/lib/python{0}/site-packages'.format(platform.python_version()[0:3]))
#sys.path.insert(0, '/home/c/cx71361/KMgroup/venv/lib/python3.9/site-packages')
os.environ["DJANGO_SETTINGS_MODULE"] = "KMgroup.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()