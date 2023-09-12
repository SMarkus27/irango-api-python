# Third-Party Library
from decouple import config


class RestaurantsMongoDBRepository:
    _mongodb_database = config("MONGODB_RESTAURANTS_DATABASE")
    _mongodb_collection = config("MONGODB_RESTAURANTS_DATABASE")
