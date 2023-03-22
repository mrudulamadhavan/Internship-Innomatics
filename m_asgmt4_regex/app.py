
# Step 1 - Import necessary modules
    
from flask import Flask, request,render_template
import re

# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)

# Step 3 - Create an END POINT using routes and bind them with a functionality
@app.route('/',methods=['POST','GET'])
def reg_match():
    if request.method=='POST':
        n=request.form['regex']
        s=request.form['string']
        c=0
        res=[]
        for it in re.finditer(r"{}".format(n),s):
            st=""
            c=c+1
            st=st+"Match {} --> \'{}\'  @  start index: {} ; end index: {} ".format(c,it.group(),it.start(),it.end())
            res.append(st)
        return render_template("result.html",ans="Match Found!",regex=n,string=s,count=c,spans=res)
    else:
        return render_template("result.html",count=-1)

# Step 4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)