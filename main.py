import boto3
from flask import Flask, render_template, request, url_for, flash, redirect
#from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired

s3 = boto3.client('')

app = Flask(__name__)


class BasicForm(Form):
    ids = StringField("ID", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def main():
    return render_template("index.html")


'''
Code will go here that routes a person to a specific bucket
Depending on state
if hit wisconsin button go to wisconsin bucket and etc....
They will be different forms attached to different buckets
'''


@app.route('/minnesota', methods=['POST', 'GET'])
def minnesota():
    min_form = BasicForm()
    return render_template('minnesota.html', min_form=min_form)


@app.route('/wisconsin', methods=['POST', 'GET'])
def wisconsin():
    wis_form = BasicForm()
    return render_template('wisconsin.html', wis_form=wis_form)


if __name__ == '__main__':
    app.run()
