from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates
import weather
import water
import sensor


app = FastAPI()

templates =  Jinja2Templates(directory="templates")

@app.get('/')
async def read_root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request, "name": "shalom", "weather": weather.get_weather(), "sensor_data":sensor.sensor_data()})


LOCATION="Accra"


from fastapi_utilities import repeat_every

@app.on_event('startup')
@repeat_every(seconds=3)
async def watering_system():
    # Pass weather data, sensor data as args
    water.water_code()

# if __name__ == '__main__':  
#     uvicorn.run(app, host='127.0.0.1', port=8000)