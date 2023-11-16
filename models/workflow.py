```python
from odoo import models, fields, api

class Workflow(models.Model):
    _name = 'pcbuilder.workflow'
    _description = 'Workflow for build order status'

    name = fields.Char(string='Workflow Name', required=True)
    status = fields.Selection([
        ('component_selection', 'Component Selection'),
        ('compatibility_check', 'Compatibility Check'),
        ('select_configuration', 'Select Configuration'),
        ('review_pricing', 'Review Pricing'),
        ('save_configuration', 'Save Configuration'),
        ('create_build_order', 'Create Build Order'),
        ('build_order_approval', 'Build Order Approval'),
        ('payment', 'Payment'),
        ('assembly', 'Assembly'),
        ('delivery', 'Delivery'),
    ], string='Status', default='component_selection')

    build_order_id = fields.Many2one('pcbuilder.build_order', string='Build Order')

    @api.model
    def create(self, vals):
        build_order = self.env['pcbuilder.build_order'].browse(vals['build_order_id'])
        if build_order:
            vals['status'] = 'component_selection'
        return super(Workflow, self).create(vals)

    def action_next(self):
        if self.status == 'component_selection':
            self.status = 'compatibility_check'
        elif self.status == 'compatibility_check':
            self.status = 'select_configuration'
        elif self.status == 'select_configuration':
            self.status = 'review_pricing'
        elif self.status == 'review_pricing':
            self.status = 'save_configuration'
        elif self.status == 'save_configuration':
            self.status = 'create_build_order'
        elif self.status == 'create_build_order':
            self.status = 'build_order_approval'
        elif self.status == 'build_order_approval':
            self.status = 'payment'
        elif self.status == 'payment':
            self.status = 'assembly'
        elif self.status == 'assembly':
            self.status = 'delivery'
        else:
            return
        self._cr.commit()
```