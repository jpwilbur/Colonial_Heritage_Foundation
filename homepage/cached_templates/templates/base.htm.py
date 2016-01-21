# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453323311.0362332
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['above_columns', 'title', 'right_content', 'left_content', 'main_body', 'center_content', 'footer', 'header', 'maintenance_message', 'alert_message']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def above_columns():
            return render_above_columns(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def alert_message():
            return render_alert_message(context._locals(__M_locals))
        def center_content():
            return render_center_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def main_body():
            return render_main_body(context._locals(__M_locals))
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
        __M_writer('\n\n      <!-- every hour i work is netflix for two months. -->\n\n      <!DOCTYPE html>\n      <html>\n      <meta charset="UTF-8">\n\n  <head>\n    <title>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n    </title>\n')
        __M_writer('\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <link rel="stylesheet" href="')
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


def render_above_columns(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_columns():
            return render_above_columns(context)
        __M_writer = context.writer()
        __M_writer('\n                  above_columns content\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n        webpage title\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\n                right column content\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\n                left column content\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_columns():
            return render_above_columns(context)
        def footer():
            return render_footer(context)
        def header():
            return render_header(context)
        def alert_message():
            return render_alert_message(context)
        def center_content():
            return render_center_content(context)
        def right_content():
            return render_right_content(context)
        def left_content():
            return render_left_content(context)
        def main_body():
            return render_main_body(context)
        def maintenance_message():
            return render_maintenance_message(context)
        __M_writer = context.writer()
        __M_writer('\n    <body>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenance_message'):
            context['self'].maintenance_message(**pageargs)
        

        __M_writer('\n')
        __M_writer('      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n')
        __M_writer('      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert_message'):
            context['self'].alert_message(**pageargs)
        

        __M_writer('\n')
        __M_writer('        <div class="container">\n          <div class="row">\n            <div class="col-md-12 bg-info text-center">\n              <h1>\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'above_columns'):
            context['self'].above_columns(**pageargs)
        

        __M_writer('\n')
        __M_writer('              </h1>\n            </div>\n          </div>\n          <div class="row">\n            <div class="text-left col-md-2 bg-danger">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\n')
        __M_writer('            </div>\n\n            <div class=" col-md-8 bg-warning">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        __M_writer('\n')
        __M_writer('            </div>\n\n            <div class="text-right col-md-2 bg-primary  ">\n              ')
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


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_content():
            return render_center_content(context)
        __M_writer = context.writer()
        __M_writer('\n                <h1>center column content</h1>\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n            footer content\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n        header content\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintenance_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintenance_message():
            return render_maintenance_message(context)
        __M_writer = context.writer()
        __M_writer('\n        maintence_message content\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alert_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert_message():
            return render_alert_message(context)
        __M_writer = context.writer()
        __M_writer('\n        alert_message content\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"132": 30, "261": 40, "267": 261, "17": 2, "19": 0, "196": 75, "154": 30, "159": 34, "160": 36, "165": 38, "166": 40, "171": 42, "172": 44, "47": 2, "48": 3, "177": 50, "178": 52, "52": 3, "53": 4, "183": 59, "184": 61, "57": 4, "189": 66, "190": 68, "63": 19, "64": 21, "65": 21, "66": 24, "67": 24, "68": 27, "69": 27, "70": 27, "201": 82, "75": 85, "76": 88, "77": 88, "78": 88, "207": 64, "84": 48, "213": 64, "90": 48, "219": 80, "96": 14, "225": 80, "102": 14, "195": 73, "231": 36, "108": 71, "237": 36, "114": 71, "243": 32, "62": 16, "120": 57, "249": 32, "126": 57, "255": 40}, "uri": "base.htm", "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/base.htm"}
__M_END_METADATA
"""
