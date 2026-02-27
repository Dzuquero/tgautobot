import requests
URL = "https://carsensor.net/api/search"
def fetch_cars():
    try:
        r = requests.get(URL, timeout=10)
        r.raise_for_status()
        data = r.json()
    except Exception:
        return []
    cars = []
    for c in data.get("results", []):
        cars.append(dict(
            brand=c.get("brand"),
            model=c.get("model"),
            year=c.get("year"),
            price=c.get("price"),
            color=c.get("color"),
            url=c.get("url"),
        ))
    return cars
