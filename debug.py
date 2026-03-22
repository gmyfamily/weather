import httpx

response = httpx.get("https://wttr.in/Shanghai", params={"format": "j1"})
print(response.status_code)
print(response.text[:200])
