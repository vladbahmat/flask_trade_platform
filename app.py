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
    from trade_platform import rest_api as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e5a605cc-56d9-497e-a7ef-6982797f8ee8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Lipetsk4859@localhost:5432/flask_trade_platform'
db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
register_flask_bluenprint(app)

swagger = Swagger(app=app)

if __name__ == '__main__':
    app.run(debug=True)
