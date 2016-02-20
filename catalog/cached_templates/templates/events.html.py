# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455906520.9840882
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/events.html'
_template_uri = 'events.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['above_content', 'full_length_content']


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
        events = context.get('events', UNDEFINED)
        def above_content():
            return render_above_content(context._locals(__M_locals))
        def full_length_content():
            return render_full_length_content(context._locals(__M_locals))
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


def render_above_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_content():
            return render_above_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <h3>All Events</h3>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_full_length_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        events = context.get('events', UNDEFINED)
        def full_length_content():
            return render_full_length_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <p class="text-right"><a id="createeventlink" class="btn btn-primary">Create Event</a></p>\r\n\r\n  <table class="table table-striped">\r\n    <tr>\r\n      <th>Event Name</th>\r\n      <th>Event Start Date</th>\r\n      <th>Event End Date</th>\r\n      <th>Venue</th>\r\n      <th>Actions</th>\r\n    </tr>\r\n\r\n')
        for event in events:
            __M_writer('      <tr>\r\n        <td> ')
            __M_writer(str(event.eventName))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(event.startDate))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(event.endDate))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(event.venue.venueName))
            __M_writer(' </td>\r\n        <td>\r\n          <a data-eid = ')
            __M_writer(str( event.id ))
            __M_writer(' data-toggle="modal" class="editeventlink">Edit</a> |\r\n          <a data-eid = ')
            __M_writer(str( event.id ))
            __M_writer(' data-toggle="modal" class="delete_button deletelink">Delete</a>\r\n        </td>\r\n      </tr>\r\n')
        __M_writer('  </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.html", "line_map": {"66": 7, "73": 7, "74": 19, "75": 20, "76": 21, "77": 21, "78": 22, "79": 22, "80": 23, "81": 23, "82": 24, "83": 24, "84": 26, "85": 26, "86": 27, "87": 27, "88": 31, "28": 0, "94": 88, "38": 1, "43": 5, "48": 32, "54": 3, "60": 3}, "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/events.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
