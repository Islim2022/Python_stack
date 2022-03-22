from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/dojo')
def index_2():
    return "Dojo!"

@app.route('/say/<name>')
def index_3(name):
    return "Hi " + name + "!"

@app.route('/repeat/<count>/<name>')
def index_4(name,count):
    num = int(count)
    return f'{name} '  * num
if __name__=="__main__":
    app.run(debug=True)


