from flask import render_template
from flask import Blueprint

bp = Blueprint('routing', __name__, url_prefix='/home')

@bp.route("/")
def Home():
    return render_template("/home/index.html")