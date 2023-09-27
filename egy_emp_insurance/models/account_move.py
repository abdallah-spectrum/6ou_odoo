from odoo import api, fields, models, _
from pprint import pprint


class AccountAccount(models.Model):
    _inherit = 'account.account'

    # egy_emp = fields.Many2one('account.report')
    account_report = fields.Many2one('emp.account.report')