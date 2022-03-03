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
        from config.commands import create_db, create_api
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    is_custom_cmd = False

    try:
        if sys.argv[1] == 'create-db':
            is_custom_cmd = True
            create_db(sys.argv[2])
        elif sys.argv[1] == 'create-api':
            is_custom_cmd = True
            if len(sys.argv) == 3:
                create_api(sys.argv[2])
            else:
                create_api(sys.argv[2], list(sys.argv[3:]))
    except:
        pass

    if not is_custom_cmd:
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
