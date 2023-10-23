import requests

from dependencies import translate_key

def get_translation(text, target_lang):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    lang_map = {"korean": 'ko', "spanish": "es", "english": "en"}

    payload = {
        "q": text,
        "target": lang_map[target_lang],
        "source": "en"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": translate_key,
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    res = response.json()
    return res['data']['translations']