import json


def format_result(data: dict) -> str:
    # Форматируем вывод согласно формату (по умолчанию json)
    result = {v["status"] + ' ' + k: v["value"] for k, v in data.items()}
    result = json.dumps(result, indent=2).replace('"', '').replace(',', '')
    return result
