```python
from models.build_order import BuildOrder

def create_build_order(configuration):
    # Check if configuration is valid
    if not configuration:
        raise ValueError("Invalid configuration")

    # Create a new build order
    build_order = BuildOrder(configuration)

    # Save the build order to the database
    build_order.save()

    # Trigger the BUILD_ORDER_CREATED event
    trigger_event('BUILD_ORDER_CREATED', build_order)

    return build_order
```