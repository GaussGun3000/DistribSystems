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
    # Сначала сортируем по длине слова
    sorted_by_length = sorted(suggestions, key=lambda x: len(x))
    # Если есть одинаковые по длине слова, сортируем их по алфавиту
    sorted_alphabetically = sorted(sorted_by_length, key=lambda x: (len(x), x))
    # Возвращаем только первые три слова (если есть)
    return sorted_alphabetically[:3]

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('term')
    suggestions = [word for word in WORDS if word.startswith(search)] if search else []
    top_three_suggestions = select_top_three_suggestions(suggestions)
    return jsonify(top_three_suggestions)


@app.route('/')
def index():
    return render_template_string(htmls.AUTOCOMPLETE)


if __name__ == '__main__':
    app.run(debug=True)
