from pathlib import Path

# Filesystem paths
BASE_PATH = Path(__file__).parent.parent
DATA_PATH = BASE_PATH / "data"
MODELS_PATH = BASE_PATH / "models"
PROJECTS_PATH = BASE_PATH / "projects"
INPUT_DATA_PATH = DATA_PATH / "inputs"
OUTPUT_DATA_PATH = DATA_PATH / "outputs"
LOGGING_DIR = BASE_PATH / "log"
