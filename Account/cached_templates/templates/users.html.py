# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455054340.195243
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/Account/templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['center_content', 'above_columns']


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
        def center_content():
            return render_center_content(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        def above_columns():
            return render_above_columns(context._locals(__M_locals))
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


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_content():
            return render_center_content(context)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <p class="text-right"><a href="/manager/users.create" class="btn btn-primary">Create User</a></p>\r\n\r\n  <table class="table table-striped">\r\n    <tr>\r\n      <th>Username:</th>\r\n      <th>First Name:</th>\r\n      <th>Last Name:</th>\r\n      <th>Email:</th>\r\n      <th>Groups:</th>\r\n      <th>Actions:</th>\r\n      <th></th>\r\n      <th></th>\r\n    </tr>\r\n\r\n')
        for user in users:
            __M_writer('      <tr>\r\n        <td> ')
            __M_writer(str( user.username))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str( user.first_name))
            __M_writer('</td>\r\n        <td> ')
            __M_writer(str( user.last_name))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str( user.email))
            __M_writer(' </td>\r\n        <td></td>\r\n        <td></td>\r\n        <td></td>\r\n        <td>\r\n          <a href="/manager/users.edit/')
            __M_writer(str(user.id))
            __M_writer('">Edit</a>\r\n          |\r\n          <a href="/manager/users.delete/')
            __M_writer(str(user.id))
            __M_writer('" class="delete_button">Delete</a>\r\n        </td>\r\n      </tr>\r\n')
        __M_writer('  </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_above_columns(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_columns():
            return render_above_columns(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <h3>All Users</h3>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "users.html", "line_map": {"64": 24, "65": 24, "66": 25, "67": 25, "68": 26, "69": 26, "70": 27, "71": 27, "72": 32, "73": 32, "74": 34, "75": 34, "76": 38, "82": 3, "88": 3, "28": 0, "94": 88, "38": 1, "43": 5, "48": 39, "54": 7, "61": 7, "62": 22, "63": 23}, "source_encoding": "utf-8", "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/Account/templates/users.html"}
__M_END_METADATA
"""
