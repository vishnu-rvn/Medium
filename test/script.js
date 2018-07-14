var btn = document.getElementById('modal-button');
var close_btn = document.getElementById("close-button");
var modal = document.getElementById('modal')

function openModal(argument) {
	modal.style.display = 'block';
}
function closeModal(argument) {
	modal.style.display = 'none';
}
btn.addEventListener('click', openModal);
close_btn.addEventListener('click', closeModal)