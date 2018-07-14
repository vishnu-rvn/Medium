// var delete_form = document.getElementById('delete-form');
// delete_form.addEventListener('submit', deleteItem);

// function deleteItem(e){
// 	e.preventDefault();
// 	var url = delete_form.getAttribute("method");
// 	console.log(url)
// 	var xhttp = new XMLHttpRequest();
// 	xhttp.open('POST', url, true);
// 	xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
// 	xhttp.setRequestHeader('X-CSRFToken', csrf_token);
// 	xhttp.onload = function(){
// 		if(this.status == 200){
// 			location.reload();
// 		} else{
// 			console.log(this.status)
// 			console.log("error")
// 		}
// 	}
// 	xhttp.send();
// }

document.addEventListener('click', (e)=>{
	if(e.target.tagName == 'BUTTON' && e.target.className == 'comment-button'){
		var comment = document.getElementById('comment'+e.target.value);
		if (comment.style.display == 'none') {
			getComments(comment_id=e.target.value);
			comment.style.display = 'block';
		} else if (comment.style.display == 'block') {
			comment.style.display = 'none';
		};
	};
});

function getComments(comment_id){
	var xhttp = new XMLHttpRequest();
	var url = '/post/'+comment_id+'/comments';
	xhttp.open('GET', url, true);
	xhttp.onload = function () {
		if (this.status == 200){
			console.log(JSON.parse(this.responseText));
		} else {
			console.log("error");
			console.log(this.status)
		}
	}
	xhttp.send();
}