# -*- coding: utf-8 -*-
# Part of Marital Status.
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Marital status',
    'version': '10.0.1.1',
    "category": 'Bluestar/Generic module',
    'complexity': "easy",
    'description': """
Marital Status
==============

Add a manageable marital status list which can be linked to an OpenERP
object like partner.

The list is initialized with this standard values :

* Married
* Divorced
* Single
* PACS (civil partnership)
* Widow, widower
    """,
    'author': 'Bluestar Solutions Sàrl',
    'website': 'http://www.blues2.ch',
    'depends': ['sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'data/bss_marital_status_data.xml',
        'views/bss_marital_status_views.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['images/marital_status_tree.png', ],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
