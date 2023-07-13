function translate() {
    var unicodeText = document.getElementById('unicodeText').value;
    var utf16Result = document.getElementById('utf16Result');

    var result = "";
    for (var i = 0; i < unicodeText.length; i++) {
        var char = unicodeText.charAt(i);
        if (!['.', ',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '{', '}', '[', ']', '"'].includes(char)) {
            var utf16Char = char.charCodeAt(0).toString(16);
            result += "\\u" + utf16Char.toUpperCase();
        }
    }

    utf16Result.textContent = result;
}
