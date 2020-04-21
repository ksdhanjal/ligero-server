import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/pi/led_project/method3_ksd/')
from server import app as application
application.secret_key = 'ksd'