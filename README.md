# BackendCodingChallenge

This repository contains the beginnings of a django application. The purpose of the application is to (1) handle database interactions via models/ORM, (2) function as a REST API, (3) Ingest and process new datasets.

Currently the settings, requirements, file structure and a few initial models are set up. Additionally, a sample dataset in .csv format is located in the ‘test_data’ directory.

Requirements for the challenge:
- Create additional models that capture the data in the dataset. Docstrings on the models list the required fields.
- Create REST API endpoints using DjangoRestFramework that perform the following functions:
    - Endpoint that returns ‘Inspection’ data, both for a single Inspection object and collection of objects. Update functionality is not supported. Destroy functionality should ‘soft delete’ the object rather than delete the record from the database.
    - Endpoint with CRUD functionality on the Measurement model.
    - Endpoint that accepts a csv file of measurements (test_data/so_test_data.csv will be used) and saves each row of the csv as a measurement object.
    - A simple unit test that validates the success of the csv upload

In the file structure, some imports are included in otherwise blank files. The imported modules do not all have to be used, and additional imports can be added as needed. Additional packages can also be utilized and added to the requirements.txt file.
