from flask import Flask, render_template, session, redirect, request, jsonify
import json

app = Flask(__name__)
app.secret_key = "James wuz here."

# root route
@app.route('/')

# SENSEI BONUS: Adjust your code to display both how many times the user has actually visited the page,
# as well as the value of the counter, given the above functionality
def index():
    if "count" not in session:
        session["count"] = 0
    if "visits" not in session:
        session["visits"] = 0

    session["visits"] += 1

    counter = session["count"]
    visits = session["visits"]

    return render_template("index.html", counter=counter, visits=visits)

# increment form method
@app.route('/increment', methods=["POST"])
def increment():
    increment_value = int(request.form.get("increment", 1))
    session["count"] += increment_value

    return jsonify({"counter": session["count"], "visits": session["visits"]})

# increment counter by two method
@app.route('/increment-by-two', methods=["POST"])
def increment_by_two():
    session["count"] += 2

    return jsonify({"counter": session["count"], "visits": session["visits"]})

# destroy_session route
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
