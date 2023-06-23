from flask import render_template, request, redirect, url_for
import forms
from searching import search


def index():
    """ generate form for html page
    """
    form = forms.FODMAPForm()
    return render_template('index.html', form=form)


def submitted():
    if request.method == 'POST':
        search_key = request.form['search_key']
        search_term = request.form['search_term']

        # fuzzywuzzybuddy
        ret = search(search_key, search_term)
        ret_dict = {"ret": ret, "key": search_key, "search_term":search_term}


    return render_template('results.html', results=ret_dict)