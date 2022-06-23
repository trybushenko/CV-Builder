from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row

class ContactForm(forms.Form):
	name=forms.CharField()#required=False
	email=forms.EmailField(label='E-Mail')
	mobile=forms.CharField()
	address=forms.CharField()
	skills_1=forms.CharField(label='Skill 1')
	skills_2=forms.CharField(label='Skill 2')
	skills_3=forms.CharField(required=False, label='Skill 3')
	skills_4=forms.CharField(required=False, label='Skill 4')

	experience_1_title=forms.CharField(label='Work or Volunteer Experience №1 title')
	experience_1_dur=forms.CharField(label='Work or Volunteer Experience №1 duration')
	experience_1_desc=forms.CharField(label='Work or Volunteer Experience №1 description')

	experience_2_title=forms.CharField(required=False, label='Work or Volunteer Experience №2 title')
	experience_2_dur=forms.CharField(required=False, label='Work or Volunteer Experience №2 duration')
	experience_2_desc=forms.CharField(required=False, label='Work or Volunteer Experience №2 description')

	education_1=forms.CharField(label='Education №1 title')
	education_1_dur=forms.CharField(label='Education №1 duration')
	education1_score=forms.CharField(label='Education №1 score')

	education_2=forms.CharField(label='Education №2 title')
	education_2_dur=forms.CharField(label='Education №2 duration')
	education2_score=forms.CharField(label='Education №2 score')

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper
		self.helper.form_class = ' container justify-content-center '
		self.helper.form_method="post"
		self.helper.layout=Layout(
			Row(
                Column('name', css_class='form-group col-md-5  mb-10'),
                Column('email', css_class='form-group col-md-7 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('mobile', css_class='form-group col-md-5  mb-10'),
                Column('address', css_class='form-group col-md-7 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('skills_1', css_class='form-group col-md-6  mb-10'),
                Column('skills_2', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('skills_3', css_class='form-group col-md-6  mb-10'),
                Column('skills_4', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('experience_1_title', css_class='form-group col-md-7  mb-10'),
                Column('experience_1_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
			'experience_1_desc',
			Row(
                Column('experience_2_title', css_class='form-group col-md-7  mb-10'),
                Column('experience_2_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
			'experience_2_desc',
			'education_1',
			Row(
                Column('education_1_dur', css_class='form-group col-md-6 mb-10'),
                Column('education1_score', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			'education_2',
			Row(
                Column('education_2_dur', css_class='form-group col-md-6  mb-10'),
                Column('education2_score', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Submit('submit','Submit',css_class="btn-success")
			)