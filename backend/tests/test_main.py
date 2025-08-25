from backend.app.main import app

def test_app_creation():
    """Test that the FastAPI app is created successfully"""
    assert app is not None
    assert app.title == "RAGFlow Pro API"
    assert app.version == "1.0.0"

def test_app_routes():
    """Test that required routes are registered"""
    routes = [route.path for route in app.routes]
    assert "/" in routes
    assert "/health" in routes