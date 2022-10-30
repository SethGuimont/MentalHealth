import os
import boto3
from flask import Flask, render_template, request, url_for, flash, redirect, flash, \
    Response, session
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename

# s3 = boto3.client('')

app = Flask(__name__)
app.config['DEBUG'] = True


BUCKET_NAME = 'medformmadeeasy'


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


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


'''
Routes below are for forms and listing off s3 contents
'''


@app.route('/files')
def files():
    my_bucket = BUCKET_NAME
    #summeries = my_bucket.objects.all()
    return render_template('files.html', my_bucket=my_bucket) #, files=summeries)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    my_bucket = BUCKET_NAME
    my_bucket.Object(file.filename).put(Body=file)
    flash('File uploaded successfully')
    return redirect(url_for('files'))


@app.route('/download', methods=['POST'])
def download():
    key = request.form['key']

    s3_resource = boto3.resource('s3')
    my_bucket = BUCKET_NAME

    file_obj = my_bucket.Object(key).get()

    return Response(
        file_obj['BODY'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
    )


if __name__ == '__main__':
    app.run()
