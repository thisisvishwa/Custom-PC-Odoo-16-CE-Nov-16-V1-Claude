```python
from odoo import models, fields, api

class CompatibilityCheck(models.Model):
    _name = 'pcbuilder.compatibility_check'
    _description = 'Compatibility Check'

    component_ids = fields.Many2many('pcbuilder.component', string='Components')
    is_compatible = fields.Boolean('Is Compatible', compute='_check_compatibility')

    @api.depends('component_ids')
    def _check_compatibility(self):
        for record in self:
            # Placeholder for actual compatibility logic
            record.is_compatible = True
```