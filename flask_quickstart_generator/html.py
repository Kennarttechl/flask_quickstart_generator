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
{% extends "update_account.html" %}

<title>{% block title %}Create Account{% endblock title %}</title>
<!--  -->
{% block user_profile %} {% endblock user_profile %}
<!--  -->
{% block password %} {% endblock password %}

<!--  -->
{% block form %}
<div id="create" class="form-container">
  <h4 class="text-danger">Create New User</h4>
  <form method="post">
    {{ form.hidden_tag() }}
    <div class="mb-3">{{ form.username(class="form-control mb-3")}}</div>
    <!--  -->
    <div class="mb-3">{{ form.email(class="form-control mb-3")}}</div>
    <!--  -->
    <div class="mb-3">{{ form.password(class="form-control mb-3")}}</div>
    <!--  -->
    <div class="mb-3">
      {{ form.confirm_password(class="form-control mb-3")}}
    </div>
    <!--  -->
    <div class="mb-3">{{ form.user_role(class="form-control mb-3")}}</div>
    <!--  -->
    <button type="submit" class="btn btn-success">Create User</button>
  </form>
</div>
{% endblock form %}
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

    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/flash.css') }}"
    />
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
      <!-- Include the flash message section here -->
      {% include 'flash_message.html' %}
    </div>

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

    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/flash.css') }}"
    />
  </head>
  <body>
    {% block top_navbar %}
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
        <img src="{{ image_file }}" alt="User" />
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
              <a href="{{ url_for('super_admin_secure.user_logout')}}">
                <i class="fas fa-sign-out-alt"></i> Logout
              </a>
            </li>
          </ul>
        </div>
      </div>
    </header>
    {% endblock top_navbar %}

    <div class="main-section">
      {% block sidebar %}
      <aside class="sidebar">
        <div class="logo">
          <i class="fas fa-tachometer-alt"></i>
          Flask Administration
        </div>
        <hr />
        <ul class="nav-menu">
          <li>
            <a
              href="{{ url_for('super_admin_secure.secure_adashboard')}}"
              class="active"
            >
              <i class="fas fa-home"></i> Dashboard
            </a>
          </li>

          <li class="has-submenu">
            {% block access_control %}
            <a href="#!">
              <i class="fas fa-file-invoice"></i>
              Access Control
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li>
                <a href="{{ url_for('super_admin_secure.add_role')}}"
                  >User Roles</a
                >
              </li>
              <li><a href="#!">Permissions</a></li>
              <li><a href="#!">Security Settings</a></li>
            </ul>
            {% endblock access_control %}
          </li>

          <li class="has-submenu">
            {% block admin_tools %}
            <a href="#!">
              <i class="fas fa-user-tie"></i> Admin Tools
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">User Management</a></li>
              <li><a href="#!">Activity Logs</a></li>
              <li><a href="#!">System Settings</a></li>
            </ul>
            {% endblock admin_tools %}
          </li>

          <li class="has-submenu">
            {% block user_account %}
            <a href="#!">
              <i class="fas fa-users"></i>
              User Accounts
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li>
                <a href="{{ url_for('account_.secure_account_update')}}"
                  >Edit Profile</a
                >
              </li>
              <li>
                <a href="{{ url_for('authent_.secure_register')}}"
                  >Create Account</a
                >
              </li>
              <li>
                <a href="#">Manage Accounts</a>
              </li>
              <li><a href="#!">Password Reset</a></li>
              <li><a href="#!">Account Activation</a></li>
            </ul>
            {% endblock user_account %}
          </li>

          <li class="has-submenu">
            {% block report_analitics %}
            <a href="#!">
              <i class="fas fa-chart-line"></i>
              Reports & Anlyt
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">Search Report</a></li>
              <li><a href="#!">User Activity</a></li>
              <li><a href="#!">Performance Met</a></li>
            </ul>
            {% endblock report_analitics %}
          </li>

          <li class="has-submenu">
            {% block system_health %}
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
            {% endblock system_health %}
          </li>

          <li class="has-submenu">
            {% block database_mgt %}
            <a href="#!">
              <i class="fas fa-database"></i>
              Database Mgt
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">Backup Database</a></li>
              <li><a href="#!">View Tables</a></li>
            </ul>
            {% endblock database_mgt %}
          </li>

          <li class="has-submenu">
            {% block notification %}
            <a href="#!">
              <i class="fas fa-bell"></i>
              Notifications
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">View Alerts</a></li>
              <li><a href="#!">Set Up Alerts</a></li>
            </ul>
            {% endblock notification %}
          </li>

          <li class="has-submenu">
            {% block api_mgt %}
            <a href="#!">
              <i class="fas fa-code"></i>
              API Mgt
              <i class="fas fa-chevron-right arrow"></i>
            </a>
            <ul class="submenu">
              <li><a href="#!">Admin</a></li>
              <li><a href="#!">Super Admin</a></li>
            </ul>
            {% endblock api_mgt %}
          </li>

          <li>
            {% block settings %}
            <a href="#!"> <i class="fas fa-user-cog"></i> Settings </a>
            {% endblock settings %}
          </li>
        </ul>
      </aside>
      {% endblock sidebar %}

      <div class="main-content">
        {% block content_header %}
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
        {% endblock content_header %} {% block dashboard_container %}
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
        {% endblock dashboard_container %} {% block table_container %}
        <div class="table-container overflow-auto">
          <h3 class="main--title">Admin Activity Logs</h3>
          <hr />
          <div class="search-container">
            {% block search %}
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
            {% endblock search%}
          </div>

          <table class="table table-striped table-bordered">
            {% block table %}
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
            {% endblock table %}
          </table>

          <div class="d-flex justify-content-between mb-2">
            {% block table_footer %}
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
            {% endblock table_footer %}
          </div>
        </div>
        {% endblock table_container %} {% block bottom_table %}
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
        {% endblock bottom_table %} {% block line_charts %}
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
        {% endblock line_charts %} {% block pie_charts %}
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
        {% endblock pie_charts %} {% block bar_charts %}
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
        {% endblock bar_charts %} {% block profile_overview %}
        <div class="content-header">
          <h1>Profile Overview</h1>
          <p class="invoice-meta">User: <strong>John Doe</strong></p>
        </div>
        {% endblock profile_overview %}

        <div class="profile-container">
          {% block profile_container %}
          <div class="profile-left-panel">
            {% block left_pannel %}
            <div class="profile-user">
              <img src="{{ image_file }}" alt="User" width="80" height="80" />
              <h2 class="profile-name">{{ current_user.username }}</h2>
              <p class="profile-email">{{ current_user.email }}</p>
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
            {% endblock left_pannel %}
          </div>

          <div id="profile-overview" class="content-section active-section">
            {% block user_profile_overview %}
            <h3>About Me</h3>
            <div class="profile-details">
              <p><strong>Full Name:</strong> {{ current_user.username }}</p>
              <p><strong>Phone:</strong> 123-123-555</p>
              <p><strong>Email:</strong> {{ current_user.email }}</p>
            </div>
            {% endblock user_profile_overview %}
          </div>

          <div id="edit-profile" class="content-section">
            {% block edit_form_field %}
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
            {% endblock edit_form_field %}
          </div>

          <div id="create-account" class="content-section">
            {% block create_new_user %}
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
            {% endblock create_new_user %}
          </div>

          <div id="password-reset" class="content-section">
            {% block reset_password %}
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
            {% endblock reset_password %}
          </div>
          {% endblock profile_container %}
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
<script src="{{ url_for('static', filename='js/too_many.js')}}"></script>
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


ACCOUNT_SETTING_FORM_HTML =\
"""
{% extends "base.html" %}
<head>
  {% block head %}
  <title>{% block title %}Account Update{% endblock title %}</title>

  <link
    rel="stylesheet"
    href="{{ url_for('static', filename='css/account.css')}}"
  />

  <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    rel="stylesheet"
  />
  {% endblock head %}
</head>

{% block body %} {% block content %}
<div class="page-wrapper">
  <div class="container">
    <nav class="sidebar shadow-sm">
      <div class="text-center">
        <img src="{{ image_file }}" alt="Profile" class="profile-img" />
        <h3 class="mt-2">{{ current_user.username }}</h3>
        <p>{{ current_user.email }}</p>
        <p>123-123-555</p>
      </div>
      <hr />
      <ul class="nav flex-column">
        <li class="nav-item">
          <a class="nav-link" id="profileLink">Profile Overview</a>
        </li>
        {% block account %}
        <li class="nav-item">
          <a class="nav-link" id="createLink">Create Account</a>
        </li>
        {% endblock account %}
        <!--  -->
        {% block password %}
        <li class="nav-item">
          <a class="nav-link" id="resetLink">Password Reset</a>
        </li>
        {% endblock password %}
        <li class="nav-item">
          <strong
            ><a
              class="nav-link"
              href="{{ url_for('super_admin_secure.secure_adashboard')}}"
              >Back to Dashboard</a
            ></strong
          >
        </li>
      </ul>
    </nav>

    <!-- Main Content -->
    <main class="content-area">
      <div id="profile" class="profile-container">
        <h4 class="text-danger">Profile Overview</h4>
        <p><strong>Name:</strong> {{ current_user.username }}</p>
        <p><strong>Email:</strong> {{ current_user.email }}</p>
        <p><strong>Phone:</strong> 123-123-555</p>
      </div>

      {% block form %}
      <div id="reset" class="reset-container">
        <h4 class="text-danger">Reset Password</h4>
        <form method="post" enctype="multipart/form-data">
          {{ form.hidden_tag() }}
          <div class="mb-3">{{ form.email(class="form-control mb-3")}}</div>
          <!--  -->
          <div class="mb-3">{{ form.username(class="form-control mb-3")}}</div>
          <!--  -->
          <div class="mb-3">{{ form.password(class="form-control mb-3")}}</div>
          <!--  -->
          <div class="mb-3">
            {{ form.confirm_password(class="form-control mb-3")}}
          </div>
          <!--  -->
          {% if form.username.errors %} {% for error in form.username.errors %}
          <span class="text-danger">{{ error }}</span>
          {% endfor %} {% endif %}
          <!--  -->
          {% block user_profile %}
          <div class="form-group">
            {{ form.picture(class='form-control mb-3')}} {% if
            form.picture.errors %} {% for error in form.picture.errors %}
            <span class="text-danger">{{ error }}</span>
            {% endfor %} {% endif %}
          </div>
          {% endblock user_profile %}
          <button type="submit" class="btn btn-warning">Reset Password</button>
        </form>
      </div>
      {% endblock form %}
    </main>
  </div>
  <!-- Include the flash message section here -->
  {% include 'flash_message.html' %}
</div>
{% endblock content %}
<script src="{{ url_for('static', filename='js/account.js')}}"></script>
{% endblock body %}
"""


PROFILE_UPDATE_HTML =\
"""

{% extends "sadashboard_secure.html" %} 


{% block top_navbar %}
{{ super() }}
{% endblock top_navbar %}
<!--  -->
{% block sidebar %}
{{ super() }}
{% endblock sidebar %}
<!--  -->
{% block access_control %}
{{ super() }}
{% endblock access_control %}
<!--  -->
{% block admin_tools %}
{{ super() }}
{% endblock admin_tools %}
<!--  -->
{% block user_account %}
{{ super() }}
{% endblock user_account %}
<!--  -->
{% block report_analitics %}
{{ super() }}
{% endblock report_analitics %}
<!--  -->
{% block system_health %}
{{ super() }}
{% endblock system_health %}
<!--  -->
{% block database_mgt %}
{{ super() }}
{% endblock database_mgt %}
<!--  -->
{% block notification %}
{{ super() }}
{% endblock notification %}
<!--  -->
{% block api_mgt %}
{{ super() }}
{% endblock api_mgt %}
<!--  -->
{% block settings %}
{{ super() }}
{% endblock settings %}
<!--  -->
{% block content_header %}

{% endblock content_header %}
<!--  -->
{% block dashboard_container %}

{% endblock dashboard_container %}
<!--  -->
{% block table_container %}

{% endblock table_container %}
<!--  -->
{% block search %}

{% endblock search%}
<!--  -->
{% block table %}

{% endblock table %}
<!--  -->
{% block table_footer %}

{% endblock table_footer %}
<!--  -->
{% block bottom_table %}

{% endblock bottom_table %}
<!--  -->
{% block line_charts %}
{{ super()}}
{% endblock line_charts %}
<!--  -->
{% block pie_charts %}
{{ super()}}
{% endblock pie_charts %}
<!--  -->
{% block bar_charts %}
{{ super()}}
{% endblock bar_charts %}
<!--  -->
{% block profile_overview %}
{{ super() }}
{% endblock profile_overview %}
<!--  -->
{% block profile_container %}
{{ super() }}
{% endblock profile_container %}
<!--  -->
{% block left_pannel %}
{{ super() }}
{% endblock left_pannel %}
<!--  -->
{% block user_profile_overview %}
{{ super() }}
{% endblock user_profile_overview %}
<!--  -->
{% block edit_form_field %}
{{ super() }}
{% endblock edit_form_field %}
<!--  -->
{% block create_new_user %}
{{ super() }}
{% endblock create_new_user %}
<!--  -->
{% block reset_password %}
{{ super() }}
{% endblock reset_password %}
"""


VIEW_HTML =\
  """
{% extends "base.html" %} 

{% block head %}
<title>{% block title %}Flask QuickStart{% endblock title %}</title>

<link rel="stylesheet" href="{{ url_for('static', filename='css/view.css')}}" />

{% endblock head %} {% block body %} {% block content %}

<body>
  <div class="container">
    <p>Run your application and click on the link below:</p>
    <a href="http://127.0.0.1:5000/superlogin" target="_blank">Login Here</a>
    <p><strong>Default Email:</strong> admin@example.com</p>
    <p><strong>Default Username:</strong> admin</p>
    <p><strong>Default Password:</strong> adminpass</p>
  </div>
</body>

{% endblock content %}
<!-- <script src="Your js scripts path here "></script> -->
{% endblock body %}
"""


USER_ROLE_HTML =\
  """ 
{% extends "signup.html" %}

<title>{% block title %}User Role{% endblock title %}</title>
<!--  -->
{% block user_profile %} {% endblock user_profile %}
<!--  -->
{% block password %} {% endblock password %}

{% block account %}
<li class="nav-item">
    <a class="nav-link" id="createLink">Add User Role</a>
  </li>
{% endblock account %}

<!--  -->
{% block form %}
<div id="create" class="form-container">
  <h4 class="text-danger">User Role/ID</h4>
  <form method="post">
    {{ form.hidden_tag() }}
    <!--  -->
    <div class="mb-3">{{ form.role_name(class="form-control mb-3")}}</div>
    <!--  -->
    <button type="submit" class="btn btn-success">Add Role</button>
  </form>
</div>
{% endblock form %}
"""