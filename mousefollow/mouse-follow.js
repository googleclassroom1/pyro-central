document.addEventListener('mousemove', function(e) {
    const freddy = document.getElementById('freddy');
    if (freddy) {
        freddy.style.backgroundImage = 'url("/images/cursor.png")';
        freddy.style.backgroundSize = 'contain';
        freddy.style.backgroundRepeat = 'no-repeat';
        freddy.style.left = (e.clientX - freddy.offsetWidth / 2) + 'px';
        freddy.style.top = (e.clientY - freddy.offsetHeight / 2) + 'px';
    }
});
