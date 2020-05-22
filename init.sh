set -e

# Configure Virtual Env
python3 -m venv interview_app_env
source interview_app_env/bin/activate
pip install -r requirements.txt

# Init DB
export FLASK_APP=jcrm_lite
export FLASK_ENV=development
flask init-db
