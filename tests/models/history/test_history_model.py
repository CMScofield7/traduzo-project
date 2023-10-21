import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    history_json = HistoryModel.list_as_json()
    history_data = json.loads(history_json)

    assert "Hello, I like videogame" in history_data[0]["text_to_translate"]
    assert "en" in history_data[0]["translate_from"]
    assert "pt" in history_data[0]["translate_to"]
