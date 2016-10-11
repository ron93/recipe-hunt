from flask import Flask,Blueprint,render_template

mod = Blueprint('admin',__name__,url_prefix='/admin')

@mod.route('/')
def admin():
    return render_template('admin/admin.html')