1) migrate all the tables
>> python manage.py makemigrations
>> python manage.py migrate

2) create super user
>> python manage.py createsuperuser

3) run the django server
>> python manage.py runserver

4) create one access token by making post request to "/api/token" by sending username and password of superuser, and also while testing api through swagger we need to click on authorization button and then we need to add the token prepend with the word Bearer
#example (Bearer access_token)

5) visit "/swagger" endpoint and see all the documentation and also can test api

6) Admin can update or add the cource and student detail from /admin page where i have override django admin class method to achive the goal.