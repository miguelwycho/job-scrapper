
from flask import Flask
from services import scrapper
from models.job import JobModel
import json
app = Flask(__name__)

@app.route('/')
def get_test():
    return "FLASK IS WORKING..."

@app.route('/jobs')
def get_jobs():
    job_list:[JobModel] = []
    job_list = scrapper.get_job_from_info_jobs()
    print(len(job_list))
    json_string = json.dumps([ob.__dict__ for ob in job_list])
    return json_string

