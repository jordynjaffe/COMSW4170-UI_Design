$("#addParkForm").submit(function(event) {
    event.preventDefault(); // Prevent default form submission

    // Clear previous error messages
    $(".error-message").remove();
    $(".form-control").removeClass("is-invalid");

    let isValid = true; // Flag to track form validity
    let firstErrorField = null; // Track first error field to focus

    // Function to show error message, clear the input, and mark the field as invalid
    function showError(id, message) {
        const inputField = $(`#${id}`);
        inputField.addClass("is-invalid");
        
        // Create the error message element
        const errorMessage = $(`<div class="error-message text-danger">${message}</div>`);
        inputField.after(errorMessage); // Insert the error message below the input field

        if (!firstErrorField) {
            firstErrorField = id; // Set first error field
        }
        isValid = false; // Mark the form as invalid

        // Clear the input field value if there's an error
        inputField.val(""); 
    }

    // Function to clear error message and mark field as valid
    function clearError(id) {
        const inputField = $(`#${id}`);
        inputField.removeClass("is-invalid");
        inputField.siblings(".error-message").remove(); // Remove any previous error messages
    }

    // Function to validate a field
    function validateField(id, type) {
        const value = $(`#${id}`).val().trim();
        console.log(`Validating ${id} with value: ${value}`); // Debugging
    
        if (!value) {
            showError(id, "This field cannot be empty.");
        } else if (type === "number") {
            if (isNaN(value)) {
                showError(id, "Please enter a valid number.");
            } else {
                const numberValue = parseFloat(value);
                if (numberValue <= 0 || numberValue > new Date().getFullYear()) {
                    showError(id, "Please enter a valid amount.");
                } else {
                    clearError(id);
                }
            }
        } else {
            clearError(id);
        }
    }
    

    // Validate required fields
    validateField("name");
    validateField("year_established", "number");
    validateField("description");
    validateField("image");
    validateField("location_states");
    validateField("scenic_landmarks");
    validateField("trail_difficulty");
    validateField("entrance_fee", "number");
    validateField("visitor_rating", "number");
    validateField("popular_activities");

    // If invalid, stop form submission
    if (!isValid) {
        console.log("Form validation failed.");
        $(`#${firstErrorField}`).focus(); // Focus on first error field
        return; // Don't submit the form
    }

    // Prepare form data for submission
    const formData = {
        name: $("#name").val(),
        year_established: $("#year_established").val(),
        description: $("#description").val(),
        image: $("#image").val(),
        location_states: $("#location_states").val().split(",").map(item => item.trim()),
        scenic_landmarks: $("#scenic_landmarks").val().split(",").map(item => item.trim()),
        trail_difficulty: $("#trail_difficulty").val().split(",").map(item => item.trim()),
        entrance_fee: $("#entrance_fee").val(),
        visitor_rating: $("#visitor_rating").val(),
        popular_activities: $("#popular_activities").val().split(",").map(item => item.trim())
    };

    // Submit form data via AJAX if valid
    $.ajax({
        type: "POST",
        url: "/add",
        data: JSON.stringify(formData),
        contentType: "application/json",
        success: function(response) {
            console.log("Success:", response);

            // Create success message
            const successMessageHtml = `
                <p style="color: red; font-weight: bold;">New item successfully created!</p>
                <div style="display: flex; justify-content: center; gap: 10px; align-items: center;">
                    <a href="/view/${response.new_id}" class="btn btn-danger custom-btn">See it here</a>
                    <button id="addAnotherButton" class="btn btn-danger custom-btn">Add Another</button>
                </div>
            `;

            // Show success message
            $("#successMessage").html(successMessageHtml).show();

            // Clear form fields and focus on first input
            $("#addParkForm input, #addParkForm textarea").val("");
            $("#name").focus();

            // Handle "Add Another" button click
            $("#addAnotherButton").click(function() {
                $("#successMessage").hide();
                $("#addParkForm").trigger("reset");
                $("#name").focus();
            });
        },
        error: function(error) {
            console.log("Error:", error);
            alert("There was an error processing your request. Please try again.");
        }
    });
});
