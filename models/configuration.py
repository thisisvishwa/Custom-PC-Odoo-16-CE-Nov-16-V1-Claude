```python
from odoo import models, fields

class Configuration(models.Model):
    _name = 'pcbuilder.configuration'
    _description = 'PC Configuration'

    name = fields.Char(string='Configuration Name', required=True)
    selected_components = fields.Many2many('pcbuilder.component', string='Selected Components')
    prices = fields.Float(compute='_compute_total_price', string='Total Price', store=True)
    compatibility_checks = fields.Boolean(string='Compatibility Checks', default=True)

    def _compute_total_price(self):
        for record in self:
            total_price = 0.0
            for component in record.selected_components:
                total_price += component.price
            record.prices = total_price

    def check_compatibility(self):
        # Implement compatibility check logic here
        pass
```