# -*- coding: utf-8 -*-

from odoo import models, fields, api


class account_def_pro_acc_payble(models.Model):
    _inherit='res.partner'

    def default_get(self, fields):
        defaults = super(account_def_pro_acc_payble, self).default_get(fields)

        l = self.env['account.account'].search_read([('code', '=', '20300701')], limit=1)
        deft_account =  l[0]
        defaults['property_account_payable_id'] = deft_account
        return defaults