# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime


class RentalRequest(models.Model):
    _name = "rental.request"
    _description = "rental request"

    customer_id = fields.Many2one('res.partner', string='Customer',
                                  required=True, change_default=True,
                                  index=True, tracking=1, )
    request_date_id = fields.Date(string='Request date',
                                  default=fields.Date.today)
    customer_vehicle_id = fields.Many2one('vehicle.rental',
                                          domain="[('state', '=', 'available')]",
                                          store=True)
    rent_id = fields.Float(related='customer_vehicle_id.rent_value',
                           string='Rent')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirm', 'Confirm'),
         ('return', 'Returned')],
        string="Status", default='draft')
    request = fields.Char(string='Request', required=True, readonly=True,
                          default=lambda self: _('New'))
    date_from = fields.Date(string='Start Date', store=True)
    date_to = fields.Date('End Date', store=True,)
    no_of_days = fields.Char(compute='_compute_number_of_days',
                                string='No of days', store=True)
   # no_year = fields.Integer(string='year', store=True)
                               #  number_of_days = fields.Float(
                               #     'Duration (Days)', compute='_compute_number_of_days', store=True,
                               #    readonly=False, copy=False, tracking=True, )

    @api.depends('date_from', 'date_to')
    def _compute_number_of_days(self):
        fmt = '%Y-%m-%d'
        for record in self:
            date_from = fields.Date.to_string(record.date_from).date()
            date_to = fields.Date.to_string(record.date_to).date()
            print(date_from)
            print(date_to)
            d1 = datetime.strptime(date_from, fmt)
            d2 = datetime.strptime(date_to, fmt)
            if d2 > d1:
                record.no_of_days = (d2 - d1).days
            else:
                raise ValueError('end date should be superior than start day')


      #     record.no_year = datetime.strptime(record.date_from, fmt).year

    #  @api.depends('date_from', 'date_to')
    #  def _compute_days(self):
    #      fmt = '%m%d%Y'
    #      for record in self:
    #          d1 = datetime.strptime(record.date_from, fmt).date()
    #          d2 = datetime.strptime(record.date_to, fmt).date()
    #          if d2 > d1:
    #              record.days = (d2 - d1).days
    #          else:
    #              raise ValueError('end date should be superior than start day')

    @api.model
    def create(self, vals):
        if not vals.get('request') or vals['request'] == _('New'):
            vals['request'] = self.env['ir.sequence'].next_by_code(
                'rental.request') or _('New')
        return super(RentalRequest, self).create(vals)

    def action_confirm(self):
        print('clicked on button')
        self.state = 'confirm'

    def action_return(self):
        print('clicked on button')
        self.state = 'return'
