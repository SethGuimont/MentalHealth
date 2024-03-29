from resources import list_files, download_file
from flask import Flask, render_template, request, send_file, redirect, url_for
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired
from scraper.crawler import *
from models import *



#https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
# Create db tables
with app.app_context():
    db.create_all()

BUCKET_NAME = 'mental-health-sxk-1'


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


@app.route('/files')
def files():
    contents = list_files(BUCKET_NAME)
    return render_template('files.html', contents=contents)


@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    BUCKET = BUCKET_NAME
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)


@app.route("/crawler_pdf")
def run_pdfcrawl():
    return render_template('pdf_crawler.html')


@app.route("/crawler_docx")
def run_docxcrawl():
    return render_template('docx_crawler.html')


@app.route("/employee_portal")
def employee_portal():
    return render_template("employee.html")


@app.route("/employee_login", methods=['GET', 'POST'])
def employee_login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' or request.form == 'admin':
            return redirect(url_for('employee_portal'))
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
