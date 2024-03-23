import pytest
import requests
from lambda_forge.constants import BASE_URL

@pytest.mark.integration(method="GET", endpoint="/private_hello_world")
def test_private_hello_world_status_code_is_200():

    headers = {
        "secret": "9cgKnXvck1Lbh4N5ZaJcsqK0xL6DyRDzxjXmQ6VVQIOoooDF839z"
    }
    response = requests.get(url=f"{BASE_URL}/private_hello_world", headers=headers)

    assert response.status_code == 200 
