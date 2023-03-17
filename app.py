from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1, 
    'title': 'Data Analyst',
    'location': 'Bangkok, Thailand',
    'salary': '$ 12,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Remote',
    'salary': '$ 15,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'San Fransisco, USA',
    'salary': '$ 12,500'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Sydney, Australia',
    'salary': '$ 14,000'
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Hannah')

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)