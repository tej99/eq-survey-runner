#!/usr/bin/env bash

current_dir=$(dirname "${BASH_SOURCE[0]}")
parent_dir=$(dirname "${current_dir}")
path_to_parent="$( cd "${parent_dir}" && pwd )"

# Clone translation schema
git clone -b 885-remove-cy-suffix https://github.com/ONSdigital/eq-translations.git "${path_to_parent}"/temp/eq-translations
# Install prerequisites and run translation
(
  source "$(which virtualenvwrapper.sh)"
  mkvirtualenv --python="$(which python3)" eq-translations
  workon eq-translations
  pip install -r "${path_to_parent}"/temp/eq-translations/requirements.txt
  cd "${path_to_parent}"/temp/eq-translations || exit
  while read -r line
    do
      filename_regex="([a-zA-Z_]+)_translate_([a-zA-Z]{2}).xlsx"
      if [[ $line =~ $filename_regex ]]; then
        schema=${BASH_REMATCH[1]};
        country_code=${BASH_REMATCH[2]};
        mkdir -p "${path_to_parent}"/app/data/"${country_code}"
        ./scripts/run_translate_survey.sh "${path_to_parent}"/app/data/"${schema}".json translations/"${schema}"_translate_"${country_code}".xlsx "${path_to_parent}"/app/data/"${country_code}"
      fi
  done < <(find "${path_to_parent}"/temp/eq-translations -name "*.xlsx" -exec basename {} \;)
  deactivate
  rmvirtualenv eq-translations
)
# Delete repo
rm -rf "${path_to_parent}"/temp
