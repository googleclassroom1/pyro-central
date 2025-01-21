document.addEventListener('mousemove', function(e) {
    const freddy = document.getElementById('freddy');
    if (freddy) {
        console.log('Mouse moved:', e.clientX, e.clientY); // Add this line
        freddy.style.left = (e.clientX - freddy.offsetWidth / 2) + 'px';
        freddy.style.top = (e.clientY - freddy.offsetHeight / 2) + 'px';
    }
});
