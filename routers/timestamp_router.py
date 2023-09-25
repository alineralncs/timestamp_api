from datetime import date
from os import getenv

from dotenv import find_dotenv
from fastapi import APIRouter, HTTPException
from fastapi.security import APIKeyHeader

from .operations import convert_date_to_timestamp, convert_timestamp_to_date

router = APIRouter()


@router.get("/timestamp-to-date")
def timestamp_to_date(timestamp: float):
    """Convert a timestamp to a date"""

    try:
        return convert_timestamp_to_date(timestamp)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/date-to-timestamp")
def timestamp_to_date(date: str):
    """Convert a timestamp to a date"""

    try:
        return convert_date_to_timestamp(date)
    except Exception as e:
       
        raise HTTPException(status_code=400, detail=str(e))
