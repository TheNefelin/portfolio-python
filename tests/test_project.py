async def test_create_project(client):
  response = await client.post("/api/project/", json={
    "name": "Portfolio",
    "language_ids": [],
    "technology_ids": [],
  })
  assert response.status_code == 201
  data = response.json()
  assert data["name"] == "Portfolio"
  assert "id_project" in data


async def test_create_project_duplicate(client):
  await client.post("/api/project/", json={
    "name": "Blog",
    "language_ids": [],
    "technology_ids": [],
  })
  response = await client.post("/api/project/", json={
    "name": "Blog",
    "language_ids": [],
    "technology_ids": [],
  })
  assert response.status_code == 400
  assert "already exists" in response.json()["detail"]


async def test_get_all_project_empty(client):
  response = await client.get("/api/project/pagination")
  assert response.status_code == 200
  data = response.json()
  assert data["items"] == []
  assert data["total"] == 0


async def test_get_all_project(client):
  await client.post("/api/project/", json={"name": "P1", "language_ids": [], "technology_ids": []})
  await client.post("/api/project/", json={"name": "P2", "language_ids": [], "technology_ids": []})
  response = await client.get("/api/project/pagination")
  assert response.status_code == 200
  data = response.json()
  assert data["total"] == 2


async def test_get_project_by_id(client):
  created = (await client.post("/api/project/", json={
    "name": "API",
    "language_ids": [],
    "technology_ids": [],
  })).json()
  response = await client.get(f"/api/project/{created['id_project']}")
  assert response.status_code == 200
  assert response.json()["name"] == "API"


async def test_get_project_by_id_not_found(client):
  response = await client.get("/api/project/9999")
  assert response.status_code == 404


async def test_update_project(client):
  created = (await client.post("/api/project/", json={
    "name": "Old",
    "language_ids": [],
    "technology_ids": [],
  })).json()
  response = await client.put(f"/api/project/{created['id_project']}", json={
    "name": "New",
    "language_ids": [],
    "technology_ids": [],
  })
  assert response.status_code == 200
  assert response.json()["name"] == "New"


async def test_update_project_not_found(client):
  response = await client.put("/api/project/9999", json={
    "name": "Nope",
    "language_ids": [],
    "technology_ids": [],
  })
  assert response.status_code == 404


async def test_update_project_duplicate(client):
  await client.post("/api/project/", json={
    "name": "First",
    "language_ids": [],
    "technology_ids": [],
  })
  created = (await client.post("/api/project/", json={
    "name": "Second",
    "language_ids": [],
    "technology_ids": [],
  })).json()
  response = await client.put(f"/api/project/{created['id_project']}", json={
    "name": "First",
    "language_ids": [],
    "technology_ids": [],
  })
  assert response.status_code == 400


async def test_delete_project(client):
  created = (await client.post("/api/project/", json={
    "name": "Temp",
    "language_ids": [],
    "technology_ids": [],
  })).json()
  response = await client.delete(f"/api/project/{created['id_project']}")
  assert response.status_code == 204


async def test_delete_project_not_found(client):
  response = await client.delete("/api/project/9999")
  assert response.status_code == 404


async def test_create_project_with_relations(client):
  lang = (await client.post("/api/language/", json={"name": "Python"})).json()
  tech = (await client.post("/api/technology/", json={"name": "FastAPI"})).json()

  response = await client.post("/api/project/", json={
    "name": "Full App",
    "description": "A full stack app",
    "repo_url": "https://github.com/test/repo",
    "app_url": "https://example.com",
    "language_ids": [lang["id_language"]],
    "technology_ids": [tech["id_technology"]],
  })
  assert response.status_code == 201
  data = response.json()
  assert data["name"] == "Full App"
  assert data["description"] == "A full stack app"
  assert len(data["languages"]) == 1
  assert data["languages"][0]["name"] == "Python"
  assert len(data["technologies"]) == 1
  assert data["technologies"][0]["name"] == "FastAPI"


async def test_pagination(client):
  for i in range(5):
    await client.post("/api/project/", json={
      "name": f"Proj_{i}",
      "language_ids": [],
      "technology_ids": [],
    })

  response = await client.get("/api/project/pagination?page=1&limit=2")
  assert response.status_code == 200
  data = response.json()
  assert len(data["items"]) == 2
  assert data["total"] == 5

  page2 = (await client.get("/api/project/pagination?page=3&limit=2")).json()
  assert len(page2["items"]) == 1
