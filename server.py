from email.quoprimime import quote
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
        
def write_to_contact(data):
    with open('database_contact.csv', newline='', mode="a") as contact_database:
        name = (data['name']).title()
        email = data["email"]
        country_code = data["country_code"]
        phone = data["phone"]
        message = data["message"]
        csv_writer = csv.writer(contact_database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, country_code, phone, message])
        
@app.route('/contact_form', methods=['POST', 'GET'])
def contact_us():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_contact(data)
            return redirect('/thankcontact.html')
        except:
            return 'Your Work didn\'t save'
    else:
        return "ERROR 404 Cannot Contact"
    
def write_to_jobs(data):
    with open('database_jobs.csv', newline='', mode="a") as job_database:
        first_name = (data['firstname']).title()
        last_name = (data['lastname']).title()
        gender = data["gender"]
        birthday = data["birthday"]
        qualification = data["qualification"]
        username = data["username"]
        password = data["password"]
        country_code = data["country_code"]
        phone = data["phone"]
        email = data["email"]
        bio = data["bio"]
        csv_writer = csv.writer(job_database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([first_name, last_name, gender, birthday, qualification, username, password, country_code, phone, email, bio])

@app.route('/job_form', methods=['POST', 'GET'])
def jobs():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_jobs(data)
            return redirect('/thankjob.html')
        except:
            return 'Form not Submitted please try again'
    else:
        return "ERROR 404 Application not Submitted"
