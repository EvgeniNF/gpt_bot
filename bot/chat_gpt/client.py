import bot.config as cfg
import openai


class GPTClient:

    def __init__(self, model, max_tokens, temperature):
        self._model = model
        self._max_tokens = max_tokens
        self._temperature = temperature

    def send(self, request: str) -> str:
        response = openai.Completion.create(engine=self._model,
                                            prompt=request,
                                            temperature=self._temperature,
                                            max_tokens=self._max_tokens)
        return response.choices[0].text
