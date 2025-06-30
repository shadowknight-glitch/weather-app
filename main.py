import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "e16ea8b3fc9ac2c14a024d8f5fd3f347"  # Replace with your actual key

def get_weather(city):
    city = city.strip()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def show_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    weather = get_weather(city)

    if weather:
        try:
            name = weather['name']
            desc = weather['weather'][0]['description'].title()
            temp = weather['main']['temp']
            feels = weather['main']['feels_like']
            humidity = weather['main']['humidity']
            wind = weather['wind']['speed']

            result = f" City: {name}\n Weather: {desc}\n Temp: {temp}°C\n Feels Like: {feels}°C\n Humidity: {humidity}%\n Wind: {wind} m/s"
            result_label.config(text=result)
        except KeyError:
            messagebox.showerror("Error", "Failed to parse weather data.")
    else:
        messagebox.showerror("Error", "City not found or API error.")

# ------------------ GUI SETUP ------------------ #
root = tk.Tk()
root.title("☀️ Weather App")
root.geometry("420x500")
root.configure(bg="#b3e0ff")  # Sky blue

# Styling for consistent look
main_font = ("Helvetica", 14)
title_font = ("Helvetica", 20, "bold")
button_color = "#FFD54F"  # Soft yellow
hover_color = "#ffe082"
entry_bg = "#ffffff"

# Title
tk.Label(root, text="☁️ Weather Forecast", font=title_font, bg="#b3e0ff", fg="#222").pack(pady=25)

# Input field container (to fake rounded edge)
input_frame = tk.Frame(root, bg="#b3e0ff")
input_frame.pack(pady=5)

# Label + Entry box
tk.Label(input_frame, text="Enter City Name:", font=main_font, bg="#b3e0ff").pack()
city_entry = tk.Entry(input_frame, font=main_font, width=24, bd=0, bg=entry_bg, justify="center", relief="flat")
city_entry.pack(pady=6, ipady=8, ipadx=4)

# Button styling
def on_enter(e):
    weather_button['bg'] = hover_color

def on_leave(e):
    weather_button['bg'] = button_color

weather_button = tk.Button(
    root, text="Check Weather", font=main_font,
    bg=button_color, fg="black", bd=0, relief="flat",
    activebackground=hover_color, padx=20, pady=10,
    command=show_weather
)
weather_button.pack(pady=20)
weather_button.bind("<Enter>", on_enter)
weather_button.bind("<Leave>", on_leave)

# Result Frame
result_frame = tk.Frame(root, bg="white", bd=1, relief="solid", highlightthickness=0)
result_frame.pack(padx=25, pady=10, fill="both", expand=True)

# Result Label
result_label = tk.Label(result_frame, text="", font=main_font, bg="white", justify="left", anchor="nw")
result_label.pack(padx=15, pady=15, fill="both", expand=True)

# Run the app
root.mainloop()
