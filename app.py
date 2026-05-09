from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

balance = 5000

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    amount = data.get('amount', 0)
    global balance
    balance += amount
    return jsonify({'balance': balance, 'message': f'Deposited {amount}. New balance: {balance}'})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    amount = data.get('amount', 0)
    global balance
    if amount > balance:
        return jsonify({'error': 'Insufficient Balance'}), 400
    balance -= amount
    return jsonify({'balance': balance, 'message': f'Withdrew {amount}. New balance: {balance}'})

@app.route('/balance')
def check_balance():
    return jsonify({'balance': balance})

if __name__ == '__main__':
    app.run(debug=True)