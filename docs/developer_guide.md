# Developer Guide

## Getting Started

This guide will help you understand the structure and flow of the Custom PC Building module. 

## Prerequisites

- Odoo 16 Community Edition
- Python
- XML
- CSS
- Javascript

## Directory Structure

The module follows the standard Odoo module structure:

- `models/`: Contains the models for components, pricing rules, configurations, build orders, compatibility checks, and workflow.
- `views/`: Contains the XML files for the frontend views.
- `workflow/`: Contains the Python files for the workflow.
- `tests/`: Contains the unit tests for models, views, and workflow.
- `static/css/`: Contains the CSS files.
- `static/js/`: Contains the Javascript files.
- `docs/`: Contains the documentation.

## Models

The models are defined in Python files in the `models/` directory. Each model corresponds to a database table.

- `component.py`: Defines the Component model.
- `pricing_rule.py`: Defines the PricingRule model.
- `configuration.py`: Defines the Configuration model.
- `build_order.py`: Defines the BuildOrder model.
- `compatibility_check.py`: Defines the CompatibilityCheck model.
- `workflow.py`: Defines the Workflow model.

## Views

The views are defined in XML files in the `views/` directory. Each view corresponds to a screen in the frontend.

- `component_selection.xml`: Defines the component selection form.
- `configuration_summary.xml`: Defines the configuration summary view.
- `pricing.xml`: Defines the pricing view.
- `build_order_form.xml`: Defines the build order form.
- `compatibility_warnings.xml`: Defines the compatibility warnings view.

## Workflow

The workflow is defined in Python files in the `workflow/` directory. Each file corresponds to a step in the workflow.

- `component_selection.py`: Handles component selection.
- `compatibility_check.py`: Checks compatibility between components.
- `select_configuration.py`: Handles configuration selection.
- `review_pricing.py`: Handles pricing review.
- `save_configuration.py`: Saves a configuration.
- `create_build_order.py`: Creates a build order.
- `build_order_approval.py`: Approves a build order.
- `payment.py`: Processes payment.
- `assembly.py`: Assembles the PC.
- `delivery.py`: Delivers the PC.

## Testing

The tests are defined in Python files in the `tests/` directory. Each file corresponds to a type of test.

- `test_models.py`: Contains unit tests for the models.
- `test_views.py`: Contains tests for the views.
- `test_workflow.py`: Contains tests for the workflow.

## Styling

The CSS and Javascript files are located in the `static/css/` and `static/js/` directories respectively.

- `style.css`: Contains the CSS styles.
- `script.js`: Contains the Javascript scripts.

## Documentation

The documentation is located in the `docs/` directory.

- `user_manual.md`: User manual.
- `developer_guide.md`: Developer guide.

## Conclusion

This guide should give you a good understanding of the structure and flow of the Custom PC Building module. If you have any questions, please refer to the code comments or the user manual.