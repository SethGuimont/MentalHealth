from flask import Flask, render_template, request, url_for, flash, redirect
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


class BasicForm(Form):
    ids = StringField("ID", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/', methods=['POST', 'GET'])
def main():
    form = BasicForm()
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run()
