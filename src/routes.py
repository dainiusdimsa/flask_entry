from flask import render_template, request, redirect, url_for

from src import app
from src.forms import ContactForm
from src.helpers_func import is_leap_year


@app.route("/")
def get_base():
    return render_template('base.html')


@app.route("/all_leap")
def get_all_leap():
    years = []
    for year in range(1900, 2101):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            years.append(year)
    return render_template('keliamieji.html', years=years)


@app.route("/check_leap", methods=["GET", "POST"])
def check_leap():
    if request.method == "POST":
        input_year = int(request.form['year'])
        is_leap = is_leap_year(input_year)
        result = f"{input_year} yra {'KELIAMIEJI' if is_leap else 'NEKELIAMIEJI'} metai."
        return render_template("keliamieji_year.html", result=result)
    return render_template("keliamieji_year.html")


@app.route("/metai", methods=["GET", "POST"])
def add_years():
    if request.method == "POST":
        try:
            input_year = int(request.form['year'])
        except ValueError:
            input_year = 0
        is_leap = is_leap_year(input_year)
        result = f"{input_year} yra {'KELIAMIEJI' if is_leap else 'NEKELIAMIEJI'} metai."
        # return render_template("keliamieji_year.html", result=result)
        return redirect(url_for('year_leap', year=input_year))

    return render_template("keliamieji_year.html")


@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()
    if form.validate_on_submit():
        return render_template('contact_success.html', form=form)
    return render_template('contact_us.html', form=form)


@app.route("/metai/<int:year>")
def year_leap(year):
    is_leap = is_leap_year(year)
    result = f"{year} yra {'KELIAMIEJI' if is_leap else 'NEKELIAMIEJI'} metai."
    return render_template("year_leap.html", result=result)
