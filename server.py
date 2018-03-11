from flask import Flask, render_template, request, redirect, session
import random
from time import gmtime, strftime
app = Flask(__name__)
app.secret_key = "ThisIsASecret"


# Index page.
@app.route('/')
def index(): 
    if 'gold' not in session.keys():
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
    golds = 0
    time = strftime("%Y/%m/%d %H:%M %p", gmtime())
    if request.form['building'] == 'farm':
        golds = random.randrange(10, 21)
        session['activities'].append({
            'message': "Earned {} golds from the Farm! ({})".format(golds, time),
            'color': 'green'
        })
    elif request.form['building'] == 'cave':
        golds = random.randrange(5, 11)
        session['activities'].append({
            'message': "Earned {} golds from the Cave! ({})".format(golds, time),
            'color': 'green'
        })
    elif request.form['building'] == 'house':
        golds = random.randrange(2, 6)
        session['activities'].append({
            'message': "Earned {} golds from the House! ({})".format(golds, time),
            'color': 'green'
        })
    elif request.form['building'] == 'casino':
        golds = random.randrange(-50, 51)
        if golds >= 0:
            session['activities'].append({
                'message': "Earned {} golds from the Casino! ({})".format(golds, time),
                'color': 'green'
            })
        else:
            session['activities'].append({
                'message': "Entered a Casino and lost {} golds... Ouch... ({})".format(abs(golds), time),
                'color': 'red'
            })

    session['gold'] += golds

    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.pop('gold')
    return redirect('/')

app.run(debug=True)
