# -*- coding: utf-8 -*-
{
    'name': "Product Restriction on Users",

    'summary': """
    This Module adds restriction on users for accessing products for any kind of operation. 
    Admin can edit the user and add allowed products / allowed category to a specific user. 
    User can not see the products if not allowed by the admin.
    """,

    'description': """
        - This Module adds restriction on users for accessing products for any kind of operation.
        - User can not see the products if not allowed by the admin.
        - User can only see and operate on Allowed Products.
        - Restriction also applies to sales order, purchase order, stock transfer etc.
        - Admin can edit the user and add allowed produts to a specific user.
        - Note : This Restriction is Applied On Adminstrator.
    """,

    'author': "Techspawn Solutions",
    'website': "http://www.techspawn.com",

    'category': 'Others',
    'version': '14.0',
    'price': 10.00,
    'currency': 'EUR',

    'depends': ['base', 'stock', 'sale', 'product'],
    "images": ['static/description/User_Product_Restriction.gif'],

    'data': [
        #'security/ir.model.access.csv',
        'security/security.xml', 
        'user_view.xml',
    ],

}
