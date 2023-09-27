# -*- coding: utf-8 -*-
# from odoo import http


# class AnalyticRequired(http.Controller):
#     @http.route('/analytic_required/analytic_required', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/analytic_required/analytic_required/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('analytic_required.listing', {
#             'root': '/analytic_required/analytic_required',
#             'objects': http.request.env['analytic_required.analytic_required'].search([]),
#         })

#     @http.route('/analytic_required/analytic_required/objects/<model("analytic_required.analytic_required"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('analytic_required.object', {
#             'object': obj
#         })
