from odoo import api, fields, models, _
from pprint import pprint
from odoo import tools

class HrLeave(models.Model):
    _inherit = 'hr.leave.allocation'
    
    academic_degree = fields.Selection([
        ('done', 'Done'),
        ('exempted', 'Exempted'),
        ('not required', 'Not required'),
        ('postponed', 'Postponed')
    ],related='employee_id.academic_degree',store=True)

