# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455993708.4064558
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/manager/templates/users.html'
_template_uri = 'users.html'
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
        def above_content():
            return render_above_content(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <p class="text-right"><a id="createuserlink" class="btn btn-primary">Create User</a></p>\r\n\r\n  <table class="table table-striped">\r\n    <tr>\r\n      <th>Username</th>\r\n      <th>First Name</th>\r\n      <th>Last Name</th>\r\n      <th>Email</th>\r\n      <th>Address</th>\r\n      <th>City</th>\r\n      <th>State</th>\r\n      <th>Zipcode</th>\r\n      <th>Birth Date</th>\r\n      <th>Phone Number</th>\r\n      <th>Last four Credit Card Digits</th>\r\n      <th>Credit Card Expiration</th>\r\n      <th>Credit Card CVC</th>\r\n      <th>Groups:</th>\r\n      <th>Permissions:</th>\r\n      <th>Actions:</th>\r\n    </tr>\r\n\r\n')
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
            __M_writer('              </ul>\r\n            </li>\r\n          </ul>\r\n        </td>\r\n        ')

            permissions = user.user_permissions.all()
                    
            
            __M_writer('\r\n        <td>\r\n          <ul class="nav">\r\n            <li class="dropdown">\r\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Permissions<b class="caret"></b></a>\r\n              <ul class="dropdown-menu">\r\n')
            for p in permissions:
                __M_writer('                  <li>')
                __M_writer(str(p.name))
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


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/manager/templates/users.html", "line_map": {"132": 126, "28": 0, "38": 1, "43": 5, "48": 82, "54": 7, "61": 7, "62": 30, "63": 31, "64": 32, "65": 32, "66": 33, "67": 33, "68": 34, "69": 34, "70": 35, "71": 35, "72": 36, "73": 36, "74": 37, "75": 37, "76": 38, "77": 38, "78": 39, "79": 39, "80": 40, "81": 40, "82": 41, "83": 41, "84": 42, "85": 42, "86": 43, "87": 43, "88": 44, "89": 44, "90": 45, "94": 47, "95": 53, "96": 54, "97": 54, "98": 54, "99": 56, "100": 60, "104": 62, "105": 68, "106": 69, "107": 69, "108": 69, "109": 71, "110": 76, "111": 76, "112": 77, "113": 77, "114": 81, "120": 3, "126": 3}, "source_encoding": "utf-8", "uri": "users.html"}
__M_END_METADATA
"""
