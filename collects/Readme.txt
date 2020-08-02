To run the following project:

1.Go to the directory of the project folder.

2.Run the server to make sure everything runs fine by the command:

python manage.py runserver

3.Migrate the changes to create tables to view the admin page:

python manage.py migrate


4.Create a super user for the project:

python manage.py createsuperuser

Enter the Username Email and Password.
Now you can access the admin page by going to the link "http://127.0.0.1:8000/admin"

5.You can add the Category and Images through admin page.
If operational error occurs, then you can run the following command

python manage.py migrate --run-syncdb

6.To view the webpage go to the link "http://127.0.0.1:8000/weby".