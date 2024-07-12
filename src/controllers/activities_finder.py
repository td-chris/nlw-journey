class ActivitiesFinder:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def finder(self, trip_id) -> dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(trip_id)

            activities_formatted = []

            for activity in activities:
                activities_formatted.append({
                    "id": activity[0],
                    "title": activity[2],
                    "occurs_at": activity[3],
                })

            return {
                "body": {
                    "activities": activities_formatted
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