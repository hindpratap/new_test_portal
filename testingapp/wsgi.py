"""
WSGI config for testingapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
#
# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testingapp.settings')
#
# application = get_wsgi_application()


import os
import sys


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testingapp.settings')
sys.path.append('/home/raghav/home/raghav/testingapp/testingapp/')

sys.path.append('/home/raghav/home/raghav/testingapp/venv/lib/python3.7/site-packages')
application = get_wsgi_application()
