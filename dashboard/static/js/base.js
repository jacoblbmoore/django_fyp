const body = document.querySelector('body'),
    sidebar = body.querySelector('nav'),
    toggle = body.querySelector(".toggle"),
    modeSwitch = body.querySelector(".toggle-switch"),
    modeText = body.querySelector(".mode-text"),
    userProfile = body.querySelector(".user-profile");

function saveSidebarState() {
    const isCollapsed = sidebar.classList.contains("close");
    localStorage.setItem("sidebarCollapsed", isCollapsed);
}

function saveThemeState() {
    const isDark = body.classList.contains("dark");
    localStorage.setItem("themeState", isDark ? "dark" : "light");
}

function handleImageDisplay() {
    const isCollapsed = sidebar.classList.contains("close");
    const expandedLogo = document.getElementById("expanded-logo");
    const collapsedLogo = document.getElementById("collapsed-logo");

    if (isCollapsed) {
        collapsedLogo.style.display = "block";
        collapsedLogo.style.opacity = 0;
        setTimeout(() => {
            collapsedLogo.style.opacity = 1;
        }, 50);
        expandedLogo.style.display = "none";
    } else {
        expandedLogo.style.display = "block";
        expandedLogo.style.opacity = 0;
        setTimeout(() => {
            expandedLogo.style.opacity = 1;
        }, 50);
        collapsedLogo.style.display = "none";
    }

    userProfile.classList.toggle("hidden", isCollapsed);
}

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    handleImageDisplay();
    saveSidebarState();
    if (sidebar.classList.contains("close")) {
        document.querySelector(".content-container").style.marginLeft = "0";
    } else {
        document.querySelector(".content-container").style.marginLeft = "250px"; /* Adjust this value to the width of the expanded sidebar */
    }
    // Dispatch the custom event
    const sidebarToggleEvent = new CustomEvent('sidebarToggled');
    document.dispatchEvent(sidebarToggleEvent);
});


function loadThemeState() {
    const savedThemeState = localStorage.getItem("themeState");
    if (savedThemeState === "dark") {
        body.classList.add("dark");
    } else {
        body.classList.remove("dark");
    }
}

function loadSidebarState() {
    const isCollapsed = localStorage.getItem("sidebarCollapsed") === "true";
    if (isCollapsed) {
        sidebar.classList.add("close");
    } else {
        sidebar.classList.remove("close");
    }
    handleImageDisplay();
}

modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");

    if (body.classList.contains("dark")) {
        modeText.innerText = "Dark Mode";
    } else {
        modeText.innerText = "Light Mode";
    }
    saveThemeState();
});


// Call loadThemeState on page load
loadThemeState();

// Update modeText based on the current theme
if (body.classList.contains("dark")) {
    modeText.innerText = "Dark Mode";
} else {
    modeText.innerText = "Light Mode";
}

// Call loadSidebarState on page load
loadSidebarState();


// Call handleImageDisplay on page load to set the initial state of the images
handleImageDisplay();

