from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/h1', methods=['GET'])
def get_h1():
    return jsonify({'payload': 'get'})

@app.route('/h2', methods=['POST'])
def post_h2():
    return jsonify({'payload': 'post'})

@app.route('/h3', methods=['PUT'])
def put_h3():
    return jsonify({'payload': 'put'})

@app.route('/h4', methods=['DELETE'])
def delete_h4():
    return jsonify({'payload': "delete"})

@app.route('/h5', methods=['GET'])
def get_h5():
    return jsonify({'payload': 'success', 'error': False})

@app.route('/h6', methods=['GET', 'POST', 'DELETE'])
def handle_valid_methods():
    method = request.method
    payload = 'success'
    return jsonify({'method': method, 'payload': payload, 'error': False})

@app.route('/h7', methods=['GET'])
def get_user_details():
    email = request.args.get('email')
    name = request.args.get('name')

    if not email or not name:
        return {
            "payload": {},
            "error": {"available": True, "err_msg": "email and name must be provided"},
            "status": 400
        }

    try:
        payload = {"email": email, "name": name}
        error = {"available": False, "err_msg": None}
        status = 200
    except Exception as e:
        payload = {}
        error = {"available": True, "err_msg": str(e)}
        status = 500

    return {
        "payload": payload,
        "error": error,
        "status": status
    }

@app.route('/h8', methods=['POST'])
def create_user_details():
    data = request.get_json()

    if not data or 'email' not in data or 'name' not in data:
        return {
            "payload": {},
            "error": {"available": True, "err_msg": "email and name must be provided"},
            "status": 400
        }

    email = data['email']
    name = data['name']

    try:
        payload = {"email": email, "name": name}
        error = {"available": False, "err_msg": None}
        status = 200
    except Exception as e:
        payload = {}
        error = {"available": True, "err_msg": str(e)}
        status = 500

    return {
        "payload": payload,
        "error": error,
        "status": status
    }
Lista = ["foobar","bazqux","fred"]

@app.route('/h9', methods=['GET'])
def get_alias():
    alias = request.args.get('alias')

    if not alias:
        return {
            "payload": None,
            "error": {"available": True, "err_msg": "alias must be provided"},
            "status": 400
        }

    if alias in Lista:
        payload = alias
        error = {"available": False, "err_msg": None}
        status = 200
    else:
        payload = "not found"
        error = {"available": False, "err_msg": None}
        status = 404

    return {
        "payload": payload,
        "error": error,
        "status": status
    }

Lista = ["foobar","bar","baz","qux","fred"]

@app.route('/h10', methods=['POST'])
def get_alias_from_body():
    data = request.get_json()

    if not data or 'alias' not in data:
        return {
            "payload": None,
            "error": {"available": True, "err_msg": "alias must be provided"},
            "status": 400
        }

    alias = data['alias']

    if alias in Lista:
        payload = alias
        error = {"available": False, "err_msg": None}
        status = 200
    else:
        payload = "not found"
        error = {"available": False, "err_msg": None}
        status = 404

    return jsonify({
        "payload": payload,
        "error": error,
        "status": status
    })

if __name__ == '__main__':
    app.run(debug=True)