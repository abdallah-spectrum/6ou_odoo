# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
#
class accountingAccountInherit(models.Model):
    _inherit = 'account.account'
    partner_mandatory=fields.Boolean(string=" partner mandatory")





