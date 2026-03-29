from datetime import datetime, timezone
from bson import ObjectId


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def serialize_value(value):
    if isinstance(value, ObjectId):
        return str(value)
    if isinstance(value, list):
        return [serialize_value(v) for v in value]
    if isinstance(value, dict):
        return {k: serialize_value(v) for k, v in value.items()}
    return value


def serialize_doc(doc: dict | None):
    if not doc:
        return None
    return serialize_value({"id": doc["_id"], **{k: v for k, v in doc.items() if k != "_id"}})
