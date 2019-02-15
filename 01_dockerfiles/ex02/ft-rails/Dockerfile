FROM        ruby
RUN         apt-get update && apt-get upgrade -y
RUN         gem install rails
RUN         apt-get install -y build-essential libpq-dev nodejs sqlite3

ONBUILD RUN       mkdir /opt/app
ONBUILD COPY      sample_app /opt/app
ONBUILD WORKDIR   /opt/app

ONBUILD RUN       bundle install --without production
ONBUILD RUN       rails db:migrate
ONBUILD RUN       rails db:seed


#1) docker build -t ft-rails:on-build .
