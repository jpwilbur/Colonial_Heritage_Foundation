# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453346255.6103647
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'above_columns', 'account_dropdown', 'footer', 'header', 'maintenance_message', 'center_content', 'left_content', 'alert_message', 'right_content']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        def center_content():
            return render_center_content(context._locals(__M_locals))
        def account_dropdown():
            return render_account_dropdown(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def alert_message():
            return render_alert_message(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def maintenance_message():
            return render_maintenance_message(context._locals(__M_locals))
        def above_columns():
            return render_above_columns(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenance_message'):
            context['self'].maintenance_message(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert_message'):
            context['self'].alert_message(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'above_columns'):
            context['self'].above_columns(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n            Colonial Heritage Foundation\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_above_columns(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_columns():
            return render_above_columns(context)
        __M_writer = context.writer()
        __M_writer('\r\n  this is area above the columns\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_account_dropdown(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def account_dropdown():
            return render_account_dropdown(context)
        __M_writer = context.writer()
        __M_writer('\r\n              <li class="dropdown">\r\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown">My Account <b class="caret"></b></a>\r\n                <ul class="dropdown-menu">\r\n                  <li><a href="#">Account info</a></li>\r\n                  <li><a href="#">Logout</a></li>\r\n                </ul>\r\n              </li>\r\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <footer class="footer">\r\n')
        __M_writer('   ')

        import datetime
        current_year = datetime.date.today().year
        
        
        __M_writer('\r\n    Copyright &copy ')
        __M_writer(str(current_year))
        __M_writer(' - Jarrod Wilbur\r\n  </footer>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def account_dropdown():
            return render_account_dropdown(context)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <header>\r\n    <div class="container-fluid">\r\n      <nav class="navbar navbar-inverse" role="navigation">\r\n        <div class="container-fluid">\r\n          <div class="navbar-header">\r\n            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar">\r\n              <span class="sr-only">Toggle navigation</span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n            </button>\r\n            <a class="navbar-brand" href="/index">C<span class="faa faa-spin fa fa-cog animated"></span>lonial Heritage <span class="faa faa-horizontal fa fa-flag-o animated"></span>oundation</a>\r\n          </div>\r\n          <!-- Collect the nav links, forms, and other content for toggling -->\r\n          <div class="collapse navbar-collapse" id="navbar">\r\n            <ul class="nav navbar-nav">\r\n')
        __M_writer('              <li\r\n')
        if request.dmp_router_page =="index":
            __M_writer('                class="active"\r\n')
        __M_writer('              ><a href="/homepage/index">Home</a></li>\r\n              <li\r\n')
        if request.dmp_router_page =="about":
            __M_writer('                class="active"\r\n')
        __M_writer('              ><a href="/homepage/about">About</a></li>\r\n              <li\r\n')
        if request.dmp_router_page =="contact":
            __M_writer('                class="active"\r\n')
        __M_writer('              ><a href="/homepage/contact">Contact</a></li>\r\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'account_dropdown'):
            context['self'].account_dropdown(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('            </ul>\r\n          </div><!-- /.navbar-collapse -->\r\n        </div>\r\n      </nav>\r\n    </div><!-- /.container-fluid -->\r\n  </header>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintenance_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintenance_message():
            return render_maintenance_message(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="alert alert-warning" role="alert">\r\n    <div class="text-center">\r\n      <strong>Ye Be warned!</strong> This site is currently under construction.\r\n    </div>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_content():
            return render_center_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <h1>center content</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  left content\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alert_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert_message():
            return render_alert_message(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="row">\r\n    <div class="col-md-2" id="alert">\r\n      <div class="alert alert-danger alert-dismissible" role="alert">\r\n        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n        <strong>Warning!</strong> Better check yourself, you\'re not looking too good.\r\n      </div>\r\n    </div>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  right content\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"131": 87, "261": 255, "137": 54, "194": 62, "143": 54, "149": 108, "155": 108, "28": 0, "157": 111, "162": 114, "163": 115, "164": 115, "156": 111, "170": 20, "179": 20, "180": 39, "181": 40, "182": 41, "183": 43, "184": 45, "185": 46, "186": 48, "187": 50, "188": 51, "189": 53, "65": 15, "66": 17, "195": 64, "54": 1, "71": 70, "72": 72, "201": 9, "77": 83, "78": 85, "207": 9, "83": 89, "84": 91, "213": 98, "89": 95, "90": 97, "219": 98, "95": 100, "96": 102, "225": 93, "59": 5, "101": 105, "102": 107, "231": 93, "60": 7, "107": 117, "237": 74, "113": 3, "243": 74, "119": 3, "249": 103, "125": 87, "255": 103}, "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/app_base.htm"}
__M_END_METADATA
"""
