# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Employee Time-off Report in Excel',
    'version' : '14.0.1.1',
    'description': """Employee Time-off detailed report in Excel Format""",
    'category': 'Human Resource',
    'website': 'shads7039@gmail.com',
    'author': 'Suhaib Khateeb',
    'summary': 'Employee leave/Time-off report with all the required details in Excel format',
    'depends': ['base','hr', 'hr_holidays'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sak_employee_timeoff_report.xml',
        'reports/report_employee_details.xml',

             ],

    'demo': [],
    'qweb': [],
    'images':['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
