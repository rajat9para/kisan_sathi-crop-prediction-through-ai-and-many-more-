import sys
import os

# Add backend directory and parent directory to Python sys.path for Vercel serverless environment
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
backend_dir = os.path.join(parent_dir, "backend")

for p in [backend_dir, parent_dir, os.path.join(backend_dir, "app")]:
    if p not in sys.path:
        sys.path.insert(0, p)

from app.main import app
