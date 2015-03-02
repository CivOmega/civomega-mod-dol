"""
Must define three methods:

* answer_pattern(pattern, args)
* render_answer_html(answer_data)
* render_answer_json(answer_data)
"""
from .patterns import PATTERNS, DOL_AGENCY_PATTERNS, LABOR_VIOLATION_PATTERNS

import xml.etree.ElementTree as ElementTree
import os
import re
import requests
from django.template import loader, Context
from django.conf import settings

# a regular expression so we can find the variables in
# the "blah blah pattern {variable}" patterns
PATTERN_ARGS_RE = re.compile(r'{([A-Za-z0-9_]+)}')


def get_api_key():
    key = None
    try:
        key = settings.DOL_API_KEY
    except:
        pass
    if 'FDA_API_KEY' in os.environ:
        key = os.environ['DOL_API_KEY']
    if key == None:
        raise Exception("To use this module, you must have a Department of Labor API Key.")
    else:
        return key

def agency_lookup():
    url = 'http://api.dol.gov/V1/DOLAgency/Agencies/?KEY=%s' %  (get_api_key())
    resp = requests.get(url, headers={'Accept':'application/json'})
    return resp.json()


def violation_lookup_by_city(city):
    url = 'http://api.dol.gov/V1/Compliance/WHD/full/?KEY=%s&$orderby=findings_start_date desc&$filter=city_nm eq \'%s\' and flsa_cl_violtn_cnt gt 0' %  (get_api_key(), city.title())
    resp = requests.get(url, headers={'Accept':'application/json'})
    print(resp.json())
    return resp.json()


############################################################
# Pattern-dependent behavior
def answer_pattern(pattern, args):
    """
    Returns a `dict` representing the answer to the given
    pattern & pattern args.
    """
    if pattern not in PATTERNS:
      # not one of our patterns
      return None
    if len(args) != 1:
      # we didn't actually search anything. (if this is a slow API, you can
      # change this to "len(args) < 5" to wait until a certain # of letters
      # are typed in before firing off your search to the API.)
      return None

    if pattern in DOL_AGENCY_PATTERNS:
        return {
          'type': 'agency_list',
          'data': agency_lookup()
        }
    if pattern in LABOR_VIOLATION_PATTERNS:
        # We might be looking up via zip code or text search, so see what
        # pattern the user used
        args_keys = PATTERN_ARGS_RE.findall(pattern)
        kwargs = dict(zip(args_keys,args))

        if "city" in kwargs:
            # a zipcode search
            city = kwargs['city']
            return {
              'type': 'labor_violations',
              'city': city,
              'data': violation_lookup_by_city(city)
            }

    return None




############################################################
# Applicable module-wide
def render_answer_html(answer_data):
    # This receives what we got in `answer_pattern` and returns HTML.
    if answer_data and answer_data.get('type', None) == "agency_list":
      data = answer_data['data']
      template = loader.get_template('comod_dol/agency_list.html')
      return template.render(Context(data))
    elif answer_data and answer_data.get('type', None) == "labor_violations":
      data = answer_data['data']
      template = loader.get_template('comod_dol/labor_violations.html')
      return template.render(Context(data))
    else:
      # TODO: render a template for "we don't know how to handle this search
      raise Exception

def render_answer_json(answer_data):
    return json.dumps(answer_data)
