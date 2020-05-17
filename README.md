# Junari Technical Interview App

Welcome to Junari CRM Lite! This is a simple web application used in Junari
Technical interviews.

## Requirements

* Python 3.7 or above

## Set up

1. Create a virtual environment
```
python3 -m venv interview_app_env
```

2. Activate it
```
# Mac/Linux
source interview_app_env/bin/activate

# Windows
interview_app_env\Scripts\activate
```

3. Install python dependencies
```
pip install -r requirements.txt
```

4. Initialise the database
```
# Mac / Linux
./init.sh

# Windows
init.bat
```

## Running

```
# Mac / Linux
./run.sh

# Windows
run.bat
```