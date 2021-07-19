from flask import Flask, render_template, request
import os.path
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, UploadSet,DATA


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_ATTACHMENTS_DEST'] = 'uploads/attachments'

attachments = UploadSet('attachments',DATA)
configure_uploads(app,attachments)

class MyForm(FlaskForm):
    file = FileField('file')


@app.route('/', methods = ['GET','POST'])
def index():
    form = MyForm()
    
    if form.validate_on_submit():
        filename = attachments.save(form.file.data)
        return f'FileName: { filename }'
    return render_template('index.html',form = form)


if __name__ == "__main__":
    app.run()
