from flask import Flask, jsonify, request, render_template_string
import htmls
app = Flask(__name__)

# Пример списка слов для автодополнения
WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon", "banena"]


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
