from flask import Blueprint
from flask import render_template
from flask_login import login_required

blueprint = Blueprint('home', __name__, url_prefix='')


@blueprint.route('/')
@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.jinja', title='Главная')
