from flask import Blueprint

rest_api = Blueprint('/api/v1', __name__)

from trade_platform.views import *