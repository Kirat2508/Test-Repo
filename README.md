# Test-Repo

#Folder Structure

fastapi-sample/
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI workflow
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application entry point
│   ├── config.py                  # Configuration settings
│   ├── dependencies.py            # Dependency injection
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py                # Base database model
│   │   └── item.py                # Item database model
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── base.py                # Base Pydantic models
│   │   └── item.py                # Item Pydantic models
│   ├── api/
│   │   ├── __init__.py
│   │   ├── api_v1/
│   │   │   ├── __init__.py
│   │   │   ├── api.py             # API router
│   │   │   └── endpoints/
│   │   │       ├── __init__.py
│   │   │       └── items.py       # Item endpoints
│   │   └── deps.py                # API dependencies
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py              # Core configuration
│   │   └── security.py            # Security utilities
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── base.py                # Base CRUD operations
│   │   └── crud_item.py           # Item CRUD operations
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py                # Database session setup
│   │   └── init_db.py             # Database initialization
│   └── utils/
│       ├── __init__.py
│       └── utils.py               # Utility functions
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Test configuration
│   ├── test_api/
│   │   ├── __init__.py
│   │   └── test_items.py          # API tests for items
│   └── test_crud/
│       ├── __init__.py
│       └── test_items.py          # CRUD tests for items
├── alembic/
│   ├── versions/                  # Database migration versions
│   ├── env.py                     # Alembic environment
│   ├── README                     # Alembic README
│   └── script.py.mako             # Alembic script template
├── alembic.ini                    # Alembic configuration
├── .gitignore                     # Git ignore file
├── .env.example                   # Example environment variables
├── Dockerfile                     # Docker configuration
├── docker-compose.yml             # Docker Compose configuration
├── pyproject.toml                 # Project metadata and dependencies
├── README.md                      # Project README
├── LICENSE                        # Project license
└── requirements.txt               # Python dependencies
