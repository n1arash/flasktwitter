from flask import Flask, render_template, request, url_for, session, redirect,send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY']= 'you will never guess it!'

@app.route('/index/')
@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('home'))
    return render_template('index.html')

@app.route('/home')
def home():
    if 'user' in session:
        return 'you are here! <a href="/logout">Logout!</a>'
    else:
        return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    session['user'] = 'username'
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))

@app.route('/assets/<path:path>')
def send_file(path):
    return send_from_directory('assets',path)

if __name__ == '__main__':
    app.run(debug=True)
