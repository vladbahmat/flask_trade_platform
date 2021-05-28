from flask import Flask
#from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from flask_jwt_extended import JWTManager


swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda rule: True,
        }
    ],
    "static_url_path": "/schemas",
    "swagger_ui": True,
    "specs_route": "/swagger/",
}

def register_flask_bluenprint(app):
    from user import api as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

app = Flask(__name__)
print('вызов')
app.config['SWAGGER'] = {"title": "Flask-S1", "Flask-S2": 1}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Lipetsk4859@localhost:5432/flask_trade_platform'
db = SQLAlchemy(app)
jwt = JWTManager(app)
swagger = Swagger(app=app)
migrate = Migrate(app, db)
register_flask_bluenprint(app)


if __name__ == '__main__':
    #flask_app = register_app()
    app.run(debug=True)
