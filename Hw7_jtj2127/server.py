#Jordyn Jaffe jtj2127
import re
from flask import Flask, render_template, request, jsonify, redirect, url_for


#app = Flask(__name__)
app = Flask(__name__, static_folder='static')



data = {
    "1": {
        "id": "1",
        "name": "Yellowstone National Park",
        "image": "https://muir-way.com/cdn/shop/articles/yellowstone-image.jpg?v=1716511872&width=5464",
        "year_established": "1872",
        "description": "Established in 1872 and located primarily in Wyoming, Yellowstone National Park was America's first national park. It spans almost 3,500 square miles and extends into Montana and Idaho, offering visitors diverse landscapes and abundant wildlife. Yellowstone sits on top of a dormant volcano and boasts the highest concentration of geysers in the world, including the iconic Old Faithful. The park is home to bison, grizzly bears, wolves, and elk, making it a prime location for wildlife enthusiasts.",
        "location_states": ["Wyoming", "Montana", "Idaho"],
        "scenic_landmarks": ["Old Faithful", "Grand Prismatic Spring", "Yellowstone Lake"],
        "trail_difficulty": ["easy", "moderate", "challenging"],
        "entrance_fee": "35",
        "visitor_rating": "4.7",
        "popular_activities": ["hiking", "wildlife viewing", "camping", "fishing"],
        "alt": "Yellowstone National Park - Colorful Geysers and Wildlife",
    },
    "2": {
        "id": "2",
        "name": "Grand Canyon National Park",
        "image": "https://www.globalnationalparks.com/wp-content/uploads/national-park-grand-canyon-1024x682.jpg",
        "year_established": "1919",
        "description": "Grand Canyon National Park, located in Arizona, is home to one of the most breathtaking geological formations in the world. The Grand Canyon, carved by the Colorado River, stretches for 277 miles and reaches depths of over a mile. Visitors can explore scenic viewpoints, hike down into the canyon, or take a rafting trip through the river below. The park's diverse ecosystems support a variety of wildlife, including bighorn sheep, mountain lions, and condors.",
        "location_states": ["Arizona"],
        "scenic_landmarks": ["Grand Canyon", "Horseshoe Bend", "Bright Angel Trail"],
        "trail_difficulty": ["moderate", "challenging"],
        "entrance_fee": "35",
        "visitor_rating": "4.8",
        "popular_activities": ["hiking", "rafting", "scenic drives"],
        "alt": "Grand Canyon National Park - Scenic View of the Canyon",
    },
    "3": {
        "id": "3",
        "name": "Yosemite National Park",
        "image": "https://i.natgeofe.com/n/f14f6c30-8d11-4e33-a5e9-05f1b50bdde3/yosemite-national-park-california_16x9.jpg?w=1200",
        "year_established": "1890",
        "description": "Yosemite National Park, located in California, is famous for its towering granite cliffs, dramatic waterfalls, and ancient sequoia trees. The park is home to landmarks such as Half Dome, El Capitan, and Yosemite Falls, drawing millions of visitors each year. With over 750 miles of trails, it offers incredible hiking opportunities for all skill levels. Yosemite’s diverse habitats support a wide range of wildlife, including black bears, mule deer, and bobcats.",
        "location_states": ["California"],
        "scenic_landmarks": ["El Capitan", "Half Dome", "Yosemite Falls"],
        "trail_difficulty": ["easy", "moderate", "challenging"],
        "entrance_fee": "35",
        "visitor_rating": "4.9",
        "popular_activities": ["hiking", "rock climbing", "photography"],
        "alt": "Yosemite National Park - Half Dome and Waterfalls",
    },
    "4": {
        "id": "4",
        "name": "Great Smoky Mountains National Park",
        "image": "https://www.usatoday.com/gcdn/-mm-/c09164e22ed6ca7cb98e1def4341317c30929f22/c=0-153-1497-999/local/-/media/2016/08/05/USATODAY/USATODAY/636060128185669450-GreatSmokyMountainsNPChrisMobleysmall.jpg",
        "year_established": "1934",
        "description": "Great Smoky Mountains National Park is the most visited national park in the United States, spanning the border between North Carolina and Tennessee. It is known for its mist-covered mountains, lush forests, and diverse wildlife, including black bears and salamanders. Visitors can explore historic cabins, hike scenic trails, and drive through the famous Cades Cove loop. The park is especially popular in the fall when the foliage transforms into a spectacular array of colors.",
        "location_states": ["Tennessee", "North Carolina"],
        "scenic_landmarks": ["Clingmans Dome", "Cades Cove", "Roaring Fork Motor Nature Trail"],
        "trail_difficulty": ["easy", "moderate"],
        "entrance_fee": "0",
        "visitor_rating": "4.8",
        "popular_activities": ["hiking", "wildlife viewing", "scenic drives"],
        "alt": "Great Smoky Mountains National Park - Misty Mountain Landscape",
    },
    "5": {
        "id": "5",
        "name": "Zion National Park",
        "image": "https://www.nps.gov/zion/learn/nature/images/Big-Bend-11222021.jpg?maxwidth=1300&maxheight=1300&autorotate=false",
        "year_established": "1919",
        "description": "Zion National Park, located in Utah, is known for its towering sandstone cliffs, slot canyons, and breathtaking vistas. The park offers some of the most thrilling hikes in the world, including Angels Landing and The Narrows. Visitors can explore the Virgin River, which cuts through the dramatic rock formations, creating a landscape unlike any other. Zion’s diverse ecosystems provide a habitat for desert bighorn sheep, peregrine falcons, and numerous plant species.",
        "location_states": ["Utah"],
        "scenic_landmarks": ["The Narrows", "Angels Landing", "Emerald Pools"],
        "trail_difficulty": ["moderate", "challenging"],
        "entrance_fee": "35",
        "visitor_rating": "4.7",
        "popular_activities": ["hiking", "canyoneering", "rock climbing"],
        "alt": "Zion National Park - Sandstone Cliffs and Canyons",
    },
    "6": {
        "id": "6",
        "name": "Rocky Mountain National Park",
        "image": "https://www.alltrails.com/_next/image?url=https%3A%2F%2Fimages.alltrails.com%2FeyJidWNrZXQiOiJhc3NldHMuYWxsdHJhaWxzLmNvbSIsImtleSI6InVwbG9hZHMvcGhvdG8vaW1hZ2UvNjYzNDAxNjkvYjNiMjg1M2MwYWNiZDVhN2UzMDU4ODU1YTE4MTRlMWEuanBnIiwiZWRpdHMiOnsidG9Gb3JtYXQiOiJ3ZWJwIiwicmVzaXplIjp7IndpZHRoIjoxMDgwLCJoZWlnaHQiOjcwMCwiZml0IjoiY292ZXIifSwicm90YXRlIjpudWxsLCJqcGVnIjp7InRyZWxsaXNRdWFudGlzYXRpb24iOnRydWUsIm92ZXJzaG9vdERlcmluZ2luZyI6dHJ1ZSwib3B0aW1pc2VTY2FucyI6dHJ1ZSwicXVhbnRpc2F0aW9uVGFibGUiOjN9fX0%3D&w=3840&q=90",
        "year_established": "1915",
        "description": "Rocky Mountain National Park, located in Colorado, features over 300 miles of hiking trails and stunning alpine landscapes. The park is home to breathtaking peaks, pristine lakes, and diverse wildlife, including elk, moose, and black bears. Visitors can drive the famous Trail Ridge Road, which offers panoramic views at over 12,000 feet. During the fall, the park is especially popular for witnessing the elk rut, a unique and dramatic wildlife experience.",
        "location_states": ["Colorado"],
        "scenic_landmarks": ["Trail Ridge Road", "Bear Lake", "Longs Peak"],
        "trail_difficulty": ["easy", "moderate", "challenging"],
        "entrance_fee": "30",
        "visitor_rating": "4.8",
        "popular_activities": ["hiking", "wildlife watching", "scenic drives"],
        "alt": "Rocky Mountain National Park - Alpine Landscape and Trails",
    },
    "7": {
        "id": "7",
        "name": "Acadia National Park",
        "image": "https://images.downeast.com/wp-content/uploads/2023/02/twitac23.jpg",
        "year_established": "1919",
        "description": "Acadia National Park, located on the rugged coast of Maine, offers a unique blend of mountains, forests, and ocean views. Cadillac Mountain, the park’s most famous peak, is the first place in the U.S. to see the sunrise for part of the year. Visitors can explore historic carriage roads, go tide pooling along the rocky shores, or hike through dense forests. The park is home to a wide range of wildlife, including moose, puffins, and harbor seals.",
        "location_states": ["Maine"],
        "scenic_landmarks": ["Cadillac Mountain", "Jordan Pond", "Thunder Hole"],
        "trail_difficulty": ["easy", "moderate", "challenging"],
        "entrance_fee": "30",
        "visitor_rating": "4.7",
        "popular_activities": ["hiking", "scenic drives", "kayaking"],
        "alt": "Acadia National Park - Cadillac Mountain and Ocean Views",
    },
    "8": {
        "id": "8",
        "name": "Glacier National Park",
        "image": "https://cdn.aarp.net/content/dam/aarp/travel/destinations/2021/03/1140-glacier-national-park-hero.jpg",
        "year_established": "1910",
        "description": "Glacier National Park, located in Montana, is known for its rugged mountain peaks, pristine lakes, and more than 700 miles of hiking trails. The park is home to the famous Going-to-the-Sun Road, a scenic drive that offers breathtaking views of glaciers and valleys. Wildlife such as grizzly bears, mountain goats, and moose thrive in this vast wilderness. Due to climate change, many of the park’s glaciers are receding, making it a must-visit destination before they disappear.",
        "location_states": ["Montana"],
        "scenic_landmarks": ["Going-to-the-Sun Road", "Grinnell Glacier", "Many Glacier"],
        "trail_difficulty": ["moderate", "challenging"],
        "entrance_fee": "35",
        "visitor_rating": "4.8",
        "popular_activities": ["hiking", "scenic drives", "wildlife photography"],
        "alt": "Glacier National Park - Rugged Mountains and Glaciers",
    },
    "9": {
        "id": "9",
        "name": "Everglades National Park",
        "image": "https://cdn.outsideonline.com/wp-content/uploads/2019/04/15/everglades-national-park_h.jpg",
        "year_established": "1947",
        "description": "Everglades National Park in Florida is the largest tropical wilderness in the United States and a UNESCO World Heritage Site. It is home to a vast network of wetlands, mangroves, and sawgrass prairies, supporting unique wildlife such as alligators, manatees, and the elusive Florida panther. The park is a critical ecosystem that helps filter water for South Florida while protecting endangered species. Visitors can explore by airboat, kayak, or foot, immersing themselves in the beauty of this diverse landscape.",
        "location_states": ["Florida"],
        "scenic_landmarks": ["Shark Valley", "Flamingo", "Anhinga Trail"],
        "trail_difficulty": ["easy", "moderate"],
        "entrance_fee": "30",
        "visitor_rating": "4.6",
        "popular_activities": ["wildlife viewing", "boating", "birdwatching"],
         "alt": "Everglades National Park - Wetlands and Alligators",
    },
    "10": {
        "id": "10",
        "name": "Grand Teton National Park",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/04/cc/c9/fc/grand-teton.jpg?w=1200&h=-1&s=1",
        "year_established": "1929",
        "description": "Grand Teton National Park in Wyoming features dramatic mountain peaks, serene lakes, and diverse wildlife. The park is a haven for outdoor enthusiasts, offering world-class hiking, mountaineering, and wildlife photography opportunities. Jackson Hole Valley provides stunning views of the Teton Range, which rises abruptly without foothills. The park is home to grizzly bears, elk, and bald eagles, making it a premier destination for nature lovers.",
        "location_states": ["Wyoming"],
        "scenic_landmarks": ["Grand Teton", "Jenny Lake", "Schwabacher Landing"],
        "trail_difficulty": ["moderate", "challenging"],
        "entrance_fee": "35",
        "visitor_rating": "4.9",
        "popular_activities": ["hiking", "mountaineering", "wildlife photography"],
        "alt": "Grand Teton National Park - Teton Mountains and Serene Lakes",
    }
}

    



@app.route("/")
def home():
    return render_template("homepage.html", parks=data)




def highlight_text(text, query):
    """Highlight the query in the text (case-insensitive) while preserving the original case."""
    # Define a case-insensitive regex pattern for the query
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    
    # Function to highlight the matched portion
    def replace_func(match):
        return f'<mark>{match.group(0)}</mark>'
    
    # Use re.sub to replace all occurrences of the query (case-insensitive) with the highlighted version
    highlighted_text = pattern.sub(replace_func, text)
    return highlighted_text

@app.route("/search_results", methods=["GET"])
def search_results():
    search_query = request.args.get('query', '').strip()
    
    if not search_query:
        return render_template("search_results.html", results=[], query=None, message=None)

    search_query_lower = search_query.lower()

    results = []
    for park in data.values():
        match_name = search_query_lower in park["name"].lower()
        match_description = search_query_lower in park["description"].lower()
        match_activities = any(search_query_lower in activity.lower() for activity in park["popular_activities"])
        match_location = any(search_query_lower in state.lower() for state in park["location_states"])

        # If there is no match at all, skip this park
        if not (match_name or match_description or match_activities or match_location):
            continue
        
        # Pre-process the text to highlight matches
        park["highlighted_name"] = highlight_text(park["name"], search_query)
        park["highlighted_description"] = highlight_text(park["description"], search_query)
        
        # Filter and highlight only matching activities and locations
        park["highlighted_activities"] = [
            highlight_text(activity, search_query) 
            for activity in park["popular_activities"] 
            if search_query_lower in activity.lower()
        ]
        
        park["highlighted_location_states"] = [
            highlight_text(state, search_query) 
            for state in park["location_states"] 
            if search_query_lower in state.lower()
        ]

        results.append(park)

    message = f"{len(results)} result{'s' if len(results) > 1 else ''} found" if results else "No results found"
    
    return render_template("search_results.html", results=results, query=search_query, message=message)



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Log the raw data received to check if it's coming in correctly
        print(f"Received raw data: {request.data}")

        data_received = request.get_json()

        # Check if the received data is None or not valid JSON
        if not data_received:
            print("No JSON data received or invalid format")
            return jsonify({"error": "Invalid data received."}), 400

        # Extract fields from the received data
        name = data_received.get("name", "").strip()
        year_established = data_received.get("year_established", "").strip()
        description = data_received.get("description", "").strip()
        entrance_fee = data_received.get("entrance_fee", "").strip()
        image_url = data_received.get("image", "").strip()
        popular_activities = data_received.get("popular_activities", [])
        scenic_landmarks = data_received.get("scenic_landmarks", [])
        location_states = data_received.get("location_states", [])
        trail_difficulty = data_received.get("trail_difficulty", [])
        visitor_rating = data_received.get("visitor_rating", "").strip()

        # If no errors, add the new item
        new_id = str(len(data) + 1)
        data[new_id] = {
            "id": new_id,
            "name": name,
            "year_established": year_established,
            "description": description,
            "entrance_fee": entrance_fee,
            "image": image_url,  # Store user-provided image URL
            "location_states": location_states,  # Store location states
            "scenic_landmarks": scenic_landmarks,  # Store scenic landmarks
            "trail_difficulty": trail_difficulty,  # You can populate this later if needed
            "visitor_rating": visitor_rating,  # Store visitor rating
            "popular_activities": popular_activities,  # Store the activities
        }

        # Return success message with the new park's ID
        return jsonify({"success": True, "new_id": new_id}), 200

    # If it's a GET request, render the add page
    return render_template("add.html")







@app.route("/view/<id>")
def view(id):
    park = data.get(id)
    if not park:
        return "Park not found", 404
    return render_template("view.html", park=park)

# Edit route to display the editing form
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    # Fetch the park data by ID
    park = data.get(id)
    
    if not park:
        return "Park not found", 404

    # Check if these fields are lists and pass flags to the template
    is_location_states_list = isinstance(park.get('location_states'), list)
    is_scenic_landmarks_list = isinstance(park.get('scenic_landmarks'), list)
    is_popular_activities_list = isinstance(park.get('popular_activities'), list)
    is_trail_difficulty_list = isinstance(park.get('trail_difficulty'), list)

    if request.method == 'POST':
        # Update the park data from the form submission
        park['name'] = request.form['name']
        park['image'] = request.form['image']
        park['year_established'] = request.form['year_established']
        park['description'] = request.form['description']
        
        # Convert comma-separated input into a list for these fields
        park['location_states'] = [state.strip() for state in request.form.get('location_states', '').split(',')] if request.form.get('location_states') else park['location_states']
        park['scenic_landmarks'] = [landmark.strip() for landmark in request.form.get('scenic_landmarks', '').split(',')] if request.form.get('scenic_landmarks') else park['scenic_landmarks']
        park['trail_difficulty'] = [difficulty.strip() for difficulty in request.form.get('trail_difficulty', '').split(',')] if request.form.get('trail_difficulty') else park['trail_difficulty']
        park['popular_activities'] = [activity.strip() for activity in request.form.get('popular_activities', '').split(',')] if request.form.get('popular_activities') else park['popular_activities']

        park['entrance_fee'] = float(request.form['entrance_fee'])
        park['visitor_rating'] = float(request.form['visitor_rating'])

        # Redirect to the view page with updated data
        return redirect(url_for('view', id=id))

    # GET request - render the edit form with current park data
    return render_template('edit.html', park=park,
                           is_location_states_list=is_location_states_list,
                           is_scenic_landmarks_list=is_scenic_landmarks_list,
                           is_popular_activities_list=is_popular_activities_list,
                           is_trail_difficulty_list=is_trail_difficulty_list)




if __name__ == "__main__":
    app.run(debug=True, port=5001)
