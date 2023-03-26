

    function goToDashboard(sectionCount, tableCount) {
    if (sectionCount > 0 && tableCount > 0) {
    // If there is at least one section and one table, redirect to the dashboard
    window.location.href = '{% url "dashboard:index" %}';
} else {
    // Otherwise, show an alert asking the user to create a section and table
    alert('Please add at least 1 table and section to continue.');
}
}

