# -*- coding: utf-8 -*-

from odoo import api, fields, models





class EmployeeTimeOff(models.TransientModel):

        _name = 'employee_time_off.report'
        _description = 'employee_time_off.employee_time_off'
        employee = fields.Many2one('hr.employee')
        start_date = fields.Datetime('start from')
        end_date = fields.Datetime('end to ')


