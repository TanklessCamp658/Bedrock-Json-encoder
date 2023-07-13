from flask import Flask, render_template, request

app = Flask(__name__)

def translate_to_utf16(text):
    result = ""
    for char in text:
        if char not in ['.', ',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '{', '}', '[', ']']:
            utf16_char = char.encode('utf-16le').hex()
            result += f"\\u{utf16_char.upper()}"
    return result

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        unicode_text = request.form['unicode_text']
        utf16_text = translate_to_utf16(unicode_text)
        return render_template('index.html', utf16_text=utf16_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
