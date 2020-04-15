from datetime import datetime
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from webapp import db
from webapp.user.forms import LoginForm, RegistrationForm, EditProfileForm
from webapp.user.models import User

from flask import Blueprint


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('user.login'))
    return render_template('user/register.jinja', title='Register', form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('user.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home.index')
        return redirect(next_page)
    return render_template('user/login.jinja', title='Авторизация', form=form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))


@blueprint.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    tracks = [
        {'author': user, 'title': 'Test track #1'},
        {'author': user, 'title': 'Test track #2'}
    ]
    return render_template('user/user.jinja', user=user, tracks=tracks)


@blueprint.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.full_name = form.full_name.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Изменения сохранены.')
        return redirect(url_for('user.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.full_name.data = current_user.full_name
        form.about_me.data = current_user.about_me
    else:
        flash('Пожалуйста, выберите другое имя.')
    return render_template('user/edit_profile.jinja', title='Edit Profile', form=form)


@blueprint.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You can not follow yourself!')
        return redirect(url_for('user.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user.user', username=username))


@blueprint.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user.user', username=username))
