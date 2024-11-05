from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def Greetings():
    
    data = {
        1: 'Hello'
    }

    return jsonify(data)

@app.route('/users_info', methods=['GET'])
def getUsersInfo():

    id = int(request.args.get('id'))
    
    users = {
        1: {
            'name': 'John',
            'age': 20
        },
        2: {
            'name': 'Jane',
            'age': 21
        },
        3: {
            'name': 'Jim',
            'age': 22
        }
    }

    return jsonify(users[id]) 

if __name__ == '__main__':
    app.run(debug=True)