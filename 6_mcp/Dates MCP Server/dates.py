from datetime import date

def get_date() -> str:
    return date.today().isoformat()
