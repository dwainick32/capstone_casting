import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import setup_db, Movie, Actor, db

def create_app(test_config=None):
# create and configure the app
  app = Flask(__name__)
  CORS(app, resources={r"/api/": {"origins": "*"}})
  setup_db(app, 'capstone_project')

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
    response.headers.add('Access-Control-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')
    return response

  @app.route('/movies')
  def get_movies():
    movies = Movie.query.all()
    movies = [movie.format() for movie in movies]
    for movie in movies:
      movie['actors'] = [i.format() for i in movie['actors']]
    return jsonify(movies)
  
  @app.route('/actors')
  def get_actors():
    actors = Actor.query.all()
    actors = [actor.format() for actor in actors]
    return jsonify(actors)

  @app.route('/movies/create', methods=['POST'])
  def post_new_movie():
    body = request.get_json()

    title = body.get('title', None)
    release_date = body.get('release_date', None)

    movie = Movie(title=title, release_date=release_date)
    movie.insert()
    new_movie = Movie.query.get(movie.id)
    new_movie = new_movie.format()

    return jsonify({
      'success': True,
      'created': movie.id,
      'new_movie': new_movie
    })

  @app.route('/actors/create', methods=['POST'])
  def post_new_actor():
    body = request.get_json()

    name = body.get('name', None)
    age = body.get('age', None)
    gender = body.get('gender', None)
    movie_id = body.get('movie_id', None)

    actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)
    actor.insert()
    new_actor = Actor.query.get(actor.id)
    new_actor = new_actor.format()

    return jsonify({
      'success': True,
      'created': actor.id,
      'new_actor': new_actor
    })

  @app.route('/movies/delete/<int:movie_id>', methods=['DELETE'])
  def delete_movie(movie_id):
    Movie.query.filter(Movie.id == movie_id).delete()
    db.session.commit()
    db.session.close()
    return jsonify({
      "success": True,
      "message" : "Delete occured"
    })

  @app.route('/actors/delete/<int:actor_id>', methods=['DELETE'])
  def delete_movie(actor_id):
    Actor.query.filter(Actor.id == actor_id).delete()
    db.session.commit()
    db.session.close()
    return jsonify({
      "success": True,
      "message" : "Delete occured"
    })

  @app.route('/actors/patch/<int:actor_id>', methods=['PATCH'])
  def patch_actor(actor_id):

    actor = Actor.query.filter(Actor.id== actor_id)
    body = request.get_json()
    name = body.get('name', None)
    age = body.get('age', None)
    gender = body.get('gender', None)
    movie_id = body.get('movie_id', None)
    actor.name = name
    actor.age = age
    actor.gender = gender
    actor.movie_id = movie_id
    actor.update()
    return jsonify({
      "success": True,
      "message": "update occured"
    })
    
  @app.route('/movies/patch/<int:movie_id>')
  def patch_movie(movie_id):
    movie = Movie.query.filter(Movie.id == movie_id)
    body = request.get_json()
    title = body.get('title', None)
    release_date = body.get('release_date', None)
    movie.title = title
    movie.release_date = release_date
    movie.update()
    return jsonify({
      "success": True,
      "message": "update occured"
    })      


  return app

app = create_app()



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)