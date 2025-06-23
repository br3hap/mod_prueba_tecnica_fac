# -*- coding: utf-8 -*-
{
    'name': 'Prueba Técnica Fac',
    'version': '1.0',
    'summary': """ Módulo de una prueba técnica - odoo 18""",
    'author': 'Breithner Aquituari',
    'website': '',
    'category': '',
    'depends': ['base', 'account'],
    "data": [
        "reports/account_move_report.xml",
        "security/ir.model.access.csv",
        "views/account_move_views.xml",
        "views/blood_type_views.xml",
        "views/menu_views.xml",
        "wizards/type_remaining_sand.xml",

    ],
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
