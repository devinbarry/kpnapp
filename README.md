# kpnapp
Test App for KPN


This project implements a REST API server which shows the output of the Contact model. Making POST requests to the
REST endpoint allows adding new contacts to the database.

The client should be a seperate project, but I just wrote a tiny client module that be run from the command line and
included it in this project to keep things simple.

Due to the extremely wide scope of the project and no specific requirements, I have implemented this project in
the fastest and most minimal way I possibly could. It has only been tested against the tiny data set provided with
the project and only corrects for a specific type of error found in that data set (empty URL).

All the things to "take into consideration" have not been taken into consideration because the project scope does
not say how to do this.


How to run
----------

1. Install requirements (python 3.5.1), migrate database
2. python manage.py runserver
3.  - Admin site should have a Contact object.
    - /api URL should show contacts (add one through admin site)

4. Adjust hardcoded values for server location and CSV file in client.py
4. cd to client dir
5. run 'python client.py'
6. Output should look like this

>'image': 'https://cdn1.iconfinder.com/data/icons/user-pictures/100/male3-512.png', 'city': 'Killeen', 'last_name': 'Fox', 'zip': '76541', 'first_name': 'Travis', 'street': '1859 Clair Street'}
><Response [201]>
>{"url":"http://127.0.0.1:8000/api/contacts/13/","first_name":"Travis","last_name":"Fox","street":"1859 Clair Street","zip":"76541","city":"Killeen","image":"https://cdn1.iconfinder.com/data/icons/user-pictures/100/male3-512.png"}
>{'image': 'https://cdn1.iconfinder.com/data/icons/user-pictures/100/female1-512.png', 'city': 'Pittsfield', 'last_name': 'Kasmi', 'zip': '1201', 'first_name': 'Leontine', 'street': '1009 Kinney Street'}
><Response [201]>
>{"url":"http://127.0.0.1:8000/api/contacts/14/","first_name":"Leontine","last_name":"Kasmi","street":"1009 Kinney Street","zip":"1201","city":"Pittsfield","image":"https://cdn1.iconfinder.com/data/icons/user-pictures/100/female1-512.png"}
>{'image': 'http://www.google.com', 'city': 'Woodburn', 'last_name': 'Gilsing', 'zip': '97071', 'first_name': 'Shanon', 'street': '3644 Seneca Drive'}
><Response [201]>
>{"url":"http://127.0.0.1:8000/api/contacts/15/","first_name":"Shanon","last_name":"Gilsing","street":"3644 Seneca Drive","zip":"97071","city":"Woodburn","image":"http://www.google.com"}
>{'image': 'http://nothing.com', 'city': 'Macon', 'last_name': 'Dibbets', 'zip': '31201', 'first_name': 'Miray', 'street': '489 Oakridge Lane, "test"'}
><Response [201]>
>{"url":"http://127.0.0.1:8000/api/contacts/16/","first_name":"Miray","last_name":"Dibbets","street":"489 Oakridge Lane, \"test\"","zip":"31201","city":"Macon","image":"http://nothing.com"}