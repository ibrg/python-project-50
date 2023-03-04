import json


def show_result(data: dict) -> str:
    # Форматируем вывод согласно формату (по умолчанию json)

    result = {k: v['value'] for k, v in data.items()}
    result = json.dumps(result, indent=2).replace('"', '')
    print(result)
