# ------------------ Application Server code for URL Shortener APP --------------------------------

from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from wtforms import validators
import pyshorteners
import os
import re
shorter=""
url=""
# _____________________________________________________________________________________________________

app=Flask(__name__)
# _____________________________________________________________________________________________________

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqllite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)  
Migrate(app,db)

class Url(db.Model):
    __tablename__='urlshortener'
    id=db.Column(db.Integer,primary_key=True)
    url=db.Column(db.String(100))
    shorter_url = db.Column(db.String(100))
    
    def __init__(self,url,shorter_url):
        self.url=url
        self.shorter_url=shorter_url
#____________________________________________________________________________________________
        
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/',methods=["GET","POST"])
def home_page():
    global shorter_url,url
    if request.method=='POST':
        url=request.form.get('url')
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if url == '' or re.match(regex, url) is None: 
            return f"<h1><center>Please Enter a Valid URL..!!!</center></h1>"
        else :       
            if validators.url(url):
                while True:
                    s=pyshorteners.Shortener()
                    shorter_url=s.tinyurl.short(url)  
                    short_url = Url.query.filter_by(url=shorter_url).first()
                    if not short_url:                                        
                        val_pass=Url(url,shorter_url)
                        db.session.add(val_pass)
                        db.session.commit()        
                        return render_template('home.html',n=shorter_url,error=0)
            return render_template('home.html',error=1)
        
    return render_template("home.html")


@app.route('/History',methods=["GET","POST"])
def history_page():
    allurls=Url.query.all()
    return render_template('history.html',allurls=allurls)
  

@app.route('/delete/<int:id>')
def delete(id):
    item = Url.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/History')
# ____________________________________________________________________________________________________

if __name__=="__main__":
    app.run(debug=True)



