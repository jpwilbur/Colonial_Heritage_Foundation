# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455917313.6176686
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/venues.html'
_template_uri = 'venues.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['full_length_content', 'above_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def full_length_content():
            return render_full_length_content(context._locals(__M_locals))
        venues = context.get('venues', UNDEFINED)
        def above_content():
            return render_above_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'above_content'):
            context['self'].above_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'full_length_content'):
            context['self'].full_length_content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_full_length_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def full_length_content():
            return render_full_length_content(context)
        venues = context.get('venues', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <p class="text-right"><a id="createvenuelink" class="btn btn-primary">Create Venue</a></p>\r\n\r\n  <table class="table table-striped">\r\n    <tr>\r\n      <th>Venue Name</th>\r\n      <th>Address</th>\r\n      <th>City</th>\r\n      <th>State</th>\r\n      <th>Zipcode</th>\r\n      <th>Phone Number</th>\r\n      <th>Contact Name</th>\r\n      <th>Actions</th>\r\n    </tr>\r\n\r\n')
        for venue in venues:
            __M_writer('      <tr>\r\n        <td> ')
            __M_writer(str(venue.venueName))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(venue.address))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(venue.city))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(venue.state))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(venue.zipcode))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(venue.phoneNumber))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(venue.contactName))
            __M_writer(' </td>\r\n        <td>\r\n          <a data-vid = ')
            __M_writer(str( venue.id ))
            __M_writer(' data-toggle="modal" class="editvenuelink">Edit</a> |\r\n          <a data-vid = ')
            __M_writer(str( venue.id ))
            __M_writer(' data-toggle="modal" class="delete_button deletelink">Delete</a>\r\n        </td>\r\n      </tr>\r\n')
        __M_writer('  </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_above_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_content():
            return render_above_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <h3>All Venues</h3>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "venues.html", "source_encoding": "utf-8", "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/venues.html", "line_map": {"64": 24, "65": 24, "66": 25, "67": 25, "68": 26, "69": 26, "70": 27, "71": 27, "72": 28, "73": 28, "74": 29, "75": 29, "76": 30, "77": 30, "78": 32, "79": 32, "80": 33, "81": 33, "82": 37, "88": 3, "28": 0, "94": 3, "100": 94, "38": 1, "43": 5, "48": 38, "54": 7, "61": 7, "62": 22, "63": 23}}
__M_END_METADATA
"""
