from flask import Flask , render_template , redirect , url_for , request
from scripts.create_plan1 import user_inputs


app = Flask(__name__)

@app.route('/')
def welcome():
    
    return render_template("index.html")


@app.route('/submit',methods = ['POST','GET'])
def submit():
    
    if request.method=='POST':
        return "The Model CID is " + user_inputs(request.form)
     
       
   
if __name__ ==' __main__':
    app.run()
    
    
    
    
