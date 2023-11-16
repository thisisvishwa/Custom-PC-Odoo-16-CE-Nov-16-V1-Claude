```python
from models.configuration import Configuration
from models.component import Component

selectedComponents = []

def select_configuration(configuration_id):
    global selectedComponents
    global currentConfiguration

    # Fetch configuration from database
    currentConfiguration = Configuration.get_by_id(configuration_id)

    # Fetch components of the configuration
    selectedComponents = Component.get_by_ids(currentConfiguration.component_ids)

    # Trigger event to update UI
    trigger_event('CONFIGURATION_SELECTED', currentConfiguration)

def trigger_event(event_name, data):
    # Placeholder for triggering events
    pass
```