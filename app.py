from flask import Flask, render_template, request,redirect,url_for
import json
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, UploadSet,DATA
from flask_bootstrap import Bootstrap
from help import setData



app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_ATTACHMENTS_DEST'] = 'uploads/attachments'
Bootstrap(app)

attachments = UploadSet('attachments',DATA)
configure_uploads(app,attachments)

class MyForm(FlaskForm):
    file = FileField('file')

data = 0

@app.route('/', methods = ['GET','POST'])
def index():
    global data
    form = MyForm()
    filePath = "C:\\Users\\hernang2\\Documents\\Python\\flask_upload\\uploads\\attachments\\"
    if form.validate_on_submit():
        filename = attachments.save(form.file.data)
        #return f'FileName: { filename }'
        with open(filePath+str(filename), "r") as f:
            data = json.load(f)
        return redirect(url_for('display'))
    else:
        return render_template('index.html',form = form)

@app.route('/display', methods = ['GET','POST'])
def display():
    displayData = setData(data)
    show =[]
   # print(displayData)
    if request.method == 'POST':
        req = request.form['val']
        for sets in displayData:
            if req == sets[0]:
                show = sets[1]
        if len(show) == 0:
            show = displayData[0][1]

        return render_template('display.html', data = data,column_names=show.columns.values,row_data=list(show.values.tolist()), type = req,zip=zip)
    else:
        return render_template('display.html', data = data)



if __name__ == "__main__":
    app.run()
