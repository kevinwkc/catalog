import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.append('/var/www/catalog')
from main import app as application
application.secret_key="tomomi"