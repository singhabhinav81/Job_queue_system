import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_welcome():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/")
        assert response.status_code == 200
        assert 'message' in response.json()


@pytest.mark.asyncio
async def test_get_all_jobs():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/jobs")
        assert response.status_code == 200
        data = response.json()
        assert 'total' in data
        assert 'jobs' in data
        assert isinstance(data['jobs'], list)


@pytest.mark.asyncio
async def test_get_job_by_id():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/jobs/1")
        assert response.status_code == 200
        data = response.json()
        assert 'job_id' in data
        assert data['job_id'] == 1
        assert 'name' in data
        assert 'status' in data
        assert 'created_at' in data
        assert 'updated_at' in data


@pytest.mark.asyncio
async def test_get_job_by_id_not_found():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/jobs/9999")