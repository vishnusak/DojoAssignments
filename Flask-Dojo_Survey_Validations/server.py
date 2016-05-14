from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)

app.secret_key = "43298u598fjfd4087d3h0d1847yd8743"

survey_info = []

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/get_info',methods=['POST'])
def get_info():
    if (len(request.form['name']) == 0):
        flash("NAME cannot be empty. Please fill in the NAME field")
        return redirect('/')
    elif (len(request.form['comment']) == 0):
        flash("COMMENT cannot be empty. Please fill in the COMMENT field")
        return redirect('/')
    elif (len(request.form['comment']) > 120):
        flash("COMMENT cannot be more than 120 characters long. Please modify the comment and re-submit")
        return redirect('/')
    else:
        info={}
        info['name'] = request.form['name']
        info['location'] = request.form['location']
        info['language'] = request.form['fav']
        info['comment'] = request.form['comment']
        survey_info.append(info)
        return redirect('/result')

@app.route('/result', methods=['GET', 'POST'])
def show_info():
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('result.html', name=survey_info[-1]['name'], location=survey_info[-1]['location'],language=survey_info[-1]['language'],comment=survey_info[-1]['comment'])

@app.route('/showall', methods=['POST','GET'])
def show_all():
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('showall.html',info=survey_info)

app.debug = True
app.run()
