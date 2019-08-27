# app/__init__.py

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort


# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    from .models import DiseaseData

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/disease/', methods=['POST', 'GET'])
    def disease_info():
        if request.method == "POST":
            disease_name = str(request.data.get('disease_name', ''))
            disease_signs = str(request.data.get('disease_signs', ''))
            disease_symptoms = str(request.data.get('disease_symptoms', ''))
            confirmatory_tests = str(request.data.get('confirmatory_tests', ''))
            if disease_name:
                disease = DiseaseData(disease_name=disease_name, disease_signs=disease_signs, disease_symptoms=disease_symptoms, confirmatory_tests=confirmatory_tests)
                disease.save()
                response = jsonify({
                    'id': disease.id,
                    'disease_name': disease.disease_name,
                    'disease_signs': disease.disease_signs,
                    'disease_symptoms': disease.disease_symptoms,
                    'confirmatory_tests': disease.confirmatory_tests
                })
                response.status_code = 201
                return response
        else:
            # GET
            diseases = DiseaseData.get_all()
            results = []

            for disease in diseases:
                obj = {
                    'id': disease.id,
                    'disease_name': disease.disease_name,
                    'disease_signs': disease.disease_signs,
                    'disease_symptoms': disease.disease_symptoms,
                    'confirmatory_tests': disease.confirmatory_tests
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    return app