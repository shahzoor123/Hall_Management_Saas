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

      var events = document.getElementById("h1");
      var value = events.dataset.myVariable;
      console.log(value);

      var formattedEvents = serializedEvents.map(function (event) {
          return {
              title: event.fields.customer_name,
              start: event.fields.event_date,
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
            n.removeClass("was-validated");
            n[0].reset();
            l = e.event;
            v("#event-title").val(l.title);
            v("#start_date").val(l.start.toISOString().split('T')[0]); // Set the start date
            v("#end_date").val(l.end.toISOString().split('T')[0]); // Set the end date
            v("#event-time").val(l.start.toISOString().split('T')[1].slice(0, 5)); // Set the event time
            i = null;
            t.text("Edit Event");
            i = null;
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



