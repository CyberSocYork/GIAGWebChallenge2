from flask import Flask, render_template, request, url_for,redirect
from app import app, validate


@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method == "GET":
        return render_template('main.html')

    if request.method == "POST":
        username = request.form.get('username', "")
        password = request.form.get('password', "")

        if username == "cyberSocAdmin" and password == "204ZVDQD0Efadd":
            return ("""<html><head></head><body><p>the key is : 4436nZvfEEz8 <p></body></html>""")

        else:
            return render_template('main.html')



@app.route('/keyPage',methods=['GET'])
def keyPage():

    if request.method =="GET":

        if validate.validated:
            return ("""<html><head></head><body><p>the key is : 4436nZvfEEz8 <p></body></html>""")
        else:
            return ("""<html><head></head><body><p>404 not found <p></body></html>""")



if __name__ == '__main__':
    app.run()
