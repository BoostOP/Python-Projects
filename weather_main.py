import customtkinter as tk
import requests

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")


class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")

        self.api_key = "YOUR_API_CODE_HERE"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

        self.base_frame = tk.CTkFrame(master)
        self.base_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.city_label = tk.CTkLabel(self.base_frame, text="Enter City:", font=("Segoe UI Semibold", 40))
        self.city_label.pack(padx=10, pady=10)

        self.city_entry = tk.CTkEntry(
            self.base_frame, placeholder_text="City entry...", font=("Segoe UI Semibold", 15)
        )

        self.city_entry.pack(padx=5, pady=5, fill="x")

        self.weather_button = tk.CTkButton(
            self.base_frame, text="Request Weather", font=("Segoe UI Semibold", 15), command=self.get_weather
        )

        self.weather_button.pack(padx=5, pady=5)

        self.weather_label_top = tk.CTkLabel(
            self.base_frame, text="Main:", font=("Segoe UI Semibold", 25), text_color="gray"
        )

        self.weather_label_top.pack(padx=10, pady=10)

        self.weather_label = tk.CTkLabel(
            self.base_frame, text="...", font=("Segoe UI Semibold", 20), wraplength=450
        )

        self.weather_label.pack(padx=2.5, pady=2.5)

        self.other_labels_top = tk.CTkLabel(
            self.base_frame, text="Other:", font=("Segoe UI Semibold", 25), text_color="gray"
        )

        self.other_labels_top.pack(padx=5, pady=5)

        self.other_labels = tk.CTkLabel(
            self.base_frame, text="...", font=("Segoe UI Semibold", 20), wraplength=450
        )

        self.other_labels.pack(padx=2.5, pady=2.5)

        self.temperature_labels_top = tk.CTkLabel(
            self.base_frame, text="Temperatures:", font=("Segoe UI Semibold", 25), text_color="gray"
        )

        self.temperature_labels_top.pack(padx=5, pady=5)

        self.temperature_labels = tk.CTkLabel(
            self.base_frame, text="...", font=("Segoe UI Semibold", 20), wraplength=450
        )

        self.temperature_labels.pack(padx=2.5, pady=2.5)

        self.atmospheric_labels_top = tk.CTkLabel(
            self.base_frame, text="Atmospheric:", font=("Segoe UI Semibold", 25), text_color="gray"
        )

        self.atmospheric_labels_top.pack(padx=5, pady=5)

        self.atmospheric_labels = tk.CTkLabel(
            self.base_frame, text="...", font=("Segoe UI Semibold", 20), wraplength=450
        )

        self.atmospheric_labels.pack(padx=2.5, pady=2.5)

        self.wind_labels_top = tk.CTkLabel(
            self.base_frame, text="Wind:", font=("Segoe UI Semibold", 25), text_color="gray"
        )

        self.wind_labels_top.pack(padx=5, pady=5)

        self.wind_labels = tk.CTkLabel(
            self.base_frame, text="...", font=("Segoe UI Semibold", 20), wraplength=450
        )

        self.wind_labels.pack(padx=2.5, pady=2.5)

        self.creator_label = tk.CTkLabel(
            self.base_frame, text="Python 23.2.1, (Pycharm)", font=("Segoe UI Semibold", 25), text_color="gray"
        )

        self.creator_label.pack(padx=5, pady=5, expand=True)

    def get_weather(self):
        city = self.city_entry.get()

        if city:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"
            }

            response = requests.get(self.base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                weather_label_info = (
                    f"Weather in {city}: {data['weather'][0]['description']}, "
                    f"Temperature in {city}: {data['main']['temp'] * 1.8 + 32}°F, "
                )

                other_labels_info = (
                    f"Feels like: {data['main']['feels_like'] * 1.8 + 32}°F in {city}, "
                )

                temperature_labels_info = (
                    f"Temperature minimum in {city}: {data['main']['temp_min'] * 1.8 + 32}°F, "
                    f"Temperature max in {city}: {data['main']['temp_max'] * 1.8 + 32}°F, "
                )

                atmospheric_labels_info = (
                    f"Pressure in {city}: {data['main']['pressure']}, "
                    f"Humidity in {city}: {data['main']['humidity']}."
                )

                wind_labels_info = (
                    f"Wind speed in {city}: {data['wind']['speed']} (MPH), "
                    f"Wind degree in {city}: {data['wind']['deg']}."
                )

                self.weather_label.configure(text=weather_label_info)
                self.other_labels.configure(text=other_labels_info)
                self.temperature_labels.configure(text=temperature_labels_info)
                self.atmospheric_labels.configure(text=atmospheric_labels_info)
                self.wind_labels.configure(text=wind_labels_info)
            else:
                self.weather_label.configure(text="Error fetching main data.")
                self.other_labels.configure(text="Error fetching other data.")
                self.temperature_labels.configure(text="Error fetching temperature data.")
                self.atmospheric_labels.configure(text="Error fetching atmospheric data.")
                self.wind_labels.configure(text="Error fetching wind data.")
        else:
            self.weather_label.configure(text="Please enter a city for the main data to be fetched.")
            self.other_labels.configure(text="Please enter a city for the other data to be fetched.")
            self.temperature_labels.configure(text="Please enter a city for the temperature data to be fetched.")
            self.atmospheric_labels.configure(text="Please enter a city for the atmospheric data to be fetched.")
            self.wind_labels.configure(text="Please enter a city for the wind data to be fetched.")


def main():
    root = tk.CTk()
    app = WeatherApp(master=root)

    root.geometry("900x800")
    root.mainloop()

    app.master = root


if __name__ == "__main__":
    main()
