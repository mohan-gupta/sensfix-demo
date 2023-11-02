import requests

from dependencies import translate_key

def translate_text(text, target_lang):
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

def get_translation(to_translate, language):
    if language == "spanish":
        translations = translate_text(to_translate, language)
        
    elif language == "korean":
        translations = translate_text(to_translate, language)
        
    result = {}
    for idx in range(1, len(translations), 2):
        result[translations[idx-1]['translatedText']] = translations[idx]['translatedText'] 
        
    return result