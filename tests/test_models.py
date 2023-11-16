```python
import unittest
from models.component import Component
from models.pricing_rule import PricingRule
from models.configuration import Configuration
from models.build_order import BuildOrder
from models.compatibility_check import CompatibilityCheck

class TestModels(unittest.TestCase):

    def setUp(self):
        self.component = Component('Intel i7', 'Intel', '8 cores', 300)
        self.pricing_rule = PricingRule(self.component, 10, 'Black Friday')
        self.configuration = Configuration([self.component], [self.pricing_rule])
        self.build_order = BuildOrder(self.configuration, 'Pending')
        self.compatibility_check = CompatibilityCheck([self.component])

    def test_component(self):
        self.assertEqual(self.component.name, 'Intel i7')
        self.assertEqual(self.component.manufacturer, 'Intel')
        self.assertEqual(self.component.specs, '8 cores')
        self.assertEqual(self.component.price, 300)

    def test_pricing_rule(self):
        self.assertEqual(self.pricing_rule.component, self.component)
        self.assertEqual(self.pricing_rule.discount, 10)
        self.assertEqual(self.pricing_rule.promotion, 'Black Friday')

    def test_configuration(self):
        self.assertEqual(self.configuration.components, [self.component])
        self.assertEqual(self.configuration.pricing_rules, [self.pricing_rule])

    def test_build_order(self):
        self.assertEqual(self.build_order.configuration, self.configuration)
        self.assertEqual(self.build_order.status, 'Pending')

    def test_compatibility_check(self):
        self.assertEqual(self.compatibility_check.components, [self.component])

if __name__ == '__main__':
    unittest.main()
```