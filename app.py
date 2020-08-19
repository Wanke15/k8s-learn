from flask import Flask

from api.api import base_bp


app = Flask(__name__)
app.register_blueprint(base_bp)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
