from odoo import api, fields, models, _
from pprint import pprint


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    academic_degree = fields.Selection([
        ('teaching_assistant', 'معيد'),
        ('assistant_professor', 'مدرس مساعد'),
        ('professor', 'مدرس'),
        ('associate_professor', 'استاذ مساعد'),
        ('associate', 'استاذ'),
        ('vice', 'نائب')
    ],translate=True)
    military_status = fields.Selection([
        ('done', 'Done'),
        ('exempted', 'Exempted'),
        ('not required', 'Not required'),
        ('postponed', 'Postponed')
    ],translate=True)
    ssnid = fields.Char('Social Security Number', help='Social Security Number', groups="hr.group_hr_user", tracking=True,translate=True)
    certificate = fields.Selection([
        ('None', 'بدون مؤهل'),
        ('Literacy', 'محو أمية'),
        ('Primary', 'ابتدائي'),
        ('Preparatory', 'اعدادي'),
        ('Vocational Training', 'تدريب مهني'),
        ('secondary', 'ثانوي'),
        ('diploma', 'دبلوم'),
        ('Institute', 'معهد'),
        ('bachelor', 'ليسانس/ بكالوريوس'),
        ('graduate', 'خريج'),
        ('master', 'دراسات عليا'),
        ('doctor', 'دكتور'),
        ('other', 'غير ذلك'),
    ], 'Certificate Level', default='other', groups="hr.group_hr_user", tracking=True,translate=True)
    employee_id = fields.Char(string='Employee Device ID')
    graduation_year = fields.Char(translate=True)
    employee_address = fields.Char(translate=True)




# from odoo import api, fields, models, _
# from pprint import pprint
#
#
# class HrEmployee(models.Model):
#     _inherit = 'hr.employee'
#
#     academic_degree = fields.Selection([
#         ('teaching_assistant', 'معيد'),
#         ('assistant_professor', 'مدرس مساعد'),
#         ('professor', 'مدرس'),
#         ('associate_professor', 'استاذ مساعد'),
#         ('associate', 'استاذ'),
#         ('vice', 'نائب')
#     ])
#     military_status = fields.Selection([
#         ('done', 'Done'),
#         ('exempted', 'Exempted'),
#         ('not required', 'Not required'),
#         ('postponed', 'Postponed')
#     ])
#     ssnid = fields.Char('Social Security Number', help='Social Security Number', groups="hr.group_hr_user", tracking=True)
#     certificate = fields.Selection([
#         ('None', 'بدون مؤهل'),
#         ('Literacy', 'محو أمية'),
#         ('Primary', 'ابتدائي'),
#         ('Preparatory', 'اعدادي'),
#         ('Vocational Training', 'تدريب مهني'),
#         ('secondary', 'ثانوي'),
#         ('diploma', 'دبلوم'),
#         ('Institute', 'معهد'),
#         ('bachelor', 'ليسانس/ بكالوريوس'),
#         ('graduate', 'خريج'),
#         ('master', 'دراسات عليا'),
#         ('doctor', 'دكتور'),
#         ('other', 'غير ذلك'),
#     ], 'Certificate Level', default='other', groups="hr.group_hr_user", tracking=True)
#     employee_id = fields.Char(string='Employee Device ID')
#     graduation_year = fields.Char()
#     employee_address = fields.Char()
# )


