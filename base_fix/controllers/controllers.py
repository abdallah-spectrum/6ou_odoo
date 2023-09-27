# -*- coding: utf-8 -*-
# from odoo import http


# class BaseFix(http.Controller):
#     @http.route('/base_fix/base_fix', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/base_fix/base_fix/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('base_fix.listing', {
#             'root': '/base_fix/base_fix',
#             'objects': http.request.env['base_fix.base_fix'].search([]),
#         })

#     @http.route('/base_fix/base_fix/objects/<model("base_fix.base_fix"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('base_fix.object', {
#             'object': obj
#         })
