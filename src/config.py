from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

DATASET_PATH = Path(os.environ.get("dataset", "./Forbes2013.csv"))
