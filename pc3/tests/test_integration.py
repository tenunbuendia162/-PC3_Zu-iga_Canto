from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sumar_integracion():
    r = client.get("/sumar", params={"a": 3, "b": 4})
    assert r.status_code == 200
    assert r.json() == {"resultado": 7}


def test_promedio_lista_valida():
    r = client.post("/promedio", json={"valores": [2, 4, 6]})
    assert r.status_code == 200
    assert r.json() == {"promedio": 4.0}


def test_promedio_lista_vacia():
    r = client.post("/promedio", json={"valores": []})
    assert r.status_code == 400
    assert r.json() == {"detail": "Lista vacía"}


def test_integracion_completa():
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/sumar", params={"a": 1, "b": 2}).json() == {"resultado": 3}
    assert client.post("/promedio", json={"valores": [1, 3]}).json() == {"promedio": 2.0}
