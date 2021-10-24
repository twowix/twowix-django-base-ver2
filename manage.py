#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from config.settings.base import SERVER_ENV

def main():
    if SERVER_ENV == 'product':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.product')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.develop')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
