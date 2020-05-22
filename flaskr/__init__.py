import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # index page
    @app.route('/', methods=('GET', 'POST'))
    def index():
        if request.method == "GET":
            return render_template("index.html")
        if request.method == 'POST':
            BMI = request.form.get("BMI")
            smoking = request.form.get("smoking")
            pgs = request.form.get("pgs")
            pr = request.form.get("pr")
            score = 0
            if BMI == "1":
                score += 2

            if smoking == "1":
                score += 2

            if pgs == "1":
                score += 2

            if pgs == "1":
                score += 1

            return render_template("outcomes.html", score=score)
