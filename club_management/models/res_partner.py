from datetime import date
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(
        compute='_set_age'
    )
    birthdate = fields.Date()
   

    @api.depends('birthdate')
    def _set_age(self):
        for rec in self:
            if rec.birthdate:
                rec.age = (date.today() - rec.birthdate).days // 365
            else:
                rec.age = 0

    @api.constrains('birthdate')
    def _check_age_range(self):
        age = (date.today() - self.birthdate).days // 365
        if age < 20 or age > 90:
            raise UserError('Age must be in range 20 < and < 90')
