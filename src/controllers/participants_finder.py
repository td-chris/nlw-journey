class ParticipantsFinder:
    def __init__(self, participants_repository) -> None:
        self.__participants_repository = participants_repository

    def finder(self, trip_id) -> dict:
        try:
            participants = self.__participants_repository.find_participants_from_trip(trip_id)

            participants_formatted = []

            for participant in participants:
                participants_formatted.append({
                    "id": participant[0],
                    "name": participant[1],
                    "is_confirmed": participant[2],
                    "email": participant[3]
                })

            return {
                "body": {
                    "activities": participants_formatted
                },
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {
                    "error": "Bad Request",
                    "message": str(exception)
                },
                "status_code": 400
            }