BASE_HTML = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE-edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    {% block head %}
    <title>{% block title %}Flask QuickStart{% endblock title %}</title>
    {% endblock head %}

    <link
      rel="icon"
      href="{{ url_for('static', filename='icons/curt-05.png') }}"
    />

    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/bootstrap.min.css')}}"
    />

    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/fontawesome.min.css"
    />

    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    />
    
    {% assets "base_main_" %}
    <link rel="stylesheet" type="text/css" href="{{ ASSET_URL }}" />
    {% endassets %}
  </head>
  <body>
    <nav class="burger-menu">
      <ul>
        <li><a href="">Flask QuickStart</a></li>
        <li><a href="{{ url_for('view.home_page') }}">Home</a></li>
        <li>
          <a href="#"
            >Notification</a
          >
        </li>
      </ul>
    </nav>

    <header class="header-main">
      <div class="header-main-logo">
        <img
          src="#"
          alt="brand_logo"
          width="6"
          height="60"
        />
        <nav class="header-main-nav">
          <ul>
            <li>
              <a href="">Flask QuickStart</a>
            </li>
            <li>
              <a href="{{ url_for('view.home_page') }}">Home</a>
            </li>
            <li class="dropdown">
              <a href="#" class="dropbtn">More</a>
              <div class="dropdown-content">
                <a href="#">About</a>
                <a href="#">None</a>
                <a href="#">None</a>
                <a href="#">None</a>
              </div>
            </li>
          </ul>
        </nav>
      </div>

      <!--navbar side icon -->
      <div class="header-main-sm">
        <a href="#"><div class="header-main-sm-fb"></div></a>
        <a href="#"><div class="header-main-sm-in"></div></a>
        <div class="burger-menu-btn"></div>
      </div>
    </header>

    <div class="flash--message">
      {% with messages = get_flashed_messages(with_categories=True) %} {% if
      messages %} {% for category, message in messages %} {% if category ==
      "error" %}

      <div class="alert alert-danger alter-dismissable fade show" role="alert">
        <i class="fas fa-circle-xmark"></i>
        {{ message }}
      </div>

      {% else %}
      <div class="alert alert-success alter-dismissable fade show" role="alert">
        <i class="fas fa-circle-check"></i>
        {{ message }} {% endif %}{% endfor %}{% endif %}{% endwith %}
      </div>
    </div>

    {% assets "main_js" %}
    <script src="{{ ASSET_URL }}" defer></script>
    {% endassets %}

    <!--  -->
    <script src="{{ url_for('static', filename='js/bootstrap.bundle.min.js')}}"></script>
    {% block content %}{% endblock content %}

    <!--  -->
    {% block footer %}
    <div class="footer">
      <div class="footer-bottom">
        &copy; Copyright © 2024 Flask Quick Start Generator
      </div>
    </div>
    {% endblock footer %}
  </body>
</html>
"""

AUTHENTICATION_REGISTER_HTML = \
""" 
{% extends "base.html" %}

<head>
  {% block head %}
  <title>{% block title %}Register{% endblock title %}</title>

  {% assets "base_main_" %}
  <link rel="stylesheet" type="text/css" href="{{ ASSET_URL }}" />
  {% endassets %}

  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
  />
  {% endblock head %}
</head>

{% block body %} {% block content %}
<div class="page-wrapper">
  <div class="container-fluid">
    <div class="row no-gutters">
      <div
        class="col-md-4 right-section d-flex align-items-center justify-content-center"
      >
        <div class="login-container p-4 shadow-lg rounded">
          <h2>Flask QuickStart</h2>
          <form method="POST">
            {{ form.hidden_tag() }}

            <div class="form-group m-b-5">
              {{ form.username(class="form-control mb-3")}}
            </div>

            <div class="form-group m-b-5">
              {{ form.email(class="form-control mb-3")}}
            </div>

            <div class="form-group">
              {{ form.password(class="form-control mb-3")}}
            </div>

            <div class="form-group">
              {{ form.confirm_password(class="form-control mb-3")}}
            </div>

            <div class="form-group">
              {{ form.user_role(class="form-control mb-3")}}
            </div>

            <button
              type="submit"
              class="btn btn-success btn-block mb-4"
              id="submit-button"
            >
              Register
            </button>
          </form>
          <div class="text-center">
            <a
              href="{{ url_for('admin_controller.secure_dashboard')}}"
              id="toggle-form"
              >Back Dashboard</a
            >
            |
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

{% assets "main_js" %}
<script src="{{ ASSET_URL }}"></script>
{% endassets %}
<!--  -->
{% endblock content %} {% endblock body %}
"""


AUTHENTICATION_LOGIN_HTML =\
""" 
{% extends "base.html" %}

<head>
  {% block head %}
  <title>{% block title %}Flask QuickStart{% endblock title %}</title>

  {% assets "base_main_" %}
  <link rel="stylesheet" type="text/css" href="{{ ASSET_URL }}" defer />
  {% endassets %}

  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
  />
  {% endblock head %}
</head>

{% block body %} {% block content %}
<div class="page-wrapper">
  <div class="container-fluid">
    <div class="row no-gutters">
      <div
        class="right-section d-flex align-items-center justify-content-center"
      >
        <div class="login-container p-4 shadow-lg rounded">
          <h2>Flask QuickStart</h2>
          <form method="POST">
            {{ form.hidden_tag() }}

            <div id="auth-form-fields">
              <div class="form-group m-b-5">
                {{ form.username(class="form-control mb-3")}}
              </div>

              <div class="form-group">
                {{ form.password(class="form-control mb-3")}}
              </div>
            </div>
            <button
              type="submit"
              class="btn btn-primary btn-block mb-4"
              id="submit-button"
            >
              Login
            </button>
            <a
              href="#"
              class="btn btn-danger btn-block mb-4"
              id="google-login-button"
            >
              <i class="fab fa-google"></i> Login with Google
            </a>
          </form>
          <div class="text-center">
            <a href="#">Forgot Password?</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

{% assets "main_js" %}
<script src="{{ ASSET_URL }}"></script>
{% endassets %}
<!--  -->
{% endblock content %} {% endblock body %}
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
                Welcome to Flask Quickstart Generator
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
