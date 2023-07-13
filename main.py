import os
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

def translate_to_utf16(text):
    result = ""
    for char in text:
        if char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            utf16_char = char.encode('utf-16be').hex()
            result += f"\\u{utf16_char.upper()}"
        elif char in ['.', ',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '{', '}', '[', ']', '"', ':', ' ', '/', '_']:
            result += char
        elif text.lower().find("true") != -1 or text.lower().find("false") != -1:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file selected')

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error='No file selected')

        if file:
            unicode_text = file.read().decode('utf-8')
            utf16_text = translate_to_utf16(unicode_text)
            utf16_text = utf16_text.replace("\\u0074\\u0072\\u0075\\u0065", "true")
            utf16_text = utf16_text.replace("\\u0066\\u0061\\u006C\\u0073\\u0065", "false")

            output_file_path = os.path.join(app.static_folder, 'output.txt')
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(utf16_text)

            return render_template('index.html', output_file=output_file_path)

    return render_template('index.html')

@app.route('/output.txt')
def download_output():
    output_file_path = os.path.join(app.static_folder, 'output.txt')
    return send_file(output_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
