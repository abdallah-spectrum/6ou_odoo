# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveInherit(models.Model):

    _inherit='account.move'
    lms_ref=fields.Char(string='lms-integration_ref')



