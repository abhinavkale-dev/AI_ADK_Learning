import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    if city.lower() == "nagpur":
        return {"status": "success", "report": "Sunny, 50 degree"}
    return {"status": "error", "message": f"City {city} not found"}

def get_current_time(city: str) -> dict:
    if city.lower() == "nagpur":
        tz = ZoneInfo("Asia/Kolkata")
    else:
        return {"status": "error", "message": f"City {city} not found"}
    now = datetime.datetime.now(tz)
    return {"status": "success", "time": now.strftime("%H:%M:%S")}

root_agent = Agent(
    name="weather_agent",
    model="gemini-2.0-flash",
    description="A weather agent that can get the weather and time for a given city",
    instruction="You are a weather agent that can get the weather and time for a given city",
    tools=[get_weather, get_current_time],
)