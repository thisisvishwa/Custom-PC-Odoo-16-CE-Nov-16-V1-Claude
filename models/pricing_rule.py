```python
from odoo import models, fields

class PricingRule(models.Model):
    _name = 'custom_pc_builder.pricing_rule'
    _description = 'Pricing Rule'

    component_id = fields.Many2one('custom_pc_builder.component', string='Component')
    discount = fields.Float(string='Discount (%)')
    promotion = fields.Char(string='Promotion')

    def apply_discount(self, price):
        return price - (price * (self.discount / 100))

    def get_promotion(self):
        return self.promotion
```