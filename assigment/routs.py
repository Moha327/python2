from flask import Flask
app = Flask(__name__)
@app.route('/')
def world():
    return 'hello_world'
@app.route('/dojo')
def dojo():
    return 'dojo'
@app.route('/say/<name>')
def ob(name):
    return 'dojo, '+ name

@app.route('/repeat/<int:time><world>')
def cc(time,world):
    n=time*world
    return   n 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode. 