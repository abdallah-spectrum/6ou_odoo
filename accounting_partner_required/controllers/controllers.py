# -*- coding: utf-8 -*-
# from odoo import http


# class AccountingModify(http.Controller):
#     @http.route('/accounting_modify/accounting_modify', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/accounting_modify/accounting_modify/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('accounting_modify.listing', {
#             'root': '/accounting_modify/accounting_modify',
#             'objects': http.request.env['accounting_modify.accounting_modify'].search([]),
#         })

#     @http.route('/accounting_modify/accounting_modify/objects/<model("accounting_modify.accounting_modify"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('accounting_modify.object', {
#             'object': obj
#         })
