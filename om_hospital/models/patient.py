# -*- coding: utf-8 -*-
from odoo import fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "hospital management"

    name = fields.Char(string='Name')
    age = fields.Char(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male',)
    note = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('done', 'Paid'),
        ('cancel', 'Refused')
    ], string='Status', index=True, default='draft',
        help='Expense Report State')
