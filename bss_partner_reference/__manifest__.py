# -*- coding: utf-8 -*-
# Part of Automatic Partner Reference.
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Partner References',
    'version': '10.0.1.1',
    "category": 'Bluestar/Generic module',
    'complexity': "easy",
    'description': """
Automatic Partner Reference
===========================

With this module, the partner reference field becomes mandatory,
read-only and automatically filled at save from a customizable
sequence.

A configuration wizard can be used to reset all or empty reference
from existing partners.
    """,
    'author': 'Bluestar Solutions Sàrl',
    'website': 'http://www.blues2.ch',
    'depends': [],
    'data': [
        'data/res_partner_data.xml',

        'views/res_partner_views.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['images/customer_tree.png', ],
    'post_init_hook': '_auto_set_reference',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
