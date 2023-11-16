1. **Exported Variables**: 
    - `selectedComponents` (List of selected components)
    - `currentConfiguration` (Current configuration details)
    - `currentPricing` (Current pricing details)
    - `currentBuildOrder` (Current build order details)

2. **Data Schemas**: 
    - `Component` (name, manufacturer, specs, price)
    - `Configuration` (selected components, prices, compatibility checks)
    - `BuildOrder` (configuration, status)
    - `PricingRule` (component, discount, promotion)

3. **DOM Element IDs**: 
    - `componentSelectionForm` (Form for component selection)
    - `configurationSummary` (Summary of selected configuration)
    - `pricingDetails` (Details of pricing)
    - `buildOrderForm` (Form for build order)
    - `compatibilityWarnings` (Warnings for incompatible components)

4. **Message Names**: 
    - `COMPONENT_SELECTED` (Triggered when a component is selected)
    - `CONFIGURATION_SAVED` (Triggered when a configuration is saved)
    - `BUILD_ORDER_CREATED` (Triggered when a build order is created)
    - `COMPATIBILITY_CHECK_FAILED` (Triggered when compatibility check fails)

5. **Function Names**: 
    - `selectComponent(component)` (Selects a component)
    - `checkCompatibility(components)` (Checks compatibility between components)
    - `calculatePricing(components)` (Calculates pricing for selected components)
    - `saveConfiguration(configuration)` (Saves a configuration)
    - `createBuildOrder(configuration)` (Creates a build order)
    - `approveBuildOrder(order)` (Approves a build order)
    - `processPayment(order)` (Processes payment for a build order)
    - `assemblePC(order)` (Assembles PC for a build order)
    - `deliverPC(order)` (Delivers PC for a build order)