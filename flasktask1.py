# FLASK - TASK 1

# Step 1 - To import FLASK
from flask import Flask, request

# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)


# Step 3 - Create an END POINT using routes and bind them with a functionality
# Home Page
@app.route('/')
def home_page():
    return "Welcome to HOME PAGE"

# Uppercase
@app.route("/uppercase")
def upperCase():
    name = request.args.get("username")
    return name.upper()

# Check Prime or not
@app.route("/prime")
def is_prime():
    n = request.args.get("n")
    n=int(n)
    if n in [2, 3]:
        return "It's a Prime Number"
    if (n == 1) or (n % 2 == 0):
        return "It's not a Prime Number"
    r = 3
    while r * r <= n:
        if n % r == 0:
            return "It's not a Prime Number"
        r += 2
    return "It's a Prime Number"

# BillCalculator
@app.route('/bill_calc')
def bill_calc():
    amt = request.args.get("amt") 
    bill_amt = int(amt)
    tip_perc = 10
    total = bill_amt*(1 + 0.01*tip_perc)
    total = round(total,2)
    return  str(total)


# Check Armstrong or not
@app.route('/armstrong')
def armstng():
    a=request.args.get('a')
    num=int(a)
    actual_num=num
    var=0
    while(num>0):
        rem=num%10
        var=var+rem**3
        num=num//10
    if var==actual_num:
        return str("Yes,it's an Armstrong Number")
    else:
        return str("No,it's not an Armstrong Number")
    
# Dimension
@app.route('/cube')
def cube_dimns():
    side = request.args.get('s')
    a = int(side)
    Total_Surface_Area = 6 * (a ** 2)    
    Lateral_Surface_Area = 4 * (a **2)
    Volume = a ** 3
    return (f"Total Surface Area: {Total_Surface_Area} sq.unit;  Lateral Surface Area: {Lateral_Surface_Area} sq.unit;   Volume: {Volume} cubic.unit")

  
# Step 4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)
