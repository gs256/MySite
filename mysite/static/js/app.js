'use strict';

// Toggle mobile navigation
const navToggler = document.getElementById('mobileNavToggler');
const nav = document.getElementById('nav');

navToggler.onclick = function() {
    nav.classList.toggle('show');
}