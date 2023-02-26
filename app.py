from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 'jobnumber1',
  'title': 'Bathroom Tile1',
  'location': 'Delta1, UT',
  'salary': '$10,000',
}, {
  'id': 'jobnumber2',
  'title': 'Bathroom Tile2',
  'location': 'Salt Lake City2, UT',
  'salary': '$20,000',
}, {
  'id': 'jobnumber3',
  'title': 'Bathroom Tile3',
  'location': 'Delta3, UT',
  'salary': '$30,000',
}, {
  'id': 'jobnumber4',
  'title': 'Bathroom Tile4',
  'location': 'Delta4, UT',
  'salary': '$40,000',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Xyzentmts')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
