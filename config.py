"""
File         : config.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 02-Dec-2021
"""

import os


# ---------------------------------------------------------------------------------------------------------------------

class Config(object):

    RELEASE_VERSION = '1.0.0'
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456789abcdfghijklmopqrrstuvwxyz'
