# -*- coding: utf-8 -*-
# Part of Qualified Contacts.
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Qualified Contacts',
    'version': '10.0.1.1',
    "category": 'Bluestar/Generic module',
    'complexity': "easy",
    'description': """
Qualified Contacts
==================

Add a qualified many to many link between partners to manage qualified
contacts.

Rename "Contacts" tab in the partner form "Structure" and add a tab named
"Contacts" with qualified contacts.
    """,
    'author': 'Bluestar Solutions Sàrl',
    'website': 'http://www.blues2.ch',
    'depends': ['bss_one2many_action'],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rule.xml',

        'views/res_partner_views.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
