from flask import Flask, request, abort
import json
import requests

from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

  
@app.route('/api/pay', methods=['POST'])
def pay():
    order_id = request.values.get('order_id')
    pay_id = str(order_id) + '0001'

    data = {
        'status': 200,
        'message': '支付成功！',
        'order_id': order_id,
        'pay_id': pay_id
    }
    res = jsonify(data)
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
