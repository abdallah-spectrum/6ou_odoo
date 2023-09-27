# -*- coding: utf-8 -*-
# from odoo import http


# class 6ouApiMigrate(http.Controller):
#     @http.route('/6ou_api_migrate/6ou_api_migrate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/6ou_api_migrate/6ou_api_migrate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('6ou_api_migrate.listing', {
#             'root': '/6ou_api_migrate/6ou_api_migrate',
#             'objects': http.request.env['6ou_api_migrate.6ou_api_migrate'].search([]),
#         })

#     @http.route('/6ou_api_migrate/6ou_api_migrate/objects/<model("6ou_api_migrate.6ou_api_migrate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('6ou_api_migrate.object', {
#             'object': obj
#         })
