import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .participants_repository import ParticpantsRepository

db_connection_handler.connect()
participant_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())
emails_to_invite_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_participant():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticpantsRepository(conn)

    partcipant_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": emails_to_invite_id,
        "name": "Tayna"
    }

    participants_repository.registry_participant(partcipant_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticpantsRepository(conn)

    participants = participants_repository.find_participants_from_trip(trip_id)
    print(participants)

@pytest.mark.skip(reason="interacao com o banco")
def test_update_participant_status():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticpantsRepository(conn)
    
    participants_repository.update_participant_status(participant_id)
