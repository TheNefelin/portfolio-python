async def _create_grp(client, name="Social") -> dict:
  return (await client.post("/api/url-grp/", json={"name": name})).json()


async def test_create_url(client):
  grp = await _create_grp(client)
  response = await client.post("/api/url/", json={
    "name": "GitHub",
    "link": "https://github.com",
    "id_urlgrp": grp["id_urlgrp"],
  })
  assert response.status_code == 201
  data = response.json()
  assert data["name"] == "GitHub"
  assert data["link"] == "https://github.com"
  assert "id_url" in data


async def test_create_url_duplicate(client):
  grp = await _create_grp(client)
  await client.post("/api/url/", json={
    "name": "Twitter",
    "link": "https://twitter.com",
    "id_urlgrp": grp["id_urlgrp"],
  })
  response = await client.post("/api/url/", json={
    "name": "Twitter",
    "link": "https://twitter.com",
    "id_urlgrp": grp["id_urlgrp"],
  })
  assert response.status_code == 400
  assert "already exists" in response.json()["detail"]


async def test_get_all_url_empty(client):
  response = await client.get("/api/url/pagination")
  assert response.status_code == 200
  data = response.json()
  assert data["items"] == []
  assert data["total"] == 0


async def test_get_all_url(client):
  grp = await _create_grp(client)
  await client.post("/api/url/", json={
    "name": "Site1",
    "link": "https://site1.com",
    "id_urlgrp": grp["id_urlgrp"],
  })
  await client.post("/api/url/", json={
    "name": "Site2",
    "link": "https://site2.com",
    "id_urlgrp": grp["id_urlgrp"],
  })
  response = await client.get("/api/url/pagination")
  assert response.status_code == 200
  data = response.json()
  assert data["total"] == 2


async def test_get_url_by_id(client):
  grp = await _create_grp(client)
  created = (await client.post("/api/url/", json={
    "name": "DevTo",
    "link": "https://dev.to",
    "id_urlgrp": grp["id_urlgrp"],
  })).json()
  response = await client.get(f"/api/url/{created['id_url']}")
  assert response.status_code == 200
  assert response.json()["name"] == "DevTo"


async def test_get_url_by_id_not_found(client):
  response = await client.get("/api/url/9999")
  assert response.status_code == 404


async def test_update_url(client):
  grp = await _create_grp(client)
  created = (await client.post("/api/url/", json={
    "name": "OldLink",
    "link": "https://old.com",
    "id_urlgrp": grp["id_urlgrp"],
  })).json()
  response = await client.put(f"/api/url/{created['id_url']}", json={
    "name": "NewLink",
    "link": "https://new.com",
    "id_urlgrp": grp["id_urlgrp"],
  })
  assert response.status_code == 200
  assert response.json()["name"] == "NewLink"
  assert response.json()["link"] == "https://new.com"


async def test_update_url_not_found(client):
  response = await client.put("/api/url/9999", json={
    "name": "Nope",
    "link": "https://nope.com",
    "id_urlgrp": 1,
  })
  assert response.status_code == 404


async def test_delete_url(client):
  grp = await _create_grp(client)
  created = (await client.post("/api/url/", json={
    "name": "Temp",
    "link": "https://temp.com",
    "id_urlgrp": grp["id_urlgrp"],
  })).json()
  response = await client.delete(f"/api/url/{created['id_url']}")
  assert response.status_code == 204


async def test_delete_url_not_found(client):
  response = await client.delete("/api/url/9999")
  assert response.status_code == 404


async def test_pagination(client):
  grp = await _create_grp(client)
  for i in range(5):
    await client.post("/api/url/", json={
      "name": f"Url_{i}",
      "link": f"https://url{i}.com",
      "id_urlgrp": grp["id_urlgrp"],
    })

  response = await client.get("/api/url/pagination?page=1&limit=2")
  assert response.status_code == 200
  data = response.json()
  assert len(data["items"]) == 2
  assert data["total"] == 5

  page2 = (await client.get("/api/url/pagination?page=3&limit=2")).json()
  assert len(page2["items"]) == 1


async def test_filter_by_urlgrp(client):
  grp1 = await _create_grp(client, "Dev")
  grp2 = await _create_grp(client, "Social")
  await client.post("/api/url/", json={"name": "Git", "link": "https://git.com", "id_urlgrp": grp1["id_urlgrp"]})
  await client.post("/api/url/", json={"name": "Twit", "link": "https://twit.com", "id_urlgrp": grp2["id_urlgrp"]})

  response = await client.get(f"/api/url/pagination?id_urlgrp={grp1['id_urlgrp']}")
  assert response.status_code == 200
  data = response.json()
  assert data["total"] == 1
  assert data["items"][0]["name"] == "Git"
