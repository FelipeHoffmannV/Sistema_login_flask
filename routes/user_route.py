from flask import Blueprint, redirect, render_template, request, url_for, flash
from db.db import db
from models.models import Usuario 
from flask_login import LoginManager, login_user, login_required, logout_user


usuario_bp = Blueprint('usuario_bp', __name__)
lm = LoginManager()
lm.init_app(usuario_bp)

@lm.user_loader
def user_loader(id):
    user = db.session.query(Usuario).filter_by(id=id).first()
    return user

@usuario_bp.route('/')
@login_required
def home():
    return render_template('home.html')


@usuario_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        senha = request.form['senhaForm']
        
        new_user = Usuario(nome=nome)
 
        new_user.set_password(senha) 

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('usuario_bp.home'))
    

@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    nome = request.form['nomeForm']
    senha = request.form['senhaForm']

    user = Usuario.query.filter_by(nome=nome).first()

    if not user:
        return 'Usuário não cadastrado ou senha incorreta'


    if user.check_password(senha):
        login_user(user)

        return redirect(url_for('usuario_bp.home'))
    else:

        return 'Senha incorreta'


@usuario_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('usuario_bp.home'))
