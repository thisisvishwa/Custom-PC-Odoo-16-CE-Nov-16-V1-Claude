```python
from odoo import models, fields

class BuildOrder(models.Model):
    _name = 'pcbuilder.build_order'
    _description = 'Build Order'

    configuration_id = fields.Many2one('pcbuilder.configuration', string='Configuration')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('paid', 'Paid'),
        ('assembled', 'Assembled'),
        ('delivered', 'Delivered'),
    ], default='draft', string='Status')
    total_price = fields.Float(compute='_compute_total_price', string='Total Price')

    def _compute_total_price(self):
        for record in self:
            record.total_price = record.configuration_id.total_price

    def action_approve(self):
        self.status = 'approved'

    def action_pay(self):
        self.status = 'paid'

    def action_assemble(self):
        self.status = 'assembled'

    def action_deliver(self):
        self.status = 'delivered'
```