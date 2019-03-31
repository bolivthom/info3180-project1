from flask_wtf import Form
from wtforms import TextField, IntegerField, \
   TextAreaField, SubmitField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import validators, ValidationError


class UploadForm(Form):
   upload = FileField('Upload Field', validators=[
      FileRequired(),
      FileAllowed(['jpg', 'png', 'Images only!'])
   ])
   submit = SubmitField("Send")


class ProfileForm(Form):
   firstname = TextField('First Name', validators=[validators.Required()])
   lastname = TextField('Last Name', validators=[validators.Required()])
   gender = SelectField(
      'Gender',
      choices=[('m', 'Male'), ('f', 'Female')],
      validators=[validators.Required()]
   )
   email = TextField('Email', validators=[validators.Required(), validators.Email()])
   location = TextField('Location', validators=[validators.Required()])
   biography = TextAreaField('Biography')
   photo = FileField('Profile Picture', validators=[
      # FileRequired(),
   ])
   submit = SubmitField('Add Profile')