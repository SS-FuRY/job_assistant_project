from flask import Blueprint, render_template, request, redirect, url_for
import os
from app.resume_parser import parse_resume
from app.job_scraper import search_jobs
from app.auto_apply import auto_apply_to_jobs
from app.tracker import add_jobs, get_all_jobs
from werkzeug.utils import secure_filename

routes = Blueprint('routes', __name__)
UPLOAD_FOLDER = 'data/resumes/'

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/upload', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        file = request.files['resume']
        if file:
            filename = secure_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)

            resume_data = parse_resume(path)
            return render_template('preferences.html', resume_data=resume_data)

    return render_template('upload.html')

@routes.route('/preferences', methods=['POST'])
def handle_preferences():
    role = request.form.get('role')
    location = request.form.get('location')
    
    jobs = search_jobs(role, location)
    applied = auto_apply_to_jobs(jobs)
    add_jobs(applied)

    return redirect(url_for('routes.dashboard'))

@routes.route('/dashboard')
def dashboard():
    job_list = get_all_jobs()
    return render_template('dashboard.html', jobs=job_list)
