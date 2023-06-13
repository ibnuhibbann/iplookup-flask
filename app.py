from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    public_ip = requests.get('http://ip-api.com/json').json()
    return render_template('index.html', public = public_ip)


@app.route('/lookup', methods =["GET", "POST"])
def lookup():
    ipData = ''
    ipAddress = ''

    if request.method == "POST":       
        ipAddress = request.form.get("ipAddress")  
        if ipAddress:
            url = "http://ip-api.com/json/" + ipAddress
            ipData = requests.get(url).json()
    return render_template('result.html',  data = ipData, ipAddress = ipAddress)

if __name__ == "__main__":
    app.run(port = 8000, debug=True)