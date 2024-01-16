from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)



class POST(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    text = db.Column(db.Text, nullable=False)

# чтобы создать базу данных:
# from app import app, db
# app.app_context().push()
# db.create_all()

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    post = POST.query.all()
    return render_template("posts.html", posts=post)




@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]
        post = POST(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect("/index")
        except:
           return f"При добавлении статьи произошла ошибка"


    else:

        return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)
