from flask import Flask
application = Flask(__name__)
from flask import request, url_for
from flask import render_template
import urllib
import json
def coordinate(word):
    url = str("http://search-try-3ipj2efmrnrm5xbc6pipto25ay.us-east-1.cloudsearch.amazonaws.com/2013-01-01/search?q=" + word + "&size=10000")
    f = urllib.urlopen(url)
    myfile = f.read()
    dic = eval(myfile)
    output_coord = []
    output_content = []
    for line in dic['hits']['hit']:
        coord = [float(line['fields']['coordinates'][1]),float(line['fields']['coordinates'][0]),line['fields']['text']]
        output_coord.append(coord)
    return output_coord

from flask import session

@application.route('/search')
def search():
    return render_template('ent.html')


@application.route('/result', methods=['POST'])
def result():
    q1 = request.form['word']
    asd = coordinate(q1)
    counter = len(asd)
    #print content
    #word = request.form['word']
    #tea = coordinate(str(word))
    return render_template('search2.html',word = q1, counter = counter, posts=asd)



@application.route('/')
def index():
    return 'Index Page'



@application.route('/hello/')
@application.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@application.route('/projects/')
def projects():
    return 'The project page'

@application.route('/about')
def about():
    return 'The about page'



@application.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
	application.run(debug=True)
