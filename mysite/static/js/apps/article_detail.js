'use strict';

// Toggle comment modal window
const commentModal = document.getElementById('commentModal');
const commentModalToggler = document.getElementById('commentModalToggler');
const newCommentBtn = document.getElementById('newCommentBtn');

function ToggleCommentModal() {
    commentModal.classList.toggle('show');
}

commentModalToggler.onclick = ToggleCommentModal;
newCommentBtn.onclick = ToggleCommentModal;