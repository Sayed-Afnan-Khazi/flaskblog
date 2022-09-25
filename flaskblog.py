from flask import Flask, render_template,url_for, flash, redirect

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asieaubciebc'

posts = [
    {
        'title':"My first post!",
        'author':"Jane Watson",
        'post_content':"Testing out flask!!",
        'date_posted':"10-10-2019"
    },
    {
        'title':"My second post!",
        'author':"Jane Watson",
        'post_content':"Testing out flask 2!!",
        'date_posted':"11-10-2019"
    }
]

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html", posts = posts)

@app.route("/about")
def about():
    return render_template("about.html", title="Epic title")

@app.route("/register" 
        # ,methods = ['GET', 'POST']
        )
def register():
    form = RegistrationForm()
    # if form.validate_on_submit(): 
    #     flash(f"Account Created for {form.username.data}!", "success") # Bootstrap class success
    #     return redirect(url_for("home"))
    return render_template("register.html", title = "Register", form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("register.html", title = "Login", form = form)

if __name__ == "__main__":
    app.run(debug = True)
