from flask import Flask, render_template


app = Flask (__name__)

@app.route("/")

def uti():
    name = 'TOLU is quite unique'
    return render_template('index.html', name= name)


#custon error page

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404
    


@app.errorhandler(500)
def page_not_found(e):
    return render_template('error505.html'), 500
        