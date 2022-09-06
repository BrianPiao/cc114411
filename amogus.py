from flask import Flask,jsonify,request
import csv
allmov = []
with open("movies.csv") as f:
    r = csv.reader(f)
    d = list(r)
    allmov = d[1:]

lm = []
nlm = []
dnw = []

app = Flask(__name__)

@app.route("/")
def sussybaka():
    return "welcome"

@app.route("/get-movie")
def getmov():
    return jsonify({
        "data" : allmov[0],
        "status" : "success" 
    })

@app.route("/like-movie" , methods = ["POST"])
def like_movie():
    global allmov
    m = allmov[0]
    allmov = allmov[1:]
    lm.append(m)
    return jsonify({
        "status" : "success"
    }),200

@app.route("/hated-movie" , methods = ["POST"])
def hated_movie():
    global allmov
    m = allmov[0]
    allmov = allmov[1:]
    nlm.append(m)
    return jsonify({
        "status" : "success"
    }),200

@app.route("/unwatched-movie" , methods = ["POST"])
def unwatched_movie():
    global allmov
    m = allmov[0]
    allmov = allmov[1:]
    dnw.append(m)
    return jsonify({
        "status" : "success"
    }),200
    
if __name__ == "__main__":
    app.run()