"""
File         : __init__.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 02-Dec-2021
"""

from flask import Flask
from config import Config


# ---------------------------------------------------------------------------------------------------------------------

app = Flask(__name__)
app.config.from_object(Config)


# ---------------------------------------------------------------------------------------------------------------------

from index import routes
