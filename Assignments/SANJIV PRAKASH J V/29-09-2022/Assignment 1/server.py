from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def registerHandler():
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
        data = {}
        
        data["name"] = request.form.get("name")
        data["email"] = request.form.get("email")
        data["phone-number"] = request.form.get("phone-number")
        
        return render_template("success.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)