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

'''
Code will go here that routes a person to a specific bucket
Depending on state
if hit wisconsin button go to wisconsin bucket and etc....
They will be different forms attached to different buckets
'''
@app.route('/minnesota', methods=['POST', 'GET'])
def minnesota():
    min_form = BasicForm()
    return render_template('minnesota.html')

@app.route('/wisconsin', methods=['POST', 'GET'])
def wisconsin():
    wis_form = BasicForm()
    return render_template('wisconsin.html')


if __name__ == '__main__':
    app.run()
