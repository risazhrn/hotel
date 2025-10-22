import json
from datetime import datetime
from pathlib import Path

def save_json(data):
    """Menyimpan data JSON ke folder output/ dengan timestamp otomatis."""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)  # Buat folder output jika belum ada

    filename = output_dir / f"reviews_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return filename
