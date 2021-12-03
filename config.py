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
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456789abcdfghijklmopqrrstuvwxyz'
    PROJECT_CTX = os.path.dirname(os.path.abspath(__file__))
    RES_FOLDER = f'{PROJECT_CTX}{os.sep}index{os.sep}res{os.sep}'
