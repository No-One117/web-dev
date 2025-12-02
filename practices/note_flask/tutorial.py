from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'post':
       return redirect(url_for('about'))
    return ""

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    return "This is the contact page."

if __name__ == '__main__':
    app.run(debug=True)