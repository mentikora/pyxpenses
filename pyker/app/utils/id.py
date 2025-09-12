import uuid


def new_id() -> uuid.UUID:
    """
    Generate a new unique identifier (UUID4)
    """
    return uuid.uuid4()
