# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455144681.285383
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/manager/templates/edituser.html'
_template_uri = 'edituser.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['above_columns', 'center_content']


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
        def above_columns():
            return render_above_columns(context._locals(__M_locals))
        def center_content():
            return render_center_content(context._locals(__M_locals))
        userid = context.get('userid', UNDEFINED)
        form = context.get('form', UNDEFINED)
        first_name = context.get('first_name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'above_columns'):
            context['self'].above_columns(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_above_columns(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_columns():
            return render_above_columns(context)
        first_name = context.get('first_name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <h3>Edit ')
        __M_writer(str(first_name))
        __M_writer(' ')
        __M_writer(str(first_name))
        __M_writer("'s Account Information Below</h3>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        userid = context.get('userid', UNDEFINED)
        def center_content():
            return render_center_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <form action="/manager/users.edit/')
        __M_writer(str(userid))
        __M_writer('" method="POST">\r\n    <table class="table table-striped">\r\n      ')
        __M_writer(str(form))
        __M_writer('\r\n    </table>\r\n    <input class="btn btn-success" type="submit" value="Save Changes">\r\n    <a class="btn btn-default" href="/manager/users">Back</a>\r\n  </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 4, "65": 4, "66": 4, "67": 4, "82": 8, "40": 1, "73": 7, "45": 5, "81": 7, "50": 15, "83": 8, "84": 10, "85": 10, "56": 3, "91": 85, "28": 0, "63": 3}, "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/manager/templates/edituser.html", "source_encoding": "utf-8", "uri": "edituser.html"}
__M_END_METADATA
"""
