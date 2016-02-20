# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455988872.101686
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/editarea.html'
_template_uri = 'editarea.html'
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
        def center_content():
            return render_center_content(context._locals(__M_locals))
        areaid = context.get('areaid', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
        def center_content():
            return render_center_content(context)
        areaid = context.get('areaid', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <form id="editareaform" action="/catalog/venues.editarea/')
        __M_writer(str(areaid))
        __M_writer('/" method="POST">\r\n    <table class="table table-striped">\r\n      ')
        __M_writer(str(form))
        __M_writer('\r\n    </table>\r\n    <input class="btn btn-success" type="submit" value="Save Changes">\r\n    <a class="btn btn-default" href="/catalog/areas">Back</a>\r\n  </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "editarea.html", "source_encoding": "utf-8", "line_map": {"48": 3, "66": 60, "37": 1, "56": 3, "57": 4, "42": 11, "59": 6, "28": 0, "58": 4, "60": 6}, "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/editarea.html"}
__M_END_METADATA
"""
