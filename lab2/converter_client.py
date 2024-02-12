from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert_amount():
    amount = request.args.get('amount', type=int)
    rate = request.args.get('rate', type=float)
    result = amount * rate if amount and rate else None
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)