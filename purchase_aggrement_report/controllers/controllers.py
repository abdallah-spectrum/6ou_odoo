# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseAggrementReport(http.Controller):
#     @http.route('/purchase_aggrement_report/purchase_aggrement_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_aggrement_report/purchase_aggrement_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_aggrement_report.listing', {
#             'root': '/purchase_aggrement_report/purchase_aggrement_report',
#             'objects': http.request.env['purchase_aggrement_report.purchase_aggrement_report'].search([]),
#         })

#     @http.route('/purchase_aggrement_report/purchase_aggrement_report/objects/<model("purchase_aggrement_report.purchase_aggrement_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_aggrement_report.object', {
#             'object': obj
#         })
