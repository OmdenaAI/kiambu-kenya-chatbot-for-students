# Source Folder Structure


    ├── src                <- Source code folder for this project
        │
        ├── data           <- Datasets used and collected for this project
        │   
        ├── docs           <- Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
        │
        ├── references     <- Data dictionaries, manuals, and all other explanatory references used 
        │
        ├── tasks          <- Master folder for all individual task folders
        │
        ├── visualizations <- Code and Visualization dashboards generated for the project
        │
        └── results        <- Folder to store Final analysis and modelling results and code.


## Guidelines

- Data              - Folder to Store all the data collected and used for this project 
- Docs              - Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
- References        - Folder to store any referneced code/research papers and other useful documents used for this project
- Tasks             - Master folder for all tasks
  - All Task Folder names should follow specific naming convention
  - All Task folder names should be in chronologial order (from 1 to n)
  - All Task folders should have a README.md file with task Details and task goals along with an info table containing all code/notebook files with their links and information
- Visualization     - Folder to store dashboards, analysis and visualization reports
- Results           - Folder to store final analysis modelling results for the project.

# Chatbot Deployment Stack

This is the backend that is used to provide an interface for intercating with the chatbot model.

- Built in Python version 3.9.7
- Uses [Uses Flask](https://flask.palletsprojects.com/en/2.1.x/) as the server backend.
- Uses [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) for UI development.
- Uses [Flask WTForms](https://flask.palletsprojects.com/en/2.1.x/patterns/wtforms//) for the web forms.
- Uses [PyTest](https://docs.pytest.org/en/7.1.x/) for our testing framework.
- Uses [Makefile](https://makefiletutorial.com/) to execute commands

# Structure

## app
- The `app` folder contains the source code of project and the tests.

## tests
- The `tests` folder contains the tests for the system.


## Running the project
- Create a virtual environment, then install the package dependencies using command `pip install -r requirements.txt`
- To run the `application` run the command `make run`. This will start the flask app on port `5000` which can be accessed on the browser through `http://127.0.0.1:5000`.
  
## Running the tests
- To run tests, execute the command `make test`.
