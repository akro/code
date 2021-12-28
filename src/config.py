import os


def in_memory_db():
    return "sqlite:///:memory:"


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    # port = 5005 if host == "localhost" else 80
    port = 5005
    return f"http://{host}:{port}"

