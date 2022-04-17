from email.policy import default
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=True, default='text') # тут
    isActive = db.Column(db.Boolean, default=True)

class Item1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    place = db.Column(db.String(1000), nullable=False)
    text = db.Column(db.Text, nullable=True, default='text')

@app.route('/about')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data=items)


@app.route('/')
def about():
    return render_template('about.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/fin')
def fin():
    return render_template('fin.html')

@app.route('/limit')
def limit():
    return render_template('limit.html')

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = int(request.form['price']) # тут
        text = request.form['text']
        item = Item(title=title, price=price, text=text)
        print(price, title, text)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка"
    else:
        return render_template('create.html')

    @app.route('/create2', methods=['POST', 'GET'])
    def create2():
        if request.method == "POST":
            title = request.form['title']
            place = request.form['place']  # тут
            text = request.form['text']
            item1 = Item1(title=title, place=place, text=text)
            print(title, place, text)
            try:
                db.session.add(item1)
                db.session.commit()
                return redirect('/')
            except:
                return "Ошибка"
        else:
            return render_template('create2.html')


if __name__ =="__main__":
    app.run(debug=True)