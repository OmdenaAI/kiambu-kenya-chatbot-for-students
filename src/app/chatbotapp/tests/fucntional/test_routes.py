def test_index_page(test_client):
    """
    GIVEN a Flask application routes
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200

# TODO Implement any extra routes created
