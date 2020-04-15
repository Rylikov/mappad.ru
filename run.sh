#!/bin/sh
export DATABASE_URI="postgresql://mappad:mappad@localhost/mappad" && export FLASK_ENV=development && export FLASK_DEBUG=1 && export FLASK_APP=webapp && flask run
