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
        #
        # analytic_account =False
        #
        # # loop to get if have at least one
        # for index in range(len(line_ids)):
        #     # print(line_ids[index])
        #     if line_ids[index][2].get('analytic_account_id') :
        #         print( line_ids[index][2].get('analytic_account_id'))
        #         analytic_account = line_ids[index][2].get('analytic_account_id')
        #
        #
        # if analytic_account:
        #     for index  in range(len(line_ids)):
        #
        #         if not line_ids[index][2].get('analytic_account_id'):
        #             line_ids[index][2]['analytic_account_id'] = analytic_account

        # print(line_ids , 'after inject ')


        # if no analytic account at all

        for line in line_ids:
            print(line[2].get('account_id'),"__________________________account_id")
            account_id = line[2].get('account_id')
            account =self.env['account.account'].browse(account_id)

            if account.partner_mandatory :
                if not line[2].get('partner_id'):
                    print("partner required _______________________")
                    raise ValidationError(f"{account.name} require partner please select partner and save ")

            print(account.partner_mandatory)
            # if not line[2].get('analytic_account_id'):
            #     raise ValidationError("  analytic account required please select and save !")

       # get record id
        #     check if partner required for partner or not



        return super(accounting_modify, self).create(vals)













