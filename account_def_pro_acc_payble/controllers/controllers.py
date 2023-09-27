# -*- coding: utf-8 -*-
# from odoo import http


# class AccountDefProAccPayble(http.Controller):
#     @http.route('/account_def_pro_acc_payble/account_def_pro_acc_payble', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_def_pro_acc_payble/account_def_pro_acc_payble/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_def_pro_acc_payble.listing', {
#             'root': '/account_def_pro_acc_payble/account_def_pro_acc_payble',
#             'objects': http.request.env['account_def_pro_acc_payble.account_def_pro_acc_payble'].search([]),
#         })

#     @http.route('/account_def_pro_acc_payble/account_def_pro_acc_payble/objects/<model("account_def_pro_acc_payble.account_def_pro_acc_payble"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_def_pro_acc_payble.object', {
#             'object': obj
#         })
