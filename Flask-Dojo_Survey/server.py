from flask import Flask, render_template, request, redirect

app = Flask(__name__)

survey_info = []

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/get_info',methods=['POST'])
def get_info():
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
