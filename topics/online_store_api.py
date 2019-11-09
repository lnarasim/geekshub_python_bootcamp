from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/shop')
def online_product():
    return 'Hi, Welcome to Zimba online shop!'

product_mart = [
    {
        'prduct id': 1,
        'product': u'Buy nylon clothwears',
        'labels': u'skurt, pant, shirt, tops, tights', 
        'done': False
    },
    {
        'prduct id': 2,
        'product': u'Buy cotton clothwears',
        'labels': u'shirts, pants, tights, tops, saree', 
        'done': False
    }
]

@app.route('/shop/product_mart', methods=['GET'])
def get_tasks():
    return jsonify({'product_mart': product_mart})

@app.route('/shop/product_mart', methods=['POST'])
def Post_tasts():
    

if __name__ == '__main__':
    app.run()