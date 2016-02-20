# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455988214.5050855
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/editvenue.html'
_template_uri = 'editvenue.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['center_content']


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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        venueid = context.get('venueid', UNDEFINED)
        def center_content():
            return render_center_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        venueid = context.get('venueid', UNDEFINED)
        def center_content():
            return render_center_content(context)
        form = context.get('form', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <form id="editvenueform" action="/catalog/venues.edit/')
        __M_writer(str(venueid))
        __M_writer('" method="POST">\r\n    <table class="table table-striped">\r\n      ')
        __M_writer(str(form))
        __M_writer('\r\n    </table>\r\n    <input class="btn btn-success" type="submit" value="Save Changes">\r\n    <a class="btn btn-default" href="/catalog/venues">Back</a>\r\n  </form>\r\n  <br/>\r\n  <br/>\r\n  <table class="table table-striped">\r\n    <tr>\r\n      <th>Area Name</th>\r\n      <th>Location</th>\r\n      <th>Description</th>\r\n      <th>Venue</th>\r\n      <th>Actions</th>\r\n    </tr>\r\n\r\n')
        for area in areas:
            __M_writer('      <tr>\r\n        <td> ')
            __M_writer(str(area.areaName))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(area.location))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(area.description))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(area.venue.venueName))
            __M_writer(' </td>\r\n        <td>\r\n          <a data-aid = ')
            __M_writer(str( area.id ))
            __M_writer(' data-toggle="modal" class="editarealink">Edit</a> |\r\n          <a data-aid = ')
            __M_writer(str( area.id ))
            __M_writer(' data-toggle="modal" class="delete_button deletearealink">Delete</a>\r\n        </td>\r\n      </tr>\r\n')
        if areas.count() < 1:
            __M_writer('      <div class="text-center">\r\n        <h3>No areas assigned to this venue. Please click the link below to add one.</h3>\r\n')
        __M_writer('  </table>\r\n\r\n  <div class="text-right"><a id="createarealink" data-vid = ')
        __M_writer(str( venueid ))
        __M_writer(' class="btn btn-primary">Create Area</a></p></div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/editvenue.html", "line_map": {"64": 23, "65": 24, "66": 24, "67": 25, "68": 25, "69": 26, "70": 26, "71": 27, "72": 27, "73": 29, "74": 29, "75": 30, "76": 30, "77": 34, "78": 35, "79": 38, "80": 40, "81": 40, "87": 81, "28": 0, "38": 1, "43": 42, "49": 3, "58": 3, "59": 4, "60": 4, "61": 6, "62": 6, "63": 22}, "uri": "editvenue.html"}
__M_END_METADATA
"""
