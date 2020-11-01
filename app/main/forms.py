from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError
    
    
    
class BlogForm(FlaskForm):    
    blogTitle = StringField('Blog Title',validators=[Required()])
    blogDescription = StringField('Description',validators = [Required()])
    submit = SubmitField('Submit')