#Weather App
This is a dummy weather app project that checks in weather of a city. 
API used from https://openweathermap.org/

##How to run the project?
1. Clone the repository
2. Create a virtual environment for the project to run
   >>python3 -m venv .venv
   >>source .venv/bin/activate
3. Install project dependencies
   >>pip install -r requirements.txt
4. Check the list of packages installed
   >>pip list
5. Run the `weather.py` file
6. Enter the name of a city
7. The console should give you the json data for the weather of the entered city.


##Learnings
1. How to create python virtual environments using `venv`.
2. How to activate and deactivate the virtual environments.
3. Using pip to install dependencies.
4. Manage dependencies in `requirements.txt` file.
5. How to set environment variables. Use of `python-dotenv` to load and read the variables from `.env` file.
6. Basic python code -> sending a api request, reading json data, take user inputs etc.
