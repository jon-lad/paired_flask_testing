def test_example(web_client):
    response = web_client.get("/users")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "john, jane, alice"
