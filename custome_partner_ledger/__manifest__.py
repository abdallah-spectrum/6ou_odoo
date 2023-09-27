# -*- coding: utf-8 -*-
{
    'name': "custome partner ledger",

    'summary': """short module to modify on partner ledger report show emplpyess (not payable or recivable account on partner ledger report """,

    'description': """
        its add new view on accounting module no modifing on previous one 
    """,

    'author': "Abdallah Abdelsabour",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_reports'],

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
