# -*- coding: utf-8 -*-
# from odoo import http


# class Asdfg(http.Controller):
#     @http.route('/asdfg/asdfg', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asdfg/asdfg/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('asdfg.listing', {
#             'root': '/asdfg/asdfg',
#             'objects': http.request.env['asdfg.asdfg'].search([]),
#         })

#     @http.route('/asdfg/asdfg/objects/<model("asdfg.asdfg"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asdfg.object', {
#             'object': obj
#         })

