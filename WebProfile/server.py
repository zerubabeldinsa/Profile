from flask import Flask
from flask import Flask, render_template
from views import views


app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2320)




