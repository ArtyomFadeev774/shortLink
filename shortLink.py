from flask import render_template, Flask, redirect, request
app = Flask(__name__)

links = {}

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/api')
def api():
    data = request.args.get('link1')
    key = str(hash(data))[0:6]
    if key in links:
        pass
    else:
        links[key] = data
    print(links)
    link = request.base_url + '/' + key
    return f'<a href="{link}">{link}</a>'

@app.route('/api/<link>')
def test(link):
    print(type(links[link]))
    return redirect(links[link])

app.run(debug=True)
