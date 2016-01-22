# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453485526.9865718
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/faq.html'
_template_uri = 'faq.html'
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
        def center_content():
            return render_center_content(context._locals(__M_locals))
        str = context.get('str', UNDEFINED)
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
        def center_content():
            return render_center_content(context)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h2>FAQ</h2>\r\n<div class="panel-group" id="accordion">\r\n    ')
        QA = [
               ["what is love?", "baby, dont hurt me",1],
               ["how much wood coult a woodchuck chuck if a woodchuck could chuck wood?", "around 20 if the stars are aligned",2],
               ["what is the answer to life?","42",3],
              ]
           
        
        __M_writer('\r\n')
        for question, answer, questionNum in QA:
            __M_writer('        <div class="panel panel-default">\r\n            <div class="panel-heading">\r\n                <h4 class="panel-title">\r\n                    ')
            collapseid = "collapse" + str(questionNum)
            
            __M_writer('\r\n                    <a data-toggle="collapse" data-parent="#accordion" href=#')
            __M_writer(str(collapseid))
            __M_writer('>')
            __M_writer(str(question))
            __M_writer('</a>\r\n                </h4>\r\n            </div>\r\n            <div id="')
            __M_writer(str(collapseid))
            __M_writer('" class="panel-collapse collapse">\r\n                <div class="panel-body">\r\n                    ')
            __M_writer(str(answer))
            __M_writer('\r\n                </div>\r\n            </div>\r\n        </div>\r\n')
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/homepage/templates/faq.html", "line_map": {"64": 13, "65": 16, "67": 16, "36": 1, "69": 17, "70": 17, "71": 17, "72": 20, "41": 28, "74": 22, "75": 22, "73": 20, "47": 3, "76": 27, "82": 76, "54": 3, "55": 6, "68": 17, "28": 0, "62": 11, "63": 12}, "source_encoding": "utf-8", "uri": "faq.html"}
__M_END_METADATA
"""
