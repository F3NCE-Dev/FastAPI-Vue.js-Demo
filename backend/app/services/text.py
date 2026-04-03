import random

text_list = [
    "Hello, World!",
    "Welcome to FastAPI!",
    "This is a sample text.",
]

class TextService:
    @classmethod
    def get_text(cls) -> str:
        return text_list[random.randint(0, len(text_list) - 1)]
