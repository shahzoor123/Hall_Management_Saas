
// Calender
    
var formattedEvents = serializedEvents.map(function (event) {
        return {
            title: event.fields.event_title,
            start: event.fields.start_date,
    
        };
    });


  document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    
    var calendar = new FullCalendar.Calendar(calendarEl, {
      themeSystem: 'bootstrap',
      initialView: 'dayGridMonth',
      events: formattedEvents,
    });
    calendar.render();
  });




// Sales bar chart

var montly_sale = document.getElementById("sale").getAttribute("data-my-variable");

// // Parse the values as JSON arrays
var totalSales = JSON.parse(montly_sale);

const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

const salesChartMonthlyCtx = document.getElementById('salesChartMonthly').getContext('2d');

const expenseHeadsCtx = document.getElementById('expense-heads').getContext('2d');

const salesChartMonthly = new Chart(salesChartMonthlyCtx, {
    type: 'bar',
    data: {
        labels: months,
        datasets: [{
            label: 'Monthly Sales',

            data: totalSales,
            backgroundColor: [

                'rgba(51, 255, 189, 0.5)'
            ],
            borderColor: [

                'rgba(0, 0, 0, 0.5)'
            ],
            borderWidth: 2

        }],
    },
});





// Expense heads Pie Chart

var month_event_expense = document.getElementById("month_event_expense").getAttribute("data-my-variable");

const heads = ['Construction and repairs', 'Daily expensess' , 'Other expenses', 'Salaries', 'Event expense'];
const expenseHeads = new Chart(expenseHeadsCtx, {
    type: 'pie',
    data: {
        // labels: heads,
        datasets: [{
            // label: 'Monthly Sales',
            data: [151484,150484,111184,month_event_expense,50844],
            backgroundColor: [

                '#99CCCC',
                '#CC3333',
                '#336699',
                '#33CC33',
                '#FF9933'


            ],
            hoverBackgroundColor: ['lightcoral'],
            innerRadius: .1, // Adjust the inner radius as needed
            outerRadius: .1, // Adjust the outer radius to 50 pixels
            borderWidth: 0
        }],
    },

});




// Area Chart For Expense



var montly_expense = document.getElementById("expense").getAttribute("data-my-variable");

var totalExpense = JSON.parse(montly_expense);

console.log(totalExpense)

// Create the chart options
var options1 = {
    chart: { type: "area", sparkline: { enabled: true } },
    series: [{ data: totalExpense }],
    stroke: { curve: "smooth", width: 2 },
    colors: ["#525ce5"],
    tooltip: {
        fixed: { enabled: false },
        x: { show: false },
        y: {
            title: {
                formatter: function (e) {
                    return "";
                },
            },
        },
        marker: { show: false },
    },
};

// Function to set the chart height based on screen width
function setChartHeight(chart) {
    var chartHeight = window.innerWidth >= 1800 ? 250 : 80;
    chart.updateOptions({
        chart: {
            height: chartHeight
        }
    });
}

// Create and render the chart
var chart = new ApexCharts(document.querySelector("#stastics-chartss"), options1);

chart.render();

// Call the setChartHeight function initially
setChartHeight(chart);

// Update the chart height when the window is resized
window.addEventListener('resize', function () {
    setChartHeight(chart);
});


