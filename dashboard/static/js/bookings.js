document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');

    fetch('/dashboard/get_calendar_data/')
        .then((response) => response.json())
        .then((resources) => {
            // Initialize FullCalendar with the fetched resources
            let calendar = new FullCalendar.Calendar(calendarEl, {
                // ...other calendar options...
                resources: resources,
                schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
                editable: true,
                eventResizableFromStart: true,
                eventResizableFromEnd: true,
                handleWindowResize: 'true',
                headerToolbar: {
                    left: 'today prev,next',
                    center: 'title',
                    right: 'resourceTimelineDay,resourceTimelineWeek'
                },
                titleFormat: { // Add this to customize the title format
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric',
                    weekday: 'long',
                },
                slotMinTime: '12:00:00', // Start at 12:00 PM
                slotMaxTime: '20:00:00', // End at 7:30 PM
                slotDuration: '00:15:00',
                slotLabelInterval: '00:30:00',
                nowIndicator: 'true',
                resourceAreaHeaderContent: 'Section',
                height: 'auto',
                width: 'auto',
                // contentHeight: '100%',
                resourceAreaWidth: '15%',
                aspectRatio: 1.6,
                initialView: 'resourceTimelineDay',
                businessHours: [ // specify an array instead
                    {
                        daysOfWeek: [1, 2, 3, 4], // Monday, Tuesday, Wednesday, Thursday
                        startTime: '12:00', // 12:00pm
                        endTime: '19:00' // 7:00pm
                    },
                    {
                        daysOfWeek: [5, 6], // Friday, Saturday
                        startTime: '12:00', // 12:00pm
                        endTime: '19:30' // 7:30pm
                    },
                    {
                        daysOfWeek: [0], // Sunday
                        startTime: '12:00', // 12:00pm
                        endTime: '17:00' // 5:00pm
                    }
                ],
                resourceGroupField: 'section',
                events: [
                ],

                eventContent: function (info) {
                    return {
                        html: '<b>' + info.event.title + '</b><br>' + info.event.extendedProps.description,
                        class: 'my-event-class'
                    };
                },

                eventClick: function (info) {
                    alert('Event: ' + info.event.title + '\nStart: ' + info.event.start + '\nEnd: ' + info.event.end);
                    // display more information about the event
                }
            });

            calendar.render();
        });
});

