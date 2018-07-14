document.addEventListener('click', (e)=>{
	if(e.target.tagName == 'BUTTON' && e.target.className == 'comment-button'){
		var comment = document.getElementById('comment'+e.target.value);
		if (comment.style.display == 'none') {
			getComments(post_id=e.target.value);
			comment.style.display = 'block';
			form = createForm()
			comment.appendChild(form)
		} else if (comment.style.display == 'block') {
			comment.style.display = 'none';
		};
	};
});


function getComments(post_id){
	var xhttp = new XMLHttpRequest();
	var url = '/post/'+post_id+'/comments';
	xhttp.open('GET', url, true);
	xhttp.onload = function () {
		if (this.status == 200){
			var comments = JSON.parse(xhttp.responseText);
			if (comments.length == 0) {
				console.log("no comments")
			} else {
				for (var i = comments.length - 1; i >= 0; i--) {
					comment = addComment(comments[i].username, comments[i].content)
				}
			}
		} else {
			console.log("error");
			console.log(this.status)
		}
	}
	xhttp.send();
}

function addComment (username, content) {
	var comment_box = document.createElement("div");
	comment_box.setAttribute("class", "comment-box flex flex-row flex-align");

	var user = document.createElement("h3");
	user.setAttribute('class', 'user-name')
	user.appendChild(document.createTextNode(username))

	var comment_content = document.createElement("p");
	comment_content.setAttribute('class', 'comment-content')
	comment_content.appendChild(document.createTextNode(content))

	comment_div = document.createElement('div')
	comment_div.appendChild(user)
	comment_div.appendChild(comment_content)

	comment_box.appendChild(comment_div)

	var comment = document.getElementById('comment'+post_id);
	
	return comment;
}

function createForm () {
	var form = document.createElement("form");
	var input = document.createElement("input");
	var submit = document.createElement("input");
	submit.setAttribute("type", "submit");

	form.appendChild(input);
	form.appendChild(submit);

	return form;
};