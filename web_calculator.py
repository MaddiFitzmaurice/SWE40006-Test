from flask import Flask, render_template, request

app = Flask(__name__)

def add_numbers(num1, num2):
    return num1 + num2

@app.route('/')
def welcome():
    return render_template('app.html')

@app.route('/', methods=['POST'])
def result()
    var_1 = request.form.get("var_1", type=int, default=0)
    var_2 = request.form.get("var_2", type=int, default=0)
    
    entry = add_numbers(var_1, var_2)
    return render_template('app.html', entry=entry)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
