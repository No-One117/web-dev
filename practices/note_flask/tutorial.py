from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'post':
       return redirect(url_for('about'))
    return render_template('index.html')

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    return "This is the contact page."

@app.route('/user')
def user():
    return "this is the user page."

if __name__ == '__main__':
    app.run(debug=True)