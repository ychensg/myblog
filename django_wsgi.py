#!/root/python-env/django/bin/python
# coding: utf-8

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
