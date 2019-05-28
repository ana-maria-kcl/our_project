import requests

cities = {
    'barbados': 'Holetown',
    'china': 'Beijing',
    'greece': 'Athens',
    'norway': 'Oslo',
    'spain': 'Madrid',
    'switzerland': 'Berne',
    'thailand': 'Bangkok',
}

def get_weather(country):
    city = cities[country]
    url = f"http://api.openweathermap.org/data/2.5/weather/?q={city}&units=Metric&appid=8bc86d6f307b883025df9dff9c02a895"

    r = requests.get(url).json()

    weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],

    }
    return weather