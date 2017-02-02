FROM ubuntu:14.04

ENV RUNTIME_PACKAGES="postgresql python-psycopg2"
ENV BUILD_PACKAGES="curl build-essential libpq-dev ca-certificates libffi-dev libssl-dev git"

WORKDIR /code

EXPOSE 5000

RUN apt-key adv --fetch-keys http://dl.yarnpkg.com/debian/pubkey.gpg
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y $RUNTIME_PACKAGES $BUILD_PACKAGES

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

RUN apt-get install -y nodejs yarn
RUN yarn global add gulp-cli

ADD requirements.txt /code/requirements.txt
ADD package.json /code/package.json
ADD app/assets /code/app/assets

RUN git clone git://github.com/yyuu/pyenv.git .pyenv
ENV PYENV_ROOT /code/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

ADD . /code

RUN pyenv install &&  pyenv rehash && pip install -U pip setuptools wheel

ENTRYPOINT pip install -r requirements.txt && yarn compile && python application.py runserver
