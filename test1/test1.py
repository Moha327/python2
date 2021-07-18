from flask import Flask, render_template  
app = Flask(__name__)                     
    
@app.route('/')                           
def hello():
    print("in the hello function")
    return render_template('test1.html')  

@app.route('/<name>/<times>')
def hello_person(name,times):
    print("*"*80)
    print("in the hello_person function")
    print(name)
    return render_template("test1.html" , some_name=name, num_times=int(times))
if __name__=="__main__":
    app.run(debug=True)                   