from app.core.database import get_client


def mongo_client():
    return get_client()
