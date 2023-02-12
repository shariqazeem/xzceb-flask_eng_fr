import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=["GET"])
def english_to_french():
    english_text = request.args.get("textToTranslate")
    if not english_text:
        return "textToTranslate parameter is missing in the request"
    french_text = translator.english_to_french(english_text)
    return french_text

@app.route("/frenchToEnglish", methods=["GET"])
def french_to_english():
    french_text = request.args.get("textToTranslate")
    if not french_text:
        return "textToTranslate parameter is missing in the request"
    english_text = translator.french_to_english(french_text)
    return english_text


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
