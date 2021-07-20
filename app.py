from flask import Flask, render_template, request
import json
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, UploadSet,DATA
from flask_bootstrap import Bootstrap



app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_ATTACHMENTS_DEST'] = 'uploads/attachments'
Bootstrap(app)

attachments = UploadSet('attachments',DATA)
configure_uploads(app,attachments)

class MyForm(FlaskForm):
    file = FileField('file')


@app.route('/', methods = ['GET','POST'])
def index():
    form = MyForm()
    filePath = "C:\\Users\\hernang2\\Documents\\Python\\flask_upload\\uploads\\attachments\\"
    if form.validate_on_submit():
        filename = attachments.save(form.file.data)
        #return f'FileName: { filename }'
        with open(filePath+str(filename), "r") as f:
            data = json.load(f)

        return render_template('display.html',data = data)
    return render_template('index.html',form = form)

@app.route('/display', methods = ['GET','POST'])
def display():
    #form = MyForm()
    #if form.validate_on_submit():

    return render_template('display.html')

if __name__ == "__main__":
    app.run()
