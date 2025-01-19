import os

# List of file paths to concatenate
file_paths = [
    '4-0-4.html', '404.html', 'bor.png', 'nowgg.jpg', 'settings.html', 'SudoUser-Var-{}.html',
    'VS.html', 'aboutus.html', 'apps.html', 'crazygames.jpeg', 'crisp.js', 'dark-jokes.html',
    'dahsboard.html', 'dev.html', 'easteregg.html', 'extra.html', 'forms.html', 'frogarcade.html',
    'games.html', 'images.jpeg', 'ind4x.html', 'index.html', 'kevin hart.html', 'link.txt',
    'linkies.html', 'midload.html', 'notes.txt', 'pricing.html', 'pyro-logo.png', 'signin.html',
    'signup.html', 'testing.html', 'a/calc', 'a/chat', 'app/404.html', 'app/index.js', 'app/search.js',
    'app/uv-sw.js', 'app/uv.js', 'app/uv', 'app/worker.js', 'cursor/animate.ani', 'cursor/animated.cur',
    'dashboard/eliza.html', 'dashboard/freddy.html', 'dashboard/kevinhart.gif', 'dashboard/lkbb.html',
    'dashboard/mrbean.html', 'dashboard/sully.html', 'dashboard/toby.html', 'dashboard/william.html',
    'dashboard/zach.html', 'developer/dev.html', 'frogiesarcade/README.md', 'frogiesarcade/index.js',
    'frogiesarcade/package-lock.json', 'frogiesarcade/package.json', 'frogiesarcade/placeholder',
    'frogiesarcade/render.yaml', 'frogiesarcade/vercel.json', 'g/10tilldawn', 'g/1on1soccer', 'g/2048',
    'g/ADOFAI', 'g/basketrandom', 'g/bitlife', 'g/boxingrandom', 'g/cookieclicker', 'g/placeholder',
    'g/polytrack', 'g/slope', 'g/soccerrandom', 'g/thereisnogame', 'g/volleyrandom', 'g/xx142-b2exe',
    'images/chat.jpg', 'images/download.png', 'images/eliza.png', 'images/freddy.png', 'images/gc.png',
    'images/github-6980894_960_720.webp', 'images/mrbean.jpg', 'images/placeholder', 'images/sully.jpg',
    'images/toby.jpg', 'images/william.jpg', 'images/zach.jpg', 'milbew/LICENSE.txt', 'milbew/README.txt',
    'milbew/VERSION.txt', 'milbew/cron.php', 'milbew/index.php', 'milbew/index_fallback.php', 
    'milbew/install.php', 'milbew/placeholder', 'storage/load', 'storage/placeholder', 'storage/tpe',
    'test/bitlife/TemplateData', 'test/bitlife/build', 'test/bitlife/index.html', 'test/bitlife/logo.png',
    'test/bitlife/style.css'
]

# Output file path
output_file = 'big_file.txt'

# Concatenate files
with open(output_file, 'wb') as outfile:
    for file_path in file_paths:
        if os.path.exists(file_path):
            with open(file_path, 'rb') as infile:
                outfile.write(infile.read())
                outfile.write(b'\n')  # Add a newline after each file content
