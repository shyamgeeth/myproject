# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'hospital',
    'version': '14.0.2',
    'category': 'Productivity',
    'sequence': 10,
    'summary': 'hospital management',
    'description': "hospital management",
    'website': 'https://www.odoo.com/page/hospital',
    'depends': [],
    'data': ['security/ir.model.access.csv',
             '/home/shyam/odoo/custom/om_hospital/views/patient.xml'],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
