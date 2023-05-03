# django_assignment_rest_api
django rest api assignment


Endpoints of the api
(GET Requests)
1. /api/works/

-> lists all the work available

2. /api/works/?artist=artistName

-> lists all the work with artist name 

3. /api/works/?work_type=youtube

-> list all the work with work type of youtube

(POST Requests)

4. /api/register (with username and password in request body)

-> creates a user, with username and password
eg -

<code>{
"username": "rahul",
"password": "...pass"
}</code>

5. (POST)   /api/creatework (with artist_name, link and work_type in request body)

-> creates a work, with artist name, link and work_type 
eg -

<code>{
"artist_name": "Hitesh Sir",
"link": "https://youtu.be/iZloRI4LVYY",
"work_type": "Youtube"
}</code>
