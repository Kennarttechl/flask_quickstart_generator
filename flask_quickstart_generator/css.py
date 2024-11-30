DEMO_CSS = """ 

"""




REGISTER_LOGIN_CSS =\
""" 
html,
body {
  background-color: #f2fbfd;
}

.page-wrapper {
  min-height: 100%;
  position: relative;
}


.extra-fields-hidden {
  display: none;
}

.d-none {
  display: none !important;
}

#google-login-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

#google-login-button i {
  margin-right: 10px;
}

.right-section {
  flex: 1;
  padding: 20px;
  /* padding-top: 70px; */
}

.left-section {
  flex: 1;
  /* flex: 2; */
}

.login-box:hover {
  transform: translateY(-5px);
  transition: all 0.5s ease-in-out;
}

.login-container{
  transition: all 0.5s ease-in-out;
}

.login-container:hover {
  transform: translateY(-5px);
}

.right-section {
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-container h3 {
  text-align: center;
  color: #01b7d1;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.login-container h2{
  color: #01b7d1;
  margin-bottom: 2rem;
}

.right-section{
  margin-top: 2rem;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 122rem;
}

.form-group input {
  width: 100%;
  padding: 6px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.right-section .login-container {
  width: 100%;
  max-width: 400px;
  height: auto;
  margin-top: 2rem;
  background-color: white;
  border: 1.8px #01b7d1 solid;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.right-section h2 {
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  margin-bottom: 5px;
}

/* For tablets (width up to 768px) */
@media (max-width: 768px) {
  .right-section {
    flex: 0 0 50%; /* Ensure the right section takes half the width */
    max-width: 50%; /* Ensure the right section takes half the width */
  }

  .right-section{
    margin-top: 0px;
  }
}

/* @media only screen and (max-width: 767px) */
@media only screen and (max-width: 767px) {
  .left-section {
    display: none; /* Hide the image section */
  }

  .right-section {
    flex: 0 0 100%; /* Make the login section full width */
    max-width: 100%;
    padding-top: 70px;
  }

  .login-container {
    max-width: 100%; /* Ensure the login container uses full width */
    padding: 20px; /* Adjust padding for better appearance on small screens */
  }
}
"""

BASE_CSS =\
""" 
html,
body {
  height: 100%;
  margin: 0px;
  padding: 0px;
  font-family: Arial, sans-serif;
  transition: opacity 0.7s ease-in-out;
}

body.loading {
  opacity: 0;
}

/* Burger Menu */
.burger-menu,
.burger-menu-btn {
  display: none;
}

.burger-menu {
  display: none;
  position: fixed;
  width: 85%; /* Note*/
  height: 100vh;
  z-index: 900;
  background-color: #025064;
  overflow-y: scroll;
}

/* burger transition start */
.burger-menu {
  display: none;
  transform: translateX(-100%);
  transition: opacity 0.3s ease, transform 0.3s ease;
}
/* burger transition end */

.burger-menu ul {
  width: 100%;
  height: calc(100vh - 60px);
  padding-top: 56px; /* space from top*/
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
}

.burger-menu ul li {
  flex-basis: 87%;
  border-bottom: 0.9px solid #080101;
  list-style: none;
  margin-left: -16px;
}

.burger-menu ul li:last-child {
  border-bottom: 0.9px solid #080101;
}

.burger-menu ul li a {
  display: block;
  height: 100%;
  color: #ffffff;
  font-size: 1rem;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  padding: 10px 0;
  flex-basis: 100%;
  text-align: start;
  text-decoration: none;
}
/* ----End---- */

.header-main {
  position: fixed;
  top: 0;
  width: 100%;
  height: 55px;
  display: flex;
  background-color: #025064;
  justify-content: space-between;
  border-bottom: 1px solid #ffffff;
  z-index: 1000;
}

.header-main-logo {
  width: fit-content;
  height: 100%;
  padding-left: 20px; /* Side space*/
  display: flex;
}

.header-main-logo img {
  height: 30px;
  width: auto;
  align-self: center;
}

.header-main-nav {
  height: 100%;
  width: fit-content;
}

.header-main-nav ul {
  list-style: none;
  margin-left: -2rem;
  /* display: inline-block; */
}

.header-main-nav ul li {
  display: inline;
  float: left;
}

.header-main-nav ul li {
  padding-left: 1px; /* Consistent left spacing */
}

.header-main-nav ul li a {
  padding: 0 8px;
  right: 2rem;
  line-height: 55px; /*text move top*/
  color: #ffffff;
  font-size: 1rem;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  text-decoration: none;
}

.header-main-sm {
  width: fit-content;
  height: 100%;
  padding-right: 40px; /* Side space*/
  display: flex;
  align-items: center;
  column-gap: 10px;
  padding-top: 1.1rem;
  padding-bottom: 1.1rem;
}

.header-main-sm a {
  color: #face0b;
  font-size: 1.1rem;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  text-decoration: none;
}

.header-main-sm-in {
  width: 30px;
  height: 30px;
  /* background-image: url(); */
  background-repeat: no-repeat;
  background-size: cover;
}

/* Drop down menu*/
.dropdown-content {
  display: none;
  color: #ffffff;
  min-width: 160px;
  position: absolute;
  margin: 0 0;
  border-radius: 0.4rem;
  background-color: #025064;
  z-index: 1;
}

.dropdown-content a {
  color: #1e1e28;
  padding: 8px 16px;
  text-decoration: none;
  display: block;
  line-height: 1.5;
}

.dropdown-content a:hover {
  background-color: #2c2c39;
  border-radius: 0.2rem;
}

.dropdown-content {
  display: none;
}

.dropdown-content.show {
  display: block;
}

/* Responsive on mobile & table */
@media only screen and (max-width: 768px) {
  .burger-menu-btn {
    display: block;
    margin-bottom: 1px;
    /* margin: 10px; */
    border: 1.5px solid #fdfdfd;
    border-radius: 0.3rem;
    width: 45px;
    height: 35px;
    background-image: url(../icons/menu.svg), url(../icons/close.svg);
    padding-top: 10px;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center, center left 50px;
  }

  .header-main-logo {
    padding-left: 15px; /* Side space*/
  }

  .header-main-logo ul li {
    display: block;
    line-height: 50px;
  }

  .header-main-nav {
    display: none;
    height: 100%;
  }

  .header-main-sm {
    padding-right: 15px; /* Side space*/
  }
}

/* Tablets and Small Screens */
@media only screen and (min-width: 768px) and (max-width: 991px) {
  .burger-menu-btn {
    display: block;
    margin-bottom: 1px;
    /* margin: 10px; */
    border: 1.5px solid #fdfdfd;
    border-radius: 0.3rem;
    width: 45px;

    height: 35px;
    background-image: url(../icons/menu.svg), url(../icons/close.svg);
    padding-top: 10px;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center, center left 50px;
  }

  .header-main-logo {
    padding-left: 15px; /* Side space*/
  }

  .header-main-logo ul li {
    display: block;
    line-height: 50px;
  }

  .header-main-nav {
    display: none;
    height: 100%;
  }

  .burger-menu {
    width: 50%; /* Adjusted width for tablets */
  }

  .header-main-sm {
    padding-right: 15px; /* Side space*/
  }
}
"""