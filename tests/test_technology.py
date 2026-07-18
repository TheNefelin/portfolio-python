async def test_create_technology(client):
  response = await client.post("/api/technology/", json={"name": "Django"})
  assert response.status_code == 201
  data = response.json()
  assert data["name"] == "Django"
  assert "id_technology" in data


async def test_create_technology_duplicate(client):
  await client.post("/api/technology/", json={"name": "React"})
  response = await client.post("/api/technology/", json={"name": "React"})
  assert response.status_code == 400
  assert "already exists" in response.json()["detail"]


async def test_get_all_technology_empty(client):
  response = await client.get("/api/technology/pagination")
  assert response.status_code == 200
  data = response.json()
  assert data["items"] == []
  assert data["total"] == 0


async def test_get_all_technology(client):
  await client.post("/api/technology/", json={"name": "FastAPI"})
  await client.post("/api/technology/", json={"name": "Vue"})
  response = await client.get("/api/technology/pagination")
  assert response.status_code == 200
  data = response.json()
  assert data["total"] == 2


async def test_get_technology_by_id(client):
  created = (await client.post("/api/technology/", json={"name": "PostgreSQL"})).json()
  response = await client.get(f"/api/technology/{created['id_technology']}")
  assert response.status_code == 200
  assert response.json()["name"] == "PostgreSQL"


async def test_get_technology_by_id_not_found(client):
  response = await client.get("/api/technology/9999")
  assert response.status_code == 404


async def test_update_technology(client):
  created = (await client.post("/api/technology/", json={"name": "Redis"})).json()
  response = await client.put(f"/api/technology/{created['id_technology']}", json={"name": "Redis Cluster"})
  assert response.status_code == 200
  assert response.json()["name"] == "Redis Cluster"


async def test_update_technology_not_found(client):
  response = await client.put("/api/technology/9999", json={"name": "Nope"})
  assert response.status_code == 404


async def test_update_technology_duplicate(client):
  await client.post("/api/technology/", json={"name": "Docker"})
  created = (await client.post("/api/technology/", json={"name": "Podman"})).json()
  response = await client.put(f"/api/technology/{created['id_technology']}", json={"name": "Docker"})
  assert response.status_code == 400


async def test_delete_technology(client):
  created = (await client.post("/api/technology/", json={"name": "Nginx"})).json()
  response = await client.delete(f"/api/technology/{created['id_technology']}")
  assert response.status_code == 204


async def test_delete_technology_not_found(client):
  response = await client.delete("/api/technology/9999")
  assert response.status_code == 404


async def test_pagination(client):
  for i in range(5):
    await client.post("/api/technology/", json={"name": f"Tech_{i}"})

  response = await client.get("/api/technology/pagination?page=1&limit=2")
  assert response.status_code == 200
  data = response.json()
  assert len(data["items"]) == 2
  assert data["total"] == 5

  page2 = (await client.get("/api/technology/pagination?page=3&limit=2")).json()
  assert len(page2["items"]) == 1
