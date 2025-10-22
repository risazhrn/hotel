import json
import datetime
from pathlib import Path

def save_json(data, folder="output"):
    """Menyimpan data ke folder output/ dengan nama file timestamped JSON."""
    Path(folder).mkdir(exist_ok=True)
    filename = Path(folder) / f"tripadvisor_reviews_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return filename
