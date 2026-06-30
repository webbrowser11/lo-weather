import requests

def fetch_weather_data():
    # The NWS API requires a User-Agent header; otherwise, your requests might get blocked.
    headers = {"User-Agent": "lo-weather/1.0 (terpstragraham@gmail.com)"}
    
    # ---------------------------------------------------------
    # 1. Fetch Current Observations (Your original code)
    # ---------------------------------------------------------
    obs_response = requests.get('https://api.weather.gov/stations/KPDX/observations/latest', headers=headers)
    obs_data = obs_response.json()
    
    temp_c = obs_data['properties']['temperature']['value']
    # Added a quick fallback check just in case the station sensor is temporarily down
    temp_f = (temp_c * 9/5) + 32 if temp_c is not None else None
    temp_f = round(temp_f)
    current_sky = obs_data['properties']['textDescription']
    last_updated = obs_data['properties']['timestamp']
    
    obs_string = f"{temp_f:.1f} degrees Fahrenheit, {current_sky}." if temp_f else "Temperature data unavailable."

    # ---------------------------------------------------------
    # 2. Fetch Forecast (High, Low, Day/Night Sky Cover)
    # ---------------------------------------------------------
    # We use KPDX's exact latitude/longitude to get the grid forecast URL.
    points_response = requests.get('https://api.weather.gov/points/45.5898,-122.5951', headers=headers)
    points_data = points_response.json()
    
    forecast_url = points_data['properties']['forecast']
    forecast_response = requests.get(forecast_url, headers=headers)
    forecast_data = forecast_response.json()
    
    periods = forecast_data['properties']['periods']
    
    # The API returns 12-hour periods. Period 0 is the current half of the day.
    period_1 = periods[0] 
    period_2 = periods[1] 
    
    # We have to check if right now is daytime or nighttime so we grab the right variables.
    # If you run this at 9 PM, "Today" has already passed in the API!
    if period_1['isDaytime']:
        day_temp = period_1['temperature']         # Today's High
        day_sky = period_1['shortForecast']        # Today's Sky
        night_temp = period_2['temperature']       # Tonight's Low
        night_sky = period_2['shortForecast']      # Tonight's Sky
    else:
        # If the script runs at night, period_1 is Tonight, period_2 is Tomorrow
        night_temp = period_1['temperature']       
        night_sky = period_1['shortForecast']      
        day_temp = period_2['temperature']         
        day_sky = period_2['shortForecast']        

    # ---------------------------------------------------------
    # 3. Return combined dictionary
    # ---------------------------------------------------------
    return {
        "observations-lake-oswego": obs_string,
        "last-updated-observations-lake-oswego": last_updated,
        "forecast-high": f"{day_temp} degrees fahrenheit",
        "forecast-low": f"{night_temp} degrees fahrenheit",
        "forecast-day-sky": day_sky,
        "forecast-night-sky": night_sky
    }