"""Blueprint for api"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from .blogs import *
from .experts import *
from .meals import *
from .plans import *
from .reviews import *
from .users import *
