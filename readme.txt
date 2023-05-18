Morvin Installation in Django Python
Python Version >> 3.8.10
Django Version >> 3.2.5
Bootstrap Version >> 5.0.0-beta2
>>>Installation Python
 ->https://www.python.org/downloads/
>>For Windows OS 
 -Download python  from windows store
 -Select the Python's version to download.
 -Click on the Install Now
 -Installation in Process
>>For Linux OS
 -sudo apt update
 -sudo apt install python3

>>>Note: Depending on your installation, you may need to use either pip3 or pip and for python you may need to use either python3 or python.

>>>Open terminal
 -python --version
 
>>>To check pip version  
  -py -m pip --version
  -upgread pip 
  -py -m pip install --upgrade pip
>>>Installing virtualenv   
  #linux & mac os
   ->python3 -m pip install --user virtualenv
  #Windows
  ->py -m pip install --user virtualenv
>>>Create Virtual Environment
  #linux & mac os
  ->python3 -m venv environment_name
  #Windows
  ->python -m venv environment_name
>>>Activate Environment
  #Linux & mac os
  ->source environment_name/bin/activate
  #Windows
  ->environment_name\Scripts\activate
 
>>>Install Django
 #linux & mac os
 ->pip3 install django
 #Windows
 ->pip install django
 
>>>First please check Django properly Installed or not
 #Linux/macOS
 python3 -m django --version
 #Windows
 python  -m django --version
>>>Open terminal 
 -Goto project directory using cd command
 
>>>Install libraries
->pip install django-embed-video
->pip install django-crispy-forms
->pip install django-allauth

>>>Nodejs
->Make sure to have the Node.js installed & running in your computer

>>>Yarn
->Make sure to have the yarn installed & running in your computer

>>>gulp     
->Make sure to have the gulp installed & running in your computer

>>>Git
->Make sure to have the git installed globally & running in your computer

-->Now you can just run command `gulp`
Google :-

https://console.cloud.google.com
Select Project
    New Project
    Project Name:Your Project Name
    CREATE

    Example:
    New Project
    Project Name :Morvin
    CREATE

Go to Credentials
    Create Credentials
    Select OAuth client id
    Configure consent screen *
    User Type :- External
    CREATE

    App information
    App name:Your App Name
    User support email:Your Email ID
    Developer contact information *
    Email addresses : Your Email ID
    SAVE AND CONTINUE
    SAVE AND CONTINUE
    SAVE AND CONTINUE
    BACK TO DASHBORD

    Example:-
    App information
    App name:Morvin
    User support email:morvin@support.com
    Developer contact information *
    Email addresses : morvin@support.com
    SAVE AND CONTINUE
    SAVE AND CONTINUE
    SAVE AND CONTINUE
    BACK TO DASHBORD



    Credentials
    Create Credentials
    select OAuth client id
    Create OAuth client ID *
    Application type : Web application
    Name : Your App Name
    Authorised javascript origins
    ADD URI *
        uris:- http://Your_host_name
    Authorised redirect uris
    ADD URI *
        uris:- http://Your_host_name/accounts/google/login/callback/
    CREATE

    You can Copy Your Client id & Your Client Secret

    Example :-
    Create Credentials
    select OAuth client id
    Create OAuth client ID
    Application type : Web application
    Name : Morvin
    Authorised javascript origins *
    ADD URI *
    uris:- http://127.0.0.1:8000
            http://localhost:8000
    Authorised redirect uris
    ADD URI *       
    uris:- http://127.0.0.1:8000/account/google/login/callback/
           http://localhost:8000/account/google/login/callback/

    CREATE


Facebook
    https://developers.facebook.com/apps

    Create App
    Select an app type
    Create an App *
    App Display Name: Your App Name
    App Contact Email : Your Email ID
    Create App
        Password:Your Facebook id Password
        Submit
    Go to Settings
            Basic
            You can get Your App ID & App Secret




    Example:
    Create App
    Select an app type
        Consumer
        Continue
    Create an App *
    App Display Name: Morvin
    App Contact Email : morvin@support.com
    Create App
        Password: **********
        Submit
    Go to Settings
            Basic

    Go to My App:
        Click on three dots
            Create Test App
                Test App Name:Your test app name
                Confirm
    Go to Settings/basic
        App Domains:Your Domain name
        click on add Platform
        Select Platform Any one of them
        Site URL:-URL of your site

    Example:
    Go to My App:
        Click on three dots
            Create Test App
                Test App Name:Morvin Test
                Confirm
    Go to Settings/basic
        App Domains:localhost
        click on add Platform
        Select Platform:Website
        Site URL:-https://localhost:8000/


>>To run url with Facebook api :-localhost:8000

>>To Login Social Accounts
->Go To admin panel
->127.0.0.1:8000/admin
->Social Accounts/Social Application
--Add Social Application

    ->Follow these steps
    1.Provider :- Select App Provider
    2.Name :- Enter App Name
    3.Client id :- Enter App Client id
    4.Secret key :- Enter App Secret key
    5.Sites :- Add Your Site
    6.Save



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.#databaseservername#',
        'NAME': 'Your Database Name',
        'USER' : 'Database User Name',
        'PASSWORD' : 'Your Password',
        'HOST' : "Write down Host",
        'PORT' : 'Write down port',
                
    }
}
>>>To Create superuser 
->python manage.py createsuperuser
    enter username = your_username
    enter your Email Address
    enter your password
    enter your password again 
-> Windows:-python manage.py migrate
-> Linux:-python3 manage.py migrate

>>>To load Static Files:-
>Go to Skote/setings.py
-Add following command:-
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT= os.path.join(BASE_DIR,'assets')

>Run Command In Terminal
-python manage.py collectstatic
-Goto settings.py of Main Directory

-SMTP CONFIGURATION
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'YOUR EMAIL ADDRESS'
    EMAIL_HOST_PASSWORD = 'YOUR HOST Password'
    DEFAULT_FROM_EMAIL = 'YOUR EMAIL ADDRESS'
    SERVER_EMAIL = 'YOUR EMAIL ADDRESS'


     

>>>To Set Default Layout
 >Goto templates/partial/base.html
 
<!--===========================================================================-->
                <!--Vertical Layout View-->
<!--===========================================================================-->
#STEP :-1 Select Anyone of following BodyTag 
#Make changes according choice at Line No 28
1.Dark Sidebar
<body data-sidebar="dark">   
2.light sidebar
<body data-sidebar="light"> 
2.Compact Sidebar
<body data-sidebar-size="small">  
3.Icon Sidebar
<body data-keep-enlarged="true" class="vertical-collpsed">  
4.Box Width Sidebar
<body data-keep-enlarged="true" class="vertical-collpsed" data-layout-size="boxed"> 
5.Prealoader Sidebar
 <body> 
        <!-- Loader -->
    <div id="preloader">
        <div id="status">
            <div class="spinner-chase">
                <div class="chase-dot"></div>
                <div class="chase-dot"></div>
                <div class="chase-dot"></div>
                <div class="chase-dot"></div>
                <div class="chase-dot"></div>
                <div class="chase-dot"></div>
            </div>
        </div>
    </div>
STEP:-2 Select Vertical Header and Siderbar & comment the  Horizontal Header View as shown below.
<!-- VERTICAL LAYOUT VIEW-->
<!--=================================-->
{% block header %}
    {% include 'partials/header.html' %}  
{% endblock %}          
{% block sidebar %}
    {% include 'partials/sidebar.html' %}   
{% endblock %}    
<!-- HORIZONTAL LAYOUT VIEW-->
<!--=================================-->
{% comment %} {% block header %}
    {% include 'partials/hori-header.html' %}
{% endblock %}
{% block sidebar %}
    {% include 'partials/hori-sidebar.html' %}
{% endblock %} {% endcomment %}
<!--===========================================================================-->
                        <!--Horizontal Body View-->
<!--===========================================================================-->
#STEP :-1 Select Anyone of following BodyTag 
#Make changes according choice at Line No 23
1.Horizontal Bar
<body data-topbar="dark" data-layout="horizontal"> 
2.Horizontal top Bar light
<body data-topbar="light" data-layout="horizontal">  
3.Horizontal Box Width Sidebar
<body data-topbar="dark" data-layout="horizontal" data-layout-size="boxed">  
4.Horizontal Prealoader bar
    <body data-topbar="dark" data-layout="horizontal">
        <!-- Loader -->
        <div id="preloader">
            <div id="status">
                <div class="spinner-chase">
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                    <div class="chase-dot"></div>
                </div>
            </div>
        </div> 
5.Horizontal colored Header
<body data-topbar="colored" data-layout="horizontal">
STEP :-2 Comment the Vertical layout view and Siderbar & then Select Horizontal Layout View as shown below.
<!-- VERTICAL LAYOUT VIEW-->
<!--=================================-->
{% comment %}
{% block header %}
{% include 'partials/header.html' %}  
{% endblock %}          
{% block sidebar %}
{% include 'partials/sidebar.html' %}   
{% endblock %} {% endcomment %}   
<!-- HORIZONTAL LAYOUT VIEW-->
<!--=================================-->
{% block header %}
{% include 'partials/hori-header.html' %}
{% endblock %}
{% block sidebar %}
{% include 'partials/hori-sidebar.html' %}
{% endblock %} 
<!--===========================================================================-->
>> To set Default light/dark/RTL Mode
<!--===========================================================================-->
<!--===========================================================================-->
>>Go static/js/app.js
-line number 270
<!--===========================================================================-->
>For Light theme
alreadyVisited = "light-mode-switch";
>For Dark theme
alreadyVisited = "dark-mode-switch";
>For RTL theme
alreadyVisited = "rtl-mode-switch";
# for RTL mode only
-Goto templetes/partials/base.html
 line number 3 
 <html lang="en" dir="rtl">
<!--===========================================================================-->
<!--===========================================================================-->
-> Windows:-python manage.py migrate
-> Linux:-python3 manage.py migrate
>>>Run your project
-Windows:-python manage.py runserver
-Linux:-python3 manage.py runserver
