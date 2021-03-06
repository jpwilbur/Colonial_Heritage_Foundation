# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455664751.0916784
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/Account/templates/accountinfo.html'
_template_uri = 'accountinfo.html'
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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def center_content():
            return render_center_content(context._locals(__M_locals))
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
        request = context.get('request', UNDEFINED)
        def center_content():
            return render_center_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n  <div>\r\n    <h4>Your Account Information</h4>\r\n    <hr />\r\n    <dl class="dl-horizontal">\r\n        <dt>\r\n            Username:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.username))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            Email:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.email))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            First Name:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.first_name))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            Last Name:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.last_name))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            Address:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.address))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            City:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.city))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            State:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.state))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            Zip Code:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.zipcode))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            Birth Date:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.birth))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            Phone Number:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.phoneNumber))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            Last Four Digits of Credit Card:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.ccDigits))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            Credit Card Expiration:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.ccExpiration))
        __M_writer('\r\n        </dd>\r\n\r\n        <dt>\r\n            Credit Card CVC:\r\n        </dt>\r\n\r\n        <dd>\r\n            ')
        __M_writer(str(request.user.ccCVC))
        __M_writer('\r\n        </dd>\r\n    </dl>\r\n  </div>\r\n  <p>\r\n    <a href="/Account/editaccount">Edit</a> |\r\n    <a href="/Account/changepassword">Change Password</a> |\r\n    <a href="/">Return to Homepage</a>\r\n  </p>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 46, "65": 54, "66": 54, "67": 62, "68": 62, "69": 70, "70": 70, "71": 78, "72": 78, "73": 86, "74": 86, "75": 94, "76": 94, "77": 102, "78": 102, "79": 110, "80": 110, "86": 80, "28": 0, "36": 1, "41": 120, "47": 3, "54": 3, "55": 14, "56": 14, "57": 22, "58": 22, "59": 30, "60": 30, "61": 38, "62": 38, "63": 46}, "source_encoding": "utf-8", "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/Account/templates/accountinfo.html", "uri": "accountinfo.html"}
__M_END_METADATA
"""
