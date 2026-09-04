from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image

from screen_analyzer import analyze_screen, context_to_json


class ScreenAnalyzerTests(unittest.TestCase):
    def create_image(self, directory: str) -> Path:
        image_path = Path(directory) / "test.png"
        Image.new("RGB", (320, 200), "white").save(image_path)
        return image_path

    def test_analyze_screen_returns_metadata_and_ocr_items(self) -> None:
        ocr_data = {
            "text": ["", "Hello", "world"],
            "conf": ["-1", "95.5", "88"],
            "left": ["0", "10", "70"],
            "top": ["0", "20", "20"],
            "width": ["0", "50", "45"],
            "height": ["0", "18", "18"],
        }

        with tempfile.TemporaryDirectory() as directory:
            image_path = self.create_image(directory)
            with patch("screen_analyzer.pytesseract.image_to_data", return_value=ocr_data):
                result = analyze_screen(image_path)

        self.assertEqual(result["image"]["width"], 320)
        self.assertEqual(result["image"]["height"], 200)
        self.assertEqual([item["text"] for item in result["text"]], ["Hello", "world"])
        self.assertEqual(result["text"][0]["box"], {"left": 10, "top": 20, "width": 50, "height": 18})
        self.assertEqual(result["text"][1]["confidence"], 88.0)

    def test_blank_ocr_data_returns_no_text(self) -> None:
        ocr_data = {key: [""] for key in ("text", "conf", "left", "top", "width", "height")}

        with tempfile.TemporaryDirectory() as directory:
            image_path = self.create_image(directory)
            with patch("screen_analyzer.pytesseract.image_to_data", return_value=ocr_data):
                result = analyze_screen(image_path)

        self.assertEqual(result["text"], [])

    def test_context_can_be_serialized_as_json(self) -> None:
        context = {"image": {"width": 1}, "text": []}

        serialized = context_to_json(context)

        self.assertEqual(json.loads(serialized), context)


if __name__ == "__main__":
    unittest.main()