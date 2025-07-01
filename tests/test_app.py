def test_example(web_client):
    response = web_client.get("/users")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "john, jane, alice"

"""
Test find a user by id
"""
def test_find_a_user(web_client):
    response = web_client.get("/users/2")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "jane"


"""
Test create a user
"""
def test_create_a_user(web_client):
    response = web_client.post("/users", data={'username': 'Jon'})
    assert response.status_code == 201
    assert response.data.decode("utf-8") == "User Jon created with id 4"
    assert web_client.get("/users").data.decode('UTF-8') == "john, jane, alice, Jon"



"""
Update a user
"""
def test_update_a_user(web_client):
    response = web_client.put("/users/4", data={'username': 'Jono'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Id 4 updated with username Jono"
    assert web_client.get("/users").data.decode('UTF-8') == "john, jane, alice, Jono"

"""
Delete a user
"""
def test_delte_a_user(web_client):
    response = web_client.delete("/users/4")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Message: User deleted"
    assert web_client.get("/users").data.decode('UTF-8') == "john, jane, alice"