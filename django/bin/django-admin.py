#!/usr/bin/env python
from django.core import management
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    management.execute_from_command_line(['','check'])
