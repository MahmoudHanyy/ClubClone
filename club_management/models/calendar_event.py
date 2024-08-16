from datetime import date
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class Calendar(models.Model):
    _inherit = 'calendar.event'
    
    member_ids = fields.One2many(
        'res.partner',
        'calendar_id'
    )