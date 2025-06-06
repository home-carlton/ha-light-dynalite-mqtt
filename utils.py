# utils.py
from datetime import datetime


def log(msg: str):
    print(f"{datetime.now().strftime('%H:%M:%S')} 🧠 {msg}")


def percent_to_brightness(percent_str):
    try:
        val = int(percent_str.strip('%'))
        return round(val * 255 / 100)
    except:
        return 0

#get the field value from mes type
def get_val_by_mestype(mes_type: str, fields: list, field_types: dict, to_int: bool = False):
    if not field_types:
        return None
    for idx, t in field_types.items():
        if t.lower() == mes_type.lower():
            try:
                idx_int = int(idx)
                val = fields[idx_int] if idx_int < len(fields) else None
                if val in [None, "", "<unset>", "<err>"]:
                    return None
                return int(float(val)) if to_int else val
            except (ValueError, IndexError, TypeError):
                return None
    return None