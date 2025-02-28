from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_k ey}&units=metric'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f'The weather in {city} is {weather_description} with a temperature of {temperature}°C.'
    else:
        return 'Failed to fetch weather information.'


@app.route('/')
def home():
    return render_template('index_api.html')


@app.route('/weather', methods=['POST'])
def weather():
    api_key = 'your-openweathermap-api-key'  # Replace with your API key
    city = request.form['city']
    result = get_weather(api_key, city)
    return render_template(s.html', result=result)


if name == ' main ': 
    app.run(debug=True) 