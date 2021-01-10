from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("page.html")

@app.route('/page2.html')
def page2():
    return render_template("page2.html")

@app.route('/page3.html')
def page3():
    return render_template("page3.html")

@app.route('/page4.html')
def page4():
    return render_template("page4.html")

@app.route('/page5.html')
def page5():
    return render_template("page5.html")

@app.route('/page6.html')
def page6():
    return render_template("page6.html")

@app.route('/page7.html')
def page7():
    return render_template("page7.html")

@app.route('/page8.html')
def page8():
    return render_template("page8.html")

if __name__ == '__main__':
    app.run()