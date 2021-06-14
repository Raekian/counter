from typing import Counter
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'bahhahahahahas'




# our index route will handle rendering our form
@app.route('/')
def index():
    if 'x' in session:
        session['x'] += 1
    else:
        session['x'] = 1



    return render_template("index.html")
@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')




@app.route('/post')
def plusTwo():
    if 'x' in session:
        session['x'] += 1
    else:
        session['x'] = 1
    return redirect("/")







@app.route('/destroy')
def destroy_session():
    session.clear()
    return redirect('/')







if __name__ == "__main__":
    app.run(debug=True)

# check for/find session