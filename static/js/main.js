document.addEventListener('DOMContentLoaded', function() {
    const categoryChartCanvas = document.getElementById('categoryChart');
    const dailyChartCanvas = document.getElementById('dailyChart');

    if (categoryChartCanvas || dailyChartCanvas) {
        fetch('/api/progress-data/')
            .then(response => response.json())
            .then(data => {
                if (categoryChartCanvas && data.category_chart.labels.length > 0) {
                    createCategoryChart(data.category_chart);
                }
                if (dailyChartCanvas && data.daily_chart.labels.length > 0) {
                    createDailyChart(data.daily_chart);
                }
            })
            .catch(error => console.error('Error fetching progress data:', error));
    }

    function createCategoryChart(chartData) {
        new Chart(categoryChartCanvas, {
            type: 'doughnut',
            data: {
                labels: chartData.labels,
                datasets: [{
                    label: 'Completed Challenges',
                    data: chartData.data,
                    backgroundColor: [
                        'rgba(59, 130, 246, 0.7)',
                        'rgba(239, 68, 68, 0.7)',
                        'rgba(245, 158, 11, 0.7)',
                        'rgba(16, 185, 129, 0.7)',
                        'rgba(139, 92, 246, 0.7)',
                    ],
                    borderColor: '#1f2937',
                    borderWidth: 3
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            color: '#e5e7eb'
                        }
                    },
                    title: {
                        display: false
                    }
                }
            }
        });
    }

    function createDailyChart(chartData) {
        new Chart(dailyChartCanvas, {
            type: 'line',
            data: {
                labels: chartData.labels,
                datasets: [{
                    label: 'Completed per Day',
                    data: chartData.data,
                    fill: true,
                    backgroundColor: 'rgba(59, 130, 246, 0.2)',
                    borderColor: 'rgba(59, 130, 246, 1)',
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            color: '#9ca3af',
                            stepSize: 1
                        },
                        grid: {
                            color: '#374151'
                        }
                    },
                    x: {
                        ticks: {
                            color: '#9ca3af'
                        },
                        grid: {
                            color: '#374151'
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }
});
