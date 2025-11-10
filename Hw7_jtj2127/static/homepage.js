$(document).ready(function () {
    const popularIds = ["2", "3", "5", "9", "7", "10"]; // IDs of popular parks
    const container = $("#parks-container");

    // Filter parks based on popularIds
    const popularParks = Object.values(parks).filter(park => popularIds.includes(park.id));

    if (popularParks.length === 0) {
        container.append("<p>No popular parks found!</p>");
        return;
    }

    // Render square park cards
    popularParks.forEach(park => {
        container.append(`
        <div class="col-md-6 col-lg-4 d-flex justify-content-center mb-4">
                <div class="card shadow-sm">
                <h5 class="card-title">${park.name}</h5>
                    <a href="/view/${park.id}">
                        <img src="${park.image}" class="card-img-top" alt="${[park.alt]}">
                    </a>
                    <div class="card-body">
                        <p class="card-text"><span>Located in:</span> <strong>${park.location_states}</strong></p>
                        <p class="card-text"><span>Entrance Fee:</span> <strong>$${park.entrance_fee}</strong></p>
                        <a href="/view/${park.id}" class="btn btn-primary mt-auto">Explore</a>
                    </div>
                </div>
            </div>
        `);
    });
});
