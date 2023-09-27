# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountItem(models.Model):

    _inherit='account.account'
    lms_ref=fields.Char(string='lms-integration_ref')



