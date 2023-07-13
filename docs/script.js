function translate() {
    var unicodeText = document.getElementById('unicodeText').value;
    var utf16Result = document.getElementById('utf16Result');

    var result = "";
    var words = unicodeText.split(" ");
    for (var i = 0; i < words.length; i++) {
        var word = words[i];
        var translatedWord = "";
        for (var j = 0; j < word.length; j++) {
            var char = word.charAt(j);
            if (!['.', ',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '{', '}', '[', ']', '"'].includes(char)) {
                var utf16Char = char.charCodeAt(0).toString(16);
                while (utf16Char.length < 4) {
                    utf16Char = "0" + utf16Char;
                }
                translatedWord += "\\u" + utf16Char;
            }
        }
        result += translatedWord + " ";
    }

    utf16Result.textContent = result.trim();
}
