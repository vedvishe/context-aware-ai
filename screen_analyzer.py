from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from PIL import Image
import pytesseract
from pytesseract import Output


def analyze_screen(image_path: Path) -> dict[str, Any]:
    """Extract image metadata and readable text from a captured screenshot."""
    image_path = Path(image_path)

    with Image.open(image_path) as image:
        metadata = {
            "path": str(image_path),
            "width": image.width,
            "height": image.height,
            "mode": image.mode,
        }
        ocr_data = pytesseract.image_to_data(image, output_type=Output.DICT)

    text_items = []
    for index, text in enumerate(ocr_data["text"]):
        text = text.strip()
        if not text:
            continue

        text_items.append(
            {
                "text": text,
                "confidence": float(ocr_data["conf"][index]),
                "box": {
                    "left": int(ocr_data["left"][index]),
                    "top": int(ocr_data["top"][index]),
                    "width": int(ocr_data["width"][index]),
                    "height": int(ocr_data["height"][index]),
                },
            }
        )

    return {"image": metadata, "text": text_items}


def context_to_json(screen_context: dict[str, Any]) -> str:
    """Convert screen context to readable JSON."""
    return json.dumps(screen_context, indent=2)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze a screenshot")
    parser.add_argument("image", type=Path)
    args = parser.parse_args()
    print(context_to_json(analyze_screen(args.image)))