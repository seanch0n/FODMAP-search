from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SelectField

class FODMAPForm(FlaskForm):
    search_key = SelectField(u'Search Key', choices=['low', 'high', 'either'], id='choice')
    search_term = StringField('Food:', id='food')