from flask import Flask, render_template
app = Flask(__name__)                     
    
@app.route('/play')                           
def play():
   return render_template("templates.html")

@app.route('/play/<name>/<times>')                           
def play_num(num):
   return render_template("templates.html/name/times")
@app.route('/play/<name>/<times>/<color>')                           
def play_num(num):
   return render_template("templates.html/name/times/color")
if __name__=="__main__":
    app.run(debug=True)     