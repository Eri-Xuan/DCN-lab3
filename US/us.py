from flask import Flask

app = Flask(__name__)

@app.route("/fibonacci?hostname=<hostname>&fs_port=<K>&number=<X>&as_ip=<Y>&as_port=<Z>",methods=["GET"])
def main(hostname,K,X,Y,Z):
    if (hostname is None or K is None or X is None or Y is None or Z is None):
        return "Bad Request",400
    
    



if __name__ == '__main__':
    app.run(debug=True,port=8080)