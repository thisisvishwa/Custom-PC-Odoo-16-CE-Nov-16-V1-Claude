```python
import unittest
from odoo.tests.common import TransactionCase

class TestViews(TransactionCase):

    def setUp(self):
        super(TestViews, self).setUp()
        self.Component = self.env['component.model']
        self.PricingRule = self.env['pricing.rule.model']
        self.Configuration = self.env['configuration.model']
        self.BuildOrder = self.env['build.order.model']

    def test_component_selection_view(self):
        response = self.client.get('/component_selection')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'component_selection.xml')

    def test_configuration_summary_view(self):
        response = self.client.get('/configuration_summary')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'configuration_summary.xml')

    def test_pricing_view(self):
        response = self.client.get('/pricing')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pricing.xml')

    def test_build_order_form_view(self):
        response = self.client.get('/build_order_form')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'build_order_form.xml')

    def test_compatibility_warnings_view(self):
        response = self.client.get('/compatibility_warnings')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'compatibility_warnings.xml')

if __name__ == '__main__':
    unittest.main()
```