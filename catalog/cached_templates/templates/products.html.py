# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455906870.6907296
_enable_loop = True
_template_filename = 'C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['above_content', 'full_length_content']


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
        rentproducts = context.get('rentproducts', UNDEFINED)
        bulkproducts = context.get('bulkproducts', UNDEFINED)
        def above_content():
            return render_above_content(context._locals(__M_locals))
        indproducts = context.get('indproducts', UNDEFINED)
        def full_length_content():
            return render_full_length_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'above_content'):
            context['self'].above_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'full_length_content'):
            context['self'].full_length_content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_above_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def above_content():
            return render_above_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <h3>All Products</h3>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_full_length_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rentproducts = context.get('rentproducts', UNDEFINED)
        bulkproducts = context.get('bulkproducts', UNDEFINED)
        indproducts = context.get('indproducts', UNDEFINED)
        def full_length_content():
            return render_full_length_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <p class="text-right"><a id="createproductlink" class="btn btn-primary">Create product</a></p>\r\n')
        __M_writer('\r\n  <div class="panel panel-default">\r\n      <div class="panel-heading">\r\n        <a data-toggle="collapse" data-parent="#accordion" href=#collapse1>\r\n          <h4 class="panel-title">\r\n            Individual Products\r\n          </h4>\r\n        </a>\r\n      </div>\r\n      <div id="collapse1" class="panel-collapse collapse">\r\n          <div class="panel-body">\r\n          <table class="table table-striped">\r\n            <tr>\r\n              <th>Product ID</th>\r\n              <th>Product Name</th>\r\n              <th>Description</th>\r\n              <th>Replacement Value</th>\r\n              <th>Photo</th>\r\n              <th>Size</th>\r\n              <th>Weight</th>\r\n              <th>Creation Date</th>\r\n              <th>Customization Notes</th>\r\n              <th>Action</th>\r\n            </tr>\r\n')
        for product in indproducts:
            __M_writer('              <tr>\r\n                <td> ')
            __M_writer(str(product.id))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.name))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.description))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.replacementValue))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.photoFileName))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.size))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.weight))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.creationDate))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.customizationNotes))
            __M_writer(' </td>\r\n                <td>\r\n                  <a data-pid = ')
            __M_writer(str( product.id ))
            __M_writer(' data-ptype = \'indproduct\' data-toggle="modal" class="editproductlink">Edit</a> |\r\n                  <a data-pid = ')
            __M_writer(str( product.id ))
            __M_writer(' data-toggle="modal" class="delete_button deletelink">Delete</a>\r\n                </td>\r\n              </tr>\r\n')
        __M_writer('          </table>\r\n          </div>\r\n      </div>\r\n  </div>\r\n\r\n  <div class="panel panel-default">\r\n      <div class="panel-heading">\r\n        <a data-toggle="collapse" data-parent="#accordion" href=#collapse2>\r\n          <h4 class="panel-title">\r\n            Bulk Products\r\n          </h4>\r\n        </a>\r\n      </div>\r\n      <div id="collapse2" class="panel-collapse collapse">\r\n          <div class="panel-body">\r\n          <table class="table table-striped">\r\n            <tr>\r\n              <th>Product ID</th>\r\n              <th>Product Name</th>\r\n              <th>Description</th>\r\n              <th>Replacement Value</th>\r\n              <th>Photo</th>\r\n              <th>Size</th>\r\n              <th>Weight</th>\r\n              <th>Current Bulk Price</th>\r\n              <th>Quantity Available</th>\r\n              <th>Action</th>\r\n            </tr>\r\n')
        for product in bulkproducts:
            __M_writer('              <tr>\r\n                <td> ')
            __M_writer(str(product.id))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.name))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.description))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.replacementValue))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.photoFileName))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.size))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.weight))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.currentBulkPrice))
            __M_writer(' </td>\r\n')
            __M_writer('                  <td><span class="quantityAvailable')
            __M_writer(str(product.id))
            __M_writer('"> 1000 </span> <button data-di="')
            __M_writer(str(product.id))
            __M_writer('" class="btn btn-default" id="updateQty">Update</button></td>\r\n')
            __M_writer('                <td>\r\n                  <a data-pid = ')
            __M_writer(str( product.id ))
            __M_writer(' data-ptype = \'bulkproduct\' data-toggle="modal" class="editproductlink">Edit</a> |\r\n                  <a data-pid = ')
            __M_writer(str( product.id ))
            __M_writer(' data-toggle="modal" class="delete_button deletelink">Delete</a>\r\n                </td>\r\n                </tr>\r\n')
        __M_writer('          </table>\r\n          </div>\r\n      </div>\r\n  </div>\r\n\r\n\r\n  <div class="panel panel-default">\r\n      <div class="panel-heading">\r\n        <a data-toggle="collapse" data-parent="#accordion" href=#collapse3>\r\n          <h4 class="panel-title">\r\n              Rentable Products\r\n          </h4>\r\n        </a>\r\n      </div>\r\n      <div id="collapse3" class="panel-collapse collapse">\r\n          <div class="panel-body">\r\n          <table class="table table-striped">\r\n            <tr>\r\n              <th>Product ID</th>\r\n              <th>Product Name</th>\r\n              <th>Description</th>\r\n              <th>Replacement Value</th>\r\n              <th>Photo</th>\r\n              <th>Size</th>\r\n              <th>Weight</th>\r\n              <th>Current Rental Rate</th>\r\n              <th>Available?</th>\r\n              <th>Action</th>\r\n            </tr>\r\n')
        for product in rentproducts:
            __M_writer('              <tr>\r\n                <td> ')
            __M_writer(str(product.id))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.name))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.description))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.replacementValue))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.photoFileName))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.size))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.weight))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.currentRentalRate))
            __M_writer(' </td>\r\n                <td> ')
            __M_writer(str(product.available))
            __M_writer(' </td>\r\n                <td>\r\n                  <a data-pid = ')
            __M_writer(str( product.id ))
            __M_writer(' data-ptype = \'rentalproduct\' data-toggle="modal" class="editproductlink">Edit</a> |\r\n                  <a data-pid = ')
            __M_writer(str( product.id ))
            __M_writer(' data-toggle="modal" class="delete_button deletelink">Delete</a>\r\n                </td>\r\n              </tr>\r\n')
        __M_writer('          </table>\r\n          </div>\r\n      </div>\r\n  </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "products.html", "line_map": {"28": 0, "40": 1, "45": 5, "50": 150, "56": 3, "62": 3, "68": 7, "77": 7, "78": 10, "79": 34, "80": 35, "81": 36, "82": 36, "83": 37, "84": 37, "85": 38, "86": 38, "87": 39, "88": 39, "89": 40, "90": 40, "91": 41, "92": 41, "93": 42, "94": 42, "95": 43, "96": 43, "97": 44, "98": 44, "99": 46, "100": 46, "101": 47, "102": 47, "103": 51, "104": 79, "105": 80, "106": 81, "107": 81, "108": 82, "109": 82, "110": 83, "111": 83, "112": 84, "113": 84, "114": 85, "115": 85, "116": 86, "117": 86, "118": 87, "119": 87, "120": 88, "121": 88, "122": 91, "123": 91, "124": 91, "125": 91, "126": 91, "127": 93, "128": 94, "129": 94, "130": 95, "131": 95, "132": 99, "133": 128, "134": 129, "135": 130, "136": 130, "137": 131, "138": 131, "139": 132, "140": 132, "141": 133, "142": 133, "143": 134, "144": 134, "145": 135, "146": 135, "147": 136, "148": 136, "149": 137, "150": 137, "151": 138, "152": 138, "153": 140, "154": 140, "155": 141, "156": 141, "157": 145, "163": 157}, "filename": "C:/Users/jpwil_000/Documents/School/2016 Winter Classes/IS 413/Colonial_Heritage_Foundation/catalog/templates/products.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
