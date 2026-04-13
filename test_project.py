import pytest
from project import parse_identity_card, validate_info


def test_parse_identity_card():
    sample_text = """Personal ID: 123456789012
Full name: JOHN DOE
Date of birth: 01/01/2000
Sex: Male
Nationality: Vietnamese
Place of residence: Hanoi
Date of issue: 01/01/2022
Place of issue: Ministry of Public Security"""

    info = parse_identity_card(sample_text)

    assert info["id"] == "123456789012"
    assert info["name"] == "JOHN DOE"
    assert info["dob"] == "01/01/2000"


def test_validate_info_valid():
    info = {
        "id": "123456789012",
        "name": "JOHN DOE",
        "dob": "01/01/2000",
        "gender": "Male",
        "nationality": "Vietnamese",
        "address": "Hanoi",
        "issue_date": "01/01/2022",
        "issue_place": "Ministry"
    }

    validate_info(info)


def test_validate_info_invalid_id():
    info = {
        "id": "123",
        "name": "JOHN DOE",
        "dob": "01/01/2000",
        "gender": "Male",
        "nationality": "Vietnamese",
        "address": "Hanoi",
        "issue_date": "01/01/2022",
        "issue_place": "Ministry"
    }

    with pytest.raises(ValueError):
        validate_info(info)
