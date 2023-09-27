# -*- coding: utf-8 -*-
# from odoo import http


# class CustomInv(http.Controller):
#     @http.route('/custom_inv/custom_inv', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_inv/custom_inv/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_inv.listing', {
#             'root': '/custom_inv/custom_inv',
#             'objects': http.request.env['custom_inv.custom_inv'].search([]),
#         })

#     @http.route('/custom_inv/custom_inv/objects/<model("custom_inv.custom_inv"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_inv.object', {
#             'object': obj
#         })
