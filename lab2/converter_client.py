from flask import Flask, request, render_template_string
import requests
import htmls
app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string(htmls.index_html)


@app.route('/convert-client', methods=['GET'])
def convert_client():
    amount = request.args.get('amount')
    rate = request.args.get('rate')
    if amount and rate:
        response = requests.get(f'http://localhost:5000/convert?amount={amount}&rate={rate}')
        result = response.json().get('result')
    else:
        result = None
    return render_template_string(htmls.TEMPLATE, result=result)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
