```python
from odoo import api, fields, models

class AssemblyWorkflow(models.Model):
    _name = 'pcbuilder.workflow.assembly'
    _description = 'Workflow for PC Assembly'

    build_order_id = fields.Many2one('pcbuilder.build_order', ondelete='cascade', required=True)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], default='pending', required=True)

    @api.model
    def create_assembly(self, build_order):
        assembly = self.create({
            'build_order_id': build_order.id,
            'status': 'pending',
        })
        return assembly

    def start_assembly(self):
        self.write({'status': 'in_progress'})

    def complete_assembly(self):
        self.write({'status': 'completed'})

    def fail_assembly(self):
        self.write({'status': 'failed'})
```