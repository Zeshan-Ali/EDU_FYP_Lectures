from flask import Flask
from flask import render_template
from flask import request
import os
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Book(db.Model):
    title = db.Column(db.String(80), nullable=False, primary_key=True,unique=True)

    
    def __repr__(self):
        return "<Title: {}>".format(self.title)

class Author(db.Model):
    name = db.Column(db.String(80), nullable=False, primary_key=True,unique=True)
    
    def __repr__(self):
        return "<Name: {}>".format(self.name)
   

@app.route("/",methods=["GET", "POST"])
def home():
    if request.form:
        book = Book(title=request.form.get("title"))
        db.session.add(book)
        db.session.commit()
    books = Book.query.all()
    return render_template("home.html",books=books)

# @app.route("/read_page")
# def read_page():
#     books = Book.query.all()
#     return render_template("read.html",books=books)


@app.route("/update", methods=["POST"])
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    book = Book.query.filter_by(title=oldtitle).first()
    book.title = newtitle
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)