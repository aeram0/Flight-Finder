#/usr/bin/env bash

export FN_AUTH_REDIRECT_URI="http://localhost:5000/google/auth"
export FN_BASE_URI="http://localhost:5000"
export FN_CLIENT_ID="902973835008-jddok0ca65dkvqspavb97hbi3regfe8b.apps.googleusercontent.com"
export FN_CLIENT_SECRET="KHXhN1_zw18Y0N-l5_s5lRem"

export FLASK_APP="app.py"
export FLASK_DEBUG=1
export FN_FLASK_SECRET_KEY="CS411"

python3 -m flask run -p 5000
