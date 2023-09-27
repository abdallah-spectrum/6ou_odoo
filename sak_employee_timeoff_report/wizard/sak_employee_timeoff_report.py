# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
import xlwt
import io
import base64
from xlwt import easyxf
import datetime


class PrintTimeoffReport(models.Model):
    _name = "employee.timeoff.report"

    @api.model
    def _get_from_date(self):
        company = self.env.user.company_id
        current_date = datetime.date.today()
        from_date = company.compute_fiscalyear_dates(current_date)['date_from']
        return from_date

    @api.model
    def _date_formte(self,date):
        return  date.strftime('%Y-%m-%d')

    from_date = fields.Date(string='From Date', default=_get_from_date)
    to_date = fields.Date(string='To Date', default=datetime.date.today())
    employee_id = fields.Many2one('hr.employee')
    department_id = fields.Many2one('hr.department')



    @api.model
    def get_state(self,state):
        pass



    def print_report(self):

        print('____done')

        # new_from_date = self.from_date.strftime('%Y-%m-%d')
        # new_to_date = self.to_date.strftime('%Y-%m-%d')
        #
        leave_ids = self.env['hr.leave'].sudo().search_read([('employee_id''','=',self.employee_id.id),('state','=','validate')])

        leave_ids = [{'duration_display':l['duration_display'],'date_to':self._date_formte(l['date_to']),'date_from':self._date_formte(l['date_from']),'holiday_type':l['holiday_status_id'],'create_date':self._date_formte(l['create_date'])} for l in leave_ids]

        emp=self.env['hr.employee'].search_read([('id','=',self.employee_id.id)])



        return self.env.ref('sak_employee_timeoff_report.action_print_employeeTimeOff_report').report_action(self,{"leave_ids":leave_ids,'emp':emp[0]})



