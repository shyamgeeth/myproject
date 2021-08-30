from odoo import fields, models

class FleetVehicle(models.Model):
    _inherit = "fleet.vehicle"
    _description = "vehicle rental management"
    registration_date = fields.Date(string='Registration date',
                                    default=fields.Date.today)
