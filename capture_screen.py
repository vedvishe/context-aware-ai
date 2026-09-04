from __future__ import annotations

import argparse
from pathlib import Path

import mss
from mss import tools
from screen_analyzer import analyze_screen, context_to_json


def capture_screen(output_path: Path) -> Path:
    """Capture the primary monitor and save it as a PNG image."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with mss.MSS() as screenshotter:
        if len(screenshotter.monitors) < 2:
            raise RuntimeError("No primary monitor is available for capture")

        primary_monitor = screenshotter.monitors[1]
        screenshot = screenshotter.grab(primary_monitor)
        tools.to_png(
            screenshot.rgb,
            screenshot.size,
            output=str(output_path),
        )

    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Capture the primary Windows monitor")
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=Path("screenshots/screenshot.png"),
        help="PNG path to create (default: screenshots/screenshot.png)",
    )
    parser.add_argument(
        "--analyze",
        action="store_true",
        help="Analyze the captured screenshot with OCR and print JSON context",
    )
    args = parser.parse_args()

    saved_path = capture_screen(args.output)
    print(f"Screenshot saved to {saved_path.resolve()}")
    if args.analyze:
        print(context_to_json(analyze_screen(saved_path)))


if __name__ == "__main__":
    main()
