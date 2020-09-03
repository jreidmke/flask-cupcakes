"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres4@localhost/cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

# JSON API Routes

@app.route('/')
def form():
    cupcakes = Cupcake.query.all()
    return render_template('index.html', cupcakes = cupcakes)

@app.route('/api/cupcakes')
def list_cupcakes():
    cupcakes = [cupcake.serialize_cupcake() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def cupcake_detail(cupcake_id):
    cupcake = Cupcake.query.get(cupcake_id).serialize_cupcake()
    return jsonify(cupcake=cupcake)

@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    new_cupcake=Cupcake(flavor=request.json['flavor'], size=request.json['size'], rating=request.json['rating'], image=request.json['image'])
    db.session.add(new_cupcake)
    db.session.commit()
    resp_json = jsonify(cupcake=new_cupcake.serialize_cupcake())
    return (resp_json, 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get(cupcake_id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize_cupcake())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="DELETED")