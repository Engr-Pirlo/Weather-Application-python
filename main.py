import tkinter as tk
import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == "404":
        return "City not found"
    else:
        weather = f"Weather: {data['weather'][0]['description'].capitalize()}\nTemperature: {data['main']['temp']}°C\nHumidity: {data['main']['humidity']}%"
        return weather

def search():
    city = entry.get()
    weather = get_weather(city)
    label.config(text=weather)

root = tk.Tk()
root.title("Weather Application")

label1 = tk.Label(root, text="Enter city name:")
label1.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Search", command=search)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()