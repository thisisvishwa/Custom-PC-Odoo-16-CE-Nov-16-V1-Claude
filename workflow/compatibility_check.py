```python
from models.component import Component
from models.configuration import Configuration

def checkCompatibility(components):
    # Initialize compatibility as True
    compatibility = True

    # Check compatibility between CPU and motherboard
    if not Component.isCompatible(components['CPU'], components['Motherboard']):
        compatibility = False
        print("Incompatible CPU and Motherboard selected.")

    # Check compatibility between RAM and motherboard
    if not Component.isCompatible(components['RAM'], components['Motherboard']):
        compatibility = False
        print("Incompatible RAM and Motherboard selected.")

    # Check compatibility between GPU and power supply
    if not Component.isCompatible(components['GPU'], components['Power Supply']):
        compatibility = False
        print("Incompatible GPU and Power Supply selected.")

    # Check compatibility between storage and motherboard
    if not Component.isCompatible(components['Storage'], components['Motherboard']):
        compatibility = False
        print("Incompatible Storage and Motherboard selected.")

    # If all components are compatible, save the configuration
    if compatibility:
        Configuration.save(components)
        print("Configuration saved successfully.")
    else:
        print("Please select compatible components.")

    return compatibility
```