```python
from odoo import api, fields, models

class Delivery(models.Model):
    _name = 'pcbuilder.workflow.delivery'
    _description = 'Delivery Workflow for Custom PC Building'

    build_order_id = fields.Many2one('pcbuilder.build_order', ondelete='cascade', required=True)
    delivery_status = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
    ], default='pending', required=True)

    @api.model
    def create_delivery(self, build_order):
        delivery = self.create({
            'build_order_id': build_order.id,
            'delivery_status': 'pending',
        })
        return delivery

    def start_delivery(self):
        self.write({'delivery_status': 'in_progress'})

    def complete_delivery(self):
        self.write({'delivery_status': 'delivered'})

    def fail_delivery(self):
        self.write({'delivery_status': 'failed'})
```