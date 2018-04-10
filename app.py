from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template("hello.html")

@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>Michigan Sports Info!</h1>
        <ul>
            <li><a href="/fball"> Men's Football </a></li>
        </ul>
    '''

@app.route('/hello', methods=['GET', 'POST'])
def hellop():
    if request.method =="POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
    else:
        firstname = ''
        lastname = ''
    return render_template("hello.html", firstname=firstname, lastname=lastname)

@app.route('/bball', methods=['GET', 'POST'])
def bball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_bball_seasons(sortby, sortorder)
    else:
        seasons = model.get_bball_seasons()

    return render_template("seasons.html", seasons=seasons)

@app.route('/fball', methods=['GET', 'POST'])
def fball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_fball_seasons(sortby, sortorder)
    else:
        seasons = model.get_fball_seasons()

    return render_template("seasons.html", seasons=seasons)


if __name__ == '__main__':
    model.init_bball()
    model.init_football()
    app.run(debug=True)
