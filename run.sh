set -e

# Activate Virtual Env
source interview_app_env/bin/activate

# Run App
export FLASK_APP=jcrm_lite
export FLASK_ENV=development
flask run
