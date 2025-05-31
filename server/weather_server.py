from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(city: str) -> str:
    """Get weather information for a city"""
    fake_weather = {
        "北京": "晴，25°C",
        "上海": "多云，28°C",
        "广州": "小雨，30°C"
    }
    return fake_weather.get(city, "未知城市，无法获取天气信息")

if __name__ == "__main__":
    mcp.run(transport="stdio")
