from flask import jsonify, Blueprint, request

# importacao de controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participants_finder import ParticipantsFinder
from src.controllers.participant_confirmer import ParticipantConfimer

from src.controllers.activity_creator import ActivityCreator
from src.controllers.activities_finder import ActivitiesFinder

# importacao de repositorios
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.activities_repository import ActivitiesRepository

# importacao de conexoes
from src.models.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    # pegar connection do db que foi iniciada no run.py
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    # pegar connection do db que foi iniciada no run.py
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(tripId)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
    # pegar connection do db que foi iniciada no run.py
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmer(trips_repository)

    response = controller.confirm(tripId)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_link(tripId):
    # pegar connection do db que foi iniciada no run.py
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_link(tripId):
    # pegar connection do db que foi iniciada no run.py
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinder(links_repository)

    response = controller.find(tripId)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invites_to_trip(tripId):
    # pegar connection do db que foi iniciada no run.py
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = ParticipantCreator(participants_repository, emails_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def get_trip_participants(tripId):
    # pegar connection do db que foi iniciada no run.py
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantsFinder(participants_repository)

    response = controller.finder(tripId)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route("/participants/<participantId>/confirm", methods=["PATCH"])
def confirm_invite(participantId):
    # pegar connection do db que foi iniciada no run.py
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantConfimer(participants_repository)

    response = controller.confirm(participantId)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
    # pegar connection do db que foi iniciada no run.py
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityCreator(activities_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId):
    # pegar connection do db que foi iniciada no run.py
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivitiesFinder(activities_repository)

    response = controller.finder(tripId)

    return jsonify(response['body']), response['status_code']
