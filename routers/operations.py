from datetime import datetime
import logging
from fastapi import HTTPException

def convert_timestamp_to_date(timestamp: int):
    """ Convert a timestamp to a date and to miliseconds"""

    try:
        if len(str(timestamp)) == 13:
            timestamp_seconds = timestamp * 1000
        else:
            timestamp_seconds = timestamp

        data = datetime.fromtimestamp(timestamp_seconds)

        formated_data = data.strftime("%Y-%m-%d %H:%M:%S")

        print(f"timestamp_seconds: {timestamp_seconds}, formatted_date {formated_data}")
        return {"timestamp ": timestamp_seconds, "formatted_date": formated_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def convert_date_to_timestamp(date: str):
    """ Convert a date to a timestamp """
    timestamp = datetime.strptime(date, "%Y-%m-%d").timestamp()
    return {"date": date, "timestamp": timestamp}