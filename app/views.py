from flask import render_template, flash, redirect, url_for, session, Markup, request, g
from app import app
from app import models as mdl
from .forms import frontpage, searchform, complaintform, pub_acc
from flask.ext.login import login_user, logout_user, current_user, login_required



print "Top of Views"
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    print "Top of index"
    form = frontpage()
    session['complaint_or_search'] = form.complaint_or_search.data

    complaint_or_search = session['complaint_or_search']

    if complaint_or_search == 'search':
        return redirect(url_for('search'))
    elif complaint_or_search == 'complaint':
        return redirect(url_for('choose_complaint_type'))

    return render_template('index.html',
                           title='FCHR Assistant',
                           form=form,
                          )

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = searchform()
    session['searchall'] = form.searchall.data

    searchall = session['searchall']


    return render_template('search.html',
                           title='FCHR Opinion Search.html',
                           form=form
                           )

@app.route('/choose-complaint-type', methods=['GET', 'POST'])
def choose_complaint_type():
    form = complaintform()
    session['what_kind_complaint'] = form.what_kind_complaint.data

    what_kind_complaint = session['what_kind_complaint']

    if what_kind_complaint == 'pub_acc':
        return redirect(url_for('pub_acc_complaint_assistant'))
    elif what_kind_complaint == '':
        pass


    return render_template('choose-complaint-type.html',
                           title='Complaint Builder',
                           form=form
                           )

@app.route('/pub-acc-complaint-assistant', methods=['GET', 'POST'])
def pub_acc_complaint_assistant():
    form = pub_acc()

    if form.validate_on_submit():
        session['complaintant_lastname'] = form.complaintant_lastname._value()
        session['complaintant_firstname'] = form.complaintant_firstname._value()
        session['complaintant_mi'] = form.complaintant_mi._value()
        session['complaintant_streetaddress'] = form.complaintant_streetaddress._value()
        session['complaintant_aptnum'] = form.complaintant_aptnum._value()
        session['complaintant_city'] = form.complaintant_city._value()
        session['complaintant_county'] = form.complaintant_county._value()
        session['complaintant_state'] = form.complaintant_state.data
        session['complaintant_zip'] = form.complaintant_zip._value()
        session['complaintant_phone'] = form.complaintant_phone._value()
        session['complaintant_email'] = form.complaintant_email._value()
        session['complaintant_dob'] = form.complaintant_dob._value()
        session['complaintant_sex'] = form.complaintant_sex.data


        session['otherperson_rel'] = form.otherperson_rel._value()
        session['otherperson_lastname'] = form.otherperson_lastname._value()
        session['otherperson_firstname'] = form.otherperson_firstname._value()
        session['otherperson_mi'] = form.otherperson_mi._value()
        session['otherperson_streetaddress'] = form.otherperson_streetaddress._value()
        session['otherperson_aptnum'] = form.otherperson_aptnum._value()
        session['otherperson_city'] = form.otherperson_city._value()
        session['otherperson_state'] = form.otherperson_state.data
        session['otherperson_zip'] = form.otherperson_zip._value()
        session['otherperson_phone'] = form.otherperson_phone._value()

        session['organization_name'] = form.organization_name._value()
        session['organization_streetaddress'] = form.organization_streetaddress._value()
        session['organization_city'] = form.organization_city._value()
        session['organization_county'] = form.organization_county._value()
        session['organization_state'] = form.organization_state.data
        session['organization_zip'] = form.organization_zip._value
        session['organization_phone'] = form.organization_phone._value()
        session['organization_type'] = form.organization_type._value()
        session['organization_owner'] = form.organization_owner._value()
        session['organization_ownerphone'] = form.organization_ownerphone._value()

        session['org_pr_name'] = form.org_pr_name._value()
        session['org_pr_streetaddress'] = form.org_pr_streetaddress._value()
        session['org_pr_city'] = form.org_pr_city._value()
        session['org_pr_county'] = form.org_pr_county._value()
        session['org_pr_state'] = form.org_pr_state.data
        session['org_pr_zip'] = form.org_pr_zip._value()
        session['org_pr_phone'] = form.org_pr_phone._value()

        session['reason_color'] = form.reason_color.data
        session['reason_color_choose'] = form.reason_color_choose.data
        session['reason_natorigin'] = form.reason_natorigin.data
        session['reason_natorigin_choose'] = form.reason_natorigin_choose.data
        session['reason_sex'] = form.reason_sex.data
        session['reason_sex_choose'] = form.reason_sex_choose.data
        session['reason_preg'] = form.reason_preg.data
        session['reason_religion'] = form.reason_religion.data
        session['reason_disability'] = form.reason_disability.data
        session['reason_disability_choose'] = form.reason_disability_choose.data
        session['reason_familial_status'] = form.reason_familial_status.data
        session['reason_race'] = form.reason_race.data
        session['reason_race_choose'] = form.reason_race_choose.data

        session['harm_description'] = form.harm_description._value()

        session['reason_other'] = form.reason_other.data
        return redirect(url_for('publicaccomodationcomplaint'))
    else:
        pass

    return render_template('pub-acc-complaint-assistant.html',
                           title='Public Access Builder.html',
                           form=form
                           )

@app.route('/public-accomodation-complaint', methods=['GET', 'POST'])
def publicaccomodationcomplaint():
    form = pub_acc
    complaintant_lastname = session['complaintant_lastname']
    complaintant_firstname = session['complaintant_firstname']
    complaintant_mi = session['complaintant_mi']
    complaintant_streetaddress = session['complaintant_streetaddress']
    complaintant_city = session['complaintant_city']
    complaintant_county = session['complaintant_county']
    complaintant_state = session['complaintant_state']
    complaintant_zip = session['complaintant_zip']
    complaintant_phone = session['complaintant_phone']
    complaintant_email = session['complaintant_email']
    complaintant_dob = session['complaintant_dob']
    complaintant_sex = session['complaintant_sex']

    otherperson_rel = session['otherperson_rel']
    otherperson_lastname = session['otherperson_lastname']
    otherperson_firstname = session['otherperson_firstname']
    otherperson_mi = session['otherperson_mi']
    otherperson_streetaddress = session['otherperson_streetaddress']
    otherperson_aptnum = session['otherperson_aptnum']
    otherperson_city = session['otherperson_city']
    otherperson_state = session['otherperson_state']
    otherperson_zip = session['otherperson_zip']
    otherperson_phone = session['otherperson_phone']

    #3.	I believe that I was discriminated against by the following organization(s):
    organization_name = session['organization_name']
    organization_streetaddress = session['organization_streetaddress']
    organization_city = session['organization_city']
    organization_county = session['organization_county']
    organization_state = session['organization_state']
    organization_zip = session['organization_zip']
    organization_phone = session['organization_phone']
    organization_type = session['organization_type']
    organization_owner = session['organization_owner']
    organization_ownerphone = session['organization_ownerphone']

    org_pr_name = session['org_pr_name']
    org_pr_streetaddress = session['org_pr_streetaddress']
    org_pr_city = session['org_pr_city']
    org_pr_county = session['org_pr_county']
    org_pr_state = session['org_pr_state']
    org_pr_zip = session['org_pr_zip']
    org_pr_phone = session['org_pr_phone']

    reason_race = session['reason_race']
    reason_race_choose = session['reason_race_choose']
    reason_color = session['reason_color']
    reason_color_choose = session['reason_color_choose']
    reason_natorigin = session['reason_natorigin']
    reason_natorigin_choose = session['reason_natorigin_choose']
    reason_sex = session['reason_sex']
    reason_sex_choose = session['reason_sex_choose']
    reason_preg = session['reason_preg']
    reason_religion = session['reason_religion']
    reason_disability = session['reason_disability']
    reason_disability_choose = session['reason_disability_choose']
    reason_familial_status = session['reason_familial_status']
    reason_other = session['reason_other']

    harm_description = session['harm_description']

    if reason_race == True:
        reason_race = "Yes"
    else:
        reason_race = "No"
        reason_race_choose = "N/A"




    if reason_other == True:
        reason_other = "Yes"
    else:
        reason_other = "No"

    return render_template('public-accomodation-complaint.html',
                           title='Public Accomodation Complaint',
                           complaintant_lastname=complaintant_lastname,
                           complaintant_firstname=complaintant_firstname,
                           complaintant_mi=complaintant_mi,
                           complaintant_streetaddress=complaintant_streetaddress,
                           complaintant_city=complaintant_city,
                           complaintant_county=complaintant_county,
                           complaintant_state=complaintant_state,
                           complaintant_zip=complaintant_zip,
                           complaintant_phone=complaintant_phone,
                           complaintant_email=complaintant_email,
                           complaintant_dob=complaintant_dob,
                           complaintant_sex=complaintant_sex,

                           otherperson_rel=otherperson_rel,
                           otherperson_lastname=otherperson_lastname,
                           otherperson_firstname=otherperson_firstname,
                           otherperson_mi=otherperson_mi,
                           otherperson_streetaddress=otherperson_streetaddress,
                           otherperson_aptnum=otherperson_aptnum,
                           otherperson_city=otherperson_city,
                           otherperson_state=otherperson_state,
                           otherperson_zip=otherperson_zip,
                           otherperson_phone=otherperson_phone,

                           organization_name=organization_name,
                           organization_streetaddress=organization_streetaddress,
                           organization_city=organization_city,
                           organization_county=organization_county,
                           organization_state=organization_state,
                           organization_zip=organization_zip,
                           organization_phone=organization_phone,
                           organization_type=organization_type,
                           organization_owner=organization_owner,
                           organization_ownerphone=organization_ownerphone,

                           org_pr_name=org_pr_name,
                           org_pr_streetaddress=org_pr_streetaddress,
                           org_pr_city=org_pr_city,
                           org_pr_county=org_pr_county,
                           org_pr_state=org_pr_state,
                           org_pr_zip=org_pr_zip,
                           org_pr_phone=org_pr_phone,

                           reason_race=reason_race,
                           reason_race_choose=reason_race_choose,
                           reason_color=reason_color,
                           reason_color_choose=reason_color_choose,
                           reason_natorigin=reason_natorigin,
                           reason_sex=reason_sex,
                           reason_sex_choose=reason_sex_choose,
                           reason_preg=reason_preg,
                           reason_religion=reason_religion,
                           reason_disability=reason_disability,
                           reason_disability_choose=reason_disability_choose,
                           reason_familial_status=reason_familial_status,
                           reason_other=reason_other,

                           harm_description=harm_description,
                           )



@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml')

@app.route('/Stylesheet.css')
def stylesheet():
    return render_template('stylesheet.css')

@app.route('/confirm_text_info')
def text_info():
    return render_template('confirm_text_info.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    #db.session.rollback()
    return render_template('500.html'), 500
