import os

# List of file paths to concatenate
file_paths = [
    '4-0-4.html', '404.html', 'settings.html', 'SudoUser-Var-{}.html',
    'VS.html', 'aboutus.html', 'apps.html', 'dark-jokes.html',
    'dahsboard.html', 'dev.html', 'easteregg.html', 'extra.html',
    'forms.html', 'frogarcade.html', 'games.html', 'ind4x.html', 'index.html',
    'kevin hart.html', 'linkies.html', 'midload.html', 'pricing.html',
    'signin.html', 'signup.html', 'testing.html', 'app/404.html',
    'dashboard/eliza.html', 'dashboard/freddy.html', 'dashboard/lkbb.html',
    'dashboard/mrbean.html', 'dashboard/sully.html', 'dashboard/toby.html',
    'dashboard/william.html', 'dashboard/zach.html', 'developer/dev.html',
    'test/bitlife/index.html'
]

css_files = ['test/bitlife/style.css']
js_files = ['crisp.js', 'app/index.js', 'app/search.js', 'app/uv-sw.js', 'app/uv.js', 'app/worker.js', 'frogiesarcade/index.js']

output_file = 'big_file.html'

# Concatenate files
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Write the HTML structure
    outfile.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Combined Files</title>\n<style>\n')
    
    # Add CSS content
    for file_path in css_files:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n')
    
    outfile.write('</style>\n</head>\n<body>\n')
    
    # Add HTML content
    for file_path in file_paths:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n')
    
    # Add JavaScript content
    outfile.write('<script>\n')
    for file_path in js_files:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n')
    outfile.write('</script>\n</body>\n</html>')
