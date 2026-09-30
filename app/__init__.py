import click
from flask import Flask, redirect, render_template, url_for

from app.extensions import csrf, db, migrate
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from app import models
    from app.tasks import bp as tasks_bp

    app.register_blueprint(tasks_bp)

    @app.context_processor
    def globals_():
        return {"app_name": app.config["APP_NAME"]}

    @app.get("/")
    def index():
        return redirect(url_for("tasks.index"))

    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        db.session.rollback()
        return render_template("errors/500.html"), 500

    @app.shell_context_processor
    def shell():
        return {"db": db, "Task": models.Task}

    @app.cli.command("test-db")
    def test_db():
        value = db.session.execute(db.text("SELECT 1")).scalar()
        click.echo(f"Conexión correcta (SELECT 1 = {value})")

    return app
