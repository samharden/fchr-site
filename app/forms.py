from flask import flash, Markup
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, RadioField, SelectField, TextField, TextAreaField, validators
from wtforms.validators import DataRequired

class frontpage(Form):
    complaint_or_search = SelectField('complaint_or_search', choices=[('complaint','Begin FCHR Complaint'),
                                            ('search', 'Search FCHR Decisions')],
                                            default="", validators=[DataRequired()])

class searchform(Form):
    searchall = TextAreaField('searchall')

    def validate(self):
        if not Form.validate(self):
            #print "not form validate"
            if "<" in self.searchall.data:
                #info = Markup("<h2 style='color:red'> Really? Try Harder. </h2>")
                #<img src="/static/500_error.jpg">
                info = Markup("<img src='/static/hackers.jpg'>")
                flash(info)
                return False
            elif self.searchall.data:
                #print "Should return True"
                return True
            #print "Should return False"
            info = Markup('<h2 style="color:red"> Must enter at least one search term. </h2>')
            flash(info)
            return False
        return True


class complaintform(Form):
    what_kind_complaint = SelectField('what_kind_complaint', choices=[
                                            ('emp','Employment'),
                                            ('housing', 'Housing'),
                                            ('pub_acc', 'Public Accomodation')
                                            ],
                                            default="", validators=[DataRequired()])


class pub_acc(Form):
    #1. Personal Information
    complaintant_lastname = TextField('complaintant_lastname', validators=[DataRequired()])
    complaintant_firstname = TextField('complaintant_firstname')
    complaintant_mi = TextField('complaintant_mi')
    complaintant_streetaddress = TextField('complaintant_streetaddress')
    complaintant_aptnum = TextField('complaintant_aptnum')
    complaintant_city = TextField('complaintant_city')
    complaintant_county = TextField('complaintant_county')
    complaintant_state = SelectField('complaintant_state', choices=[
                                    ('AL','AL'),
                                    ('FL','FL'),
                                    ('GA','GA'),
                                    ])
    complaintant_zip = TextField('complaintant_zip')
    complaintant_phone = TextField('complaintant_phone')
    complaintant_email = TextField('complaintant_email')
    complaintant_dob = TextField('complaintant_dob')
    complaintant_sex = SelectField('complaintant_sex', choices=[
                                    ('Female','Female'),
                                    ('Male','Male'),
                                    ('N/A','N/A')
                                    ])

    #2.	Please provide the name of a person we can contact if we are unable to reach you:
    otherperson_rel = TextField('otherperson_rel')
    otherperson_lastname = TextField('otherperson_lastname')
    otherperson_firstname = TextField('otherperson_firstname')
    otherperson_mi = TextField('otherperson_mi')
    otherperson_streetaddress = TextField('otherperson_streetaddress')
    otherperson_aptnum = TextField('otherperson_aptnum')
    otherperson_city = TextField('otherperson_city')
    otherperson_county = TextField('otherperson_county')
    otherperson_state = SelectField('otherperson_state', choices=[
                                    ('AL','AL'),
                                    ('FL','FL'),
                                    ('GA','GA'),
                                    ])
    otherperson_zip = TextField('otherperson_zip')
    otherperson_phone = TextField('otherperson_phone')
    #3.	I believe that I was discriminated against by the following organization(s):
    organization_name = TextField('organization_name')
    organization_streetaddress = TextField('organization_streetaddress')
    organization_city = TextField('organization_city')
    organization_county = TextField('organization_county')
    organization_state = SelectField('organization_state', choices=[
                                    ('fl','FL')
                                    ])
    organization_zip = TextField('organization_zip')
    organization_phone = TextField('organization_phone')
    organization_type = TextField('organization_type')
    organization_owner = TextField('organization_owner')
    organization_ownerphone = TextField('organization_ownerphone')

    #4. Organization Representative Contact Information (If known):
    org_pr_name = TextField('org_pr_name')
    org_pr_streetaddress = TextField('org_pr_streetaddress')
    org_pr_city = TextField('org_pr_city')
    org_pr_county = TextField('org_pr_county')
    org_pr_state = SelectField('org_pr_state', choices=[
                                    ('fl','FL')
                                    ])
    org_pr_zip = TextField('org_pr_zip')
    org_pr_phone = TextField('org_pr_phone')

    #5. What is the reason for your claim of public accomodation discrimination?

    reason_race = BooleanField('reason_race')
    reason_race_choose = SelectField('reason_race_choose', choices=[
                                    ('black','Black'),
                                    ('white','White'),
                                    ('asian','Asian'),
                                    ('nhpi','Nat. Hawaiian / Pac. Islander'),
                                    ('amerindian','American Indian')
                                    ])
    reason_color = BooleanField('reason_color')
    reason_color_choose = SelectField('reason_color_choose', choices=[
                                    ('lightskinned','Light Skinned'),
                                    ('darkskinned','Dark Skinned'),
                                    ('other','Other')
                                    ])
    reason_natorigin = BooleanField('reason_natorigin')
    reason_natorigin_choose = SelectField('reason_natorigin_choose', choices=[
                                    ('hisp','Hispanic'),
                                    ('mex','Mexican'),
                                    ('mideast','Middle Eastern'),
                                    ('eastindian','East Indian'),
                                    ('asian','Asian'),
                                    ('northafrican','Northern African'),
                                    ('southafrican','Southern African')
                                    ])
    reason_sex = BooleanField('reason_sex')
    reason_sex_choose = SelectField('reason_sex_choose', choices=[
                                    ('female','Female'),
                                    ('male','Male'),
                                    ('other','Other'),
                                    ('trans','Trans')
                                    ])
    reason_preg = BooleanField('reason_preg')
    reason_religion = BooleanField('reason_religion')
    reason_disability = BooleanField('reason_disability')
    reason_disability_choose = SelectField('reason_disability_choose', choices=[
                                    ('phys','Physical'),
                                    ('ment','Mental')
                                    ])
    reason_familial_status = BooleanField('reason_familial_status')
    reason_other = BooleanField('reason_other')

    #6.	What happened to you that you believe was discriminatory?
    #Include the date(s) of harm, the action(s), and the name(s) and title(s)
    #of the person(s) who you believe discriminated against you. Please attach
    #additional pages if needed.
    harm_description = TextAreaField('harm_description')

    def validate(self):
        if not Form.validate(self):
            #print "not form validate"
            if "<" in self.complaintant_lastname.data:
                #info = Markup("<h2 style='color:red'> Really? Try Harder. </h2>")
                #<img src="/static/500_error.jpg">
                info = Markup("<img src='/static/hackers.jpg'>")
                flash(info)
                return False
            elif self.complaintant_lastname.data:
                #print "Should return True"
                return True
            #print "Should return False"
            info = Markup('<h2 style="color:red"> Must enter something. </h2>')
            flash(info)
            return False
        return True
