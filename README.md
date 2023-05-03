# django_assignment_rest_api
django rest api assignment


Endpoints of the api

1. (GET)  /api/works/ 
-> lists all the work available

2. (GET)  /api/works/?artist=artistName
-> lists all the work with artist name 

3. (GET)  /api/works/?work_type=youtube
-> list all the work with work type of youtube

4. (POST)   /api/register (with username and password in request body)
-> creates a user, with username and password
eg - 
{
"username": "rahul",
"password": "...pass"
}

5. (POST)   /api/creatework (with artist_name, link and work_type in request body)
-> creates a work, with artist name, link and work_type 
eg - 
{
"artist_name": "Hitesh Sir",
"link": "https://youtu.be/iZloRI4LVYY",
"work_type": "Youtube"
}
