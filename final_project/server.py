from machinetranslation import translator
from deep_translator import MyMemoryTranslator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text
   

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
  english_text = MyMemoryTranslator (source ='french', target='english').translate(french_text)
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
   app.run(debug = True)
