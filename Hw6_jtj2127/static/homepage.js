$(document).ready(function () {
    const popularIds = ["1", "3", "5"];  // Popular IDs of the parks
    console.log("Popular IDs:", popularIds); // Log popular IDs to ensure they're what you expect

    // The parks data is now available directly in the JS as the 'parks' variable
    console.log("All Parks:", parks);  // Log the parks data passed from Flask

    const container = $("#parks-container");
    if (container.length === 0) {
        console.error("Could not find the parks container element.");
    } else {
        console.log("Parks container found.");
    }

    // Convert parks object to an array and filter the parks based on popularIds
    const popularParks = Object.values(parks).filter(park => {
        console.log("Checking park:", park);  // Log each park to see what's inside
        console.log("Does this park ID match popularIds?", popularIds.includes(park.id)); // Check if the park's ID is in popularIds
        return popularIds.includes(park.id);  // Comparison with string IDs
    });

    console.log("Filtered popular parks:", popularParks);  // Log the filtered parks

    if (popularParks.length === 0) {
        console.warn("No popular parks found!");
    }

    // Render park names dynamically as links
    popularParks.forEach(park => {
        console.log("Rendering park:", park);  // Log each park being rendered
        container.append(`
            <div class="park-item">
                <a href="/view/${park.id}">
                    <h2>${park.name}</h2>  <!-- Display the park name as a link -->
                </a>
            </div>
        `);
    });
});
