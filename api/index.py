import os
import sys

# Ensure parent directory is in sys.path for importing app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
