def format_itineraries(itineraries):
    formatted_itinerary = ""
    for index, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        formatted_itinerary += f"Itinerary {index}: {traveler_name} - From {origin} to {destination}\n"
    return formatted_itinerary.strip()

flight_itineraries = []

while True:
    traveler_name = input("Please enter your first name (or type 'stop' to finish): ")
    if traveler_name.lower() == 'stop':
        break
    origin = input("Where are you leaving from? ")
    destination = input("Where are you going? ")
    flight_itineraries.append((traveler_name, origin, destination))

result = format_itineraries(flight_itineraries)
print(result)