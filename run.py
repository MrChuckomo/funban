"""
File         : run.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 02-Dec-2021
"""

from index import app


# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5050)
