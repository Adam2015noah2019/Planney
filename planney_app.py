# List of activities with different locations, prices, and time durations
activities = [
    # Abu Dhabi Locations
    {"name": "Yas Waterworld", "price": 250, "time": 5, "people": "any", "type": "family", "city": "abu dhabi", "location": "Yas Waterworld Abu Dhabi"},
    {"name": "Warner Bros. World Abu Dhabi", "price": 295, "time": 4, "people": "any", "type": "family", "city": "abu dhabi", "location": "Warner Bros. World Abu Dhabi"},
    {"name": "Emirates Palace", "price": 0, "time": 2, "people": "any", "type": "friends", "city": "abu dhabi", "location": "Emirates Palace"},
    {"name": "Corniche Beach", "price": 0, "time": 3, "people": "any", "type": "family", "city": "abu dhabi", "location": "Abu Dhabi Corniche"},
    {"name": "Sheikh Zayed Grand Mosque", "price": 0, "time": 2, "people": "any", "type": "family", "city": "abu dhabi", "location": "Sheikh Zayed Grand Mosque"},
    {"name": "Louvre Abu Dhabi", "price": 60, "time": 3, "people": "any", "type": "family", "city": "abu dhabi", "location": "Louvre Abu Dhabi"},
    {"name": "Ferrari World Abu Dhabi", "price": 295, "time": 4, "people": "any", "type": "family", "city": "abu dhabi", "location": "Ferrari World Abu Dhabi"},
    {"name": "Mangrove Kayaking", "price": 150, "time": 2, "people": "any", "type": "friends", "city": "abu dhabi", "location": "Mangrove National Park"},
    {"name": "Desert Safari", "price": 250, "time": 6, "people": "any", "type": "family", "city": "abu dhabi", "location": "Abu Dhabi Desert"},
    {"name": "Al Ain Zoo", "price": 30, "time": 3, "people": "any", "type": "family", "city": "al ain", "location": "Al Ain Zoo"},
    {"name": "Jebel Hafeet", "price": 0, "time": 2, "people": "any", "type": "friends", "city": "al ain", "location": "Jebel Hafeet"},
    {"name": "Wadi Adventure", "price": 100, "time": 4, "people": "any", "type": "friends", "city": "al ain", "location": "Wadi Adventure"},
    {"name": "Hili Archaeological Park", "price": 0, "time": 1, "people": "any", "type": "family", "city": "al ain", "location": "Hili Archaeological Park"},
    {"name": "Green Mubazzarah", "price": 0, "time": 2, "people": "any", "type": "family", "city": "al ain", "location": "Green Mubazzarah"},
    {"name": "Yas Marina Circuit Tour", "price": 120, "time": 2, "people": "any", "type": "friends", "city": "abu dhabi", "location": "Yas Marina Circuit"},

    # Dubai Locations
    {"name": "Burj Khalifa", "price": 159, "time": 2, "people": "any", "type": "family", "city": "dubai", "location": "Burj Khalifa"},
    {"name": "Dubai Mall", "price": 0, "time": 3, "people": "any", "type": "family", "city": "dubai", "location": "Dubai Mall"},
    {"name": "Palm Jumeirah", "price": 0, "time": 2, "people": "any", "type": "friends", "city": "dubai", "location": "Palm Jumeirah"},
    {"name": "Dubai Marina", "price": 0, "time": 2, "people": "any", "type": "friends", "city": "dubai", "location": "Dubai Marina"},
    {"name": "The Dubai Fountain", "price": 0, "time": 1, "people": "any", "type": "family", "city": "dubai", "location": "The Dubai Fountain"},
    {"name": "Global Village", "price": 20, "time": 4, "people": "any", "type": "family", "city": "dubai", "location": "Global Village"},
    {"name": "IMG Worlds of Adventure", "price": 335, "time": 5, "people": "any", "type": "family", "city": "dubai", "location": "IMG Worlds of Adventure"},
    {"name": "Ski Dubai", "price": 200, "time": 3, "people": "any", "type": "friends", "city": "dubai", "location": "Ski Dubai"},
    {"name": "Desert Safari Dubai", "price": 250, "time": 6, "people": "any", "type": "family", "city": "dubai", "location": "Dubai Desert"},
    {"name": "Dubai Frame", "price": 50, "time": 2, "people": "any", "type": "family", "city": "dubai", "location": "Dubai Frame"},
    {"name": "Ain Dubai", "price": 130, "time": 2, "people": "any", "type": "family", "city": "dubai", "location": "Ain Dubai"},
    {"name": "Dubai Garden Glow", "price": 65, "time": 3, "people": "any", "type": "family", "city": "dubai", "location": "Dubai Garden Glow"},
    {"name": "La Mer Beach", "price": 0, "time": 3, "people": "any", "type": "friends", "city": "dubai", "location": "La Mer Beach"},
    {"name": "Jumeirah Beach", "price": 0, "time": 3, "people": "any", "type": "family", "city": "dubai", "location": "Jumeirah Beach"},
    {"name": "Atlantis Aquaventure", "price": 320, "time": 5, "people": "any", "type": "family", "city": "dubai", "location": "Atlantis Aquaventure"},

    # Sharjah locations
    {"name": "Al Noor Island", "price": 35, "time": 3, "people": "any", "type": "family", "city": "sharjah", "location": "Al Noor Island"},
    {"name": "Sharjah Aquarium", "price": 25, "time": 2, "people": "any", "type": "family", "city": "sharjah", "location": "Sharjah Aquarium"},
    {"name": "Mleiha Archaeological Centre", "price": 50, "time": 4, "people": "any", "type": "friends", "city": "sharjah", "location": "Mleiha Archaeological Centre"},
    {"name": "Sharjah Art Museum", "price": 0, "time": 2, "people": "any", "type": "friends", "city": "sharjah", "location": "Sharjah Art Museum"},
    {"name": "Blue Souk (Central Market)", "price": 0, "time": 3, "people": "any", "type": "family", "city": "sharjah", "location": "Blue Souk Sharjah"},
    {"name": "Sharjah Science Museum", "price": 10, "time": 2, "people": "any", "type": "family", "city": "sharjah", "location": "Sharjah Science Museum"},
    {"name": "Sharjah Heritage Museum", "price": 10, "time": 2, "people": "any", "type": "family", "city": "sharjah", "location": "Sharjah Heritage Museum"},
    {"name": "Sharjah Desert Park", "price": 15, "time": 3, "people": "any", "type": "family", "city": "sharjah", "location": "Sharjah Desert Park"},
    {"name": "Al Majaz Waterfront", "price": 0, "time": 3, "people": "any", "type": "family", "city": "sharjah", "location": "Al Majaz Waterfront"},
    {"name": "Buhaira Corniche", "price": 0, "time": 3, "people": "any", "type": "family", "city": "sharjah", "location": "Buhaira Corniche"},
    {"name": "Sharjah Classic Cars Museum", "price": 10, "time": 2, "people": "any", "type": "friends", "city": "sharjah", "location": "Sharjah Classic Cars Museum"},
    {"name": "Arabian Wildlife Center", "price": 15, "time": 3, "people": "any", "type": "family", "city": "sharjah", "location": "Arabian Wildlife Center"},
    {"name": "Sharjah Calligraphy Museum", "price": 10, "time": 2, "people": "any", "type": "friends", "city": "sharjah", "location": "Sharjah Calligraphy Museum"},
    {"name": "Khor Fakkan Beach", "price": 0, "time": 3, "people": "any", "type": "family", "city": "sharjah", "location": "Khor Fakkan Beach"},
    {"name": "Al Montazah Parks", "price": 120, "time": 4, "people": "any", "type": "family", "city": "sharjah", "location": "Al Montazah Parks"},
    {"name": "Rain Room", "price": 25, "time": 1, "people": "any", "type": "friends", "city": "sharjah", "location": "Rain Room Sharjah"},
    {"name": "Sharjah Cricket Stadium", "price": 0, "time": 3, "people": "any", "type": "friends", "city": "sharjah", "location": "Sharjah Cricket Stadium"},
    {"name": "Al Hisn Fort Museum", "price": 10, "time": 2, "people": "any", "type": "family", "city": "sharjah", "location": "Sharjah Fort (Al Hisn)"},
    {"name": "Sharjah Maritime Museum", "price": 15, "time": 2, "people": "any", "type": "family", "city": "sharjah", "location": "Sharjah Maritime Museum"},
    {"name": "Wasit Wetland Centre", "price": 15, "time": 2, "people": "any", "type": "family", "city": "sharjah", "location": "Wasit Wetland Centre"},

    # Ajman locations
    {"name": "Ajman Beach", "price": 0, "time": 3, "people": "any", "type": "family", "city": "ajman", "location": "Ajman Beach"},
    {"name": "Ajman Museum", "price": 10, "time": 2, "people": "any", "type": "family", "city": "ajman", "location": "Ajman Museum"},
    {"name": "Al Zorah Nature Reserve", "price": 50, "time": 4, "people": "any", "type": "friends", "city": "ajman", "location": "Al Zorah Nature Reserve"},
    {"name": "Sheikh Zayed Ajman Mosque", "price": 0, "time": 2, "people": "any", "type": "family", "city": "ajman", "location": "Sheikh Zayed Ajman Mosque"},
    {"name": "City Centre Ajman", "price": 0, "time": 3, "people": "any", "type": "friends", "city": "ajman", "location": "City Centre Ajman"},
    {"name": "Ajman Marina", "price": 0, "time": 2, "people": "any", "type": "friends", "city": "ajman", "location": "Ajman Marina"},
    {"name": "Al Murabba Watchtower", "price": 0, "time": 1, "people": "any", "type": "family", "city": "ajman", "location": "Al Murabba Watchtower"},
    {"name": "Al Tallah Camel Race Course", "price": 0, "time": 3, "people": "any", "type": "friends", "city": "ajman", "location": "Al Tallah Camel Race Course"},
    {"name": "Ajman Dhow Yard", "price": 0, "time": 2, "people": "any", "type": "family", "city": "ajman", "location": "Ajman Dhow Yard"},
    {"name": "Al Jurf Park", "price": 0, "time": 3, "people": "any", "type": "family", "city": "ajman", "location": "Al Jurf Park"},
    {"name": "Marsa Ajman", "price": 0, "time": 2, "people": "any", "type": "friends", "city": "ajman", "location": "Marsa Ajman"},
    {"name": "Ajman Fish Market", "price": 0, "time": 1, "people": "any", "type": "family", "city": "ajman", "location": "Ajman Fish Market"},
    {"name": "Thumbay Medicity", "price": 0, "time": 1, "people": "any", "type": "friends", "city": "ajman", "location": "Thumbay Medicity"},
    {"name": "Hamad Bin Rashid Sports Stadium", "price": 20, "time": 3, "people": "any", "type": "friends", "city": "ajman", "location": "Hamad Bin Rashid Sports Stadium"},
    {"name": "Ajman Saray Beach", "price": 0, "time": 4, "people": "any", "type": "family", "city": "ajman", "location": "Ajman Saray Beach"},
    {"name": "Al Rashidiya Park", "price": 0, "time": 2, "people": "any", "type": "family", "city": "ajman", "location": "Al Rashidiya Park"},
    {"name": "Ajman Pearl", "price": 0, "time": 2, "people": "any", "type": "family", "city": "ajman", "location": "Ajman Pearl"},
    {"name": "Al Helio Park", "price": 0, "time": 3, "people": "any", "type": "family", "city": "ajman", "location": "Al Helio Park"},
    {"name": "Radisson Blu Beach", "price": 0, "time": 4, "people": "any", "type": "family", "city": "ajman", "location": "Radisson Blu Beach"},
    {"name": "Ajman Ladies Park", "price": 0, "time": 3, "people": "any", "type": "family", "city": "ajman", "location": "Ajman Ladies Park"},
    {"name": "Al Zorah Golf Club", "price": 250, "time": 4, "people": "any", "type": "friends", "city": "ajman", "location": "Al Zorah Golf Club"},

    # Ras Al Khaimah Locations
    {"name": "Jebel Jais", "price": 0, "time": 4, "people": "any", "type": "friends", "city": "ras al khaimah", "location": "Jebel Jais"},
    {"name": "Jais Adventure Park", "price": 300, "time": 5, "people": "any", "type": "adventure", "city": "ras al khaimah", "location": "Jais Adventure Park"},
    {"name": "Dhayah Fort", "price": 0, "time": 2, "people": "any", "type": "family", "city": "ras al khaimah", "location": "Dhayah Fort"},
    {"name": "RAK National Museum", "price": 10, "time": 2, "people": "any", "type": "family", "city": "ras al khaimah", "location": "RAK National Museum"},
    {"name": "Al Hamra Mall", "price": 0, "time": 2, "people": "any", "type": "shopping", "city": "ras al khaimah", "location": "Al Hamra Mall"},
    {"name": "Al Marjan Island", "price": 0, "time": 3, "people": "any", "type": "relaxation", "city": "ras al khaimah", "location": "Al Marjan Island"},
    {"name": "Suwaidi Pearls Farm", "price": 150, "time": 3, "people": "any", "type": "family", "city": "ras al khaimah", "location": "Suwaidi Pearls Farm"},
    {"name": "Shimal Archaeological Site", "price": 0, "time": 2, "people": "any", "type": "history", "city": "ras al khaimah", "location": "Shimal Archaeological Site"},
    {"name": "Wadi Shawka", "price": 0, "time": 4, "people": "any", "type": "adventure", "city": "ras al khaimah", "location": "Wadi Shawka"},
    {"name": "Al Qawasim Corniche", "price": 0, "time": 2, "people": "any", "type": "relaxation", "city": "ras al khaimah", "location": "Al Qawasim Corniche"},

    # Umm Al Quwain Locations
    {"name": "Dreamland Aqua Park", "price": 160, "time": 5, "people": "any", "type": "family", "city": "umm al quwain", "location": "Dreamland Aqua Park"},
    {"name": "UAQ National Museum", "price": 5, "time": 2, "people": "any", "type": "history", "city": "umm al quwain", "location": "UAQ National Museum"},
    {"name": "Al Sinniyah Island", "price": 0, "time": 3, "people": "any", "type": "nature", "city": "umm al quwain", "location": "Al Sinniyah Island"},
    {"name": "UAQ Marine Club", "price": 100, "time": 3, "people": "any", "type": "adventure", "city": "umm al quwain", "location": "UAQ Marine Club"},
    {"name": "Falaj Al Mualla Fort", "price": 0, "time": 2, "people": "any", "type": "history", "city": "umm al quwain", "location": "Falaj Al Mualla Fort"},
    {"name": "UAQ Corniche", "price": 0, "time": 2, "people": "any", "type": "relaxation", "city": "umm al quwain", "location": "UAQ Corniche"},
    {"name": "Palma Bowling Club", "price": 50, "time": 2, "people": "any", "type": "entertainment", "city": "umm al quwain", "location": "Palma Bowling Club"},
    {"name": "Mangrove Beach", "price": 0, "time": 3, "people": "any", "type": "nature", "city": "umm al quwain", "location": "Mangrove Beach"},
    {"name": "UAQ Shooting Club", "price": 200, "time": 2, "people": "any", "type": "adventure", "city": "umm al quwain", "location": "UAQ Shooting Club"},
    {"name": "Barracuda Beach Resort", "price": 0, "time": 4, "people": "any", "type": "relaxation", "city": "umm al quwain", "location": "Barracuda Beach Resort"},

    # Fujairah Locations
    {"name": "Al-Bidyah Mosque", "price": 0, "time": 1, "people": "any", "type": "history", "city": "fujairah", "location": "Al-Bidyah Mosque"},
    {"name": "Fujairah Fort", "price": 0, "time": 2, "people": "any", "type": "history", "city": "fujairah", "location": "Fujairah Fort"},
    {"name": "Fujairah Museum", "price": 5, "time": 2, "people": "any", "type": "history", "city": "fujairah", "location": "Fujairah Museum"},
    {"name": "Snoopy Island", "price": 100, "time": 4, "people": "any", "type": "adventure", "city": "fujairah", "location": "Snoopy Island"},
    {"name": "Fujairah Corniche", "price": 0, "time": 2, "people": "any", "type": "relaxation", "city": "fujairah", "location": "Fujairah Corniche"},
    {"name": "Ain Al Madhab Hot Springs", "price": 20, "time": 2, "people": "any", "type": "relaxation", "city": "fujairah", "location": "Ain Al Madhab Hot Springs"},
    {"name": "Fujairah Adventure Park", "price": 150, "time": 3, "people": "any", "type": "adventure", "city": "fujairah", "location": "Fujairah Adventure Park"},
    {"name": "Al Aqah Beach", "price": 0, "time": 3, "people": "any", "type": "relaxation", "city": "fujairah", "location": "Al Aqah Beach"},
    {"name": "Wadi Wurayah National Park", "price": 0, "time": 5, "people": "any", "type": "adventure", "city": "fujairah", "location": "Wadi Wurayah National Park"},
    {"name": "Madhab Spring Park", "price": 10, "time": 2, "people": "any", "type": "family", "city": "fujairah", "location": "Madhab Spring Park"},
    {"name": "Dibba Rock", "price": 150, "time": 4, "people": "any", "type": "adventure", "city": "fujairah", "location": "Dibba Rock"},
    {"name": "Fujairah Mall", "price": 0, "time": 2, "people": "any", "type": "shopping", "city": "fujairah", "location": "Fujairah Mall"},
    {"name": "Masafi Market", "price": 0, "time": 2, "people": "any", "type": "shopping", "city": "fujairah", "location": "Masafi Market"},
    {"name": "Fujairah Grand Mosque", "price": 0, "time": 1, "people": "any", "type": "history", "city": "fujairah", "location": "Fujairah Grand Mosque"},
    {"name": "Shark Island", "price": 200, "time": 4, "people": "any", "type": "adventure", "city": "fujairah", "location": "Shark Island"},
    {"name": "Bithnah Fort", "price": 0, "time": 2, "people": "any", "type": "history", "city": "fujairah", "location": "Bithnah Fort"},
    {"name": "Al Hayl Castle", "price": 0, "time": 2, "people": "any", "type": "history", "city": "fujairah", "location": "Al Hayl Castle"},
    {"name": "Fujairah Beach", "price": 0, "time": 3, "people": "any", "type": "relaxation", "city": "fujairah", "location": "Fujairah Beach"},
    {"name": "Khor Fakkan Waterfall", "price": 0, "time": 2, "people": "any", "type": "relaxation", "city": "fujairah", "location": "Khor Fakkan Waterfall"},
    {"name": "Scuba Diving at Fujairah", "price": 300, "time": 4, "people": "any", "type": "adventure", "city": "fujairah", "location": "Fujairah Diving Sites"},
]

# List of hotels based on budget
hotels = {
    "abu dhabi": {
        "luxury": ["Emirates Palace", "St. Regis Saadiyat Island"],
        "mid range": ["Radisson Blu", "Marriott Downtown"],
        "budget": ["Premier Inn", "Holiday Inn Express"]
    },
    "dubai": {
        "luxury": ["Burj Al Arab", "Atlantis The Palm"],
        "mid range": ["Sheraton Dubai", "Movenpick"],
        "budget": ["Citymax Hotel", "Days Dubai"]
    },
    "sharjah": {
        "luxury": ["The Act Hotel", "The Chedi Al Bait"],
        "mid range": ["Golden Sands Hotel", "Copthorne Hotel"],
        "budget": ["Crystal Plaza Hotel", "Al Naha Hotel"]
    },
    "ras al khaimah": {
        "luxury": ["Hilton Al Hamra", "The Ritz Carlton"],
        "mid range": ["Hilton Garden Inn", "Citymax Hotel"],
        "budget": ["Aja Hotel", "Actico Hotel"]
    },
    "ajman": {
        "luxury": ["Wyndham Savoy", "The Sheen Beach Resort"],
        "mid range": ["Hyandam Hotel", "Ramada Hotel"],
        "budget": ["Reef Hotel", "Al Smou Hotel"]
    },
    "umm al quwain": {
        "luxury": ["Vida Beach Resort", "Palma Beach Resort"],
        "mid range": ["Barracuda Beach Resort", "Flamingo Beach Resort"],
        "budget": ["Pearl Hotel", "Royal Residence Hotel"]
    },
    "fujairah": {
        "luxury": ["Le Merdien Al Aqah Beach Resort", "Fairmont Fujairah Beach Resort"],
        "mid range": ["Fujairah Rotana Resort", "Novotel Fujairah"],
        "budget": ["City Tower Hotel", "Ibis Fujairah"]
    }
}

# Function to generate a Google Maps URL for restaurant search with a category
def find_restaurants_on_google_maps(city, category):
    # Generate a Google Maps URL for restaurants in the specified city and category
    return f"https://www.google.com/maps?q={category}+restaurants+in+{city.replace(' ', '+')}"

# Main program
def main():
    # User Input
    try:
        budget = int(input("Enter your budget (AED): "))
        time_available = int(input("Enter time available (hours): "))
        people_count = input("Enter number of people: ")
        company_type = input("Are you with: family, friends, or other? ").strip().lower()
        city = input("Enter your city: ").strip().lower()

        # Find matching activities
        suggestions = [act for act in activities if act["price"] <= budget and act["time"] <= time_available and act["city"] == city]

        if suggestions:
            print("\nHere are some activities you can do:")
            for i, act in enumerate(suggestions, start=1):
                print(f"{i}. {act['name']} - https://www.google.com/maps?q={act['name'].replace(' ', '+')}")

            try:
                selected_activity = int(input("Select an activity number for more details: ")) - 1
                if 0 <= selected_activity < len(suggestions):
                    activity = suggestions[selected_activity]
                    print(f"You've selected: {activity['name']} located at {activity['location']}")

                    # Ask about dining
                    dining_out = input("Are you dining out? (yes/no): ").strip().lower()
                    if dining_out == "yes":
                        # List of valid categories
                        categories = {
                            "1": "American",
                            "2": "Arabic",
                            "3": "European",
                            "4": "Indian",
                            "5": "Mexican",
                            "6": "Asian (Chinese, Japanese, Korean)"
                        }
                        print("\nSelect a cuisine category:")
                        for key, value in categories.items():
                            print(f"{key}. {value}")

                        while True:
                            category_choice = input("Enter the number corresponding to your preferred cuisine: ").strip()
                            if category_choice in categories:
                                category = categories[category_choice]
                                google_maps_url = find_restaurants_on_google_maps(city, category)
                                print(f"Here are some {category} restaurants in {city.capitalize()}: {google_maps_url}")
                                break
                            else:
                                print("Invalid choice. Please enter a valid number.")
                else:
                    print("Invalid activity number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        else:
            print("No matching activities found. Try adjusting your filters.")

        # Ask about hotels
        staying = input("Are you booking a hotel? (yes/no): ").strip().lower()
        if staying == "yes":
            while True:
                try:
                    nights = int(input("How many nights are you staying? "))
                    if nights > 0:
                        break
                    else:
                        print("Please enter a valid number of nights.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            while True:
                hotel_budget = input("Luxury, Mid-range, or Budget? ").strip().lower()
                if hotel_budget in ["luxury", "mid range", "budget"]:
                    if city in hotels and hotel_budget in hotels[city]:
                        print(f"Recommended hotel: {hotels[city][hotel_budget][0]}")
                        break
                    else:
                        print("Invalid city or hotel budget.")
                        break
                else:
                    print("Invalid budget type. Please try again.")

    except ValueError:
        print("Invalid input. Please enter valid numbers for budget and time.")


if __name__ == "_main_":
    main()  # Corrected indentation here
