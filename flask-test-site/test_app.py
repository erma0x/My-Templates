# helloTest.py
# at the end point / call method hello which returns "hello world"


from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("index.html",
  content=["Bioinformatician","Data Scientist","Quantitative developer"]) 



@app.route("/user")
def user_page(name):
  return 'Hello {0}'.format(name)


@app.route("/admin")
def admin(name):
  return redirect(url_for("user", name='ADMIN'))


 
if __name__ == '__main__':
  
  app.run(host='0.0.0.0')
  
  #app.run()
  
  
  
    

