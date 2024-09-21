from app.api.app import create_app
from config import get_config
config = get_config()
app = create_app()

if __name__ == "__main__":
    import uvicorn
    print(config.auth_config.PUBLIC_KEY)
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8002,
        reload=True,
    )
