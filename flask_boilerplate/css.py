DEMO_CSS = \
""" 
@font-face {
  font-family: "navfont";
  src: url("../"),
    url("../");
    /* url("../fonts/Roboto/RobotoSlab-Bold.woff") format("woff"); */
  font-style: normal;
}

@font-face {
  font-family: "adminfont";
  src: url("../"),
    url("../");
  font-weight: 500;
  font-style: normal;
}

html,
body {
  height: 100%;
  margin: 0px;
  padding: 0px;
  font-family: Arial, sans-serif;
}

.header-main {
  position: fixed;
  top: 0;
  width: 100%;
  height: 40px;
  /* height: 55px; */
  display: flex;
  background-color: #20202a;
  justify-content: space-between;
  border-bottom: 1px solid #4e4e5f;
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
  /* margin-left: 1rem; */
  /* display: inline-block; */
}

.header-main-nav ul li {
  display: inline;
  float: left;
}

.header-main-nav ul li a {
  padding: 0 8px;
  line-height: 40px; /*text move top*/
  color: #ffc107;
  font-size: 1.1rem;
  font-family: navfont;
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
  font-family: adminfont;
  text-decoration: none;
}

.header-main-sm .fa-right-from-bracket{
  color: #face0b;
}

.header-main-sm-in {
  width: 30px;
  height: 30px;
  background-image: url(../icons/linkedin.svg);
  background-repeat: no-repeat;
  background-size: cover;
}

.burger-menu,
.burger-menu-btn {
  display: none;
}

/* Drop down menu*/
.dropdown-content {
  display: none;
  color: #ffc107;
  min-width: 160px;
  position: absolute;
  margin: 0 0;
  border-radius: 0.4rem;
  background-color: #20202a;
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
    /* margin: 10px; */
    border: 1.5px solid #444452;
    border-radius: 0.3rem;
    width: 45px;
    height: 33px;
    padding-top: 10px;
    background-image: url(../icons/menu.svg), url(../icons/close.svg);
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center, center left 50px;
  }

  .burger-menu {
    display: none;
    position: fixed;
    width: 85%; /* Note*/
    height: 100vh;
    z-index: 900;
    background-color: #242431;
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
  }

  .burger-menu ul li:last-child {
    border-bottom: 0.9px solid #080101;
  }

  .burger-menu ul li a {
    display: block;
    height: 100%;
    color: #ffc107;
    font-size: 1.2rem;
    font-family: navfont;
    padding: 10px 0;
    flex-basis: 100%;
    text-align: start;
    text-decoration: none;
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


/* ====== toggle switch ========= */

/* Light theme */
body.light-mode {
  background-color: #fff;
  color: #000;
}

/* Dark theme */
body.dark-mode {
  background-color: #2c2c37;
  color: #fff;
}

/* Toggle switch styles */
.toggle-switch {
  position: relative;
  display: inline-block;
  width: 65px;
  height: 34px;
  background-color: #ccc;
  border-radius: 34px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  transition: .4s;
}

.slider::before {
  position: absolute;
  content: "";
  width: 26px;
  height: 26px;
  top: 3.6px;
  left: 7px;
  background-color: #ffffff;
  border-radius: 50%;
  transition: .4s;
  
}

.toggle-switch input:checked + .slider {
  background-color: #0cc73a;
  border-radius: 34px;
  
}

.toggle-switch input:checked + .slider::before {
  transform: translateX(26px);
}




/* const toggleSwitch = document.getElementById('dark-mode-toggle');

toggleSwitch.addEventListener('change', () => {
  const body = document.body;
  if (toggleSwitch.checked) {
    body.classList.add('dark-mode');
    body.classList.remove('light-mode');
    // Store preference in session
    sessionStorage.setItem('dark_mode', true);
  } else {
    body.classList.add('light-mode');
    body.classList.remove('dark-mode');
    // Remove preference from session (optional)
    sessionStorage.removeItem('dark_mode');
  }
});

// Check initial session preference (optional)
if (sessionStorage.getItem('dark_mode') === 'true') {
  toggleSwitch.checked = true;
  document.body.classList.add('dark-mode');
}
*/
"""