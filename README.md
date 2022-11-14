<div id="top"></div>

<h3 align="center">Django Fee MS</h3>

  <p align="center">
    Django school fee system.
  </p>
  
  ![homepage_screenshot](https://raw.githubusercontent.com/lynchzival/Django-SchoolMSFee/main/screenshot/Screenshot%202022-06-29%20at%2021-17-24%20SCHOOL%20-%20Dashboard.png)
</div>

### Built With

* [Django](https://laravel.com)
* [Bootstrap](https://getbootstrap.com) ([SBAdmin2](https://startbootstrap.com/theme/sb-admin-2))
* [JQuery](https://jquery.com)
* [Postgresql](https://www.postgresql.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* [Download Python](https://www.python.org/)
* [Download Postgresql](https://www.postgresql.org/download/)

### Installation
 
1. Clone the repo

   ```sh
   git clone https://github.com/lynchzival/Django-SchoolFee.git
   ```
   
2. Extract compressed vendor folder in static folder
3. Create venv inside the project folder

   ```sh
   python -m venv .\venv
   ```
4. Activate your venv

   ```sh
   venv\Scripts\activate
   ```
   You might run into "execution of scripts is disabled" error, in that case visit this [stackoverflow question](https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system) for a fix.

5. Install packages

   ```sh
   pip install -r requirements.txt
   ```
 
6. Config database in setting.py located in school folder

7. Generate secret key

   ```sh
   python
   ```
   ```sh
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```
   Assign the value to SECRET_KEY = '' variable inside setting.py file
   
8. Migration

   ```sh
   python manage.py migrate
   ```
   
9. Create superuser

   ```sh
   python manage.py createsuperuser
   ```
   
10. Run server

    ```sh
    python manage.py runserver
    ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- FEATURES -->
## Features

- Profile Management
- Payment Report
- Payment Transaction Activity Log 
- Payment Receipt

<p align="right">(<a href="#top">back to top</a>)</p>
