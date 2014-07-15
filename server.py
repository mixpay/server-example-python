from flask import Flask
from flask import request
from OpenSSL.crypto import load_privatekey, FILETYPE_PEM, sign  
from urllib import quote
import base64 

app = Flask(__name__)

@app.route("/sign", methods=['GET', 'POST'])
def signService():
    params = []
    for arg in request.args:
        param = '%s=%s' % (arg, request.args[arg])
        params.append(param)
    raw_string = "&".join(sorted(params))
    print raw_string

    key = load_privatekey(FILETYPE_PEM, open("rsa_private_key.pem").read())  
    content = raw_string 
       
    sign_string = sign(key, content, 'sha1')  
    sign64 = base64.b64encode(sign_string)
    sign_encoded = quote(sign64)

    return sign_encoded

@app.route("/notify", methods=['POST'])
def notify():
    return "success"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')