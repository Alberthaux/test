from app import app
from flask import render_template, url_for, redirect
from app.forms import EmailSend
from app.util import get_gallery
from app.mail import send_message


@app.route("/")
def home0():
    return redirect(url_for('gallery'))


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/lifedrawing")
def gallery(page='lifedrawing'):
    return render_template('gallery.html',
                           page=page,
                           dir_list=get_gallery(page))


@app.route("/sls")
def sls(page='sls'):
    return render_template('gallery.html',
                           page=page,
                           dir_list=get_gallery(page))


@app.route("/3d")
def mediterranee(page='3d'):
    return render_template('gallery.html',
                           page=page,
                           dir_list=get_gallery(page))


@app.route("/contact", methods=['GET', 'POST'])
def contactform():
    form = EmailSend()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.msg.data
        send_message(name, email, message)
    return render_template('contact.html',
                           form=form)
