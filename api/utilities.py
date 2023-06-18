def convert_celcius_to_fahrenheit(celcius: float) -> float:
    return (celcius * 9/5) + 32

def convert_wind_direction_deg_to_text(deg: int) -> str:
    return [
        "north",
        "north-northeast",
        "northeast",
        "east-northeast",
        "east",
        "east-southeast",
        "southeast",
        "south-southeast",
        "south",
        "south-southwest",
        "southwest",
        "west-southwest",
        "west",
        "west-northwest",
        "northwest",
        "north-northwest"
    ][round(deg/22.5)%16]

def get_wind_speed_description(speed: float) -> str:
    if speed >= 0 and speed <= 0.2:
        return 'calm'
    elif speed > 0.3 and speed <= 1.5:
        return 'light air'
    elif speed > 1.6 and speed <= 3.3:
        return 'light breeze'
    elif speed > 3.4 and speed <= 5.4:
        return 'gentle breeze'
    elif speed > 5.5 and speed <= 7.9:
        return 'moderate breeze'
    elif speed > 8 and speed <= 10.7:
        return 'fresh breeze'
    elif speed > 10.8 and speed <= 13.8:
        return 'strong breeze'
    elif speed > 13.9 and speed <= 17.1:
        return 'moderate gale'
    elif speed > 17.2 and speed <= 20.7:
        return 'fresh gale'
    elif speed > 20.8 and speed <= 24.4:
        return 'strong gale'
    elif speed > 24.5 and speed <= 28.4:
        return 'full gale/storm'
    elif speed > 28.5 and speed <= 32.6:
        return 'violent storm'
    elif speed >= 32.7:
        return 'hurricane'
    else:
        return f'not description found for this speed value: {speed} m/s'
    
def get_localized_human_time_from_unix(unix: int, timezone: int) -> str:
    from datetime import datetime

    timezone /= 3600
    date = datetime.utcfromtimestamp(unix)
    local_hour = int(date.hour + timezone)

    return f'{local_hour}:{date.minute}' if local_hour-10 >= 0 else f'0{local_hour}:{date.minute}'