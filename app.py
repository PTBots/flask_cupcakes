"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'soshhhh2342'

connect_db(app)

@app.route('/')
def index():
    """Renders homepage"""

    return render_template('index.html')

@app.route('/api/cupcakes')
def list_cupcakes():
    """Renders list of all cupcakes"""

    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = all_cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """Gets information on specific cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def new_cupcake():
    """adds a new cupcake to the database and displays it on the page"""

    data = request.json

    cupcake = Cupcake(
        flavor = data['flavor'],
        size = data['size'],
        rating = data['rating'],
        image = data['image'] or None
    )

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 201)

@app.route('/api/cupcake/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    data = request.json
    cupcake.flavor = data.get('flavor', cupcake.flavor)
    cupcake.size = data.get('size', cupcake.size)
    cupcake.rating = data.get('rating', cupcake.rating)
    cupcake.image = data.get('image', cupcake.image)

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcake/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")
