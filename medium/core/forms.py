from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from medium.core.models import User


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
	last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("User already exists")

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError("Email already exists")


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')
	remember_me = BooleanField('Remember Me')


class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(), Length(min=1, max=50)])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Post')