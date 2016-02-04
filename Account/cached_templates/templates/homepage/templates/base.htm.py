# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454532197.907894
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['maintenance_message', 'alert_message', 'main_body', 'right_content', 'title', 'center_content', 'header', 'footer', 'above_columns', 'left_content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def alert_message():
            return render_alert_message(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def center_content():
            return render_center_content(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def maintenance_message():
            return render_maintenance_message(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def main_body():
            return render_main_body(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def above_columns():
            return render_above_columns(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n  ')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n    ')
        from datetime import datetime 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datetime'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n      <!-- every hour i work is netflix for two months. -->\n\n      <!DOCTYPE html>\n      <html>\n      <meta charset="UTF-8">\n\n  <head>\n    <title>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n    </title>\n')
        __M_writer('\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage\\media\\bootstrap\\css\\bootstrap.min.css">\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome-animation/0.0.7/font-awesome-animation.css">\n    <link rel="icon" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/CHF.ico">\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)))
        __M_writer('\n  </head>\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_body'):
            context['self'].main_body(**pageargs)
        

        __M_writer('\n  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>\n')
        __M_writer('  ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintenance_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintenance_message():
            return render_maintenance_message(context)
        __M_writer = context.writer()
        __M_writer('\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alert_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert_message():
            return render_alert_message(context)
        __M_writer = context.writer()
        __M_writer('\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert_message():
            return render_alert_message(context)
        def center_content():
            return render_center_content(context)
        def header():
            return render_header(context)
        def maintenance_message():
            return render_maintenance_message(context)
        def left_content():
            return render_left_content(context)
        def main_body():
            return render_main_body(context)
        def right_content():
            return render_right_content(context)
        def above_columns():
            return render_above_columns(context)
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n    <body>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenance_message'):
            context['self'].maintenance_message(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n')
        __M_writer('      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert_message'):
            context['self'].alert_message(**pageargs)
        

        __M_writer('\n')
        __M_writer('        <div class="container">\n          <div class="row">\n            <div class="col-md-12 text-center">\n              <h1>\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'above_columns'):
            context['self'].above_columns(**pageargs)
        

        __M_writer('\n')
        __M_writer('              </h1>\n            </div>\n          </div>\n          <div class="row">\n            <div class="text-left col-md-2">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\n')
        __M_writer('            </div>\n\n            <div class=" col-md-8">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        __M_writer('\n')
        __M_writer('            </div>\n\n            <div class="text-right col-md-2">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\n')
        __M_writer('            </div>\n          </div>\n        </div>\n        <div class="container">\n          <hr/>\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n        </div>\n    </body>\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_content():
            return render_center_content(context)
        __M_writer = context.writer()
        __M_writer('\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_above_columns(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_columns():
            return render_above_columns(context)
        __M_writer = context.writer()
        __M_writer('\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "line_map": {"259": 55, "134": 31, "193": 67, "265": 55, "139": 34, "140": 36, "271": 265, "17": 2, "146": 40, "19": 0, "151": 41, "152": 43, "47": 2, "157": 48, "158": 50, "176": 70, "163": 56, "164": 58, "169": 62, "170": 64, "199": 14, "223": 37, "175": 68, "48": 3, "52": 3, "53": 4, "57": 4, "187": 67, "62": 15, "63": 18, "64": 20, "65": 20, "66": 21, "67": 21, "68": 22, "69": 22, "70": 25, "71": 25, "72": 28, "73": 28, "74": 28, "205": 14, "79": 79, "80": 82, "81": 82, "82": 82, "211": 61, "88": 33, "217": 61, "94": 33, "181": 76, "100": 40, "229": 37, "145": 38, "106": 40, "235": 75, "112": 31, "241": 75, "247": 47, "253": 47}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
