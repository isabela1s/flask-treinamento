from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/Hello-World")
    def Hello_World():
        return "hello world"
    return app