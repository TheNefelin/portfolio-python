async def test_create_language(client):
  response = await client.post("/api/language/", json={"name": "Python"})
  assert response.status_code == 201
  data = response.json()
  assert data["name"] == "Python"
  assert "id_language" in data


async def test_create_language_duplicate(client):
  await client.post("/api/language/", json={"name": "Java"})
  response = await client.post("/api/language/", json={"name": "Java"})
  assert response.status_code == 400
  assert "already exists" in response.json()["detail"]


async def test_get_all_language_empty(client):
  response = await client.get("/api/language/pagination")
  assert response.status_code == 200
  data = response.json()
  assert data["items"] == []
  assert data["total"] == 0
  assert data["page"] == 1
  assert data["limit"] == 20


async def test_get_all_language(client):
  await client.post("/api/language/", json={"name": "Rust"})
  await client.post("/api/language/", json={"name": "Go"})
  response = await client.get("/api/language/pagination")
  assert response.status_code == 200
  data = response.json()
  assert data["total"] == 2


async def test_get_language_by_id(client):
  created = (await client.post("/api/language/", json={"name": "TypeScript"})).json()
  response = await client.get(f"/api/language/{created['id_language']}")
  assert response.status_code == 200
  assert response.json()["name"] == "TypeScript"


async def test_get_language_by_id_not_found(client):
  response = await client.get("/api/language/9999")
  assert response.status_code == 404
  assert "not found" in response.json()["detail"].lower()


async def test_update_language(client):
  created = (await client.post("/api/language/", json={"name": "Kotlin"})).json()
  response = await client.put(f"/api/language/{created['id_language']}", json={"name": "Kotlin Native"})
  assert response.status_code == 200
  assert response.json()["name"] == "Kotlin Native"


async def test_update_language_not_found(client):
  response = await client.put("/api/language/9999", json={"name": "Nope"})
  assert response.status_code == 404


async def test_update_language_duplicate(client):
  await client.post("/api/language/", json={"name": "Swift"})
  created = (await client.post("/api/language/", json={"name": "Objective-C"})).json()
  response = await client.put(f"/api/language/{created['id_language']}", json={"name": "Swift"})
  assert response.status_code == 400
  assert "already exists" in response.json()["detail"]


async def test_delete_language(client):
  created = (await client.post("/api/language/", json={"name": "Dart"})).json()
  response = await client.delete(f"/api/language/{created['id_language']}")
  assert response.status_code == 204


async def test_delete_language_not_found(client):
  response = await client.delete("/api/language/9999")
  assert response.status_code == 404


async def test_pagination(client):
  for i in range(5):
    await client.post("/api/language/", json={"name": f"Lang_{i}"})

  response = await client.get("/api/language/pagination?page=1&limit=2")
  assert response.status_code == 200
  data = response.json()
  assert len(data["items"]) == 2
  assert data["total"] == 5
  assert data["page"] == 1
  assert data["limit"] == 2

  page2 = (await client.get("/api/language/pagination?page=3&limit=2")).json()
  assert len(page2["items"]) == 1
