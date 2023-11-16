```python
from models.pricing_rule import PricingRule

def review_pricing(currentConfiguration):
    total_price = 0
    for component in currentConfiguration['selectedComponents']:
        pricing_rule = PricingRule.get_by_component(component)
        if pricing_rule:
            total_price += pricing_rule.apply_discount(component['price'])
        else:
            total_price += component['price']
    currentConfiguration['currentPricing'] = total_price
    return currentConfiguration
```