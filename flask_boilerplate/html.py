BASE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE-edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

{% block head %}
<title>{% block title %}Flask BoilerPlate{% endblock title %}</title>
{% endblock head %}

<link rel="icon" href="">

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css">
</head>

{% assets "base_main_" %}
<link rel="stylesheet" type="text/css" href="{{ ASSET_URL }}">
{% endassets %}

<body>
{% block body %}

<!-- Write the rest of your code hear -->



<div class="flash--message">
  {% with messages = get_flashed_messages(with_categories=True) %} {% if
  messages %} {% for category, message in messages %} {% if category ==
  "error" %}

  <div class="alert alert-danger alter-dismissable fade show" role="alert">
    <i class="fa-solid fa-circle-xmark"></i>
    {{ message }}
  </div>

  {% else %}
  <div class="alert alert-success alter-dismissable fade show" role="alert">
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
{% endblock body %}


{% block footer %}
{% endblock footer %}
</body>
</html>
"""


DEMO_HTML_TEMPLATES = """ 
{% extends "base.html" %}

{% block head %}
<title>{% block title %}Flask Boiler_Plate{% endblock title %}</title>

{% assets "base_main_" %}
<link rel="stylesheet" type="text/css" href="{{ ASSET_URL }}"/>
{% endassets %}
{% endblock head %}

{% block body %}
<!-- The rest of your code here -->

<section class="hero is-primary">
    <div class="hero-body">
        <div class="container">
            <h1 class="title is-1">
                Welcome to Flask Boilerplate Generator
            </h1>
            <h2 class="subtitle">
                By eliminating repetitive tasks, you can focus on the core logic of your application.
            </h2>
            <label class="toggle-switch">
                <input type="checkbox" id="dark-mode-toggle">
                <span class="slider round"></span>
            </label>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="content">
            <h1></h1>
            <h1>flask-boilerplate</h1>
            <ul>
                <li class=""><b>-v  for creating virtualenv</b></li>
                <li class=""> <b>command for creating app => create-app </b> <i>demo_app</i></li>
            </ul>
        </div>
    </div>
</section>


{% assets "main_js" %}
<script src="{{ ASSET_URL }}"></script>
{% endassets %}

{% assets "bootstrap_js" %}
<script src="{{ ASSET_URL }}"></script>
{% endassets %}


{% block footer %}
<footer class="footer is-fixed-bottom">
    <div class="content has-text-centered">
    <p>
      Happy Hacking!
    </p>
    </div>
</footer>
{% endblock footer %}
{% endblock body %}
"""


FLASH_MESSAGE = """
{% assets "new_css" %}
<link rel="stylesheet" type="text/css" href="{{ ASSET_URL }}"/>
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
      {{ message }}
    </div>

    {% else %}
    <div class="alert alert-success alter-dismissable fade show" role="alert">
      {{ message }}
    </div>
    {% endif %}{% endfor %}{% endif %}{% endwith %}
  </div>
</div>
{% endblock message %}
"""


NOT_USE = """ 
<script src="https://unpkg.com/htmx.org@1.9.12"></script>

<select class="section">
  <div class="columns">
    <div class="column is-on-third is-offset-one-third">
      <input
        type="text"
        class="input"
        placeholder="Search"
        name="q"
        hx-get="search"
        hx-trigger="keyup change delay:500ms"
        hx-target="#results"
      />
    </div>
    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>Title</th>
          <th>Performance</th>
          <th>Peak Position</th>
          <th>Time on Chart</th>
          <th>Chart Debut</th>
        </tr>
      </thead>
      <tbody id="results"></tbody>
    </table>
  </div>
</select>

{% for result in results %}
<tr>
  <td>{{ result.username }}</td>
  <td>{{ result.email }}</td>
  <td>{{ result.password }}</td>
  <td>{{ result.user_profile }}</td>
  <td>{{ result.confirm_password }}</td>
</tr>
{% endfor %} -->
"""
