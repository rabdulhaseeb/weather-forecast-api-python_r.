import requests

# Function to get weather data
def get_moosam(shehar, key_pass):
    link = f"http://api.openweathermap.org/data/2.5/weather?q={shehar}&appid={key_pass}&units=metric"
    try:
        jawab = requests.get(link)
        jawab.raise_for_status()  # Raise an error for bad status codes
        data = jawab.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        if jawab.status_code == 404:
            print("Error: City not found. Please check the city name.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")
    return None

# Main function
def main():
    print("Welcome to the Weather Forecast Application")
    key_pass = "4cc2e6d4d00c056527500cab0ea2efd4"

    while True:
        shehar = input("Enter city name (or type 'exit' to quit): ")
        if shehar.lower() == 'exit':
            print("Thank you for using the Weather Forecast Application!")
            break

        weather_data = get_moosam(shehar, key_pass)

        if weather_data:
            if weather_data["cod"] == 200:
                weather_description = weather_data["weather"][0]["description"]
                temperature = weather_data["main"]["temp"]
                humidity = weather_data["main"]["humidity"]
                wind_speed = weather_data["wind"]["speed"]

                print(f"\nCurrent weather in {shehar}:")
                print(f"Weather: {weather_description}")
                print(f"Temperature: {temperature} °C")
                print(f"Humidity: {humidity}%")
                print(f"Wind Speed: {wind_speed} m/s\n")
            elif weather_data["cod"] == 400:
                print("Bad Request: The request was unacceptable. Please check the city name.\n")
            elif weather_data["cod"] == 500:
                print("Server Error: The server encountered an error. Please try again later.\n")
            else:
                error_message = weather_data.get("message", "Unable to retrieve data")
                print(f"Sorry, weather data not available for this city. Error: {error_message}\n")
        else:
            print("No data returned from the API. Please try again later.\n")

        # Ask if the user wants to try again or exit
        try_again = input("Do you want to check the weather for another city? (yes to continue, no to exit): ").lower()
        if try_again == 'no':
            print("Thank you for using the Weather Forecast Application!")
            break

if __name__ == "__main__":
    main()
