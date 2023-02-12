import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(API_KEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

LANGUAGE_TRANSLATOR.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """Translate English text to French text.

    Args:
        english_text (str): The text in English to be translated.

    Returns:
        str: The translated French text.
    """
    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text
    
def french_to_english(french_text):
    """Translate French text to English text.

    Args:
        french_text (str): The text in French to be translated.

    Returns:
        str: The translated English text.
    """
    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
