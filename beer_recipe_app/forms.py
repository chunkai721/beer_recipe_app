from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    """User Registration Form."""
    
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    """User Login Form."""
    
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Login')

class RecipeForm(FlaskForm):
    """Recipe Form."""
    
    name = StringField('Recipe Name',
                       validators=[DataRequired(), Length(min=2, max=100)])
    ingredients = TextAreaField('Ingredients',
                                validators=[DataRequired()])
    cost = FloatField('Cost',
                      validators=[DataRequired()])
    submit = SubmitField('Save Recipe')
