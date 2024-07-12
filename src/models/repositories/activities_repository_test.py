import pytest
import uuid
from datetime import datetime
from src.models.settings.db_connection_handler import db_connection_handler
from .activities_repository import ActivitiesRepository

db_connection_handler.connect()
activity_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activity_infos = {
        "id": activity_id,
        "trip_id": trip_id,
        "title": "Mergulho",
        "occurs_at": datetime.strptime("03-01-2024", "%d-%m-%Y"),
    }

    activities_repository.registry_activity(activity_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities = activities_repository.find_activities_from_trip(trip_id)
    print(activities)
