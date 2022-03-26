from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def create_dojo():
    print(request.form)
    name = request.form['name']
    locations = request.form['locations']
    language = request.form['languages']
    comment = request.form['comment']
    return render_template("result.html", name = name, location = locations, language = language, comment = comment)

if __name__ == "__main__":
    app.run(debug = True)
