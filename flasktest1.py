"""
flask 
django REST
rapidapi
fastapi

conda install flask
pip install flask
"""

from flask import Flask, url_for, json, request, jsonify 

def factorial(nb):
    if nb== 0:
        return 1
    else:
        return factorial(nb-1) * nb
    
app = Flask(__name__) 

@app.errorhandler(404) 
def not_found(error=None):     
    message = {             
        'status': 404,             
        'message': 'Not Found: ' + request.url,     }     
    resp = jsonify(message)     
    resp.status_code = 404 
    return resp
 
@app.route('/') # http://localhost:5000/
def api_root():     
    return 'Welcome' 

@app.route('/articles') # http://localhost:5000/articles
def api_articles():     
    return 'List of ' + url_for('api_articles') 

@app.route('/numbers/<nb>') # http://localhost:5000/numbers/34
def api_numbers(nb): 
    nb=int(nb)    
    return f"{nb}**2 is {nb**2}"

@app.route('/sqrt/<nbr>') # http://localhost:5000/sqrt/900
def api_sqrt(nbr):
    import math 
    try:     
        return f"'sqrt':{math.sqrt(int(nbr))}" 
    except:
        resp = jsonify("Wrong argument received")     
        resp.status_code = 405
        return resp

# http://localhost:5000/facto/23 + GET
@app.route('/facto/<int:number>', methods=["GET", "POST"]) 
def api_facto(number):
    if request.method == "GET":     
        result=factorial(number) 
        message={"nb":number, "factorial":result}
        resp = jsonify(message)     
        resp.status_code = 200
        return resp
    elif request.method == "POST":
        message={"nb":number, "factorial":"PROBLEM!!"}
        resp = jsonify(message)     
        resp.status_code = 401
        return resp
    
if __name__ == '__main__':     
    app.run(host="localhost")
    