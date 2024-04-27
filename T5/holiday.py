# city_flight = input("which city did you fly to?:")

# city_costs = {
#     "New York": 300,
#     "Los Angeles": 250,
#     "Chicago": 280,
#     "Miami": 350,
#     "San Francisco": 280
# }
# num_nights = input("what was the number of nights at the hotel?:")


# rental_days = input("The number of days you hired the car for?:")


# def hotel_cost(num_nights, unit_cost=150):
#     hcost = num_nights * unit_cost
#     return hcost

# def plane_cost(city_flight):
#     if city_flight in city_costs:
#     # Get the flight cost for the chosen city
#         flight_cost = city_costs[city_flight]
#         print(f"The cost of flying to {city_flight} is ${flight_cost}.")
#     else:
#         print("Invalid city name. Please choose a city from the list.")
#     return flight_cost
    
# def car_rental(rental_days, daily_cost=150):
#     total_rental = rental_days * daily_cost
#     print(f"The total cost of car rental was {total_rental}")
    
# def holiday_cost(num_nights, city_flight, rental_days):
#     total_cost = sum(int(hotel_cost(num_nights)), int(plane_cost(city_flight)), int(car_rental(rental_days)))
#     return total_cost
#     print(f"Total cost of the trip {total_cost}")

def hotel_cost(num_nights):
  """Calculates the total hotel cost based on the number of nights.

  Args:
      num_nights: The number of nights the user will stay at the hotel.

  Returns:
      The total cost of the hotel stay. (price per night * number of nights)
  """
  price_per_night = 180  # You can adjust this price
  return num_nights * price_per_night

def plane_cost(city_flight):
  """Calculates the plane cost based on the destination city.

  Args:
      city_flight: The city the user is flying to.

  Returns:
      The cost of the flight to the chosen city.
  """
  flight_costs = {
      "London": 500,
      "Manchester": 700,
      "Birmingham": 1200,
  }
  return flight_costs.get(city_flight, 800)  # Default cost for other cities

def car_rental(rental_days):
  """Calculates the total car rental cost based on the number of rental days.

  Args:
      rental_days: The number of days the user will rent the car.

  Returns:
      The total cost of the car rental. (daily rental cost * number of days)
  """
  daily_rental_cost = 40  # You can adjust this price
  return rental_days * daily_rental_cost

def holiday_cost(num_nights, city_flight, rental_days):
  """Calculates the total cost of the holiday.

  Args:
      num_nights: The number of nights the user will stay at the hotel.
      city_flight: The city the user is flying to.
      rental_days: The number of days the user will rent the car.

  Returns:
      The total cost of the entire holiday.
  """
  return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

def main():
  """Prompts the user for input and prints the holiday cost breakdown."""
  city_flights = ["London", "Manchester", "Birmingham"]
  print("Available Destination Cities:")
  for city in city_flights:
    print(city)

  city_flight = input("Enter your destination city: ")
  num_nights = int(input("Enter the number of nights you'll stay: "))
  rental_days = int(input("Enter the number of days you'll rent a car: "))

  total_cost = holiday_cost(num_nights, city_flight, rental_days)

  print(f"\nYour holiday details:")
  print(f"Destination City: {city_flight}")
  print(f"Number of Nights: {num_nights}")
  print(f"Number of Car Rental Days: {rental_days}")
  print(f"Total Holiday Cost: ${total_cost}")

if __name__ == "__main__":
  main()
