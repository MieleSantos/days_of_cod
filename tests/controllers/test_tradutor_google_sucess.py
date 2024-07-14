from googletrans import Translator


def test_google_tradutor_sucess():

    translator = Translator()
    resp = translator.translate("blue")
    assert resp == "azul"
