```python
from odoo import models, fields

class Component(models.Model):
    _name = 'pcbuilder.component'
    _description = 'PC Component'

    name = fields.Char(string='Component Name', required=True)
    manufacturer = fields.Char(string='Manufacturer')
    specs = fields.Text(string='Specifications')
    price = fields.Float(string='Price', digits=(12, 2))

    def selectComponent(self, component):
        self.ensure_one()
        # Logic for selecting a component goes here

    def checkCompatibility(self, components):
        self.ensure_one()
        # Logic for checking compatibility between components goes here

    def calculatePricing(self, components):
        self.ensure_one()
        # Logic for calculating pricing for selected components goes here
```