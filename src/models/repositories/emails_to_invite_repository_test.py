import pytest
import uuid
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
email_to_invite_id = str(uuid.uuid4())
trip_id = "d68469eb-075b-471c-b9df-dc4439333b86"

@pytest.mark.skip(reason="interacao com o banco")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email_infos = {
        "id": email_to_invite_id,
        "trip_id": trip_id,
        "email": "taynaemail.com"
    }

    emails_to_invite_repository.registry_email(email_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    print(emails)

