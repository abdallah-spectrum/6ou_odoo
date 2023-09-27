# -*- coding: utf-8 -*-
{
    'name': "update working time attendence v4",

    'summary': """
      15-6-2023 allow working time attendence overnight 
       """,

    'description': """
        modify working hours so allow overnight shifts
          19/6 => fix overlap check  
          11/7 => fix negative values in attendence sum total       
    """,

    'author': "Abdallah",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','resource','hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
