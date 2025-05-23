LOG_CSS =\
""" 
 
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
/* Montserrat */
body,
html {
  height: 100%;
  font-family: Arial, sans-serif;
}

h2 {
  font-size: 35px;
}

.container-fluid {
  display: flex;
  height: 100vh;
  padding: 0;
}

.left {
  flex: 1;
  background: url("https://images.pexels.com/photos/450035/pexels-photo-450035.jpeg")
    no-repeat center center;
  background-size: cover;
  min-height: 100vh;
  height: auto;
}

.right {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f9f9f9;
  flex-direction: column;
  text-align: center;
  padding: 3px;
}

.right form {
  width: 80%;
  max-width: 400px;
  margin: 0;
}

input {
  margin-bottom: 15px; /* Adjust the space between the input field*/
  width: 100%;
  min-height: 2.6rem; /* Adjust the input field height*/
}

@media screen and (max-width: 1024px) {
  .container-fluid {
    flex-direction: column;
  }

  .left,
  .right {
    flex: 1 1 50%;
  }
}

@media only screen and (min-width: 768px) and (max-width: 810px) {
  .container-fluid {
    flex-direction: column;
  }

  .left {
    height: 40vh;
    background-position: top;
    order: 1;
  }

  .right {
    height: auto;
    padding: 100px;
    justify-content: flex-start;
    align-items: center;
    min-height: 80vh;
  }

  .right form {
    width: 150%;
  }
}

@media screen and (max-width: 375px) {
  .container-fluid {
    flex-direction: column;
  }

  .left {
    min-height: 50vh;
    background-position: center;
    order: 1;
  }

  .right {
    justify-content: center;
    align-items: center;
    padding-top: 2rem;
    min-height: 60vh;
  }

  .right h2 {
    font-size: 20px;
  }

  .right form {
    width: 95%;
  }

  input {
    min-height: 2.5rem;
  }
}

/* Dark Mode styles */
.dark-mode {
  /* background: #242435; */
  background-color: #2f3d40;
  color: white;
}

.dark-mode .right {
  background-color: #2f3d40;
  /* background: #242435; */
  color: white;
}

.dark-mode h2,
.dark-mode p {
  color: white;
}

/* Toggle Switch */
.toggle-switch {
  position: fixed;
  top: 30px;
  right: 30px;
  display: flex;
  align-items: center;
  cursor: pointer;
  z-index: 1000;
}

.toggle-switch input {
  display: none;
}

.slider {
  width: 50px;
  height: 25px;
  background: #44f378;
  border-radius: 25px;
  position: relative;
  transition: background 0.3s;
}

.slider:before {
  content: "";
  position: absolute;
  width: 20px;
  height: 20px;
  background: white;
  border-radius: 50%;
  top: 50%;
  left: 4px;
  transform: translateY(-50%);
  transition: left 0.3s;
}

input:checked + .slider {
  background: #007bff;
}

input:checked + .slider:before {
  left: 26px;
}
"""

SADASHBOARD_CSS =\
""" 
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

body {
  background-color: #f5f9f9;
  color: #333;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  transition: background-color 0.3s, color 0.3s;
}

/* Top bar & sidebar toggle section (fixed full width) */
.topbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 60px;
  background-color: #ffffff;
  border-bottom: 1px solid #e0e0e0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1.5rem;
  z-index: 200;
  transition: background-color 0.3s, border-color 0.3s;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.topbar-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.toggle-sidebar {
  cursor: pointer;
  font-size: 1.2rem;
  color: #999;
  transition: color 0.3s;
}

.toggle-sidebar:hover {
  color: #666;
}
/* End top bar & Sidebar toggle */

/* Top bar search input section */
.input-group {
  margin-bottom: 2px;
}

.input-group .form-control {
  width: 100%;
  max-width: 192px;
}

.input-group form {
  display: flex;
}

.input-group input {
  flex: 1;
  width: 2px;
  margin-right: 5px;
}

.input-group button {
  width: 40px;
  padding: 0;
  display: flex;
  color: #ffffff;
  justify-content: center;
  align-items: center;
}
/* End top bar search input section */

/* Table search section */
.search-container {
  margin-bottom: 20px;
}

.search-container .form-control {
  width: 100%;
  max-width: 300px;
}

.search-container form {
  display: flex;
}

.search-container input {
  flex: 1;
  margin-right: 5px;
}
/* End table search section */

/* Top bar user profile & dropdown menu section */
.user-profile {
  display: flex;
  align-items: center;
  position: relative;
  cursor: pointer;
  gap: 0.5rem;
}

.user-profile img {
  width: 35px;
  height: 35px;
  border-radius: 50%;
  object-fit: cover;
}

.user-profile span {
  font-weight: 500;
  color: #333;
  transition: color 0.3s;
}

.user-profile i {
  color: #888;
  transition: transform 0.3s;
}

.dropdown-menu {
  position: absolute;
  top: 130%;
  right: 0;
  background-color: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: none;
  min-width: 150px;
  z-index: 99;
  transition: background-color 0.3s, border-color 0.3s;
}

.dropdown-menu ul {
  list-style: none;
  margin: 0;
  padding: 0.5rem 0;
}

.dropdown-menu ul li {
  padding: 0.5rem 1rem;
}

.dropdown-menu ul li a {
  color: #333;
  text-decoration: none;
  display: block;
  transition: background 0.3s, color 0.3s;
}

.dropdown-menu ul li:hover {
  background-color: #f0f0f0;
}

.user-profile.open .dropdown-menu {
  display: block;
}

.user-profile.open i {
  transform: rotate(180deg);
}

.user-profile i {
  transform: none !important;
  -webkit-transform: none !important;
}
/* End top bar user profile & dropdown menu section */

/* Main section & sidebar section */
.main-section {
  flex: 1;
  display: flex;
  transition: margin-left 0.3s ease;
  margin-top: 60px;
  margin-left: 250px;
}

.main-section.sidebar-closed {
  margin-left: 0;
}

/* Sidebar section */
.sidebar {
  position: fixed;
  top: 60px;
  left: 0;
  bottom: 0;
  width: 250px;
  background-color: #ffffff;
  border-right: 1px solid #e0e0e0;
  padding: 1rem;
  overflow-y: auto;
  transition: transform 0.3s ease, background-color 0.3s, border-color 0.3s;
  z-index: 150;
}

/* Override Bootstrap for Sidebar */
.sidebar .nav-menu {
  margin: 0 !important;
  padding: 0 !important;
  list-style: none !important;
}

.sidebar .nav-menu li {
  margin: 0 !important;
  padding: 0 !important;
}

@font-face {
  font-family: "tech";
  src: url("../fonts/EBGaramond-Medium.woff") format("woff2"),
    url("../fonts/EBGaramond-Medium.woff") format("woff");
  font-style: normal;
}

.sidebar .nav-menu li a {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: #333;
  padding: 0.5rem 0.75rem;
  border-radius: 5px;
  transition: background-color 0.3s;
  transition: left 0.7s ease;
  font-family: tech;
  font-size: 1.2rem;
  letter-spacing: 0.2px;
}

.sidebar.closed {
  transform: translateX(-100%);
}

.logo {
  font-size: 1.1rem;
  font-weight: 600;
  color: #0fb690;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  transition: color 0.3s;
}

.logo i {
  margin-right: 0.5rem;
}

.nav-menu {
  list-style: none;
  margin-top: 1rem;
}

.nav-menu li {
  margin-bottom: 0.5rem;
}

.nav-menu li a {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: #333;
  padding: 0.5rem 0.75rem;
  border-radius: 5px;
  transition: background-color 0.3s, color 0.3s;
}

.nav-menu li a:hover {
  background-color: #f0f0f0;
}

.nav-menu li a.active {
  background-color: #dff0eb;
  color: #0fb690;
  font-weight: 500;
}

.nav-menu li a i {
  margin-right: 0.5rem;
}

/* Sidebar submenu style section*/
.has-submenu > a {
  position: relative;
  justify-content: space-between;
  align-items: center;
}
.has-submenu > a .arrow {
  font-size: 0.8rem;
  margin-left: auto;
  transition: transform 0.3s;
}
.submenu {
  display: none;
  margin-left: 1.5rem;
}
.submenu li a {
  font-size: 0.9rem;
}
.has-submenu.open .submenu {
  display: block;
}
.has-submenu.open .arrow {
  transform: rotate(90deg);
}
/* End Main section & sidebar section */

/* Main content section */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 1rem;
  background-color: #d5e7e2;
  overflow-y: auto;
  transition: background-color 0.3s, color 0.3s;
}
/* End main content section */

/* Content head section */
.content-header {
  padding: 1.5rem 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  transition: color 0.3s;
}
.content-header h1 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.content-header .invoice-meta {
  font-size: 0.9rem;
  color: #666;
}
.invoice-info {
  text-align: right;
}
.invoice-info p {
  margin: 0.25rem 0;
}
/* End content head section */

/* Dashboard Cards*/
.dashboard-container {
  display: grid;
  margin-bottom: 25px;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.dashboard-box {
  padding: 20px;
  border-radius: 8px;
  color: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.dashboard-box:nth-child(1) {
  background-color: #53736a; /* Light Blue */
}

.dashboard-box:nth-child(2) {
  background-color: #37b24d; /* Green */
}

.dashboard-box:nth-child(3) {
  background-color: #3d3d3d; /* Orange */
}

.dashboard-box:nth-child(4) {
  background-color: #506266; /* Red */
}

.dashboard-box:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

.dashboard-box h2 {
  font-size: 1.2rem;
  margin-bottom: 10px;
}

.dashboard-box p {
  font-size: 1.5rem;
  font-weight: bold;
  margin: 5px 0;
}

.dashboard-box .subtext {
  font-size: 0.9rem;
  opacity: 0.8;
}
/* End dashboard cards*/

/* Table container section */
.table-container {
  padding: 1rem;
  background-color: #fff;
  border-radius: 6px;
  transition: background-color 0.3s, color 0.3s;
}

/* Light white shadow for the table */
.table-light-shadow {
  box-shadow: 0 4px 8px rgba(255, 255, 255, 0.2);
}

h3 {
  font-size: 18px;
  color: #ec530c;
}

h1 {
  font-size: 18px;
  color: #ec530c !important;
}

.main--title h4 {
  font-size: 20px;
  color: #0e0000;
}

.table-container {
  width: 100%;
  overflow-x: auto;
}

.table-container {
  width: 100%;
  overflow-x: auto;
  background-color: white;
  padding: 20px;
  margin-bottom: 25px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.main--title {
  text-align: center;
}

.table-container .table {
  width: 100%;
  border-collapse: collapse;
}

.table-container .table th,
.table-container .table td {
  border: 1px solid #ddd;
  padding: 8px;
}

.table-container .table th {
  text-align: left;
  color: white;
  font-size: 13px;
  background-color: #c2c0a6;
}

.table-container .table td a {
  background-color: black;
  text-decoration: none;
}

table {
  width: 100%;
  border-collapse: collapse;
  background-color: #fff;
  border-radius: 2px;
  overflow: hidden;
  transition: background-color 0.3s, color 0.3s;
}

thead {
  background-color: #f0f0f0;
}

thead tr th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  color: #666;
}

tbody tr td {
  padding: 1rem;
  border-bottom: 1px solid #e0e0e0;
  font-size: 1.03rem;
  color: #333;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-weight: 490;
  letter-spacing: 0.5px;
}

tbody tr:last-child td {
  border-bottom: none;
}

/* Line, Pie, Bar charts Section */
.three-line-charts-wrapper {
  display: flex;
  justify-content: space-around;
  align-items: flex-start;
  gap: 2rem;
  margin: 20px 0;
  overflow-x: auto;
}

.single-line-box canvas {
  max-width: 300px;
  max-height: 250px;
}

.single-line-box {
  background-color: #fff;
  border-radius: 5px;
  padding: 1rem;
  flex: 1;
  text-align: center;
  color: #333;
  min-width: 200px;
}

.single-pie-box canvas {
  max-width: 250px;
  max-height: 250px;
}

.three-pie-charts-wrapper {
  display: flex;
  justify-content: space-around;
  align-items: flex-start;
  gap: 2rem;
  margin: 20px 0;
  overflow-x: auto;
}

.single-pie-box {
  background-color: #fff;
  border-radius: 5px;
  padding: 1rem;
  flex: 1;
  text-align: center;
  color: #333;
  min-width: 200px;
}

h1 {
  margin-bottom: 1rem;
  text-align: center;
}

.single-bar-box canvas {
  max-width: 250px;
  max-height: 250px;
}

.three-bar-charts-wrapper {
  display: flex;
  justify-content: space-around;
  align-items: flex-start;
  gap: 2rem;
  margin: 20px 0;
  overflow-x: auto;
}

.single-bar-box {
  background-color: #fff;
  border-radius: 5px;
  padding: 1rem;
  flex: 1;
  text-align: center;
  color: #333;
  min-width: 200px;
}
/* End Line, Pie, Bar charts Section */

/* Container for profile and content sections */
.profile-container {
  display: flex;
  gap: 2rem;
}

.profile-user {
  text-align: center;
  margin-bottom: 1rem;
}

.profile-menu li a {
  text-decoration: none;
  color: #333;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-weight: 640;
}

.profile-left-panel {
  flex: 0 0 250px;
  background-color: #fff;
  padding: 1rem;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Right panel (content sections) styling */
.content-section {
  width: 100%;
  display: none;
  background-color: #fff;
  padding: 1rem;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.content-section {
  display: none;
}
.active-section {
  display: block;
}
.profile-menu li {
  list-style: none;
  padding: 10px 0;
}
.profile-menu li a {
  text-decoration: none;
  cursor: pointer;
}
.profile-menu li a.active-link {
  font-weight: bold;
  color: blue;
}

.form-group {
  margin-bottom: 1rem;
}
.form-group label {
  display: block;
  margin-bottom: 0.25rem;
}
.form-group input {
  width: 100%;
  border: 1px solid #ccc;
}
/* End Container for profile and content sections */

/* Dashboard theme styling */
.dark-theme {
  background-color: #242435;
  color: #fff;
}

.dark-theme .topbar {
  background-color: #242435;
  border-color: #444;
}

.dark-theme .search-container input {
  /*background-color: #333;*/
  color: #fff;
  border-color: #444;
}

.dark-theme .sidebar {
  background-color: #242435;
  border-color: #444;
}

.dark-theme .logo,
.dark-theme .kitchen-name,
.dark-theme .nav-menu li a,
.dark-theme .nav-menu li a i {
  color: #fff;
}

.dark-theme .nav-menu li a:hover {
  background-color: #333;
}

.dark-theme .dropdown-menu {
  background-color: #242435;
  border-color: #444;
}

.dark-theme .dropdown-menu ul li a {
  color: #fff;
}

.dark-theme .main-content,
.dark-theme .table-container,
.dark-theme table {
  background-color: #242435;
  color: #fff;
}

.dark-theme .table-container {
  background-color: #242435;
  color: #fff;
  box-shadow: 0 0 10px rgb(133, 133, 133);
}

.dark-theme thead {
  background-color: #333;
}

.dark-theme .invoice-footer,
.dark-theme .invoice-total {
  background-color: #242435;
  border-color: #444;
}

/* Additional Dark Theme Overrides */
.dark-theme .user-profile span {
  color: #fff !important;
}

.dark-theme .content-header h1,
.dark-theme .content-header .invoice-meta,
.dark-theme .invoice-info p {
  color: #fff !important;
}

.dark-theme table thead tr th,
.dark-theme table tbody tr td {
  color: #fff !important;
}

.dark-theme .nav-menu li a {
  color: #fff !important;
}

/* If you want the icons to also turn white in dark theme: */
.dark-theme .nav-menu li a i,
.dark-theme .user-profile i {
  color: #fff !important;
}

.dark-theme .table,
.dark-theme .table tbody td {
  background-color: #242435 !important;
  color: #fff !important;
}

.dark-theme .table thead tr {
  background-color: #f0f0f0 !important;
}

.dark-theme .table thead th {
  color: #333 !important;
}

.dark-theme .profile-left-panel {
  background-color: #242435;
  color: #fff;
  box-shadow: 0 0 10px rgb(133, 133, 133);
}

.dark-theme .content-section {
  background-color: #242435;
  color: #fff;
  box-shadow: 0 0 10px rgb(133, 133, 133);
}

.dark-theme .profile-left-panel ul li a,
.dark-theme .content-section h3,
.dark-theme .profile-details p {
  color: #fff;
}

/* Scroll to top button icon styles */
#scrollTopBtn {
  display: none; /* Hidden by default */
  position: fixed;
  bottom: 30px;
  right: 20px;
  z-index: 99; /* Stay on top of other elements */
  font-size: 18px;
  background-color: #31db64;
  color: white;
  font-weight: 840;
  border: none;
  outline: none;
  width: 40px; /* Reduce the width */
  height: 40px; /* Reduce the height */
  cursor: pointer;
  padding: 2px;
  border-radius: 100px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

#scrollTopBtn:hover {
  background-color: #31db64;
}
/* End scroll to top button icon styles */

/* Media query to hide the button on mobile */
@media (max-width: 375px) {
  .input-group button {
    display: none;
  }
}
/* End top bar search input section */

@media screen and (max-width: 480px) {
  .sidebar {
    display: none;
  }
  .main-section {
    flex-direction: column;
    margin-left: 0;
  }
  .topbar {
    padding: 0 1rem;
  }
}

@media only screen and (min-width: 768px) and (max-width: 810px) {
  .sidebar {
    width: 200px;
  }
  .main-section {
    margin-left: 200px;
  }
}

@media only screen and (min-width: 320px) {
  .three-line-charts-wrapper {
    flex-direction: column;
    align-items: center;
  }
  .single-line-box {
    max-width: 100% !important;
  }
}

@media only screen and (min-width: 768px) and (max-width: 810px) {
  .three-line-charts-wrapper {
    flex-direction: row;
    align-items: center;
  }
  .single-line-box {
    max-width: 100% !important;
  }
}

@media only screen and (min-width: 1024px) {
  .three-line-charts-wrapper {
    flex-direction: row;
    align-items: center;
  }
}

@media only screen and (min-width: 320px) {
  .three-pie-charts-wrapper {
    flex-direction: column;
    align-items: center;
  }
  .single-pie-box {
    max-width: 100% !important;
  }
}

@media only screen and (min-width: 768px) and (max-width: 810px) {
  .three-pie-charts-wrapper {
    flex-direction: row;
    align-items: center;
  }
  .single-pie-box {
    max-width: 100% !important;
  }
}

@media only screen and (min-width: 1024px) {
  .three-pie-charts-wrapper {
    flex-direction: row;
    align-items: center;
  }
}

@media only screen and (min-width: 320px) {
  .three-bar-charts-wrapper {
    flex-direction: column;
    align-items: center;
  }
  .single-bar-box {
    max-width: 100% !important;
  }
}

@media only screen and (min-width: 768px) and (max-width: 810px) {
  .three-bar-charts-wrapper {
    flex-direction: row;
    align-items: center;
  }
  .single-bar-box {
    max-width: 100% !important;
  }
}

@media only screen and (min-width: 1024px) {
  .three-bar-charts-wrapper {
    flex-direction: row;
    align-items: center;
  }
}

@media only screen and (min-width: 810px) {
  .profile-left-panel {
    width: 100%;
  }

  .content-section {
    width: 100%;
  }
}

@media (max-width: 375px) {
  .profile-container {
    flex-direction: column;
  }

  .profile-left-panel,
  .content-section {
    width: 100%;
  }
}

/* Responsive media queries (Mobile View)*/
@media screen and (max-width: 480px) {
  .sidebar {
    display: block;
    transform: translateX(-100%);
    /* transition: transform 0.3s ease;  */
    transition: opacity 0.8s ease, transform 0.8s ease;
    width: 85%;
  }

  .sidebar.closed {
    transform: translateX(0);
  }

  .main-section.sidebar-closed {
    margin-left: 0;
  }

  .toggle-sidebar {
    display: block;
  }
}
/* End responsive media queries (Mobile View)*/

@media (max-width: 600px) {
  .dashboard-box p {
    font-size: 1.2rem;
  }
  .dashboard-box h2 {
    font-size: 1rem;
  }
}

i {
  transform: rotate(0deg); /* Ensure no rotation */
  -webkit-transform: rotate(0deg);
  -moz-transform: rotate(0deg);
}

.user-profile i {
  transform: none !important; /* Override any global transform */
  -webkit-transform: none !important;
}
"""

FLASH_MESSAGE =\
  """ 
 
/* CSS Animation for sliding-in the flash message */
@keyframes slideIn {
  from {
    transform: translateX(100%);
  }
  to {
    transform: translateX(0);
  }
}

/* CSS Animation for fading-out the flash message */
@keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}

/* Styling for the flash message container */
.flash--message {
  position: fixed;
  top: 18px;
  right: 20px;
  z-index: 9999;
  height: auto; /* Set height to auto */
  line-height: 28px; /* Adjust line-height */
}

/* Styling for each flash message */
.alert {
  animation: slideIn 0.3s forwards, fadeOut 0.3s 4s forwards;
  margin-bottom: 5px; /* Add space between messages if there are multiple */
  padding: 5px 10px; /* Adjust padding to reduce height */
}

.fas.fa-circle-check {
  color: green;
}

.fas.fa-circle-xmark {
  color: #e3371e;
}
"""


BASE_FOOTER = \
"""
.footer {
    background: hsl(240, 14%, 14%);
    color: #d3d3d3;
    position: relative;
  }
  
  .footer .footer-bottom {
    left: 0;
    bottom: 0;
    margin: 0;
    width: 100%;
    height: 25px;
    font-size: 15px;
    position: fixed;
    color: #e7900c;
    padding-top: 2px;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    text-align: center;
  }
  
  /* Media query for mobile */
  @media only screen and (max-width: 767px) {
    .footer {
      height: auto;
    }
  }
  
  /* Tablets and Small Screens */
  @media only screen and (min-width: 768px) and (max-width: 991px) {
    .footer {
      height: auto;
    }
  }
"""

BAD_REQUESTS =\
"""
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Courier New", Courier, monospace;
}

body,
html {
  height: 100%;
  overflow: hidden;
  background-color: #1b1b1b;
  color: white;
}

.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  position: relative;
}

.glitch {
  position: relative;
  text-align: center;
  color: white;
}

h1 {
  font-size: 8rem;
  color: #ff0033;
  animation: glitch-animation 2s infinite;
  position: relative;
}

h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #ff0033;
  animation: glitch-animation 3s infinite;
}

p {
  font-size: 1.5rem;
  margin-bottom: 2rem;
}

button {
  padding: 0.75rem 2rem;
  background-color: #ff0033;
  border: none;
  border-radius: 5px;
  color: white;
  font-size: 1.25rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #e60029;
}

@keyframes glitch-animation {
  0% {
    transform: translate(0);
  }
  10% {
    transform: translate(-5px, 5px);
  }
  20% {
    transform: translate(5px, -5px);
  }
  30% {
    transform: translate(-5px, -5px);
  }
  40% {
    transform: translate(5px, 5px);
  }
  50% {
    transform: translate(-5px, 5px);
  }
  60% {
    transform: translate(5px, -5px);
  }
  70% {
    transform: translate(-5px, -5px);
  }
  80% {
    transform: translate(5px, 5px);
  }
  90% {
    transform: translate(-5px, 5px);
  }
  100% {
    transform: translate(0);
  }
}

/* Media Queries for responsiveness */
@media screen and (max-width: 768px) {
  h1 {
    font-size: 5rem;
  }

  h2 {
    font-size: 2rem;
  }

  p {
    font-size: 1.2rem;
  }

  button {
    font-size: 1rem;
  }
}

@media screen and (max-width: 480px) {
  h1 {
    font-size: 3rem;
  }

  h2 {
    font-size: 1.5rem;
  }

  p {
    font-size: 1rem;
  }

  button {
    font-size: 0.9rem;
  }
}
"""


CONTENT_TOO_LARGE =\
"""
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Open Sans', sans-serif;
  }
  
  body, html {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f1c40f;
    color: #333;
  }
  
  .container {
    text-align: center;
    padding: 20px;
  }
  
  h1 {
    font-size: 7rem;
    color: #e74c3c;
    margin-bottom: 1rem;
  }
  
  h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }
  
  p {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    color: #2c3e50;
  }
  
  button {
    padding: 0.75rem 2rem;
    background-color: #e74c3c;
    border: none;
    border-radius: 5px;
    color: white;
    font-size: 1.25rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  button:hover {
    background-color: #c0392b;
  }
  
  /* File Icon */
  .file-icon {
    position: relative;
    width: 150px;
    height: 180px;
    margin: 0 auto 20px;
  }
  
  .file {
    width: 100%;
    height: 100%;
    background-color: #fff;
    border: 5px solid #e74c3c;
    border-radius: 10px;
    position: relative;
    animation: shake 2s infinite ease-in-out;
  }
  
  .fold {
    width: 50px;
    height: 50px;
    background-color: #f1c40f;
    position: absolute;
    top: -5px;
    right: -5px;
    border-top-left-radius: 10px;
    transform: rotate(45deg);
  }
  
  .exceed-text {
    position: absolute;
    bottom: -30px;
    width: 100%;
    color: #e74c3c;
    font-size: 1.5rem;
    font-weight: bold;
    text-align: center;
    animation: fade-in 2s infinite alternate;
  }
  
  /* Animation */
  @keyframes shake {
    0%, 100% {
        transform: translate(0, 0);
    }
    25% {
        transform: translate(-5px, 5px);
    }
    50% {
        transform: translate(5px, -5px);
    }
    75% {
        transform: translate(-5px, -5px);
    }
  }
  
  @keyframes fade-in {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
  }
  
  /* Responsive Design */
  @media screen and (max-width: 768px) {
    h1 {
        font-size: 5rem;
    }
  
    h2 {
        font-size: 2rem;
    }
  
    p {
        font-size: 1rem;
    }
  
    button {
        font-size: 1rem;
    }
  
    .file-icon {
        width: 120px;
        height: 150px;
    }
  
    .exceed-text {
        font-size: 1.25rem;
    }
  }
  
  @media screen and (max-width: 480px) {
    h1 {
        font-size: 4rem;
    }
  
    h2 {
        font-size: 1.5rem;
    }
  
    p {
        font-size: 0.9rem;
    }
  
    button {
        font-size: 0.9rem;
    }
  
    .file-icon {
        width: 100px;
        height: 120px;
    }
  
    .exceed-text {
        font-size: 1rem;
    }
  }
"""


FORBIDDEN =\
"""
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Arial', sans-serif;
}

body, html {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #34495e;
  color: #ecf0f1;
}

.container {
  text-align: center;
  padding: 20px;
}

h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  color: #bdc3c7;
}

button {
  padding: 0.75rem 2rem;
  background-color: #e74c3c;
  border: none;
  border-radius: 5px;
  color: white;
  font-size: 1.25rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #c0392b;
}

/* Stop Sign Animation */
.stop-icon {
  position: relative;
  width: 100px;
  height: 100px;
  margin: 0 auto 20px;
}

.stop-sign {
  width: 100px;
  height: 100px;
  background-color: #e74c3c;
  border-radius: 10px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 2rem;
  font-weight: bold;
  animation: bounce 2s infinite ease-in-out;
}

.stop-sign::before {
  content: "";
  position: absolute;
  width: 10px;
  height: 100px;
  background-color: #e74c3c;
  top: 50%;
  left: 50%;
  transform: rotate(45deg) translate(-50%, -50%);
  border-radius: 5px;
}

.stop-sign::after {
  content: "";
  position: absolute;
  width: 100px;
  height: 10px;
  background-color: #e74c3c;
  top: 50%;
  left: 50%;
  transform: rotate(45deg) translate(-50%, -50%);
  border-radius: 5px;
}

@keyframes bounce {
  0%, 100% {
      transform: translateY(0);
  }
  50% {
      transform: translateY(-10px);
  }
}

/* Responsive Design */
@media screen and (max-width: 768px) {
  h2 {
      font-size: 2rem;
  }

  p {
      font-size: 1rem;
  }

  button {
      font-size: 1rem;
  }

  .stop-sign {
      width: 80px;
      height: 80px;
      font-size: 1.5rem;
  }
}

@media screen and (max-width: 480px) {
  h2 {
      font-size: 1.5rem;
  }

  p {
      font-size: 0.9rem;
  }

  button {
      font-size: 0.9rem;
  }

  .stop-sign {
      width: 60px;
      height: 60px;
      font-size: 1.25rem;
  }
}
"""


INTERNAL_SERVER =\
"""
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Montserrat", sans-serif;
}

body,
html {
  height: 100%;
  overflow: hidden;
  background-color: #2c3e50;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}

.container {
  position: relative;
  text-align: center;
  z-index: 1;
}

h1 {
  font-size: 10rem;
  margin-bottom: 1rem;
  color: #e74c3c;
  animation: glitch-animation 1.5s infinite;
}

h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: white;
  animation: glitch-animation 2s infinite;
}

p {
  font-size: 1rem;
  margin-bottom: 2rem;
  color: #ecf0f1;
}

button {
  padding: 0.75rem 2rem;
  background-color: #e74c3c;
  border: none;
  margin-bottom: 1rem;
  border-radius: 5px;
  color: white;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #c0392b;
}

/* Glitch Effect */
@keyframes glitch-animation {
  0% {
    text-shadow: none;
  }
  20% {
    text-shadow: -2px 0 red, 2px 0 blue;
  }
  40% {
    text-shadow: 2px 0 red, -2px 0 blue;
  }
  60% {
    text-shadow: -2px 0 red, 2px 0 blue;
  }
  80% {
    text-shadow: 2px 0 red, -2px 0 blue;
  }
  100% {
    text-shadow: none;
  }
}

.glitch-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    45deg,
    rgba(231, 76, 60, 0.3),
    rgba(41, 128, 185, 0.3)
  );
  z-index: -1;
  animation: flicker 3s infinite;
}

@keyframes flicker {
  0% {
    opacity: 0.5;
  }
  50% {
    opacity: 0.8;
  }
  100% {
    opacity: 0.5;
  }
}

/* Media Queries for responsiveness */
@media screen and (max-width: 768px) {
  h1 {
    font-size: 6rem;
  }

  h2 {
    font-size: 2rem;
  }

  p {
    font-size: 1rem;
  }

  button {
    font-size: 1rem;
  }
}

@media screen and (max-width: 480px) {
  h1 {
    font-size: 4rem;
  }

  h2 {
    font-size: 1.5rem;
  }

  p {
    font-size: 0.9rem;
  }

  button {
    font-size: 0.9rem;
  }
}
"""


MAINTAINANCE =\
"""

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Montserrat', sans-serif;
  }
  
  body, html {
    height: 100%;
    background-color: #34495e;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ecf0f1;
  }
  
  .container {
    text-align: center;
    padding: 20px;
  }
  
  h1 {
    font-size: 5rem;
    color: #e74c3c;
    margin-bottom: 1rem;
  }
  
  h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }
  
  p {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    color: #bdc3c7;
  }
  
  button {
    padding: 0.75rem 2rem;
    background-color: #e74c3c;
    border: none;
    border-radius: 5px;
    color: white;
    font-size: 1.25rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  button:hover {
    background-color: #c0392b;
  }
  
  /* Gear Icon */
  .gear-icon {
    width: 120px;
    height: 120px;
    margin: 0 auto 20px;
    position: relative;
  }
  
  .gear {
    width: 100%;
    height: 100%;
    background-color: #ecf0f1;
    border-radius: 50%;
    position: relative;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
    animation: rotate 3s infinite linear;
  }
  
  .gear:before, .gear:after {
    content: '';
    position: absolute;
    background-color: #e74c3c;
    border-radius: 5px;
  }
  
  .gear:before {
    width: 60%;
    height: 10%;
    top: 45%;
    left: 20%;
  }
  
  .gear:after {
    width: 10%;
    height: 60%;
    top: 20%;
    left: 45%;
  }
  
  /* Rotation Animation */
  @keyframes rotate {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
  }
  
  /* Responsive Design */
  @media screen and (max-width: 768px) {
    h1 {
        font-size: 5rem;
    }
  
    h2 {
        font-size: 2rem;
    }
  
    p {
        font-size: 1rem;
    }
  
    button {
        font-size: 1rem;
    }
  
    .gear-icon {
        width: 100px;
        height: 100px;
    }
  }
  
  @media screen and (max-width: 480px) {
    h1 {
        font-size: 4rem;
    }
  
    h2 {
        font-size: 1.5rem;
    }
  
    p {
        font-size: 0.9rem;
    }
  
    button {
        font-size: 0.9rem;
    }
  
    .gear-icon {
        width: 80px;
        height: 80px;
    }
  }
"""


NOT_FOUND =\
"""
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Arial", sans-serif;
}

body,
html {
  height: 100%;
  overflow: hidden;
}

.container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  background: #000;
  color: white;
  text-align: center;
}

.error {
  z-index: 10;
}

h1 {
  font-size: 10rem;
  margin-bottom: 1rem;
  color: #f39c12;
  animation: glow 1s ease-in-out infinite alternate;
}

p {
  font-size: 1.5rem;
  margin-bottom: 2rem;
}

button {
  padding: 0.75rem 2rem;
  background-color: #f39c12;
  border: none;
  border-radius: 5px;
  color: white;
  font-size: 1.25rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #e67e22;
}

.stars {
  position: absolute;
  width: 100%;
  height: 100%;
  background: transparent;
  z-index: 0;
  overflow: hidden;
  pointer-events: none;
}

.stars::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 50% 50%, #f39c12 0%, transparent 80%);
  animation: rotate 120s linear infinite;
  opacity: 0.3;
}

@keyframes glow {
  from {
    text-shadow: 0 0 10px #f39c12, 0 0 20px #f39c12, 0 0 30px #e67e22;
  }
  to {
    text-shadow: 0 0 20px #e67e22, 0 0 40px #f39c12, 0 0 50px #e67e22;
  }
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* Media Queries for responsiveness */
@media screen and (max-width: 768px) {
  h1 {
    font-size: 6rem;
  }

  p {
    font-size: 1.2rem;
  }

  button {
    font-size: 1rem;
  }
}

@media screen and (max-width: 480px) {
  h1 {
    font-size: 4rem;
  }

  p {
    font-size: 1rem;
  }

  button {
    font-size: 0.9rem;
  }
}
"""


TOO_MANAY_REQUEST =\
"""
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Verdana", sans-serif;
}

body,
html {
  height: 100%;
  background-color: #2c3e50;
  color: #ecf0f1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
}

.container {
  text-align: center;
  padding: 15px;
  width: 93%;
  background-color: #34495e;
  border-radius: 10px;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 5rem;
  color: #e74c3c;
}

h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #ecf0f1;
}

p {
  font-size: 1rem;
  margin-bottom: 2rem;
}

.timer {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 2rem;
}

.timer span {
  font-size: 3rem;
  color: #f39c12;
  animation: pulse 1s infinite;
}

button {
  padding: 0.75rem 2rem;
  background-color: #e74c3c;
  border: none;
  border-radius: 5px;
  color: white;
  font-size: 1.25rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #c0392b;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}

/* Media Queries for responsiveness */
@media screen and (max-width: 768px) {
  h1 {
    font-size: 6rem;
  }

  h2 {
    font-size: 2rem;
  }

  p {
    font-size: 1rem;
  }

  button {
    font-size: 1rem;
  }
}

@media screen and (max-width: 480px) {
  h1 {
    font-size: 4rem;
  }

  h2 {
    font-size: 1.5rem;
  }

  p {
    font-size: 0.9rem;
  }

  button {
    font-size: 0.9rem;
  }
}
"""


UNAUTHORIZED =\
"""
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Arial", sans-serif;
}

body,
html {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #2c3e50;
  color: #ecf0f1;
}

.container {
  text-align: center;
  padding: 20px;
}

h1 {
  font-size: 7rem;
  color: #e74c3c;
  margin-bottom: 1rem;
}

h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  color: #bdc3c7;
}

button {
  padding: 0.75rem 2rem;
  background-color: #e74c3c;
  border: none;
  border-radius: 5px;
  color: white;
  font-size: 1.25rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #c0392b;
}

/* Lock Icon Animation */
.lock-icon {
  position: relative;
  width: 80px;
  height: 100px;
  margin: 0 auto 20px;
}

.lock-body {
  width: 80px;
  height: 50px;
  background-color: #e74c3c;
  border-radius: 10px;
  position: absolute;
  bottom: 0;
}

.lock-shackle {
  width: 60px;
  height: 60px;
  border: 8px solid #e74c3c;
  border-radius: 50px;
  position: absolute;
  top: -40px;
  left: 10px;
  border-bottom: none;
  animation: lock-animation 2s infinite alternate ease-in-out;
}

@keyframes lock-animation {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-5px);
  }
}

/* Responsive Design */
@media screen and (max-width: 768px) {
  h1 {
    font-size: 5rem;
  }

  h2 {
    font-size: 2rem;
  }

  p {
    font-size: 1rem;
  }

  button {
    font-size: 1rem;
  }

  .lock-icon {
    width: 60px;
    height: 80px;
  }
}

@media screen and (max-width: 480px) {
  h1 {
    font-size: 4rem;
  }

  h2 {
    font-size: 1.5rem;
  }

  p {
    font-size: 0.9rem;
  }

  button {
    font-size: 0.9rem;
  }

  .lock-icon {
    width: 50px;
    height: 70px;
  }
}
"""


ACCOUNT_CSS_PROFILE =\
"""
.page-wrapper {
  background-color: #d7e8df;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
}
.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  max-width: 1200px;
  width: 100%;
}
.sidebar {
  background: white;
  padding: 20px;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  width: 300px;
  height: auto;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}
.profile-img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
}
.nav-link {
  font-weight: bold;
  color: black;
  cursor: pointer;
}
.nav-link.active {
  color: blue;
}
.content-area {
  background: white;
  padding: 20px;
  border-radius: 8px;
  flex-grow: 1;
  width: 700px;
  min-height: 500px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}
.form-container,
.reset-container,
.profile-container {
  display: none;
}
.floating-btn {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: green;
  color: white;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  cursor: pointer;
}
@media (max-width: 768px) {
  .container {
    flex-direction: column;
    align-items: center;
  }
  .content-area,
  .sidebar {
    width: 90%;
  }
}

@media (max-width: 375px) {
  .container {
    flex-direction: column;
    align-items: center;
  }
  .content-area,
  .sidebar {
    width: 100%;
  }
}

@media (max-width: 320px) {
  .container {
    flex-direction: column;
    align-items: center;
  }
  .content-area,
  .sidebar {
    width: 100%;
  }
}
"""

VIEW_CSS = \
  """ 
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
}
.container {
  text-align: center;
  background: rgb(225, 247, 238);
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.container a {
  display: block;
  margin-bottom: 10px;
  font-size: 16px;
  text-decoration: none;
  color: #007bff;
}
.container p {
  margin: 5px 0;
  font-size: 17px;
}
"""