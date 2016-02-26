# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456446623.4254637
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['left_content', 'full_length_content', 'maintenance_message', 'above_content', 'header', 'title', 'center_content', 'above_columns', 'main_body', 'full_content', 'footer', 'right_content', 'alert_message']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def full_content():
            return render_full_content(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def full_length_content():
            return render_full_length_content(context._locals(__M_locals))
        def maintenance_message():
            return render_maintenance_message(context._locals(__M_locals))
        def above_content():
            return render_above_content(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def center_content():
            return render_center_content(context._locals(__M_locals))
        def above_columns():
            return render_above_columns(context._locals(__M_locals))
        def main_body():
            return render_main_body(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def alert_message():
            return render_alert_message(context._locals(__M_locals))
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
        __M_writer('\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.min.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage\\media\\bootstrap\\css\\bootstrap.min.css">\n    <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/font-awesome.min.css">\n    <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/font-awesome-animation.css">\n    <link rel="icon" href="')
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


def render_main_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        def full_length_content():
            return render_full_length_content(context)
        def maintenance_message():
            return render_maintenance_message(context)
        def above_content():
            return render_above_content(context)
        def header():
            return render_header(context)
        def center_content():
            return render_center_content(context)
        def above_columns():
            return render_above_columns(context)
        def main_body():
            return render_main_body(context)
        def full_content():
            return render_full_content(context)
        def footer():
            return render_footer(context)
        def right_content():
            return render_right_content(context)
        def alert_message():
            return render_alert_message(context)
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


"""
__M_BEGIN_METADATA
{"line_map": {"130": 36, "259": 62, "260": 64, "136": 36, "265": 69, "266": 71, "142": 92, "271": 75, "272": 77, "17": 2, "19": 0, "148": 92, "277": 81, "278": 83, "279": 87, "196": 52, "154": 40, "284": 93, "285": 95, "160": 40, "290": 102, "291": 104, "326": 80, "166": 14, "296": 111, "172": 14, "302": 68, "178": 74, "308": 68, "53": 2, "54": 3, "332": 80, "184": 74, "58": 3, "59": 4, "202": 34, "190": 52, "63": 4, "320": 110, "68": 15, "69": 18, "70": 19, "71": 19, "72": 20, "73": 20, "74": 21, "75": 21, "76": 22, "77": 22, "78": 23, "79": 23, "80": 24, "81": 24, "82": 25, "83": 25, "84": 26, "85": 26, "86": 27, "87": 27, "88": 28, "89": 28, "90": 31, "91": 31, "92": 31, "314": 110, "350": 344, "344": 44, "97": 114, "98": 117, "99": 117, "100": 117, "230": 34, "106": 61, "235": 37, "236": 39, "338": 44, "112": 61, "241": 41, "242": 43, "118": 101, "247": 45, "248": 47, "124": 101, "253": 53, "254": 55}, "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/base.htm", "source_encoding": "utf-8", "uri": "/homepage/templates/base.htm"}
__M_END_METADATA
"""
