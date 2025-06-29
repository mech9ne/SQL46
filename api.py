from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


config = {
    'user': 'root',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'sql_injection_db'
}

@app.route('/inject', methods=['POST'])
def inject():
    username = request.form['username']
    password = request.form['password']
    # Perform SQL injection attack
    import sql_injection
    result = sql_injection.inject(username, password)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
