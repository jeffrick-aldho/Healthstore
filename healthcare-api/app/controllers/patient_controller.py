from app.utils.helpers import serialize_doc


def patient_profile_controller(user: dict):
    return serialize_doc(user)
