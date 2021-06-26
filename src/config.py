from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

FORBES_DATASET_PATH = Path(os.environ.get("forbes-dataset", "./Forbes2013.csv"))
DOH_DATASET_PATH = Path(os.environ.get("DOH-dataset", "./DOH2020_combined.csv"))
