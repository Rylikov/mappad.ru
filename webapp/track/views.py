from flask import Blueprint, request, current_app
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from webapp import db
from webapp.track.forms import AddTrackForm
from webapp.track.models import Track

blueprint = Blueprint('track', __name__, url_prefix='/tracks')


@blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def add_track():
    title = 'Добавить GPS трек'
    form = AddTrackForm()
    if form.validate_on_submit():
        track = Track(
            title=form.title.data,
            author=current_user,
            description=form.description.data,
            raw_gpx=form.rawgpx.data
        )
        db.session.add(track)
        db.session.commit()
        flash('GPX трек сохранен.')
        return redirect(url_for('track.my_tracks'))
    return render_template('track/addtrack.jinja', page_title=title, form=form)


@blueprint.route('/my')
@login_required
def my_tracks():
    title = 'Мои GPS треки'
    page = request.args.get('page', 1, type=int)
    tracks = current_user.tracks.order_by(Track.timestamp.desc()).paginate(
        page, current_app.config['TRACKS_PER_PAGE'], False)
    next_url = url_for('track.my_tracks',
                       page=tracks.next_num) if tracks.has_next else None
    prev_url = url_for('track.my_tracks',
                       page=tracks.prev_num) if tracks.has_prev else None

    return render_template('track/my_tracks.jinja', page_title=title,
                           tracks=tracks.items, next_url=next_url,
                           prev_url=prev_url)


@blueprint.route('/last')
@login_required
def last_tracks():
    title = 'Новые GPS треки'
    tracks = Track.query.order_by(Track.timestamp.desc()).limit(
        current_app.config['TRACKS_PER_PAGE']).all()
    return render_template('track/last_tracks.jinja', page_title=title, tracks=tracks)
