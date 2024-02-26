from flask import Flask, jsonify, request, render_template_string
import htmls
import json
app = Flask(__name__)
import os


try:
    if 'lab3' not in os.getcwd():
        os.chdir('lab3')
    with open("words.json", "r") as file:
        WORDS = json.load(file)
except FileNotFoundError:
    print("Файл words.json не найден.")
    WORDS = []

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('term')
    suggestions = [word for word in WORDS if word.startswith(search)] if search else []
    return jsonify(suggestions)


@app.route('/')
def index():
    return render_template_string(htmls.AUTOCOMPLETE)


if __name__ == '__main__':
    app.run(debug=True)
