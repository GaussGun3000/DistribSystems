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
    exit(-1)


def select_top_three_suggestions(suggestions):
    sorted_by_length = sorted(suggestions, key=lambda x: len(x))
    sorted_alphabetically = sorted(sorted_by_length, key=lambda x: (len(x), x))
    return sorted_alphabetically[:3]


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('term').lower()
    suggestions = [word for word in WORDS if word.startswith(search)] if search else []
    top_three_suggestions = select_top_three_suggestions(suggestions)
    return jsonify(top_three_suggestions)


@app.route('/')
def index():
    return render_template_string(htmls.AUTOCOMPLETE)


@app.route('/allwords', methods=['GET'])
def allwords():
    # Simply return all WORDS in JSON format
    return jsonify(WORDS)


if __name__ == '__main__':
    app.run(debug=True)
