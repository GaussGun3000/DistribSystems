from flask import Flask, request, render_template_string
from htmls import result_html, form_html, index_html

app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string(index_html)


@app.route('/input', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        return render_template_string(result_html, name=name, surname=surname, email=email)
    return render_template_string(form_html)


if __name__ == '__main__':
    app.run(debug=True)
