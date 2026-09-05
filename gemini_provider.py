from __future__ import annotations

import json
import os
from typing import Any

from google import genai


class GeminiProvider:
    """Answer screen-context questions using Google's Gemini API."""

    def __init__(self, model: str = "gemini-2.5-flash") -> None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")

        self._client = genai.Client(api_key=api_key)
        self._model = model

    def ask(self, context: dict[str, Any], question: str) -> str:
        prompt = (
            "Answer the user's question using the structured screen context below. "
            "If the context does not contain enough information, say so clearly.\n\n"
            f"Screen context:\n{json.dumps(context, indent=2)}\n\n"
            f"User question:\n{question}"
        )

        response = self._client.models.generate_content(
            model=self._model,
            contents=prompt,
        )
        return response.text