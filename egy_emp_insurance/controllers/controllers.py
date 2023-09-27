# -*- coding: utf-8 -*-
# from odoo import http


# class EgyEmpInsurance(http.Controller):
#     @http.route('/egy_emp_insurance/egy_emp_insurance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/egy_emp_insurance/egy_emp_insurance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('egy_emp_insurance.listing', {
#             'root': '/egy_emp_insurance/egy_emp_insurance',
#             'objects': http.request.env['egy_emp_insurance.egy_emp_insurance'].search([]),
#         })

#     @http.route('/egy_emp_insurance/egy_emp_insurance/objects/<model("egy_emp_insurance.egy_emp_insurance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('egy_emp_insurance.object', {
#             'object': obj
#         })
