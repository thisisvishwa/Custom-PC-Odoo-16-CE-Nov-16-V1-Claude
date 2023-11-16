```javascript
let selectedComponents = [];
let currentConfiguration = {};
let currentPricing = {};
let currentBuildOrder = {};

document.getElementById('componentSelectionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    selectComponent(event.target.value);
});

function selectComponent(component) {
    selectedComponents.push(component);
    document.dispatchEvent(new CustomEvent('COMPONENT_SELECTED', { detail: component }));
    checkCompatibility(selectedComponents);
}

function checkCompatibility(components) {
    // Compatibility check logic goes here
    // If check fails, dispatch COMPATIBILITY_CHECK_FAILED event
    // document.dispatchEvent(new CustomEvent('COMPATIBILITY_CHECK_FAILED', { detail: incompatibleComponents }));
}

document.getElementById('configurationSummary').addEventListener('submit', function(event) {
    event.preventDefault();
    saveConfiguration(currentConfiguration);
});

function saveConfiguration(configuration) {
    currentConfiguration = configuration;
    document.dispatchEvent(new CustomEvent('CONFIGURATION_SAVED', { detail: configuration }));
    calculatePricing(selectedComponents);
}

function calculatePricing(components) {
    // Pricing calculation logic goes here
    // Update currentPricing
}

document.getElementById('buildOrderForm').addEventListener('submit', function(event) {
    event.preventDefault();
    createBuildOrder(currentConfiguration);
});

function createBuildOrder(configuration) {
    currentBuildOrder = { configuration: configuration, status: 'Pending' };
    document.dispatchEvent(new CustomEvent('BUILD_ORDER_CREATED', { detail: currentBuildOrder }));
    approveBuildOrder(currentBuildOrder);
}

function approveBuildOrder(order) {
    // Approval logic goes here
    // If approved, proceed to processPayment(order)
}

function processPayment(order) {
    // Payment processing logic goes here
    // If payment successful, proceed to assemblePC(order)
}

function assemblePC(order) {
    // Assembly logic goes here
    // If assembly successful, proceed to deliverPC(order)
}

function deliverPC(order) {
    // Delivery logic goes here
}
```