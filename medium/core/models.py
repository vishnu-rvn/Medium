from datetime import datetime
from medium import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	first_name = db.Column(db.String(60), nullable=True)
	last_name = db.Column(db.String(60), nullable=True)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)
	comments = db.relationship('Comments', backref='author', lazy=True)

	def __repr__(self):
		return "{}".format(self.username)

	def name(self):
		return "{} {}".format(self.first_name, self.last_name)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	comments = db.relationship('Comments', backref='post', lazy=True)

	def __repr__(self):
		return "{} {}".format(self.title, self.date_posted)

class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text, nullable=True)
	date_commented = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
