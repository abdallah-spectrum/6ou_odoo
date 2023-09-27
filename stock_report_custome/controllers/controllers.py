# -*- coding: utf-8 -*-
# from odoo import http


# class StockReportCustome(http.Controller):
#     @http.route('/stock_report_custome/stock_report_custome', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_report_custome/stock_report_custome/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_report_custome.listing', {
#             'root': '/stock_report_custome/stock_report_custome',
#             'objects': http.request.env['stock_report_custome.stock_report_custome'].search([]),
#         })

#     @http.route('/stock_report_custome/stock_report_custome/objects/<model("stock_report_custome.stock_report_custome"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_report_custome.object', {
#             'object': obj
#         })
