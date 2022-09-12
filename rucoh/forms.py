from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields import EmailField
from wtforms.validators import Email, EqualTo, Length, DataRequired


class EmailSend(FlaskForm):
    name = StringField(label="What's yours?", validators=[DataRequired()])
    email = EmailField(label="How about your Email?", validators=[Email(granular_message=True),
                                                                   DataRequired()])
    msg = TextAreaField(label="What's on your Mind?", validators=[Length(2, 30000),
                                                                  DataRequired()])
    submit = SubmitField(label='Submit')
