from odoo import api, fields, models, _
from pprint import pprint


class AccountReport(models.Model):
    _name = 'emp.account.report'

    draft = fields.Boolean()
    posted = fields.Boolean()
    from_date = fields.Date()
    to_date = fields.Date()
    partner_id = fields.Many2one('res.partner')
    report_type = fields.Selection([
        ('debit', 'Debit'),
        ('credit', 'Credit'),
    ], string='Debit/Credit')
    account_account = fields.One2many('account.account', 'account_report') 
    def print_report(self):
        import ipdb; ipdb.set_trace()

        data = {
            '':'egy.emp',
            'form':self.read()[0],
            'ctx':self
        }
        result = self.env.ref('egy_emp_insurance.report_insurance').with_context().report_action(self,data=data)
        return result

