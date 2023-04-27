
#modules: flask, time, and socket.
import flask
import time
import socket
#Get the IP address of the machine the script is running on
h_name = socket.gethostname()
#store it into below IP
IP_addres = socket.gethostbyname(h_name)
#flask application intance
app = flask.Flask(__name__)
#define route fot the root URL and call the indexed function
#defien the index function which gets time.
#return a string with current time/hostname and IP address
@app.route('/')
def index():
    Time= time.strftime("%H:%M:%S")
    return Time+" Serving from "+h_name+" ("+IP_addres+")\n"
#run script as main
#flask dev server port 80
#all available netwom
#enable debugging
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 80, debug = True)
  #app.run( port = 8080, debug = True)
