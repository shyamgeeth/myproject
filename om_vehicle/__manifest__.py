# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'vehicle rental',
    'version': '1.0',
    'category': 'Productivity',
    'sequence': 15,
    'summary': 'vehicle rental',
    'description': "vehicle rent management",
    'website': 'https://www.odoo.com/page/vehicle',
    'depends': ['account_fleet'],
    'data': ['security/ir.model.access.csv', 'data/rent.xml',
             'views/vehicle.xml',
             'views/registration.xml'],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
