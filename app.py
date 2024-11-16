from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/')
def home():
    html=''
    with open('index.html',"r",encoding="utf-8") as f:
        html = f.read()
        print('a')
    return html

@app.route('/url_shorten', methods=['POST'])
def submit():
    html=''
    submit = request.form.get('url')
    with open('index.html',"r",encoding="utf-8") as f:
        html = f.read()
        print('a')
    with open('data.txt',"a",encoding="utf-8") as f:
        f.write(submit+ "\n")
    with open('data.txt', "r", encoding="utf-8") as f:
        urls = f.read()
    urlarr=urls.split("\n")
    k=len(urlarr)
    print(k)
    return html.replace('<out/>',f'https://shorturl-vs7j.onrender.com{/k-1}')

@app.route('/<string:inp>')
def do(inp):
    with open('data.txt', "r", encoding="utf-8") as f:
        urls = f.read()
    urlarr=urls.split("\n")
    out=int(inp)-1
    return  redirect(urlarr[out])

app.run(debug=True,  host='0.0.0.0')
