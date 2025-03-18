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
    html = """
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/tstats/&lt;start&gt;<br>
    /api/v1.0/tstats/&lt;start&gt;/&lt;end&gt;<br>
    """
    #
    return html

#open and close session within each function, return jsonify the result
#use one function with an optional argument


#################################################
# API Routes
#################################################
@app.route("/api/account_info")
def account_info():

    return jsonify(accounts)


#################################################
# Run Server
#################################################
if __name__ == "__main__":
    app.run(debug=True)