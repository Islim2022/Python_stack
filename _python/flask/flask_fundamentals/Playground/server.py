from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def level_1():
    return render_template("index.html", num_box = 3, box_color = '#9fc5f8')

@app.route('/play/<num>')
def level_2(num):
    return render_template("index.html", num_box = int(num), box_color = '#9fc5f8')

@app.route('/play/<num>/<color>')
def level_3(num,color):
    return render_template("index.html", num_box = int(num), box_color = color)
    
if __name__ == "__main__":
    app.run(debug=True)