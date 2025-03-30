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

    <link rel="icon" href="#" />

    <!-- <link rel="stylesheet" href=" Your css path here "> -->

    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/flash.css')}}"
    />

    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/footer.css')}}"
    />
  </head>
  <body>
    {% block body %}

    <!-- WRITE YOUR THE REST OF YOUR CODE HERE -->

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

    <!-- <script src="Your js scripts path here "></script> -->
    {% block content %}{% endblock content %} {% endblock body %}

    <!-- footer  -->
    {% block footer %}
    <div class="footer">
      <div class="footer-bottom">
        &copy; Copyright 2025 Flask Quick Start Generator
      </div>
    </div>
    {% endblock footer %}
  </body>
</html>
"""

FLASH_CUSTOM_HTML = """ 
<link rel="stylesheet" href="{{ url_for('static', filename='css/flash.css') }}">

<div class="flash--message">
  {% with messages = get_flashed_messages(with_categories=True) %} {% if
  messages %} {% for category, message in messages %} {% if category ==
  "error" %}

  <div class="alert alert-danger alter-dismissable fade show" role="alert">
    <i class="fas fa-times"></i>
    {{ message }}
  </div>

  {% else %}
  <div class="alert alert-success alter-dismissable fade show" role="alert">
    <i class="fas fa-check"></i>
    {{ message }} {% endif %}{% endfor %}{% endif %}{% endwith %}
  </div>
</div>
"""

AUTHENTICATION_REGISTER_HTML = """ 
{% extends "base.html" %}

<head>
  {% block head %}
  <title>{% block title %}Register{% endblock title %}</title>

  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
  />
  
  <!-- <link rel="stylesheet" href="Your css path here"/> -->

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

<!-- <script src="Your js scripts path here "></script> -->
{% endblock content %} {% endblock body %}
"""

AUTHENTICATION_LOGIN_HTML = """ 
{% extends "base.html" %}

<head>
  {% block head %}
  <title>{% block title %}Flask QuickStart{% endblock title %}</title>

  <!-- <link rel="stylesheet" href="Your css path here"/> -->

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

<!-- <script src="Your js scripts path here "></script> -->
{% endblock content %} {% endblock body %}
"""

DEMO_HTML_TEMPLATES = """ 
{% extends "base.html" %}

{% block head %}
<title>{% block title %}Flask QuickStart{% endblock title %}</title>

<!-- <link rel="stylesheet" href="Your css path here"/> -->
{% endblock head %}

{% block body %}
{% block content %}



<!-- WRITE YOUR CODE HERE -->



{% endblock content %}
<!-- <script src="Your js scripts path here "></script> -->
{% endblock body %}
"""

SADMIN_LOGIN_SECURE = """ 
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Flask Admin</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />

    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/log.css') }}"
    />

    <link rel="stylesheet" href="{{ url_for('static', filename='css/flash.css') }}">
  </head>
  <body>
    <div class="container-fluid">
      <div class="left"></div>
      <div class="right">
        <div class="toggle-switch">
          <input type="checkbox" id="dark-mode-toggle" />
          <label class="slider" for="dark-mode-toggle"></label>
        </div>
        <h2>Flask administration</h2>
        <p>Build scalable web applications with ease</p>

        <form action="#" method="post">
          {{ form.hidden_tag() }}
          <div class="form-group">
            {{ form.email(class="form-control mb-3") }}
          </div>
          <div class="form-group">
            {{ form.username(class="form-control mb-3") }}
          </div>
          <div class="form-group">
            {{ form.password(class="form-control mb-3") }}
          </div>
          <button type="submit" class="btn btn-primary w-100">Login</button>
        </form>
      </div>
    </div>
    <!-- Include the flash message section here -->
    {% include 'flash_message.html' %}

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>

    <script src="{{ url_for('static', filename='js/log.js') }}"></script>
    <script src="{{ url_for('static', filename='js/flash_remove_dom.js') }}"></script>
  </body>
</html>
"""

SADASHBOARD_SECURE = """ 
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Flask Administration</title>

    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />

    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />

    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/sadashboard.css') }}"
    />
    
    <link rel="stylesheet" href="{{ url_for('static', filename='css/flash.css') }}">
  </head>
  <body>
    <header class="topbar">
      <div class="topbar-left">
        <i class="fas fa-angle-double-left toggle-sidebar"></i>
        <div class="input-group">
          <form method="post" class="d-flex">
            <input
              type="text"
              class="form-control"
              placeholder="Search item..."
            />
            <button class="btn btn-success" type="submit">
              <i class="fas fa-search"></i>
            </button>
          </form>
        </div>
      </div>
      <div class="user-profile">
        <img src="{{ url_for('static', filename='media/Image/s3.png')}}" alt="User" />
        <span>{{ current_user.username }}</span>
        <i class="fas fa-chevron-down"></i>
        <div class="dropdown-menu">
          <ul>
            <li>
              <a href="#settings"> <i class="fas fa-cog"></i> Settings </a>
            </li>
            <li>
              <a href="#account"> <i class="fas fa-user"></i> Account </a>
            </li>
            <li>
              <a href="#theme" id="theme-toggle">
                <i class="fas fa-moon"></i> Theme
              </a>
            </li>
            <li>
              <a href="{{ url_for('super_admin_secure.secure_superlogin')}}">
                <i class="fas fa-sign-out-alt"></i> Logout
              </a>
            </li>
          </ul>
        </div>
      </div>
    </header>

    <div class="main-section">
      <aside class="sidebar">
        <div class="logo">
          <i class="fas fa-tachometer-alt"></i>
          Flask Administration
        </div>
        <hr />
        <ul class="nav-menu">
          <li>
            <a href="#!" class="active">
              <i class="fas fa-home"></i> Dashboard
            </a>
          </li>

          <li class="has-submenu">
            <a href="#!">
              <i class="fas fa-file-invoice"></i>
              Access Control
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">User Roles</a></li>
              <li><a href="#!">Permissions</a></li>
              <li><a href="#!">Security Settings</a></li>
            </ul>
          </li>

          <li class="has-submenu">
            <a href="#!">
              <i class="fas fa-user-tie"></i> Admin Tools
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">User Management</a></li>
              <li><a href="#!">Activity Logs</a></li>
              <li><a href="#!">System Settings</a></li>
            </ul>
          </li>

          <li class="has-submenu">
            <a href="#!">
              <i class="fas fa-users"></i>
              User Accounts
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">Edit Profile</a></li>
              <li><a href="#!">Create Account</a></li>
              <li><a href="#!">Manage Accounts</a></li>
              <li><a href="#!">Password Reset</a></li>
              <li><a href="#!">Account Activation</a></li>
            </ul>
          </li>

          <li class="has-submenu">
            <a href="#!">
              <i class="fas fa-chart-line"></i>
              Reports & Anlyt
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">User Activity</a></li>
              <li><a href="#!">Performance Metrics</a></li>
            </ul>
          </li>

          <li class="has-submenu">
            <a href="#!">
              <i class="fas fa-heartbeat"></i>
              System Health
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">Resource Monitoring</a></li>
              <li><a href="#!">Uptime Monitoring</a></li>
              <li><a href="#!">Performance Reports</a></li>
            </ul>
          </li>

          <li class="has-submenu">
            <a href="#!">
              <i class="fas fa-database"></i>
              Database Mgt
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">Backup Database</a></li>
              <li><a href="#!">View Tables</a></li>
            </ul>
          </li>

          <li class="has-submenu">
            <a href="#!">
              <i class="fas fa-bell"></i>
              Notifications
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">View Alerts</a></li>
              <li><a href="#!">Set Up Alerts</a></li>
            </ul>
          </li>

          <li class="has-submenu">
            <a href="#!">
              <i class="fas fa-code"></i>
              API Mgt
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">Admin</a></li>
              <li><a href="#!">Super Admin</a></li>
            </ul>
          </li>
          <li>
            <a href="#!"> <i class="fas fa-user-cog"></i> Settings </a>
          </li>
        </ul>
      </aside>

      <div class="main-content">
        <div class="content-header">
          <div>
            <h1>Project Invoice</h1>
            <p class="invoice-meta">Date: 03/19/2025 | Invoice #: PRJ-12457</p>
          </div>
          <div class="invoice-info">
            <p>Acme Corporation</p>
            <p>Total: $4,250.00</p>
          </div>
        </div>

        <div class="dashboard-container">
          <div class="dashboard-box">
            <h2>Total Users Registered: 1,240</h2>
            <p>587.00</p>
            <p class="subtext">12.5% increase in the last week</p>
          </div>
          <div class="dashboard-box">
            <h2>System Uptime: 99.97%</h2>
            <p>6,084</p>
            <p class="subtext">Updated hourly</p>
          </div>
          <div class="dashboard-box">
            <h2>Pending Admin Tasks: 14</h2>
            <p>250.00</p>
            <p class="subtext">28.6% of total tasks pending this week</p>
          </div>
          <div class="dashboard-box">
            <h2>Total Revenue: $12,360</h2>
            <p>7,360.00</p>
            <p class="subtext">45.3% of quarterly revenue goal</p>
          </div>
        </div>

        <div class="table-container overflow-auto">
          <h3 class="main--title">Admin Activity Logs</h3>
          <hr />
          <div class="search-container">
            <form method="post" class="d-flex">
              <input
                type="text"
                class="form-control"
                placeholder="Search item..."
              />
              <button class="btn btn-success" type="submit">
                <i class="fas fa-search"></i>
              </button>
            </form>
          </div>
          <table class="table table-striped table-bordered">
            <thead>
              <tr>
                <th scope="col">USER ID</th>
                <th scope="col">ACTION</th>
                <th scope="col">TIMESTAMP</th>
                <th scope="col">STATUS</th>
                <th scope="col">ROLE</th>
                <th scope="col">IP ADDRESS</th>
                <th scope="col">SESSION DURATION</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>#U1001</td>
                <td>Login</td>
                <td>2025-03-19 08:45:12</td>
                <td>Success</td>
                <td>Admin</td>
                <td>192.168.1.15</td>
                <td>45 minutes</td>
              </tr>

              <tr>
                <td>#U1002</td>
                <td>File Upload</td>
                <td>2025-03-19 09:20:43</td>
                <td>Success</td>
                <td>User</td>
                <td>192.168.1.18</td>
                <td>30 minutes</td>
              </tr>

              <tr>
                <td>#U1003</td>
                <td>Password Change</td>
                <td>2025-03-19 09:55:11</td>
                <td>Failed</td>
                <td>Admin</td>
                <td>192.168.1.22</td>
                <td>15 minutes</td>
              </tr>
            </tbody>
            <tfoot>
              <tr>
                <td colspan="7" class="total">
                  <strong>Total Records: 3</strong>
                </td>
              </tr>
            </tfoot>
          </table>

          <div class="d-flex justify-content-between mb-2">
            <div>
              <a class="btn btn-info" href="#">1</a>
              <a class="btn btn-outline-info" href="#">2</a>
            </div>
            <div>
              <button class="btn btn-primary">
                <i class="fas fa-print"></i> Print
              </button>
              <button class="btn btn-success">
                <i class="fas fa-file-excel"></i> Excel
              </button>
            </div>
          </div>
        </div>

        <div class="table-container overflow-auto table-light-shadow">
          <div class="search-container">
            <form method="post" class="d-flex">
              <input
                type="text"
                class="form-control"
                placeholder="Search item..."
              />
              <button class="btn btn-success" type="submit">
                <i class="fas fa-search"></i>
              </button>
            </form>
          </div>

          <table class="table table-striped table-bordered">
            <thead>
              <tr>
                <th scope="col">ITEM</th>
                <th scope="col">QUANTITY</th>
                <th scope="col">PRICE</th>
                <th scope="col">AMOUNT</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Consultation Report</td>
                <td>3 reports</td>
                <td>$150.00</td>
                <td>$450.00</td>
              </tr>
              <tr>
                <td>Software License</td>
                <td>2 licenses</td>
                <td>$300.00</td>
                <td>$600.00</td>
              </tr>
              <tr>
                <td>Cloud Hosting Plan (6 Months)</td>
                <td>1 subscription</td>
                <td>$500.00</td>
                <td>$500.00</td>
              </tr>
              <tr>
                <td>Marketing Campaign (3 Weeks)</td>
                <td>2 campaigns</td>
                <td>$1,000.00</td>
                <td>$2,000.00</td>
              </tr>
              <tr>
                <td>Custom Website Design</td>
                <td>1 project</td>
                <td>$2,500.00</td>
                <td>$2,500.00</td>
              </tr>
              <tr>
                <td>Cybersecurity Audit</td>
                <td>1 audit</td>
                <td>$800.00</td>
                <td>$800.00</td>
              </tr>
            </tbody>
            <tfoot>
              <tr>
                <td colspan="4" class="total">
                  <strong>Total Amount: $6,850.00</strong>
                </td>
              </tr>
            </tfoot>
          </table>
          <a class="btn btn-info" href="#">1</a>
          <a class="btn btn-outline-info" href="#">2</a>
        </div>

        <div class="three-line-charts-wrapper">
          <div class="single-line-box">
            <canvas id="chart1"></canvas>
          </div>
          <div class="single-line-box">
            <canvas id="chart2"></canvas>
          </div>
          <div class="single-line-box">
            <canvas id="chart3"></canvas>
          </div>
        </div>

        <div class="three-pie-charts-wrapper">
          <div class="single-pie-box">
            <canvas id="pieChartA"></canvas>
          </div>
          <div class="single-pie-box">
            <canvas id="pieChartB"></canvas>
          </div>
          <div class="single-pie-box">
            <canvas id="pieChartC"></canvas>
          </div>
        </div>

        <h1>Live data</h1>
        <hr />
        <div class="three-bar-charts-wrapper">
          <div class="single-bar-box">
            <canvas id="barChartA"></canvas>
          </div>
          <div class="single-bar-box">
            <canvas id="barChartB"></canvas>
          </div>
          <div class="single-bar-box">
            <canvas id="barChartC"></canvas>
          </div>
        </div>

        <div class="content-header">
          <h1>Profile Overview</h1>
          <p class="invoice-meta">User: <strong>John Doe</strong></p>
        </div>

        <div class="profile-container">
          <div class="profile-left-panel">
            <div class="profile-user">
              <img
                src="{{ url_for('static', filename='media/Image/s3.png')}}"
                alt="User"
                width="60"
                height="60"
              />
              <h2 class="profile-name">John Doe</h2>
              <p class="profile-email">john.doe@example.com</p>
              <p class="profile-phone">123-123-555</p>
            </div>
            <hr />
            <ul class="profile-menu">
              <li>
                <a id="profile-overview-link" class="active-link"
                  >Profile Overview</a
                >
              </li>
              <li><a id="edit-profile-link">Edit Profile</a></li>
              <li><a id="create-account-link">Create Account</a></li>
              <li><a id="password-reset-link">Password Reset</a></li>
            </ul>
          </div>

          <div id="profile-overview" class="content-section active-section">
            <h3>About Me</h3>
            <div class="profile-details">
              <p><strong>Full Name:</strong> John Doe</p>
              <p><strong>Address:</strong> Redmond, Washington</p>
              <p><strong>Zip Code:</strong> 98052</p>
              <p><strong>Phone:</strong> 123-123-555</p>
              <p><strong>Email:</strong> john.doe@example.com</p>
            </div>
          </div>

          <div id="edit-profile" class="content-section">
            <h3>Edit Profile</h3>
            <form>
              <div class="form-group">
                <label for="fullName">Full Name</label>
                <input
                  type="text"
                  id="fullName"
                  class="form-control"
                  value="John Doe"
                />
              </div>
              <div class="form-group">
                <label for="contactPhone">Contact Phone</label>
                <input
                  type="text"
                  id="contactPhone"
                  class="form-control"
                  value="123-123-555"
                />
              </div>
              <div class="form-group">
                <label for="email">Email (read-only)</label>
                <input
                  type="email"
                  id="email"
                  class="form-control"
                  value="john.doe@example.com"
                  readonly
                />
              </div>
              <div class="form-group">
                <label for="address">Address</label>
                <input
                  type="text"
                  id="address"
                  class="form-control"
                  value="Redmond, Washington"
                />
              </div>
              <div class="form-group">
                <label for="city">City</label>
                <input
                  type="text"
                  id="city"
                  class="form-control"
                  value="Redmond"
                />
              </div>
              <div class="form-group">
                <label for="zipCode">Zip Code</label>
                <input
                  type="text"
                  id="zipCode"
                  class="form-control"
                  value="98052"
                />
              </div>
              <div class="form-group">
                <label for="country">Country</label>
                <input
                  type="text"
                  id="country"
                  class="form-control"
                  value="USA"
                />
              </div>
              <button type="submit" class="btn btn-success">
                Update Profile
              </button>
            </form>
          </div>

          <div id="create-account" class="content-section">
            <h3>Create New User</h3>
            <form action="#">
              <div class="form-group">
                <label for="fullName">Full Name</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter full name"
                />
              </div>
              <div class="form-group">
                <label for="email">Email</label>
                <input
                  type="email"
                  class="form-control"
                  placeholder="user@example.com"
                />
              </div>
              <div class="form-group">
                <label for="phone">Phone</label>
                <input
                  type="text"
                  id="phone"
                  class="form-control"
                  placeholder="123-123-555"
                />
              </div>
              <div class="form-group">
                <label for="password">Password</label>
                <input
                  type="password"
                  class="form-control"
                  placeholder="Enter password"
                />
              </div>
              <div class="form-group">
                <label for="confirmPass">Confirm Password</label>
                <input
                  type="password"
                  class="form-control"
                  placeholder="Re-enter password"
                />
              </div>
              <button type="submit" class="btn btn-success">Create User</button>
            </form>
          </div>

          <div id="password-reset" class="content-section">
            <h3>Password Reset</h3>
            <form>
              <div class="form-group">
                <label for="currentPass">Current Password <span>*</span></label>
                <input
                  type="password"
                  id="currentPass"
                  class="form-control"
                  placeholder="Enter your current password"
                />
              </div>
              <div class="form-group">
                <label for="newPass">New Password <span>*</span></label>
                <input
                  type="password"
                  id="newPass"
                  class="form-control"
                  placeholder="Enter new password"
                />
              </div>
              <div class="form-group">
                <label for="confirmPass">Confirm Password <span>*</span></label>
                <input
                  type="password"
                  id="confirmPass"
                  class="form-control"
                  placeholder="Enter new password again"
                />
              </div>
              <button type="submit" class="btn btn-success">
                Change Password
              </button>
              <button type="reset" class="btn btn-secondary">Clear</button>
            </form>
          </div>
        </div>
        <button id="scrollTopBtn" title="Go to top">&#8679;</button>
      </div>
    </div>
    <!-- Include the flash message section here -->
    {% include 'flash_message.html' %}

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="{{ url_for('static', filename='js/dashboard.js') }}"></script>
    <script src="{{ url_for('static', filename='js/flash_remove_dom.js') }}"></script>
  </body>
</html>
"""


BAD_REQUESTS_HTML = """
{% extends "base.html" %} {% block head %}
<title>{% block title %}Bad Request{% endblock title %}</title>

<link rel="stylesheet" href="{{ url_for('static', filename='css/400.css')}}" />
{% endblock head %} {% block body %} {% block content %}

<div class="container">
  <div class="glitch" id="glitch-text">
    <h1>400</h1>
    <h2>Bad Request</h2>
    <p>Sorry, your request couldn't be processed.</p>
    <button id="go-back-btn">Go Back</button>
  </div>
</div>

{% endblock content %}
<script src="{{ url_for('static', filename='js/error_pages_all.js')}}"></script>
{% endblock body %}
"""


CONTENT_TOO_LARGE_HTML = """
{% extends "base.html" %} {% block head %}
<title>{% block title %}File Too Large{% endblock title %}</title>

<link rel="stylesheet" href="{{ url_for('static', filename='css/413.css')}}" />
{% endblock head %} {% block body %} {% block content %}

<div class="container">
  <div class="file-icon">
    <div class="file">
      <div class="fold"></div>
    </div>
    <div class="exceed-text">TOO LARGE</div>
  </div>
  <h1>413</h1>
  <h2>Payload Too Large</h2>
  <p>The file or request data you tried to upload exceeds the allowed limit.</p>
  <button id="go-back-btn">Go Back</button>
</div>

{% endblock content %}
<script src="{{ url_for('static', filename='js/error_pages_all.js')}}"></script>
{% endblock body %}
"""


FORBIDDEN_HTML = """
{% extends "base.html" %} {% block head %}
<title>{% block title %}Forbidden{% endblock title %}</title>

<link rel="stylesheet" href="{{ url_for('static', filename='css/403.css')}}" />
{% endblock head %} {% block body %} {% block content %}

<div class="container">
  <div class="stop-icon">
    <div class="stop-sign">
      <span>403</span>
    </div>
  </div>
  <h2>Forbidden</h2>
  <p>You don't have permission to access this page.</p>
  <button id="go-back-btn">Go Back</button>
</div>

{% endblock content %}
<script src="{{ url_for('static', filename='js/error_pages_all.js')}}"></script>
{% endblock body %}
"""


INTERNAL_SERVER_HTML = """
{% extends "base.html" %} {% block head %}
<title>{% block title %}Internal Server Error{% endblock title %}</title>
<link rel="stylesheet" href="{{ url_for('static', filename='css/500.css')}}" />
{% endblock head %} {% block body %}

<!--  -->
{% block content %}
<div class="container">
  <div class="glitch-error">
    <h1>500</h1>
    <h2>Internal Server Error</h2>
    <p>Something went wrong on our end. Please try again later.</p>
    <button id="server_refresh-btn">Retry</button>
  </div>
  <div class="glitch-background"></div>
</div>

{% endblock content %}
<script src="{{ url_for('static', filename='js/error_pages_all.js')}}"></script>
{% endblock body %}

"""


MAINTAINANCE_HTML = """
{% extends "base.html" %} {% block head %}
<title>{% block title %}503 Service Unavailable{% endblock title %}</title>
<link rel="stylesheet" href="{{ url_for('static', filename='css/503.css')}}" />
{% endblock head %}

<!--  -->
{% block body %} {% block content %}
<div class="container">
  <div class="gear-icon">
    <div class="gear"></div>
  </div>
  <h1>503</h1>
  <h2>Service Unavailable</h2>
  <p>
    Our service is temporarily unavailable. We're working on it and will be back
    soon!
  </p>
  <button id="main-reload-btn">Try Again</button>
</div>

{% endblock content %}
<script src="{{ url_for('static', filename='js/maintainance.js')}}"></script>
{% endblock body %}
"""


NOT_FOUND_HTML = """
<!-- This is the not_found.html template -->

{% extends "base.html" %} {% block head %}
<title>{% block title %}404 Page Not Found{% endblock title %}</title>

<link rel="stylesheet" href="{{ url_for('static', filename='css/404.css')}}" />
{% endblock head %} {% block body %} {% block content %}

<div class="container">
  <div class="error">
    <h1>404</h1>
    <p>Oops! The page you're looking for doesn't exist.</p>
    <button id="go-back-btn">Go Back</button>
  </div>
  <div class="stars"></div>
</div>

{% endblock content %}
<script src="{{ url_for('static', filename='js/notfound.js')}}"></script>
{% endblock body %}
"""


TOO_MANAY_REQUEST_HTML = """
{% extends "base.html" %} {% block head %}
<title>{% block title %}Too Many Requests{% endblock title %}</title>

<link rel="stylesheet" href="{{ url_for('static', filename='css/429.css')}}" />
{% endblock head %} {% block body %} {% block content %}

<div class="container">
  <div class="error-message">
    <h1>429</h1>
    <h2>Too Many Requests</h2>
    <p>You've sent too many requests in a short time. Please wait.</p>
    <div class="timer">
      <span id="countdown">10</span>
      <p>seconds remaining</p>
    </div>
    <button id="retry-btn">Retry</button>
    <!-- Assign an id to the button -->
  </div>
</div>

{% endblock content %}
<script src="{{ url_for('static', filename='js/error_pages_all.js')}}"></script>
{% endblock body %}
"""


UNAUTHORIZED_HTML = """
{% extends "base.html" %} {% block head %}
<title>{% block title %}Unauthorized{% endblock title %}</title>

<link rel="stylesheet" href="{{ url_for('static', filename='css/401.css')}}" />
{% endblock head %} {% block body %} {% block content %}

<div class="container">
  <div class="lock-icon">
    <div class="lock-body"></div>
    <div class="lock-shackle"></div>
  </div>
  <h1>401</h1>
  <h2>Unauthorized</h2>
  <p>Oops! You don't have permission to access this page.</p>
  <button id="go-back-btn">Go Back</button>
</div>

{% endblock content %}
<script src="{{ url_for('static', filename='js/error_pages_all.js')}}"></script>
{% endblock body %}
"""
