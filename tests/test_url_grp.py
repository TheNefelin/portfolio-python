async def test_create_url_grp(client):
  response = await client.post("/api/url-grp/", json={"name": "Social"})
  assert response.status_code == 201
  data = response.json()
  assert data["name"] == "Social"
  assert "id_urlgrp" in data


async def test_create_url_grp_duplicate(client):
  await client.post("/api/url-grp/", json={"name": "Work"})
  response = await client.post("/api/url-grp/", json={"name": "Work"})
  assert response.status_code == 400
  assert "already exists" in response.json()["detail"]


async def test_get_all_url_grp_empty(client):
  response = await client.get("/api/url-grp/pagination")
  assert response.status_code == 200
  data = response.json()
  assert data["items"] == []
  assert data["total"] == 0


async def test_get_all_url_grp(client):
  await client.post("/api/url-grp/", json={"name": "Personal"})
  await client.post("/api/url-grp/", json={"name": "Professional"})
  response = await client.get("/api/url-grp/pagination")
  assert response.status_code == 200
  data = response.json()
  assert data["total"] == 2


async def test_get_url_grp_by_id(client):
  created = (await client.post("/api/url-grp/", json={"name": "Blogs"})).json()
  response = await client.get(f"/api/url-grp/{created['id_urlgrp']}")
  assert response.status_code == 200
  assert response.json()["name"] == "Blogs"


async def test_get_url_grp_by_id_not_found(client):
  response = await client.get("/api/url-grp/9999")
  assert response.status_code == 404


async def test_update_url_grp(client):
  created = (await client.post("/api/url-grp/", json={"name": "OldGrp"})).json()
  response = await client.put(f"/api/url-grp/{created['id_urlgrp']}", json={"name": "NewGrp"})
  assert response.status_code == 200
  assert response.json()["name"] == "NewGrp"


async def test_update_url_grp_not_found(client):
  response = await client.put("/api/url-grp/9999", json={"name": "Nope"})
  assert response.status_code == 404


async def test_update_url_grp_duplicate(client):
  await client.post("/api/url-grp/", json={"name": "Dev"})
  created = (await client.post("/api/url-grp/", json={"name": "Other"})).json()
  response = await client.put(f"/api/url-grp/{created['id_urlgrp']}", json={"name": "Dev"})
  assert response.status_code == 400


async def test_delete_url_grp(client):
  created = (await client.post("/api/url-grp/", json={"name": "Temp"})).json()
  response = await client.delete(f"/api/url-grp/{created['id_urlgrp']}")
  assert response.status_code == 204


async def test_delete_url_grp_not_found(client):
  response = await client.delete("/api/url-grp/9999")
  assert response.status_code == 404


async def test_pagination(client):
  for i in range(5):
    await client.post("/api/url-grp/", json={"name": f"Grp_{i}"})

  response = await client.get("/api/url-grp/pagination?page=1&limit=2")
  assert response.status_code == 200
  data = response.json()
  assert len(data["items"]) == 2
  assert data["total"] == 5

  page2 = (await client.get("/api/url-grp/pagination?page=3&limit=2")).json()
  assert len(page2["items"]) == 1


async def test_detail_endpoint(client):
  grp = (await client.post("/api/url-grp/", json={"name": "Social"})).json()
  await client.post("/api/url/", json={
    "name": "GitHub",
    "link": "https://github.com",
    "id_urlgrp": grp["id_urlgrp"],
  })

  response = await client.get("/api/url-grp/detail")
  assert response.status_code == 200
  data = response.json()
  assert len(data) == 1
  assert data[0]["name"] == "Social"
  assert len(data[0]["urls"]) == 1
  assert data[0]["urls"][0]["name"] == "GitHub"
