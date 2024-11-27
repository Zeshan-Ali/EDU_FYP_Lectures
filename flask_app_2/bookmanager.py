from flask import Flask, render_template, redirect  ,request
from flask_sqlalchemy import SQLAlchemy
import os


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)  # initialzation of db
class Book(db.Model):
    title = db.Column(db.String(80), nullable=False, primary_key=True,unique=True)
    no_of_pages = db.Column(db.Integer, nullable=False)

    
    def __repr__(self):
        return "<Title: {}>".format(self.title)
    def __repr__(self):
       return "<no of pages: {}>".format(self.no_of_pages)

@app.route('/',methods=['GET','POST'])
def firsr_function():
 if request.form:
    title = request.form['name']
    no_of_pages = request.form['page']
    new_book = Book(title=title,no_of_pages=no_of_pages)
    db.session.add(new_book)
    db.session.commit()
 return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == '__main__':
 app.run(debug=True)