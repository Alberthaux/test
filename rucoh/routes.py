from rucoh import app
from flask import render_template
from rucoh.forms import EmailSend
from rucoh.util import get_gallery
from rucoh.mail import send_message


@app.route("/")
def home0():
    return render_template('home.html')


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


@app.route("/mediterranee")
def mediterranee(page='mediterranee'):
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
