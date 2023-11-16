```python
from odoo import api, fields, models

class BuildOrderApproval(models.Model):
    _name = 'pcbuilder.workflow.build_order_approval'
    _description = 'Build Order Approval Workflow'

    build_order_id = fields.Many2one('pcbuilder.models.build_order', ondelete='cascade', string='Build Order')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending', string='Status')

    @api.multi
    def approve_build_order(self):
        self.ensure_one()
        if self.build_order_id:
            self.status = 'approved'
            self.build_order_id.status = 'approved'
            return True
        return False

    @api.multi
    def reject_build_order(self):
        self.ensure_one()
        if self.build_order_id:
            self.status = 'rejected'
            self.build_order_id.status = 'rejected'
            return True
        return False
```