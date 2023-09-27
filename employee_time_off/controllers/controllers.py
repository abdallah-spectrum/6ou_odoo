# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeTimeOff(http.Controller):
#     @http.route('/employee_time_off/employee_time_off', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_time_off/employee_time_off/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_time_off.listing', {
#             'root': '/employee_time_off/employee_time_off',
#             'objects': http.request.env['employee_time_off.employee_time_off'].search([]),
#         })

#     @http.route('/employee_time_off/employee_time_off/objects/<model("employee_time_off.employee_time_off"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_time_off.object', {
#             'object': obj
#         })
