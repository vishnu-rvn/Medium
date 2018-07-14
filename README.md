# Medium
A mini blog.

### Techs Used
*Python
*Flask
*CSS
*Javascript
*HTML5

##### Have some better ideas? Or got a cool feature to implement? Fork this.
##### To run it in your local:
Download or clone it into your local directory.
Open the terminal and type in the codes(if you're deleting the db details and creating your own data), This will start the app with an empty database
```python
>>> from medium import db
>>> db.create_all()
>>> db.session.commit()
```
Now:
```python
>>> python run.py
```
and hit enter. Launch a browser.
```sh
127.0.0.1:5000
```
and you're good to go.

# TODO
[x] Basic authentication
[x] Posts
[x] Post View
[ ] Comments Section
[ ] Profile view
[ ] CRUD Posts
[ ] CRUD Comments
