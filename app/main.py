"""Main module to run the API server."""
import uvicorn

from app import app_config

if __name__ == "__main__":
    uvicorn.run(
        "api:app_api",
        host=app_config.API_HOST,
        port=app_config.API_PORT,
        reload=app_config.API_DEBUG,
    )
