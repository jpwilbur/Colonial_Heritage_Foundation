# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455661423.730949
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/manager/templates/users.html'
_template_uri = 'users.html'
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
        users = context.get('users', UNDEFINED)
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
        __M_writer('\r\n  <h3>All Users</h3>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_full_length_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def full_length_content():
            return render_full_length_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <p class="text-right"><a id="createuserlink" class="btn btn-primary">Create User</a></p>\r\n\r\n  <table class="table table-striped">\r\n    <tr>\r\n      <th>Username</th>\r\n      <th>First Name</th>\r\n      <th>Last Name</th>\r\n      <th>Email</th>\r\n      <th>Address</th>\r\n      <th>City</th>\r\n      <th>State</th>\r\n      <th>Zipcode</th>\r\n      <th>Birth Date</th>\r\n      <th>Phone Number</th>\r\n      <th>Last four Credit Card Digits</th>\r\n      <th>Credit Card Expiration</th>\r\n      <th>Credit Card CVC</th>\r\n      <th>Groups:</th>\r\n      <th>Actions:</th>\r\n    </tr>\r\n\r\n')
        for user in users:
            __M_writer('      <tr>\r\n        <td> ')
            __M_writer(str(user.username))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.first_name))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.last_name))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.email))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.address))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.city))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.state))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.zipcode))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.birth))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.phoneNumber))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.ccDigits))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.ccExpiration))
            __M_writer(' </td>\r\n        <td> ')
            __M_writer(str(user.ccCVC))
            __M_writer(' </td>\r\n        ')

            groups = user.groups.all()
                    
            
            __M_writer('\r\n        <td>\r\n          <ul class="nav">\r\n            <li class="dropdown">\r\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Groups<b class="caret"></b></a>\r\n              <ul class="dropdown-menu">\r\n')
            for group in groups:
                __M_writer('                  <li>')
                __M_writer(str(group))
                __M_writer('</li>\r\n')
            __M_writer('              </ul>\r\n            </li>\r\n          </ul>\r\n        </td>\r\n        <td>\r\n          <a data-pid = ')
            __M_writer(str( user.id ))
            __M_writer(' data-toggle="modal" class="edituserlink">Edit</a> |\r\n          <a data-pid = ')
            __M_writer(str( user.id ))
            __M_writer(' data-toggle="modal" class="delete_button deletelink">Delete</a>\r\n        </td>\r\n      </tr>\r\n')
        __M_writer('  </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "users.html", "source_encoding": "utf-8", "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/manager/templates/users.html", "line_map": {"28": 0, "38": 1, "43": 5, "48": 66, "54": 3, "60": 3, "66": 7, "73": 7, "74": 29, "75": 30, "76": 31, "77": 31, "78": 32, "79": 32, "80": 33, "81": 33, "82": 34, "83": 34, "84": 35, "85": 35, "86": 36, "87": 36, "88": 37, "89": 37, "90": 38, "91": 38, "92": 39, "93": 39, "94": 40, "95": 40, "96": 41, "97": 41, "98": 42, "99": 42, "100": 43, "101": 43, "102": 44, "106": 46, "107": 52, "108": 53, "109": 53, "110": 53, "111": 55, "112": 60, "113": 60, "114": 61, "115": 61, "116": 65, "122": 116}}
__M_END_METADATA
"""
