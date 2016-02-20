# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455769137.1533306
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/editproduct.html'
_template_uri = 'editproduct.html'
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
        ptype = context.get('ptype', UNDEFINED)
        productid = context.get('productid', UNDEFINED)
        def center_content():
            return render_center_content(context._locals(__M_locals))
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
        ptype = context.get('ptype', UNDEFINED)
        productid = context.get('productid', UNDEFINED)
        def center_content():
            return render_center_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <form id="editproductform" action="/catalog/products.edit/')
        __M_writer(str(productid))
        __M_writer('/')
        __M_writer(str(ptype))
        __M_writer('" method="POST">\r\n    <table id=\'editProductTable\' class="table table-striped" data-ptype="')
        __M_writer(str( ptype ))
        __M_writer('">\r\n      ')
        __M_writer(str(form))
        __M_writer('\r\n    </table>\r\n    <input class="btn btn-success" type="submit" value="Save Changes">\r\n    <a class="btn btn-default" href="/catalog/products">Back</a>\r\n  </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "editproduct.html", "source_encoding": "utf-8", "line_map": {"64": 5, "65": 6, "66": 6, "38": 1, "72": 66, "28": 0, "43": 11, "49": 3, "58": 3, "59": 4, "60": 4, "61": 4, "62": 4, "63": 5}, "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/editproduct.html"}
__M_END_METADATA
"""
