# -*- coding: utf-8 -*-
# from odoo import http


# class CustomePartnerLedger(http.Controller):
#     @http.route('/custome_partner_ledger/custome_partner_ledger', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custome_partner_ledger/custome_partner_ledger/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custome_partner_ledger.listing', {
#             'root': '/custome_partner_ledger/custome_partner_ledger',
#             'objects': http.request.env['custome_partner_ledger.custome_partner_ledger'].search([]),
#         })

#     @http.route('/custome_partner_ledger/custome_partner_ledger/objects/<model("custome_partner_ledger.custome_partner_ledger"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custome_partner_ledger.object', {
#             'object': obj
#         })
