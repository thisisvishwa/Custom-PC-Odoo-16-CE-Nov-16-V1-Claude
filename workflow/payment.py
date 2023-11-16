```python
from odoo import api, fields, models

class Payment(models.Model):
    _name = 'custom.pc.building.payment'
    _description = 'Payment for Custom PC Building'

    build_order_id = fields.Many2one('custom.pc.building.build_order', string='Build Order')
    payment_method = fields.Selection([
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ], string='Payment Method', required=True)
    payment_status = fields.Selection([
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], string='Payment Status', default='pending')
    transaction_id = fields.Char(string='Transaction ID')

    @api.model
    def process_payment(self):
        # This is a placeholder function. In a real-world application, this function would integrate with a payment gateway.
        self.payment_status = 'completed'
        return True
```