class Smartphone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def make_call(self, phone_number):
        if self.battery_percentage > 0:
            print(f"Calling {phone_number}...")
            self.battery_percentage -= 5  # Simulate battery drain
        else:
            print("Battery is dead. Please charge your phone.")

    def send_message(self, phone_number, message):
        if self.battery_percentage > 0:
            print(f"Sending message to {phone_number}: {message}")
            self.battery_percentage -= 2  # Simulate battery drain
        else:
            print("Battery is dead. Please charge your phone.")

    def check_battery(self):
        print(f"Battery at {self.battery_percentage}%.")

# Example usage
phone = Smartphone("Apple", "iPhone 14", 100)
phone.make_call("123-456-7890")
phone.send_message("123-456-7890", "Hello there!")
phone.check_battery()
