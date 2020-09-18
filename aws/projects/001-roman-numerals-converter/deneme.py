from flask import Flask, render_template, request, redirect, url_for
import converter

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.form == 'POST':
        num = request.form.get("number")
        rom = converter(num)
        return render_template("result.html", number_decimal = num, number_roman = rom)
    else:
        pass

@app.route("/", methods = ['GET', 'POST'])
def result():
    if request.form == 'POST':
        num = request.form.get("number")
        rom = converter(num)
        return render_template("result.html", number_decimal = num, number_roman = rom)
    else:
        pass
        # num = request.form.get("number")
        # return render_template("result.html", developer_name = num)
    
if __name__ == "__main__":
    app.run(debug=True)