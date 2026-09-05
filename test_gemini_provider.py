from __future__ import annotations

import os
import unittest
from unittest.mock import Mock, patch

from gemini_provider import GeminiProvider


class GeminiProviderTests(unittest.TestCase):
    @patch.dict(os.environ, {"GEMINI_API_KEY": "test-key"})
    @patch("gemini_provider.genai.Client")
    def test_ask_sends_structured_context_and_returns_text(
        self, client_constructor: Mock
    ) -> None:
        response = Mock(text="The screen shows a terminal error.")
        client = client_constructor.return_value
        client.models.generate_content.return_value = response
        context = {"image": {"width": 320}, "text": [{"text": "Error"}]}

        provider = GeminiProvider()
        answer = provider.ask(context, "What is wrong?")

        self.assertEqual(answer, "The screen shows a terminal error.")
        client_constructor.assert_called_once_with(api_key="test-key")
        client.models.generate_content.assert_called_once()
        request = client.models.generate_content.call_args.kwargs
        self.assertEqual(request["model"], "gemini-2.5-flash")
        self.assertIn('"width": 320', request["contents"])
        self.assertIn("What is wrong?", request["contents"])

    @patch.dict(os.environ, {}, clear=True)
    def test_missing_api_key_raises_clear_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "GEMINI_API_KEY"):
            GeminiProvider()


if __name__ == "__main__":
    unittest.main()