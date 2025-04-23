import requests

BASE_URL = "http://dev.mysoloro.com/api/v1"


def test_get_all_clubs():
    response = requests.get(f"{BASE_URL}/clubs")

    # Check for successful response
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Check if response is JSON
    try:
        data = response.json()
    except Exception:
        assert False, "Response is not valid JSON"

    # Optional: Check if response is a list or has 'clubs' key
    assert isinstance(data, (list, dict)), f"Unexpected response type: {type(data)}"

    # Print output for debugging
    print("Response:", data)
