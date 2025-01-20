document.addEventListener('mousemove', function(e) {
    const freddy = document.getElementById('freddy');
    if (freddy) {
        freddy.style.left = (e.pageX - freddy.offsetWidth / 2) + 'px';
        freddy.style.top = (e.pageY - freddy.offsetHeight / 2) + 'px';
    }
});
