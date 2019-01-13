import json
import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     '/Translate?text={}&from={}&to={}'.format(
                         text, source_language, dest_language),
                     headers=auth)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))




'''
Command to add new translation file for new language:
(venv) pybabel init -i messages.pot -d app/translations -l <new lang code eg. es(for spanish), fr(for french)>

Command to compile the newly added language to prepare it for use:
{venv} pybabel compile -d app/translations

Commands to execute for any translation update on messages.po file:
1. (venv) pybabel extract -F babel.cfg -k _l -o messages.pot .
2. (venv) pybabel update -i messages.pot -d app/translations
'''