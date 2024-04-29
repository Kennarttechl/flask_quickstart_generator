
BASE_HTML = \
"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE-edge">
<meta name="viewport" content="device-width, initial-scale=1.0">

{% block head %}
<title>{% block title %}Flask Boiler Plate{% endblock title %}</title>
{% endblock head %}

<link rel="icon" href="">
</head>

{% assets "base_main_" %}
<link rel="stylesheet" type="text/css" href="{{ ASSET_URL }}">
{% endassets %}

<body>
{% block body %}
<h2>Flask Boiler Plate</h2>
<p>Congratulation!</p>
{% endblock body %}


<div class="flash--message">
  {% with messages = get_flashed_messages(with_categories=True) %} {% if
  messages %} {% for category, message in messages %} {% if category ==
  "error" %}

  <div class="alert alert-danger alter-dismissable fade show" role="alert">
    <!-- <i class="bi bi-x-circle-fill"></i> -->
    <i class="fa-solid fa-circle-xmark"></i>
    {{ message }}
  </div>

  {% else %}
  <div class="alert alert-success alter-dismissable fade show" role="alert">
    <!-- <i class="bi bi-check-circle-fill"></i> -->
    <i class="fa-solid fa-circle-check"></i>
    {{ message }} {% endif %}{% endfor %}{% endif %}{% endwith %}
  </div>
</div>

{% assets "main_js" %}
<script src="{{ ASSET_URL }}"></script>
{% endassets %}

{% assets "bootstrap_js" %}
<script src="{{ ASSET_URL }}"></script>
{% endassets %}
{% block content %}{% endblock content %}

{% block footer %}
{% endblock footer %}
</body>
</html>
"""


DEMO_HTML_TEMPLATES = \
""" 
{% extends "base.html" %}

{% block head %}
<title>{% block title %}Flask Boiler_Plate{% endblock title %}</title>

<link rel="icon" href="">

{% assets "new_css" %}
<link rel="stylesheet" type="text/css" href="{{ ASSET_URL }}"/>
{% endassets %}
{% endblock head %}

{% block body %}





{% assets "main_js" %}
<script src="{{ ASSET_URL }}"></script>
{% endassets %}

{% assets "bootstrap_js" %}
<script src="{{ ASSET_URL }}"></script>
{% endassets %}

{% endblock body %}
"""


DEMO_HTML = \
"""
{% extends "base.html" %}

{% block body %}
    <!-- Hero section with background image -->
    <section class="hero is-primary is-fullheight" style="background-image: url('https://via.placeholder.com/1500x800')">
        <div class="hero-body">
            <div class="container">
                <h1 class="title is-1">
                    Welcome to Flask Boilerplate Generator
                </h1>
                <h2 class="subtitle">
                    Kickstart your Flask projects with ease
                </h2>
            </div>
        </div>
    </section>
{% endblock body %}
"""


FLASH_MESSAGE = \
"""
{% assets "new_css" %}
<link rel="stylesheet" type="text/css" href="{{ ASSET_URL }}" />
{% endassets %}

<link
  rel="stylesheet"
  href="{{ url_for('static', filename='css/fontawesome.min.css') }}"
/>

<link
  rel="stylesheet"
  href="{{ url_for('static', filename='css/bost-4.1.3/css/bootstrap.min.css')}}"
/>

{% block message %}
<div class="container">
  <div class="flash--message">
    {% with messages = get_flashed_messages(with_categories=True) %} {% if
    messages %} {% for category, message in messages %} {% if category ==
    "error" %}

    <div class="alert alert-danger alter-dismissable fade show" role="alert">
      {{ message safe }}
    </div>

    {% else %}
    <div class="alert alert-success alter-dismissable fade show" role="alert">
      {{ message safe }}
    </div>
    {% endif %}{% endfor %}{% endif %}{% endwith %}
  </div>
</div>
{% endblock message %}
"""