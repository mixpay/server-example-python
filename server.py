import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
from flask import request
from OpenSSL import crypto 
from urllib import quote
import base64 

app = Flask(__name__)

@app.route("/sign", methods=['GET','POST']) 
def signService(): 
    if request.method == 'POST':
        params = request.form
    else:
        params = request.args

    kv_array = []
    for param in params:
        kv = '%s=%s' % (param, params[param])
        kv_array.append(kv)
    content = "&".join(sorted(kv_array))

    key = crypto.load_privatekey(crypto.FILETYPE_PEM, open("rsa_private_key.pem").read())  
    sign_string = crypto.sign(key, content, 'sha1')  
    sign64 = base64.b64encode(sign_string)
    sign_encoded = quote(sign64)

    print "content: " + content
    print "sign: " + sign_encoded

    return sign_encoded

@app.route("/notify", methods=['POST'])
def notify():
    return "success"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
