# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class stock_report_custome(models.Model):
#     _name = 'stock_report_custome.stock_report_custome'
#     _description = 'stock_report_custome.stock_report_custome'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
