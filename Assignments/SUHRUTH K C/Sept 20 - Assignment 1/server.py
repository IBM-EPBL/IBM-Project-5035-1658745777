from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/register',methods=['GET','POST'])
def handle_regiser():
    if request.method == 'GET':
        return render_template('web_page.html')
    elif request.method == 'POST':
        data = {}
        data['name'] = request.form.get('name')
        data['email'] = request.form.get('email')
        data['number'] = request.form.get('number')
        
        return render_template('success.html',data=data)
        

if __name__ == '__main__':
    app.run(debug=True)