# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455602063.779748
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['header', 'maintenance_message', 'center_content', 'footer', 'title', 'left_content', 'main_body', 'alert_message', 'above_columns', 'full_length_content', 'full_content', 'above_content', 'right_content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def full_content():
            return render_full_content(context._locals(__M_locals))
        def center_content():
            return render_center_content(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def main_body():
            return render_main_body(context._locals(__M_locals))
        def above_columns():
            return render_above_columns(context._locals(__M_locals))
        def full_length_content():
            return render_full_length_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def maintenance_message():
            return render_maintenance_message(context._locals(__M_locals))
        def alert_message():
            return render_alert_message(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def above_content():
            return render_above_content(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
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
        __M_writer('homepage/media/CHF.ico">\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/moment.min.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap-datetimepicker.min.js"></script>\n    <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap-datetimepicker.min.css">\n\n')
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


def render_main_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        def maintenance_message():
            return render_maintenance_message(context)
        def full_content():
            return render_full_content(context)
        def alert_message():
            return render_alert_message(context)
        def center_content():
            return render_center_content(context)
        def footer():
            return render_footer(context)
        def left_content():
            return render_left_content(context)
        def main_body():
            return render_main_body(context)
        def above_columns():
            return render_above_columns(context)
        def full_length_content():
            return render_full_length_content(context)
        def above_content():
            return render_above_content(context)
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <body>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenance_message'):
            context['self'].maintenance_message(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert_message'):
            context['self'].alert_message(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n        <div class="container">\n          <div class="row">\n            <div class="col-md-12 text-center">\n              <h1>\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'above_columns'):
            context['self'].above_columns(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n              </h1>\n            </div>\n          </div>\n          <div class="row">\n            <div class="text-left col-md-2">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n            </div>\n\n            <div class=" col-md-8">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'full_content'):
            context['self'].full_content(**pageargs)
        

        __M_writer('\n')
        __M_writer('            </div>\n\n            <div class=" col-md-8">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        __M_writer('\n')
        __M_writer('            </div>\n\n            <div class="text-right col-md-2">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\n')
        __M_writer('            </div>\n          </div>\n        </div>\n')
        __M_writer('\n        <div class="container-fluid">\n          <div class="row">\n            <div class="col-md-12 text-center">\n              <h1>\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'above_content'):
            context['self'].above_content(**pageargs)
        

        __M_writer('\n')
        __M_writer('              </h1>\n            </div>\n          </div>\n\n          <div class="row">\n            <div class=" col-md-12">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'full_length_content'):
            context['self'].full_length_content(**pageargs)
        

        __M_writer('\n')
        __M_writer('            </div>\n          </div>\n        </div>\n\n        <div class="container">\n          <hr/>\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n        </div>\n    </body>\n  ')
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


def render_full_length_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def full_length_content():
            return render_full_length_content(context)
        __M_writer = context.writer()
        __M_writer('\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_full_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def full_content():
            return render_full_content(context)
        __M_writer = context.writer()
        __M_writer('\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_above_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_content():
            return render_above_content(context)
        __M_writer = context.writer()
        __M_writer('\n                ')
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


"""
__M_BEGIN_METADATA
{"uri": "/homepage/templates/base.htm", "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"130": 74, "260": 102, "261": 104, "136": 110, "266": 111, "142": 110, "272": 44, "17": 2, "205": 37, "19": 0, "148": 14, "278": 44, "154": 14, "284": 52, "160": 61, "290": 52, "326": 92, "166": 61, "296": 101, "172": 34, "302": 101, "206": 39, "200": 34, "308": 68, "53": 2, "54": 3, "58": 3, "59": 4, "332": 80, "63": 4, "320": 92, "68": 15, "69": 18, "70": 20, "71": 20, "72": 21, "73": 21, "74": 22, "75": 22, "76": 25, "77": 25, "78": 26, "79": 26, "80": 27, "81": 27, "82": 28, "83": 28, "84": 31, "85": 31, "86": 31, "249": 87, "344": 338, "217": 45, "218": 47, "91": 114, "92": 117, "93": 117, "94": 117, "223": 53, "224": 55, "100": 40, "229": 62, "230": 64, "314": 68, "106": 40, "235": 69, "236": 71, "338": 80, "112": 36, "241": 75, "242": 77, "211": 41, "118": 36, "247": 81, "248": 83, "212": 43, "124": 74, "254": 93, "255": 95}}
__M_END_METADATA
"""
