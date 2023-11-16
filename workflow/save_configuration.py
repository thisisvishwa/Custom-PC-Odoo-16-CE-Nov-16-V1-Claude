```python
from odoo import api, models

class SaveConfiguration(models.Model):
    _name = 'pcbuilder.configuration'
    _description = 'Configuration Model'

    selectedComponents = fields.Many2many('pcbuilder.component', string='Selected Components')
    currentPricing = fields.Float(compute='_compute_current_pricing', string='Current Pricing')

    @api.depends('selectedComponents')
    def _compute_current_pricing(self):
        for record in self:
            record.currentPricing = sum(component.price for component in record.selectedComponents)

    def save_configuration(self):
        self.ensure_one()
        self.write({
            'selectedComponents': [(6, 0, self.selectedComponents.ids)],
            'currentPricing': self.currentPricing,
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
```