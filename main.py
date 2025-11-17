from flask import Flask
from models.models import Usuario
from db.db import db
from routes.user_route import usuario_bp
from flask_login import LoginManager




app = Flask(__name__)
app.secret_key = 'minha_chave'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'usuario_bp.login'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
db.init_app(app)

@login_manager.user_loader
def user_loader(id):
    usuario = db.session.query(Usuario).filter_by(id=id).first()
    return usuario


app.register_blueprint(usuario_bp)

with app.app_context():
    if __name__ == '__main__':
        db.create_all()
    app.run(debug=True)