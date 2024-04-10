
BASE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE-edge">
<meta name="viewport" content="device-width, initial-scale=1.0">

{% block head %}
<title>{% block title %}Flask Boiler Plate{% endblock %}</title>
{% endblock head %}

<link rel="icon" href="{{ url_for('static', filename='icons/brand-logo.svg')}}">
</head>
<body>
{% block body %}
<h2>Flask Boiler Plate</h2>
<p>Congratulation!</p>
{% endblock body %}

{% block content %}{% endblock content %}

{% block footer %}
{% endblock footer %}
</body>
</html>
"""


DEMO_HTML = """
{% extends "base.html" %}
    
{% block body %}
    <section class="hero is-primary">
    <div class="hero-body">
        <div class="container">
            <h1 class="title is-1">
                Welcome to Flask CLI
            </h1>
            <h2 class="subtitle">
                By eliminating repetitive tasks, you can focus on the core logic of your application.
            </h2>
        </div>
    </div>
</section>
<section class="section">
    <div class="container">
        <div class="content">
            <h1></h1>
            <h1>flask-cli</h1>
            <ul>
                <li class=""><b>--init</b></li>
                <li class=""> <b>create-app</b> <i>my_demo_app</i> </li>
            </ul>
        </div>
    </div>
</section>
{% endblock body %}
"""