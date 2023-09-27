# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
#
class accounting_modify(models.Model):
    _inherit = 'account.move'
    custome_field=fields.Char(string="hello custome")


    @api.model
    def create(self, vals):


        line_ids = vals.get('line_ids', [])
        print(line_ids)
        print("hello from custome ___________________create")
        #

        for line in line_ids:
            print(line[2].get('account_id'),"__________________________account_id")
            account_id = line[2].get('account_id')
            account =self.env['account.account'].browse(account_id)
        #
            if account.analtic_mandatory :
                if not line[2].get('analytic_account_id'):
                    print("analytic account required _______________________")
                    raise ValidationError(f"{account.name} require analytic please select analytic account and save ")

        #     print(account.partner_mandatory)
            # if not line[2].get('analytic_account_id'):
            #     raise ValidationError("  analytic account required please select and save !")

       # get record id
        #     check if partner required for partner or not



        return super(accounting_modify, self).create(vals)













