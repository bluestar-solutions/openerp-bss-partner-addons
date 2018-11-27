# -*- coding: utf-8 -*-
# Part of Resident Permits.
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Resident Permits',
    'version': '10.0.1.0',
    "category": 'Bluestar/Generic module',
    'complexity': "easy",
    'description': """
Resident Permits
================

Add a manageable resident permit list which can be linked to an
OpenERP object like partner.

The list is initialized with Switzerland official resident permit
values (which will be moved in a l10n dedicated module in next
release).
    """,
    'author': 'Bluestar Solutions Sàrl',
    'website': 'http://www.blues2.ch',
    'depends': ['sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'data/bss_resident_permit_data.xml',
        'views/bss_resident_permit_views.xml',
    ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['images/resident_permit_tree.png', ],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
