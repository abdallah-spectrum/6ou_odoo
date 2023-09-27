# -*- coding: utf-8 -*-
{
    'name': "library app",

    'summary': """
      
       """,
"category": "Services/library",
    'description': """
            
    """,

    'author': "Abdallah",
    'website': "",

'depends':['base'],
    # always loaded
    'data': [
        'security/security_library.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_list_template.xml',
        'views/book_view.xml',

    ],
    # only loaded in demonstration mode

}
