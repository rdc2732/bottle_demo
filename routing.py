from bottle import run, route

@route('/login')
def login():
    return '<h1>On the login page</h1>'

@route('/register')
def register():
    return '<h1>On the register page</h1>'

@route('/article/<id>')
def article(id):
    return '<h1>You are viewing article ' + id + '</h1>'

@route('/page/<id>/<name>')
def page(id, name):
    return '<h1>Your are on page ' + id + ' with a name of ' + name + '.</h1>'

if __name__ == '__main__':
    run(debug=True, reloader=True)

