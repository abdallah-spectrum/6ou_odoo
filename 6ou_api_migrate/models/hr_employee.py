# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hrEmployess(models.Model):

    _inherit='hr.employee'
    lms_ref=fields.Char(string='lms-integration_ref')



