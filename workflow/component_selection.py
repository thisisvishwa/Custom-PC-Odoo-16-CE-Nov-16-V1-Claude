```python
from models.component import Component

selectedComponents = []

def selectComponent(component):
    if isinstance(component, Component):
        selectedComponents.append(component)
        print(f"{component.name} has been selected.")
    else:
        print("Invalid component.")

def COMPONENT_SELECTED(component):
    selectComponent(component)
    checkCompatibility(selectedComponents)

def checkCompatibility(components):
    from models.compatibility_check import CompatibilityCheck
    compatibility_check = CompatibilityCheck(components)
    if compatibility_check.is_compatible():
        print("All components are compatible.")
    else:
        print("Some components are not compatible.")
        from views.compatibility_warnings import show_warnings
        show_warnings(compatibility_check.get_warnings())
```