def translate_to_utf16(text):
    result = ""
    for char in text:
        if char not in ['.', ',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '{', '}', '[', ']', '"']:
            utf16_char = char.encode('utf-16le').hex()
            result += f"\\u{utf16_char.upper()}"
    return result

# Example usage
unicode_text = input("Import your text here: ")
utf16_text = translate_to_utf16(unicode_text)

# Export the result to a text file
file_path = "utf16_output.txt"  # Specify the file path
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(utf16_text)

print(f"Result exported to: {file_path}")
