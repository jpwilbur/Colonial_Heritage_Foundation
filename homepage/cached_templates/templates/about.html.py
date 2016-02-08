# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454814381.622011
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['center_content', 'right_content', 'above_columns', 'left_content', 'active']


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
        def center_content():
            return render_center_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def above_columns():
            return render_above_columns(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def active():
            return render_active(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'active'):
            context['self'].active(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'above_columns'):
            context['self'].above_columns(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_content():
            return render_center_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n <div class="content">\r\n   <h3>Center Content</h3>\r\n   <h4>Ex elit eirmod vim. Qui ei novum debet menandri. Quis modus tacimates sea cu. Purto vulputate comprehensam duo ne. Sit viderer expetendis ne, rebum scaevola ponderum eum ex. An mollis saperet vocibus sit. Id esse simul rationibus ius, eu vel semper nonumes.\r\n\r\nMel te stet appellantur. Et invidunt concludaturque eos, ne oratio cetero labores duo. Porro comprehensam sea ex. Duo te falli petentium expetenda, quo odio ridens adipiscing ne.\r\n\r\nPrima tantas eu cum. Te eos maiestatis definitionem. In movet fuisset eleifend pri, ad est ferri aperiri euripidis, partiendo constituto inciderint ad sit. Cu sed ponderum accusata intellegat, ut pri vitae moderatius appellantur. Pri audiam reprimique ex, sale utamur est an. Pericula tractatos sapientem has at, vim no fugit choro. Stet idque mucius in est, facer bonorum philosophia an usu.\r\n\r\nEos id modo atomorum definitionem. Amet semper at est, ut vim brute efficiantur, quo electram voluptaria interpretaris ex. His ne oporteat inimicus, est cu erant accumsan, est maluisset conceptam te. Eam facilis efficiantur ad. Ea luptatum principes has, vidisse noluisse ea vel, quando utamur vis ad.\r\n\r\n     </h4>\r\n </div>\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="content">\r\n    <h4>Right Content</h3>\r\n    <h5>Ex elit eirmod vim. Qui ei novum debet menandri. Quis modus tacimates sea cu. Purto vulputate comprehensam duo ne. Sit viderer expetendis ne, rebum scaevola ponderum eum ex. An mollis saperet vocibus sit. Id esse simul rationibus ius, eu vel semper nonumes.\r\n\r\n Mel te stet appellantur.\r\n  </h4>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_above_columns(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_columns():
            return render_above_columns(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <h1>A little about us</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="content">\r\n    <h4>Left Content</h3>\r\n    <h5>Ex elit eirmod vim. Qui ei novum debet menandri. Quis modus tacimates sea cu. Purto vulputate comprehensam duo ne. Sit viderer expetendis ne, rebum scaevola ponderum eum ex. An mollis saperet vocibus sit. Id esse simul rationibus ius, eu vel semper nonumes.\r\n\r\n Mel te stet appellantur.\r\n  </h4>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_active(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def active():
            return render_active(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <li><a href="/homepage/index">Home</a></li>\r\n  <li class="active"><a href="/homepage/about">About</a></li>\r\n  <li><a href="/homepage/contact">Contact</a></li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 3, "80": 9, "98": 45, "68": 47, "134": 128, "104": 45, "28": 0, "74": 9, "43": 1, "110": 35, "48": 7, "116": 35, "53": 22, "86": 25, "58": 33, "92": 25, "122": 3, "63": 43}, "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/about.html", "source_encoding": "utf-8", "uri": "about.html"}
__M_END_METADATA
"""
