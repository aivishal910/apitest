from fastapi import FastAPI
from pydantic import BaseModel
from mtranslate import translate
from langdetect import detect

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str
    source_lang: str = "auto"  # Auto-detect by default

@app.post("/translate")
def translate_text(request: TranslationRequest):
    try:
        # Detect the language of the input text
        detected_lang = detect(request.text)
        
        # If already in English, return original
        if detected_lang == "en":
            return {
                "translated_text": request.text,
            }

        # Otherwise translate to English
        translated = translate(request.text, "en", request.source_lang)
        return {
            "translated_text": translated,
        }

    except Exception as e:
        return {"error": str(e)} 
