from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index_ex.html')

@app.route('/about/<username>')
def about(username = None):
    return render_template('about_ex.html',name = username)

@app.route('/blog')
def blog():
    return 'These are my blogs'

@app.route('/<username>/<int:post_id>/<int:post_id2>')
def name_param( post_id,post_id2,username = None):
    return render_template('name_param.html',name = username, a= post_id, b=post_id2)

#@app.route('/blog')
#def blogs():
#    return 'Blog!!s'
