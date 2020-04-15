from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length


class AddTrackForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()],
                        render_kw={"class": "form-control"})
    description = TextAreaField('Описание', validators=[
                                Length(min=0, max=140)],
                                render_kw={"class": "form-control"})
    rawgpx = HiddenField(validators=[DataRequired()])
    submit = SubmitField('Сохранить', render_kw={"class": "btn btn-primary"})
