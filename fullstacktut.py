from flask import Flask
SvrMgrVaj = Flask(__name__)

# [==] CodTdo

if __name__ == '__main__':
    SvrMgrVaj.run(debug=True)
    

@SvrMgrVaj.route('/', methods=['GET'])
def NamApiFnc():
    return "<h1>Welcome to Website</h1>"