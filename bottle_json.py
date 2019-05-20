from bottle import route, run

@route('/')
def index():
    return {"name" : "jasonData", "myLIst" : [1,2,3,4,5]}

if __name__ == '__main__':
    run(debug=True, reloader=True)
