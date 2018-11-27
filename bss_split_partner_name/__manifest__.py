# -*- coding: utf-8 -*-
# Part of Split Partner Name.
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Split Partner Name',
    'version': '10.0.1.0',
    "category": 'Bluestar/Generic module',
    'complexity': "easy",
    'description': """
Split Partner Name
==================

Add a first name and a last name fields on partner and keep the field name
synchronized with the concatenation of the first name and the last name.

Update standard views to use split name.
    """,
    'author': 'Bluestar Solutions Sàrl',
    'website': 'http://www.blues2.ch',
    'depends': [],
    'data': ['views/res_partner_views.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],
    'post_init_hook': '_auto_init',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
