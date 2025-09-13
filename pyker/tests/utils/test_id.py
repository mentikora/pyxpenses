import uuid

from app.utils.id import new_id


def test_new_id_returns_uuid() -> None:
    """Ensure new_id returns a UUID object"""
    result = new_id()

    assert isinstance(result, uuid.UUID)


def test_new_id_uniqueness() -> None:
    """Two calls to new_id should return different values"""
    id1 = new_id()
    id2 = new_id()

    assert id1 != id2


def test_new_id_type_is_uuid() -> None:
    """Check multiple calls always return UUID, not string"""
    for _ in range(10):
        result = new_id()

        assert isinstance(result, uuid.UUID)


def test_new_id_hex_format() -> None:
    """UUID has valid hex representation of 32 characters"""
    result = new_id()
    hex_str = result.hex

    assert len(hex_str) == 32
    assert all(c in "0123456789abcdef" for c in hex_str)


def test_new_id_str_format() -> None:
    """UUID string representation has 36 characters with dashes"""
    result = str(new_id())

    assert len(result) == 36
    assert result.count("-") == 4
