!(function (v) {
  "use strict";
  function e() { }
  (e.prototype.init = function () {
      var a = v("#event-modal"),
          t = v("#modal-title"),
          n = v("#form-event"),
          l = null,
          i = null,
          r = document.getElementsByClassName("needs-validation"),
          e = new Date(),
          s = e.getDate(),
          d = e.getMonth(),
          y = e.getFullYear();

      new FullCalendarInteraction.Draggable(
          document.getElementById("external-events"),
          {
              itemSelector: ".external-event",
              eventData: function (e) {
                  return { title: e.innerText, className: v(e).data("class") };
              },
          }
      );

 

      var formattedEvents = serializedEvents.map(function (event) {
          return {
              title: event.fields.event_title,
              start: event.fields.start_date,
      
          };
      });

      var calendarEl = document.getElementById('calendar');
      var calendar = new FullCalendar.Calendar(calendarEl, {
          plugins: ["bootstrap", "interaction", "dayGrid", "timeGrid"],
          editable: true,
          droppable: true,
          selectable: true,
          defaultView: "dayGridMonth",
          themeSystem: "bootstrap",
          header: {
              left: "prev,next today",
              center: "title",
              right: "dayGridMonth,timeGridWeek,timeGridDay,listMonth",
          },
          events: formattedEvents,

          eventClick: function (e) {
            a.modal("show");

            
            var value = serializedEvents;

            console.log(typeof(value));
            l = e.event;

            var customerName = l.title;
            var eventDate = l.start.toISOString().split('T')[0];
            var eventTime = 'Night'; // Access the title of the clicked event



            
                    // Search for the event with a matching 'customerName'
            var eventTime = null;
            for (var i = 0; i < value.length; i++) {
                var event = value[i].fields;
                if (event.event_title === customerName) {
                  eventTime = event.event_time;
                  break;
                }
              }
              
              if (eventTime !== null) {
                console.log("Event time for " + customerName + ": " + eventTime);
              } else {
                console.log("Event not found for customer: " + customerName);
              }
                    
      
            console.log(customerName);
            console.log(eventDate);
            console.log(eventTime);

            v("#Customer_Name").val(customerName);
            v("#Event_Date").val(eventDate); // Set the start date
            // v("#end_date").val(l.end.toISOString().split('T')[0]); // Set the end date
            v("#Event_Time").val(eventTime); // Set the event time
        },
        
          dateClick: function (e) {
              o(e);
          }
      });

      calendar.render();

      function o(e) {
          a.modal("show");
          n.removeClass("was-validated");
          n[0].reset();
          v("#event-title").val();
          v("#start_date").val();
          v("#end_date").val();
          t.text("Add Event");
          i = e;
      }

  v(n).on("submit", function (e) {
    e.preventDefault();
    v("#form-event :input");
    var t = v("#event-title").val();
    var start_date = v("#start_date").val();
    var end_date = v("#end_date").val();
    var event_time = v("#event-time").val();

    if (!r[0].checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
        r[0].classList.add("was-validated");
    } else {
        var newEvent = {
            title: t,
            start: start_date + "T" + event_time + ":00",
            end: end_date + "T" + event_time + ":00",
            allDay: false,
            className: "bg-success" // You can set the class name here, or use the existing class from the event
        };

        if (l) {
            // Update existing event
            l.setProp("title", t);
            l.setStart(start_date + "T" + event_time + ":00");
            l.setEnd(end_date + "T" + event_time + ":00");
            l.setProp("classNames", [newEvent.className]);
        } else {
            // Create new event
            calendar.addEvent(newEvent);
        }

        a.modal("hide");
    }
});


      v("#btn-delete-event").on("click", function (e) {
          if (l) {
              l.remove();
              l = null;
              a.modal("hide");
          }
      });

      v("#btn-new-event").on("click", function (e) {
          o({ date: new Date(), allDay: true });
      });
  });

  (v.CalendarPage = new e()), (v.CalendarPage.Constructor = e);
})(window.jQuery);

(function () {
  "use strict";
  window.jQuery.CalendarPage.init();
})();



