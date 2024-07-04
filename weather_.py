import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("800x800")
        
        self.api_key = "7231b2966fd11feff843f7732713b5fe"  
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

        self.create_widgets()
 
    def create_widgets(self):
        self.city_label = tk.Label(self.root, text="Enter City:", font=('consolas', 40))
        self.city_label.pack(pady=10)
        self.city_entry = tk.Entry(self.root, width=30, font=('', 20))
        self.city_entry.pack()
        self.search_button = tk.Button(self.root, text="Search", command=self.search_city, font=('Ariel', 25))
        self.search_button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="", wraplength=300, font=('Ariel', 30))
        self.result_label.pack(pady=20)

    def search_city(self):
        city = self.city_entry.get().strip()
        if city:
            weather_data = self.get_weather_data(city)
            if weather_data:
                self.display_weather(weather_data)
            else:
                messagebox.showerror("Error", "City not found. Please enter a valid city name.")
        else:
            messagebox.showwarning("Warning", "Please enter a city name.")

    def get_weather_data(self, city):
        try:
            params = {'q': city, 'appid': self.api_key, 'units': 'metric'}
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")
            return None

    def display_weather(self, weather_data):
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        weather_text = f"City: {city}\nTemperature: {temperature}°C\nDescription: {description}"
        self.result_label.config(text=weather_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()