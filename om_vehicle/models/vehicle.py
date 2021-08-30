# -*- coding: utf-8 -*-
import datetime

from odoo import fields, models
from datetime import datetime,timedelta


class VehicleRental(models.Model):
    _name = "vehicle.rental"
    _description = "vehicle rental management"
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    registration_id = fields.Date(related='vehicle_id.registration_date',
                                  string='Registration Date', store=True)
    vehicle_name = fields.Char(string='Name')
    brand_id = fields.Many2one(string='Brand', related='vehicle_id.brand_id',
                               store=True)
    model_year = fields.Date(string='Model year')
    currency_id = fields.Many2one('res.currency', string='Currency')
    rent_value = fields.Float(string="Rent")
    state = fields.Selection(
        [('available', 'Available'), ('not_available', 'Not available'),
         ('sold', 'Sold')],
        string="Status", default='available')
