// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

const renderChart=(data,labels)=>{
var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: labels,
        datasets: [{
            data: data,
            backgroundColor: ['#4e73df', '#1cc88a'],
            hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
            hoverBorderColor: "rgba(234, 236, 244, 1)",
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
};

const getChartData=()=>{
    console.log('fetching');
    fetch('/pay_this_month')
    .then(res=>res.json())
    .then(results=>{
        console.log('results', results);
        const pay_data = results.pay_data;
        const [labels,data] = [
            Object.keys(pay_data),
            Object.values(pay_data),
        ];

        renderChart(data, labels)
    });
};

document.onload=getChartData();