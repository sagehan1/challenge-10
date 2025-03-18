# Import the dependencies.
from flask import Flask, jsonify, render_template


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# HTML Routes
#################################################
@app.route("/")
def home():
    context_values = {
        'first_name': "Danny",
        'last_name': "Boy",
        'accounts': [
            {   
                'number': 123,
                'nickname': "Checking",
                'balance': -127.24,
            },
            {  
                'number': 456,
                'nickname': "Savings",
                'balance': 2244.55,
            },
        ]
    }
    return render_template("accounts.html", context=context_values)
#    return "<h1>Hello</h1>"
#################################################
# API Routes
#################################################
@app.route("/api/account_info")
def account_info():
    accounts = [
            {   
                'number': 123,
                'nickname': "Checking",
                'balance': -127.24,
            },
            {  
                'number': 456,
                'nickname': "Savings",
                'balance': 2244.55,
            },
        ]
    return jsonify(accounts)


#################################################
# Run Server
#################################################
if __name__ == "__main__":
    app.run(debug=True)