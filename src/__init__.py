from flask import Flask
from .routes import origin

app = Flask(__name__)

def init_app(config):
    app.config.from_object(config)
    #blueprints
    app.register_blueprint(origin.main,url_prefix="/")
    
    return app
