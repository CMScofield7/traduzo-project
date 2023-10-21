from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.find()
    if request.method == "GET":
        return render_template(
            "index.html",
            languages=[language.to_dict() for language in languages],
            text_to_translate="O que deseja traduzir?",
            translate_from="pt",
            translate_to="en",
            translated="What do you want to translate?",
        )
    elif request.method == "POST":
        text_to_translate = request.form["text-to-translate"]
        translate_from = request.form["translate-from"]
        translate_to = request.form["translate-to"]

        translated = GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(text_to_translate)

        return render_template(
            "index.html",
            languages=[language.to_dict() for language in languages],
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated,
        )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    language = LanguageModel.find()
    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]

    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=[language.to_dict() for language in language],
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
