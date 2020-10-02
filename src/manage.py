#!/usr/bin/env python
"""
    @author : Ujjawal Sinha
    @email : ujjawalsinhacool16021998@gmail.com
    @created at : 2020-09-26 22:26:27
    @desc : Django's command-line utility for administrative tasks.
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
