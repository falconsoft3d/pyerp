//Team chart
    var ctx = document.getElementById("team-chart");
    ctx.height = 150;
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["2013", "2014", "2015", "2016", "2017", "2018"],
            type: 'line',
            defaultFontFamily: 'PT Sans',
            datasets: [{
                data: [0, 3, 1, 3, 0, 3],
                label: "Expense",
                backgroundColor: 'transparent',
                borderColor: '#ddbb00',
                borderWidth: 2,
                pointStyle: 'circle',
                pointRadius: 3,
                pointBorderColor: '#ddbb00',
                pointBackgroundColor: '#ddbb00',
                    }] 
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: true,
            },
            legend: {
                position: 'top',
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                },


            },
            scales: {
                xAxes: [{
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Month'
                    }
                        }],
                yAxes: [{
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                        }]
            },
            title: {
                display: false,
            }
        }
    });