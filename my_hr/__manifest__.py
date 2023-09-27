# -*- coding: utf-8 -*-
{
    'name': "spectrum_employee 3",

    'summary': """
        base hr module to practice 
        """,

    'description': """
        Long description of module's purpose
    """,
    'sequence': 1,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_payroll',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/hr_contract.xml',
        'views/hr_employee.xml',
        'views/views.xml',
        # 'data/cron.xml',
        'data/tax.main.csv',
        'data/tax.detail.csv',
        # 'data/custom_channels.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,

}
