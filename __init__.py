import os
from  flask import Flask,jsonify,request,abort
from models import Plant,setup_db
from flask_cors import CORS

def create_app(test_config=None):
	app=Flask(__name__)
	setup_db(app)
	cors=CORS(app)

	#cors Headers
	@app.after_request
	def after_request(response):
		response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,True')
		response.headers.add('Access-Control-Allow-Methods','GET,PATCH,POST,DELETE,OPTIONS')
		return response

	@app.route('/')
	def index():
		return jsonify({
			'message':'Hello world'
			})

	@app.route('/plants')
	def get_plants():
		plants=Plant.query.all()
		formatted_plants=[plant.format() for plant in plants]
		
		return jsonify({
			'success':True,
			'plants':formatted_plants
			})

	
	@app.route('/smile/<int:Plant_id>')
	def get_specific_plant(Plant_id):
		plant=Plant.query.filter(Plant.Plant_id).one_or_none()
		if plant is None:
			abort(404)
			
		else:
			return jsonify({
				'success':True,
				'Plant_info':plant.format()
				})


	return app