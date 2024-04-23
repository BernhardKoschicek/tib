#!/bin/bash

pybabel extract -F tib/translations/babel.cfg -k _l -o tib/translations/messages.pot .
#babel init -i translations/messages.pot -d translations -l de
# pybabel compile -d translations
pybabel update -i tib/translations/messages.pot -d tib/translations/

