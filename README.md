# ActivityPeriod-models
Design and implementation of a Django application with User and ActivityPeriod models and to populate the database with some dummy data, and design an API to serve that data in the json format.

<br>

## using the Application & API Endpoints
[Click here for Live View](http://3.6.165.171:4200/)
---

 - JSON response of all the User and ActivityPeriods
    - {URL} + /
    - [Click here for Live View](http://3.6.165.171:4200/)

 - Generate 1 Random User 
    - {URL} + /generateuser
    - [Link to Generate Random User](http://3.6.165.171:4200/generateuser)

 - Generate Activity For Random User
    - {URL} + /generateactivity
    - [Link to Generate Activity for User](http://3.6.165.171:4200/generateactivity)


<br>
<br>


# Setup and Installation
##  Setup Virtual environment Pyhton3


- clone Repositry
    <pre><code> git clone https://github.com/khushrajjain/ActivityPeriod-models.git</pre></code>


- install virtualenv if not installed
    <pre><code> pip install virtualenv </pre></code> 

- Create virtual environment for Python 3 and activate
    <pre><code>virtualenv venv -p python3 </pre></code> 
    <pre><code>source venv/bin/activate</pre></code>

- Install all the packages
    <pre><code>pip install -r requirements.txt</pre></code>

- Go to Projecr Dir
    <pre><code>cd ActivityPeriod/</code></pre>

- Migrate
    <pre><code>python manage.py migrate</code></pre>

- Run Server
    <pre><code>python manage.py runserver</code></pre>

