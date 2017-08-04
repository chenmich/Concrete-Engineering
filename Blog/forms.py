from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class Editor(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    text = TextAreaField("text",         
        id="target-editor-twitter", validators=[DataRequired()])
    tags = StringField("tags", validators=[DataRequired()])
    draft = BooleanField("draft", default=False)
    submit = SubmitField("submit")
