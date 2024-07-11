from flask import jsonify, Blueprint, request

# importacao de controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

# importacao de repositorios
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository

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
