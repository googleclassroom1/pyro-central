documentdocument.addEventListener('mousemove', function(e) {
    const freddy = document.getElementById('freddy');
    if (freddy) {
        freddy.style.left = (e.clientX - freddy.offsetWidth / 2) + 'px';
        freddy.style.top = (e.clientY - freddy.offsetHeight / 2) + 'px';
    }
});
