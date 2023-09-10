from flask import Flask, render_template, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)


@app.route("/")
def mathify():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route("/about")
def about():
  return render_template('about.html')


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)

  if not job:
    return "Not Found", 404
  else:
    return render_template('jobdesc.html', job=job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submit.html', application=data, job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=1002, debug=True)
