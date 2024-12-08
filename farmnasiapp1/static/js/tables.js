// countySelection.js

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("countySelectionForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission

        // Get all checkboxes
        var checkboxes = document.querySelectorAll('input[name="county"]:checked');
        var selectedCounties = [];

        // Collect values of selected checkboxes
        checkboxes.forEach(function(checkbox) {
            selectedCounties.push(checkbox.value);
        });

        // Display selected counties
        if (selectedCounties.length === 0) {
            alert("No counties selected.");
        } else {
            alert("Selected counties: " + selectedCounties.join(', '));
        }
    });
});