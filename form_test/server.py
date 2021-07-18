from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods=['POST'])
def create_user():
    print("*"*50)
    print(request.form)
    print(f"username submitted:{request.form['name']}")
    print(f"email submitted:{request.form['email']}")
    
    return render_template("show.html", name =request.form['name'] ,email =request.form['email'])


if __name__ == "__main__":
    app.run(debug=True)