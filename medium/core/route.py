from medium import app, db, bcrypt
from flask import render_template, flash, redirect, url_for, request, jsonify
from medium.core.forms import RegistrationForm, LoginForm, PostForm
from medium.core.models import User, Post, Comments
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/', methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember_me.data)
			return redirect(url_for('home'))
		else:
			flash('Login unsuccessful')
	return render_template("login.html", title='Login', form=form)


@app.route("/register", methods=['POST', 'GET'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('about'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password, 
			first_name=form.first_name.data, last_name=form.last_name.data)
		db.session.add(user)
		db.session.commit()
		flash("Account created for {}".format(form.username.data), 'success')
		return redirect(url_for('login'))
	return render_template("register.html", title='Register', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/home', methods=['POST', 'GET'])
@login_required
def home():
	form = PostForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			post = Post(title=form.title.data, content=form.content.data, author=current_user)
			db.session.add(post)
			db.session.commit()
		return redirect(url_for('home'))
	else:
		posts = Post.query.all()
		return render_template("home.html", posts=posts, form=form)


@app.route('/post/<int:post_id>')
@login_required
def post(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('post.html', post=post)

@app.route('/user/<int:user_id>')
@login_required
def profile(user_id):
	user = User.query.get_or_404(user_id)
	posts = Post.query.filter_by(user_id=user_id)
	return render_template('profile.html', user=user, posts=posts)


@app.route('/post/<int:post_id>/delete', methods=['POST'])
def test_page(post_id):
	print(request.data)
	post = Post.query.get_or_404(post_id)
	db.session.delete(post)
	db.session.commit()
	return jsonify({'Status': 'OK'})

@app.route('/post/<int:post_id>/comments', methods=['GET'])
def comments(post_id):
	comm = []
	comments = Comments.query.filter_by(post_id=post_id)
	for comment in comments:
		user = User.query.get(comment.user_id)
		c = {}
		c['content'] = comment.content
		c['username'] = user.username
		c['post_id'] = comment.post_id
		c['date_comment'] = comment.date_commented
		comm.append(c)
	return jsonify(comm)

@app.route('/post/<int:post_id>/comment_on', methods=['POST'])
def comment_on(post_id):
	pass