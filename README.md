# django-RESTapi2

-  <u>  For all users' details</u>:

    http://localhost:8000/users-api/details/

-  <u>  For details of user with specific id</u>:

    http://localhost:8000/users-api/details/<id>

- <u>To register a new user</u>:

    Send a JSON POST to:

    http://localhost:8000/users-api/register/

    <details>
    <summary>JSON POST format</summary>
    {

        "username" : "<username>",

        "password" : "<password>"

    }
    </detials>
-  <u>To login and receive JWT</u>:
    
    Send a JSON POST to:

    http://localhost:8000/users-api/jwt-auth/

    <details>
    <summary>JSON POST format</summary>
    {

        "username" : "<username>",

        "password" : "<password>"

    }