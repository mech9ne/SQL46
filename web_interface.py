from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Call API to perform SQL injection attack
        import requests
        response = requests.post('http://localhost:5000/inject', data={'username': username, 'password': password})
        return response.text
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
