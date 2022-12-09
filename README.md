# Setup the project
Assuming, python 3.9 or above is installed and the code is cloned.
## Step-1 : Setup the virtual environment.
command:
> python -m venv venv
assume the virtual environment:
> source venv/bin/activate

## Step-2 : Install the required modules from requirements.py
command:
> pip install -r requirements.txt

## Step-3 : Run data ingestion
command:
> python data_ingestion.py

## Step-4 : Run data analysis
command:
> python data_analysis.py

## Step-5 : Run the fast_api server
command:
> make run

## Step-6 : Run the unit tests
command
> make test