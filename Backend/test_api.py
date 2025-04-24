import requests

BASE_URL = "http://dev.mysoloro.com/api/v1"

def test_get_all_clubs_status_code():
    """Test if GET /clubs returns status code 200"""
    response = requests.get(f"{BASE_URL}/clubs")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

def test_get_all_clubs_content_type():
    """Test if Content-Type is application/json"""
    response = requests.get(f"{BASE_URL}/clubs")
    assert response.headers["Content-Type"] == "application/json", "Content-Type is not application/json"

def test_get_all_clubs_response_not_empty():
    """Test if response contains at least one club or a valid structure"""
    response = requests.get(f"{BASE_URL}/clubs")
    data = response.json()
    assert isinstance(data, list), "Response is not a list"
    # Optional: Add condition if at least one club expected
    # assert len(data) > 0, "No clubs returned"


