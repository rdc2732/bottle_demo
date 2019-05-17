from bottle import route, run, template

@route('/')
def index():
    return template('index', name='Rick')

if __name__ == '__main__':
    run(debug=True, reloader=True)
