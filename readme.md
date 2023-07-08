# Django Forms

The Detailed explanation for Django Forms is on [YouTube](https://youtube.com/playlist?list=PLKnjLEpehhFmYkmP0PHLoMxRpxty3uKb_)

## Steps to run the django project
1. Clone this project and upen the project filder in the `Terminal`.
2. Create the virtual environment using commad `python -m venv env`.
3. To activate environment you can perform command given below
    ```bash
    # FOR WINDOWS
    env/script/activate
    ```
    ```bash
    # FOR LINUX
    env/bin/activate
    ```
4. After activating environment run command to install all requirements run command `pip install -r requirements.txt`
5. Agter installing all the packages run 2 command given below
    ```bash
    python manage.py makemigrations
    ```

    ```bash
    python manage.py migrate
    ```
6. Now, it is veru important to create `super user` and to create that you need to perform command `python manage.py createsuperuser` and provide all the details asked after running that command.
6. Now Finally run the server by performing command `python manage.py runserver`.