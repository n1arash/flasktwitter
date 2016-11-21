from flask import Flask, render_template, request, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY']= 'you will never guess it!'

@app.route('/', methods=['GET'])
def index():
    if 'user' in session:
        return url_for('home')
    return render_template('index.html')

@app.route('/home', methods=['GET'])
def home():
    if 'user' in session:
        pass #show the twit's...
    else:
        pass #show the texts....

@app.route('/login', methods=['POST'])
def login():
    pass
        
if __name__ == '__main__':
    app.run(debug=True)
