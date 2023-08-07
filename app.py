from flask import Flask,render_template,request,redirect
from flask_migrate import Migrate
from models import db, WebPage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://titi:password@localhost:5432/short_urls_db"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://<username>:<password>@<server>:5432/<db_name>"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/your_short_url', methods = ['POST', 'GET'])
def short_url():
    if request.method == 'GET':
        return 'Get it via the url form'

    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = request.form['short_url']
        new_web_page = WebPage(long_url=long_url, short_url=short_url)
        db.session.add(new_web_page)
        db.session.commit()
        return f'Done!! Your_short_url is {short_url}'

@app.route('/<short_url>')
def redirect_to_url(short_url):
    web_page = WebPage.query.filter_by(short_url=short_url).first()
    # return f'{short_url} is here to make some noise!'
    if web_page:
        url = web_page.long_url
        print(url)
        return redirect(url, code=302)

    return f"This short url isn't in our database"


if __name__ == '__main__':
    app.run(debug=True)
