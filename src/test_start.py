import pytest
from httpx import AsyncClient

from start import app


@pytest.mark.anyio
async def test_root():
    """Access home"""
    async with AsyncClient(app=app, base_url="http://localhost:8000") as url:
        response = await url.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Tomato"}
