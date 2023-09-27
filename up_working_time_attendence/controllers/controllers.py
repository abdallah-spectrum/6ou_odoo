# -*- coding: utf-8 -*-
# from odoo import http


# class UpWorkingTimeAttendence(http.Controller):
#     @http.route('/up_working_time_attendence/up_working_time_attendence', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/up_working_time_attendence/up_working_time_attendence/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('up_working_time_attendence.listing', {
#             'root': '/up_working_time_attendence/up_working_time_attendence',
#             'objects': http.request.env['up_working_time_attendence.up_working_time_attendence'].search([]),
#         })

#     @http.route('/up_working_time_attendence/up_working_time_attendence/objects/<model("up_working_time_attendence.up_working_time_attendence"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('up_working_time_attendence.object', {
#             'object': obj
#         })
