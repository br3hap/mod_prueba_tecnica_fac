# -*- coding: utf-8 -*-
{
    'name': 'Prueba Técnica Fac',
    'version': '1.0',
    'summary': """ Módulo de una prueba técnica - odoo 18""",
    'author': 'Breithner Aquituari',
    'website': '',
    'category': '',
    'depends': ['base', 'account', 'web'],
    "data": [
        "security/ir.model.access.csv",
        "views/account_move_views.xml",
        "views/blood_type_views.xml",
        "views/menu_views.xml",
        "reports/account_move_report.xml",
        "wizards/account_move_due_date_wizard.xml",
        "wizards/type_remaining_sand.xml"
    ],

    'assets': {
        'web.assets_backend': [
            'mod_prueba_tecnica_fac/static/src/js/button_open_wizard.js',
        ],
    },
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
