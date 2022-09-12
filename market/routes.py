from market import app
from flask import render_template
from market.forms import EmailSend
from market.util import get_gallery
from market.mail import send_message


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/<page>")
def gallery(page):
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
