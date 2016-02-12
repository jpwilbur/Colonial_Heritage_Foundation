# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455305887.2980952
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/Account/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['right_content', 'footer', 'alert_message', 'maintenance_message', 'title', 'header', 'left_content', 'above_columns', 'account_dropdown', 'center_content']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def alert_message():
            return render_alert_message(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def maintenance_message():
            return render_maintenance_message(context._locals(__M_locals))
        def account_dropdown():
            return render_account_dropdown(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def center_content():
            return render_center_content(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def above_columns():
            return render_above_columns(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
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


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
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


def render_alert_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert_message():
            return render_alert_message(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="row">\r\n    <div class="col-md-2" id="alert">\r\n      <div class="alert alert-danger alert-dismissible" role="alert">\r\n        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n        <strong>Warning!</strong> This is a warning. You have been warned.\r\n      </div>\r\n    </div>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintenance_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintenance_message():
            return render_maintenance_message(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="alert alert-warning" role="alert">\r\n    <div class="text-center">\r\n      <strong>')
        __M_writer(str(request.user.first_name + ' ' + request.user.last_name + ',' if request.user.is_authenticated() else ''))
        __M_writer('Ye Be warned!</strong> This site is currently under construction.\r\n    </div>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  Colonial Heritage Foundation\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def account_dropdown():
            return render_account_dropdown(context)
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n')

        menu_tabs = [
          [ "Sign Up",   "signup"    ],
        ]
        
        
        __M_writer('\r\n  <header>\r\n    <div class="navbar navbar-inverse">\r\n        <div class="container">\r\n            <div class="navbar-header">\r\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\r\n                    <span class="icon-bar"></span>\r\n                    <span class="icon-bar"></span>\r\n                    <span class="icon-bar"></span>\r\n                </button>\r\n                <a class="navbar-brand" href="/index">C<span class="faa faa-spin fa fa-cog animated"></span>lonial Heritage <span class="faa faa-horizontal fa fa-flag-o animated"></span>oundation</a>\r\n            </div>\r\n            <div class="navbar-collapse collapse">\r\n                <ul class="nav navbar-nav">\r\n')
        for tab, page in menu_tabs:
            __M_writer('                     <li class="')
            __M_writer(str( 'active' if request.dmp_router_page == page else ''))
            __M_writer('"><a href="/Account/')
            __M_writer(str(page))
            __M_writer('">')
            __M_writer(str(tab))
            __M_writer('</a></li>\r\n')
        __M_writer('                </ul>\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'account_dropdown'):
            context['self'].account_dropdown(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n\r\n')
        __M_writer('  </header>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_above_columns(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_columns():
            return render_above_columns(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_account_dropdown(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def account_dropdown():
            return render_account_dropdown(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if not request.user.is_authenticated():
            __M_writer('                    <ul class="nav navbar-nav navbar-right">\r\n                      <li class="dropdown">\r\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">My Account <b class="caret"></b></a>\r\n                        <ul class="dropdown-menu">\r\n                          <li><a href="/Account/signup">Sign up</a></li>\r\n                          <li><a id="loginlink" class="a">Log in</a></li>\r\n                        </ul>\r\n                      </li>\r\n                    </ul>\r\n')
        else:
            __M_writer('                    <ul class="nav navbar-nav navbar-right">\r\n                      <li class="dropdown">\r\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">My Account <b class="caret"></b></a>\r\n                        <ul class="dropdown-menu">\r\n                          <li><a href="#">Account info</a></li>\r\n                          <li><a href="/Account/logout">Logout</a></li>\r\n                        </ul>\r\n                      </li>\r\n                    </ul>\r\n')
        __M_writer('                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_content():
            return render_center_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"256": 54, "257": 55, "258": 65, "131": 149, "132": 152, "133": 152, "264": 141, "138": 155, "139": 156, "140": 156, "194": 20, "270": 141, "146": 119, "276": 270, "152": 119, "28": 0, "158": 9, "165": 9, "166": 12, "167": 12, "173": 3, "179": 3, "54": 1, "185": 20, "59": 5, "60": 7, "65": 15, "66": 17, "195": 21, "71": 115, "72": 117, "201": 25, "202": 39, "203": 40, "204": 40, "77": 128, "78": 130, "205": 40, "208": 40, "209": 40, "210": 42, "83": 133, "84": 135, "206": 40, "215": 65, "216": 114, "89": 138, "90": 140, "207": 40, "222": 137, "95": 142, "96": 144, "228": 137, "101": 146, "102": 148, "234": 132, "107": 158, "253": 43, "240": 132, "113": 145, "246": 43, "119": 145, "125": 149, "254": 44, "255": 45}, "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/Account/templates/app_base.htm", "source_encoding": "utf-8", "uri": "app_base.htm"}
__M_END_METADATA
"""
