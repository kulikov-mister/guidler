# utils/validate_data.py
import aiohttp


# чекер данных ордера перед записью в бд
def validate_order_data(order_data):
    required_fields = [
        "user_id", "first_latitude", "first_longitude",
        "second_latitude", "second_longitude", "payment_method",
        "comment", "location_id", "distance", "cost"
    ]

    missing_fields = [field for field in required_fields if field not in order_data or order_data[field] is None]
    
    if missing_fields:
        raise ValueError(f"Отсутствуют следующие обязательные поля: {', '.join(missing_fields)}")

    return True


# проверка bing ключа
async def validate_bing_key(api_key: str) -> bool:
    url = f"https://dev.virtualearth.net/REST/v1/Locations?query=New%20York&key={api_key}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.status == 200