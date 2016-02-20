# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455903444.5890362
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['above_columns', 'left_content', 'footer', 'header', 'maintenance_message', 'title', 'alert_message', 'right_content', 'account_dropdown', 'center_content']


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
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def account_dropdown():
            return render_account_dropdown(context._locals(__M_locals))
        def above_columns():
            return render_above_columns(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def maintenance_message():
            return render_maintenance_message(context._locals(__M_locals))
        def alert_message():
            return render_alert_message(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def center_content():
            return render_center_content(context._locals(__M_locals))
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
        def header():
            return render_header(context)
        def account_dropdown():
            return render_account_dropdown(context)
        __M_writer = context.writer()
        __M_writer('\r\n')

  ## Display name, view name, app name
        menu_tabs = [
          [ "Users",   "users" , "manager"    ],
          [ "Products",   "products" , "catalog"    ],
          [ "Venues",   "venues" , "catalog"    ],
          [ "Events",   "events" , "catalog"    ],
        ]
        
        
        __M_writer('\r\n  <header>\r\n    <div class="navbar navbar-inverse">\r\n        <div class="container">\r\n            <div class="navbar-header">\r\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\r\n                    <span class="icon-bar"></span>\r\n                    <span class="icon-bar"></span>\r\n                    <span class="icon-bar"></span>\r\n                </button>\r\n                <a class="navbar-brand" href="/index">C<span class="faa faa-spin fa fa-cog animated"></span>lonial Heritage <span class="faa faa-horizontal fa fa-flag-o animated"></span>oundation</a>\r\n            </div>\r\n            <div class="navbar-collapse collapse">\r\n                <ul class="nav navbar-nav">\r\n')
        for tab, page, app in menu_tabs:
            __M_writer('                     <li class="')
            __M_writer(str( 'active' if request.dmp_router_page == page else ''))
            __M_writer('"><a href="/')
            __M_writer(str(app))
            __M_writer('/')
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


def render_maintenance_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def maintenance_message():
            return render_maintenance_message(context)
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


def render_account_dropdown(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def account_dropdown():
            return render_account_dropdown(context)
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
{"uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"131": 141, "260": 48, "261": 49, "262": 58, "263": 59, "264": 69, "137": 153, "194": 69, "270": 145, "143": 153, "144": 156, "145": 156, "259": 47, "276": 145, "150": 159, "151": 160, "152": 160, "282": 276, "28": 0, "158": 20, "167": 20, "168": 21, "178": 29, "179": 43, "180": 44, "181": 44, "182": 44, "183": 44, "184": 44, "185": 44, "186": 44, "187": 44, "60": 7, "189": 46, "65": 15, "66": 17, "195": 118, "54": 1, "71": 119, "72": 121, "201": 9, "77": 132, "78": 134, "208": 9, "209": 12, "210": 12, "83": 137, "84": 139, "216": 3, "89": 142, "90": 144, "222": 3, "95": 146, "96": 148, "59": 5, "228": 123, "101": 150, "102": 152, "188": 44, "234": 123, "107": 162, "240": 149, "113": 136, "246": 149, "119": 136, "252": 47, "125": 141}, "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm"}
__M_END_METADATA
"""
