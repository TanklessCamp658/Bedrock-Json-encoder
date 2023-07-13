function translateToUtf16(text) {
  let result = "";
  for (let i = 0; i < text.length; i++) {
    const char = text[i];
    if (/[a-z]/.test(char)) {
      const utf16Char = char.charCodeAt(0).toString(16).toUpperCase();
      result += `\\u${utf16Char.padStart(4, '0')}`;
    } else if (
      /[.,0123456789{}[\]": \/ _]/.test(char) ||
      text.toLowerCase().includes("true") ||
      text.toLowerCase().includes("false")
    ) {
      result += char;
    }
  }
  return result;
}

function translateFile() {
  const inputFile = document.getElementById("inputFile").files[0];
  if (inputFile) {
    const reader = new FileReader();
    reader.onload = function (e) {
      const unicodeText = e.target.result;
      const utf16Text = translateToUtf16(unicodeText);

      const replacedText = utf16Text
        .replace(/\\u0074\\u0072\\u0075\\u0065/g, "true")
        .replace(/\\u0066\\u0061\\u006C\\u0073\\u0065/g, "false");

      const outputElement = document.getElementById("output");
      outputElement.textContent = replacedText;
    };
    reader.readAsText(inputFile);
  } else {
    alert("Please select a file.");
  }
}

function exportToFile() {
  const outputText = document.getElementById("output").value;

  if (!outputText) {
    alert("No output to export.");
    return;
  }

  const fileExtension = prompt("Enter the desired file extension (e.g., txt, json, java):");
  if (!fileExtension) {
    alert("Invalid file extension.");
    return;
  }

  const blob = new Blob([outputText], { type: "text/plain" });

  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `Encoded.${fileExtension}`;
  a.click();
}
