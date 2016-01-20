# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453314163.392431
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['above_columns', 'center_content', 'right_content', 'left_content', 'maintenance_message', 'title']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def above_columns():
            return render_above_columns(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def center_content():
            return render_center_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def maintenance_message():
            return render_maintenance_message(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n  ')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n    ')
        from datetime import datetime 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datetime'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n      <!-- every hour i work is netflix for two months. -->\n\n      <!DOCTYPE html>\n      <html>\n      <meta charset="UTF-8">\n\n      <head>\n        <title>\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\n\n      <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n      <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage\\media\\bootstrap\\css\\bootstrap.min.css">\n      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">\n      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome-animation/0.0.7/font-awesome-animation.css">\n      <link rel="icon" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/CHF.ico">\n\n')
        __M_writer('      ')
        __M_writer(str( static_renderer.get_template_css(request, context)))
        __M_writer('\n  </head>\n\n\n\n  <body>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenance_message'):
            context['self'].maintenance_message(**pageargs)
        

        __M_writer('\n    </div>\n      <header>\n        <div class="container-fluid">\n          <nav class="navbar navbar-inverse" role="navigation">\n            <div class="container-fluid">\n              <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar">\n                  <span class="sr-only">Toggle navigation</span>\n                  <span class="icon-bar"></span>\n                  <span class="icon-bar"></span>\n                  <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="/index">Colonial Heritage Foundation</a>\n              </div>\n              <!-- Collect the nav links, forms, and other content for toggling -->\n              <div class="collapse navbar-collapse" id="navbar">\n                <ul class="nav navbar-nav">\n                  <li><a href="/index">Home</a></li>\n                  <li><a href="/about">About</a></li>\n                  <li><a href="/contact">Contact</a></li>\n                  <li class="dropdown">\n                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">My Account <b class="caret"></b></a>\n                    <ul class="dropdown-menu">\n                      <li><a href="#">Account info</a></li>\n                      <li><a href="#">Logout</a></li>\n                    </ul>\n                  </li>\n                </ul>\n              </div><!-- /.navbar-collapse -->\n            </div>\n          </nav>\n        </div><!-- /.container-fluid -->\n      </header>\n      <div class="row">\n        <div class="col-md-2" id="alert">\n          <div class="alert alert-danger alert-dismissible" role="alert">\n            <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n            <strong>Warning!</strong> Better check yourself, you\'re not looking too good.\n          </div>\n        </div>\n      </div>\n      <div class="container">\n        <div class="row">\n          <div class="col-md-12 bg-info text-center">\n            <h1>\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'above_columns'):
            context['self'].above_columns(**pageargs)
        

        __M_writer('\n            </h1>\n          </div>\n        </div>\n        <div class="row">\n          <div class="text-left col-md-2 bg-danger">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\n          </div>\n\n          <div class=" col-md-8 bg-warning">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        __M_writer('\n          </div>\n\n          <div class="text-right col-md-2 bg-primary  ">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\n          </div>\n        </div>\n      </div>\n      <div class="container">\n        <hr/>\n        <footer class="footer">\n          Copyright &copy ')
        __M_writer(str( datetime.now().year))
        __M_writer(' - Jarrod Wilbur\n        </footer>\n      </div>\n\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_above_columns(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_columns():
            return render_above_columns(context)
        __M_writer = context.writer()
        __M_writer('\n                this is area above the columns\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_content():
            return render_center_content(context)
        __M_writer = context.writer()
        __M_writer('\n              <h1>center content</h1>\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\n              right content\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\n              left content\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintenance_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintenance_message():
            return render_maintenance_message(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="alert alert-warning alert-dismissible" role="alert">\n      <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n      <div class="text-center">        \n            <strong>Ye Be warned!</strong> This site is currently under construction.\n        </div>\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Colonial Heritage Foundation')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"66": 35, "17": 2, "133": 89, "71": 83, "145": 29, "139": 89, "76": 91, "109": 95, "81": 97, "19": 0, "121": 101, "86": 103, "87": 110, "88": 110, "89": 116, "90": 116, "91": 116, "157": 14, "97": 81, "151": 29, "163": 14, "39": 2, "40": 3, "169": 163, "103": 81, "44": 3, "45": 4, "49": 4, "115": 95, "54": 14, "55": 17, "56": 17, "57": 20, "58": 20, "59": 23, "60": 23, "61": 23, "127": 101}, "uri": "base.htm", "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/base.htm"}
__M_END_METADATA
"""
