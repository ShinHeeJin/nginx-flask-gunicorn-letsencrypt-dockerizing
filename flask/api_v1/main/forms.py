from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TokenizerForm(FlaskForm):
    input_sentence = StringField("문장입력", validators=[DataRequired()])
    submit = SubmitField("submit")