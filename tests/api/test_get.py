import pytest

### Testing all API Get requests

#Test for get all products list
def test_get_all_products(base_url, session):
    url = f"{base_url}/productsList"
    response = session.get(url)

    assert response.status_code == 200
    assert "products" in response.text.lower()
    assert response.elapsed.total_seconds() < 5

#Test for get user detail by email
@pytest.mark.parametrize("email,expected_status", [
    ("test123@exampl.com",200),
    ("notest@gmail.com",200),
    ("xoxoxoxoxoxoxoxoxoxoxoxoxoxo123@yahoo.com", 400),
])
def test_get_user_detail_by_email(base_url, session, email, expected_status):
    url = f"{base_url}/getUserDetailByEmail"
    params = {"email": email}
    response = session.get(url, params=params)

    assert response.status_code == 200
    json = response.json()
    assert json.get("message") == expected_status