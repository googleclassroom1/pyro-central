document.addEventListener('mousemove', function(e) {
    const freddy = document.getElementById('freddy');
    if (freddy) {
        freddy.style.left = e.pageX + 'px';
        freddy.style.top = e.pageY + 'px';
    }
});
