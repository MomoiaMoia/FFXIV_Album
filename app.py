from flask import Flask,request
from flask.helpers import flash
from flask.templating import render_template, render_template_string
from werkzeug.utils import redirect
from flask_login import login_user, login_required
from flask_login import LoginManager
from flask_login import logout_user
from user_login import User
import os
import configparser




#实例主程序
app = Flask(__name__)
app.secret_key="secret string"
#配置
app.config['check'] = True
# 实例登录模组
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login_api'
login_manager.init_app(app)
#用户引导，请勿修改
@login_manager.user_loader
def load_user(user_id):
    user = User(1,"我将轻声叹息将往事回顾","temp")
    return user

@app.route("/")
def main_page():
    print(app.config.get("check"))
    if app.config.get("check"):
        return render_template("desktop/index.html")
    return render_template("desktop/index2.html")

@app.route("/api",methods=['GET','POST'])
def login_api():
    if request:
        user = load_user(1)
        print(request.form.get('pwd'))
        pwd = request.form.get("pwd")
        if user.is_authenticated(pwd):
            login_user(user, remember=True)
            return render_template_string("Thanks")
        else:
            flash("拒绝访问")
            return redirect("/")


@app.route("/delall")
def del_all():
    app.config['check'] = False
    print("Shutdown Success")
    return redirect("/logout")

@app.route("/index")
@login_required
def index_page():
    return render_template('desktop/main.html')


@app.route("/ourmeet")
@login_required
def memory_one():
    return render_template("desktop/ourmeet.html")


@app.route("/ournewyear")
@login_required
def memory_two():
    return render_template("desktop/ournewyear.html")


@app.route("/our****")
@login_required
def memory_three():
    return render_template("desktop/our____.html")


@app.route("/journey-of-the-white-knight")
@login_required
def memory_four():
    return render_template("desktop/journey-of-the-white-knight.html")


@app.route("/ourmemory")
@login_required
def memory_five():
    return render_template("desktop/ourmemory.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)