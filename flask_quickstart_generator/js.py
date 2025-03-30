SADASHBOARD_JS = """ 
// USER PROFILE DROPDOWN
const userProfile = document.querySelector(".user-profile");
userProfile.addEventListener("click", () => {
  userProfile.classList.toggle("open");
});
document.addEventListener("click", function (e) {
  if (userProfile && !userProfile.contains(e.target)) {
    userProfile.classList.remove("open");
  }
});

// TOGGLE SIDEBAR
const sidebar = document.querySelector(".sidebar");
const toggleSidebar = document.querySelector(".toggle-sidebar");
const mainSection = document.querySelector(".main-section");

// Toggle sidebar when clicking the toggle button
toggleSidebar.addEventListener("click", () => {
  sidebar.classList.toggle("closed");
  mainSection.classList.toggle("sidebar-closed");
});

// Close sidebar when clicking outside of it
document.addEventListener("click", (e) => {
  const isClickInsideSidebar = sidebar.contains(e.target);
  const isClickOnToggle = toggleSidebar.contains(e.target);

  if (!isClickInsideSidebar && !isClickOnToggle) {
    sidebar.classList.remove("closed");
    mainSection.classList.remove("sidebar-closed");
  }
});

// SUBMENU TOGGLE (Accordion behavior)
const submenuParents = document.querySelectorAll(".has-submenu");
submenuParents.forEach((parentLi) => {
  const menuLink = parentLi.querySelector("a");
  menuLink.addEventListener("click", (e) => {
    e.preventDefault();
    // Close other submenus
    submenuParents.forEach((otherLi) => {
      if (otherLi !== parentLi) {
        otherLi.classList.remove("open");
      }
    });
    // Toggle current submenu
    parentLi.classList.toggle("open");
  });
});

// On page load, check localStorage and apply the theme
if (localStorage.getItem("theme") === "dark") {
  document.body.classList.add("dark-theme");
} else {
  document.body.classList.remove("dark-theme");
}

const themeToggle = document.getElementById("theme-toggle");
themeToggle.addEventListener("click", (e) => {
  e.preventDefault();
  document.body.classList.toggle("dark-theme");
  // Save the selection in localStorage
  if (document.body.classList.contains("dark-theme")) {
    localStorage.setItem("theme", "dark");
  } else {
    localStorage.setItem("theme", "light");
  }
});

//FIRST SECTION: 3 SIDE-BY-SIDE LINE CHARTS
const ctx1 = document.getElementById("chart1").getContext("2d");
const chart1 = new Chart(ctx1, {
  type: "line",
  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], // Months or timeline periods
    datasets: [
      {
        label: "Project Milestones (Count)",
        data: [2, 3, 5, 7, 9, 11], // Number of milestones completed each month
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        borderColor: "rgba(75, 192, 192, 1)",
        fill: true,
        tension: 0.2,
      },
    ],
  },
  options: {
    scales: {
      y: { beginAtZero: true },
    },
    plugins: {
      title: {
        display: true,
        text: "Project Milestone Progress",
      },
    },
  },
});

// 2) Team Task Completion Summary
const ctx2 = document.getElementById("chart2").getContext("2d");
const chart2 = new Chart(ctx2, {
  type: "line",
  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], // Months or periods
    datasets: [
      {
        label: "Team Task Completion (Count)", // Professional label
        data: [8, 12, 18, 22, 30, 35], // Number of tasks completed each month
        backgroundColor: "rgba(153, 102, 255, 0.2)",
        borderColor: "rgba(153, 102, 255, 1)",
        fill: true,
        tension: 0.2,
      },
    ],
  },
  options: {
    scales: {
      y: { beginAtZero: true },
    },
    plugins: {
      title: {
        display: true,
        text: "Team Task Completion Progress", // Added professional chart title
      },
    },
  },
});

// 3) Task Completion Efficiency
const ctx3 = document.getElementById("chart3").getContext("2d");
const chart3 = new Chart(ctx3, {
  type: "line",
  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], // Time periods (months)
    datasets: [
      {
        label: "Task Completion Efficiency (%)", // New professional label
        data: [85, 80, 90, 87, 92, 95], // Task completion efficiency in percentage
        backgroundColor: "rgba(153, 102, 255, 0.2)",
        borderColor: "rgba(153, 102, 255, 1)",
        fill: true,
        tension: 0.2,
      },
    ],
  },
  options: {
    scales: {
      y: { beginAtZero: true, max: 100 }, // Efficiency percentage with max set to 100
    },
    plugins: {
      title: {
        display: true,
        text: "Task Completion Efficiency Over Time", // Professional chart title
      },
    },
  },
});

//THREE PIE CHARTS, EACH IN ITS OWN BOX Left//
const ctxPieA = document.getElementById("pieChartA").getContext("2d");
const pieChartA = new Chart(ctxPieA, {
  type: "pie",
  data: {
    labels: ["One", "Two", "Three"],
    datasets: [
      {
        label: "Sample A",
        data: [30, 40, 30],
        backgroundColor: ["#36a2eb", "#ff6384", "#ffce56"],
      },
    ],
  },
});

// Middle
const ctxPieB = document.getElementById("pieChartB").getContext("2d");
const pieChartB = new Chart(ctxPieB, {
  type: "pie",
  data: {
    labels: ["Alpha", "Beta", "Gamma"],
    datasets: [
      {
        label: "Sample B",
        data: [25, 50, 25],
        backgroundColor: ["#4bc0c0", "#9966ff", "#ff9f40"],
      },
    ],
  },
});

// Right
const ctxPieC = document.getElementById("pieChartC").getContext("2d");
const pieChartC = new Chart(ctxPieC, {
  type: "pie",
  data: {
    labels: ["Red", "Green", "Blue"],
    datasets: [
      {
        label: "Sample C",
        data: [33, 33, 34],
        backgroundColor: ["#ff6384", "#36a2eb", "#4bc0c0"],
      },
    ],
  },
});

// === THIRD SECTION: 3 SIDE-BY-SIDE BAR CHARTS ===
// Left Bar
const ctxBarA = document.getElementById("barChartA").getContext("2d");
const barChartA = new Chart(ctxBarA, {
  type: "bar",
  data: {
    labels: ["Mon", "Tue", "Wed", "Thu", "Fri"],
    datasets: [
      {
        label: "Bar A",
        data: [5, 8, 3, 10, 6],
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        borderColor: "rgba(255, 99, 132, 1)",
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: { beginAtZero: true },
    },
  },
});

// Middle Bar
const ctxBarB = document.getElementById("barChartB").getContext("2d");
const barChartB = new Chart(ctxBarB, {
  type: "bar",
  data: {
    labels: ["Mon", "Tue", "Wed", "Thu", "Fri"],
    datasets: [
      {
        label: "Bar B",
        data: [7, 2, 9, 4, 12],
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: { beginAtZero: true },
    },
  },
});

// Right Bar
const ctxBarC = document.getElementById("barChartC").getContext("2d");
const barChartC = new Chart(ctxBarC, {
  type: "bar",
  data: {
    labels: ["Mon", "Tue", "Wed", "Thu", "Fri"],
    datasets: [
      {
        label: "Bar C",
        data: [10, 4, 6, 8, 9],
        backgroundColor: "rgba(255, 206, 86, 0.2)",
        borderColor: "rgba(255, 206, 86, 1)",
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: { beginAtZero: true },
    },
  },
});

// Select the links and sections
const profileOverviewLink = document.getElementById("profile-overview-link");
const editProfileLink = document.getElementById("edit-profile-link");
const createAccountLink = document.getElementById("create-account-link");
const passwordResetLink = document.getElementById("password-reset-link");

const profileOverviewSection = document.getElementById("profile-overview");
const editProfileSection = document.getElementById("edit-profile");
const createAccountSection = document.getElementById("create-account");
const passwordResetSection = document.getElementById("password-reset");

// Function to hide all sections
function hideAllSections() {
  profileOverviewSection.classList.remove("active-section");
  editProfileSection.classList.remove("active-section");
  createAccountSection.classList.remove("active-section");
  passwordResetSection.classList.remove("active-section");
}

// Function to remove 'active-link' from all links
function deactivateAllLinks() {
  profileOverviewLink.classList.remove("active-link");
  editProfileLink.classList.remove("active-link");
  createAccountLink.classList.remove("active-link");
  passwordResetLink.classList.remove("active-link");
}

// Event listeners for links
profileOverviewLink.addEventListener("click", () => {
  hideAllSections();
  deactivateAllLinks();
  profileOverviewSection.classList.add("active-section");
  profileOverviewLink.classList.add("active-link");
});

editProfileLink.addEventListener("click", () => {
  hideAllSections();
  deactivateAllLinks();
  editProfileSection.classList.add("active-section");
  editProfileLink.classList.add("active-link");
});

createAccountLink.addEventListener("click", () => {
  hideAllSections();
  deactivateAllLinks();
  createAccountSection.classList.add("active-section");
  createAccountLink.classList.add("active-link");
});

passwordResetLink.addEventListener("click", () => {
  hideAllSections();
  deactivateAllLinks();
  passwordResetSection.classList.add("active-section");
  passwordResetLink.classList.add("active-link");
});

// Initially, show the profile overview section
profileOverviewSection.classList.add("active-section");
profileOverviewLink.classList.add("active-link");

// Show the button when the user scrolls down 20px from the top of the page
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  const scrollTopBtn = document.getElementById("scrollTopBtn");
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollTopBtn.style.display = "block";
  } else {
    scrollTopBtn.style.display = "none";
  }
}

// Smoothly scroll to the top of the page when the user clicks the button
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// Get the button
let scrollToTopBtn = document.getElementById("scrollTopBtn");

// Add click event listener to the button
scrollToTopBtn.addEventListener("click", function () {
  window.scrollTo({
    top: 0,
    behavior: "smooth", // Smooth scrolling effect
  });
});
"""


LOG_JS = """ 
const darkModeToggle = document.getElementById("dark-mode-toggle");
const mainContainer = document.querySelector(".container-fluid");

// Check localStorage for dark mode preference on page load
window.addEventListener("DOMContentLoaded", () => {
  const darkMode = localStorage.getItem("darkMode");

  // Apply dark mode if it was enabled
  if (darkMode === "enabled") {
    mainContainer.classList.add("dark-mode");
    darkModeToggle.checked = true; // Set the toggle to ON
  }
});

// Add event listener to the toggle switch
darkModeToggle.addEventListener("change", () => {
  if (darkModeToggle.checked) {
    mainContainer.classList.add("dark-mode");
    localStorage.setItem("darkMode", "enabled"); // Save dark mode state to localStorage
  } else {
    mainContainer.classList.remove("dark-mode");
    localStorage.setItem("darkMode", "disabled"); // Save light mode state to localStorage
  }
});
"""

FLASH_DOM_REMOVE = """ 
document.addEventListener("DOMContentLoaded", function () {
    // Find all the flash messages
    const flashMessages = document.querySelectorAll(".flash--message .alert");

    // For each flash message, set a timeout to remove it after the animation completes
    flashMessages.forEach(function (message) {
      // Get the total animation time (slideIn + fadeOut)
      const totalAnimationTime = 4000; // 4 seconds (or match your fade-out duration)

      // Set a timeout to remove the message from the DOM after the animation ends
      setTimeout(function () {
        message.remove(); // This will remove the element from the DOM
      }, totalAnimationTime);
    });
});
"""

ERROR_PAGES = """
document.addEventListener("DOMContentLoaded", function () {
  // Select the button by id
  const goBackButton = document.getElementById("go-back-btn");

  // Attach the click event handler to the button
  if (goBackButton) {
    goBackButton.addEventListener("click", function () {
      window.history.back();
    });
  }
});

// Too manay request
document.addEventListener("DOMContentLoaded", function () {
  // Countdown Timer Logic
  let timeLeft = 40; // You can adjust the time
  const countdownElement = document.getElementById("countdown");
  const retryButton = document.getElementById("retry-btn");

  const countdown = setInterval(() => {
    timeLeft--;
    countdownElement.innerText = timeLeft;

    if (timeLeft <= 0) {
      clearInterval(countdown);
      document.querySelector(".timer").innerHTML =
        "<p>You can try again now.</p>";
    }
  }, 1000);

  // Retry button logic
  if (retryButton) {
    retryButton.addEventListener("click", function () {
      location.reload(); // Reloads the page after countdown finishes
    });
  }
});

// 500 server
document.addEventListener("DOMContentLoaded", function () {
  // Select the button by its id
  const refreshBtn = document.getElementById("server_refresh-btn");

  // Attach the click event if the button exists
  if (refreshBtn) {
    refreshBtn.addEventListener("click", function () {
      location.reload(); // Refresh the page on click
    });
  }
});
"""

MAINTAINANCE_JS = """ 
document.addEventListener('DOMContentLoaded', function () {
    // Auto-refresh every 10 minutes (600000 milliseconds)
    setInterval(function () {
        window.location.reload();
    }, 60000);

    // Bind click event to the reload button (if it exists) to allow immediate reload
    const reloadBtn = document.getElementById('main-reload-btn');
    if (reloadBtn) {
        reloadBtn.addEventListener('click', function () {
            window.location.reload();
        });
    }
});
"""

NOT_FOUND_JS = """ 
document.addEventListener("DOMContentLoaded", function () {
    // Select the button by id
    const goBackButton = document.getElementById("go-back-btn");
  
    // Attach the click event handler to the button
    if (goBackButton) {
      goBackButton.addEventListener("click", function () {
        window.history.back();
      });
    }
  });  
"""
