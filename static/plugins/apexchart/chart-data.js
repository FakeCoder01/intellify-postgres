


'use strict';

$(document).ready(function () {

	// chart-student-graph
	if ($('#chart-student-graph').length > 0) {
		var options = {
			chart: {
				height: 350,
				type: "area",
				toolbar: {
					show: true
				},
			},
			dataLabels: {
				enabled: false
			},
			stroke: {
				curve: "smooth"
			},
			series: [{
				name: "BEN",
				color: '#D33F49',
				data: [45, 40, 75, 51, 42, 42,]
			},

			{
				name: "MATH",
				color: '#77BA99',
				data: [33, 44, 70, 39, 50, 51,]
			},
			{
				name: "HIS",
				color: '#EFF0D1',
				data: [31, 80, 40, 54, 34, 54,]
			},
			],
			xaxis: {
				categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat',],
			}
		}
		var chartStudent = new ApexCharts(
			document.querySelector("#chart-student-graph"),
			options
		);
		chartStudent.render();

	}

	if ($('#chart-student-graph-bar').length > 0) {
		var optionsBarStu = {
			series: [{
				name: 'My Marks',
				data: [92, 71, 79, 67]
			}, {
				name: 'Class Average',
				data: [80, 77, 78, 76]
			}],
			chart: {
				type: 'bar',
				height: 350
			},
			plotOptions: {
				bar: {
					horizontal: false,
					columnWidth: '55%',
					endingShape: 'rounded'
				},
			},
			dataLabels: {
				enabled: false
			},
			stroke: {
				show: true,
				width: 2,
				colors: ['transparent']
			},
			xaxis: {
				categories: ['Math', 'English', 'Science', 'Sanskrit'],
			},
			yaxis: {
				title: {
					text: 'Marks Secured'
				}
			},
			fill: {
				opacity: 1
			},
			tooltip: {
				y: {
					formatter: function (val) {
						return "$ " + val + " thousands"
					}
				}
			}
		};
		var chartStudentBar = new ApexCharts(document.querySelector("#chart-student-graph-bar"), optionsBarStu);
		chartStudentBar.render();

	}



	// Area chart

	if ($('#apexcharts-area').length > 0) {
		var options = {
			chart: {
				height: 350,
				type: "area",
				toolbar: {
					show: false
				},
			},
			dataLabels: {
				enabled: false
			},
			stroke: {
				curve: "smooth"
			},
			series: [{
				name: "Teachers",
				data: [45, 60, 75, 51, 42, 42, 30]
			}, {
				name: "Students",
				color: '#FFBC53',
				data: [24, 48, 56, 32, 34, 52, 25]
			}],
			xaxis: {
				categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
			}
		}
		var chart = new ApexCharts(
			document.querySelector("#apexcharts-area"),
			options
		);
		chart.render();
	}

	// Bar chart

	if ($('#bar').length > 0) {
		var optionsBar = {
			chart: {
				type: 'bar',
				height: 350,
				width: '100%',
				stacked: true,
				toolbar: {
					show: false
				},
			},
			dataLabels: {
				enabled: false
			},
			plotOptions: {
				bar: {
					columnWidth: '45%',
				}
			},
			series: [{
				name: "Boys",
				color: '#fdbb38',
				data: [420, 532, 516, 575, 519, 517, 454, 392, 262, 383, 446, 551, 563, 421, 563, 254, 452],
			}, {
				name: "Girls",
				color: '#19affb',
				data: [336, 612, 344, 647, 345, 563, 256, 344, 323, 300, 455, 456, 526, 652, 325, 425, 436],
			}],
			labels: [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
			xaxis: {
				labels: {
					show: false
				},
				axisBorder: {
					show: false
				},
				axisTicks: {
					show: false
				},
			},
			yaxis: {
				axisBorder: {
					show: false
				},
				axisTicks: {
					show: false
				},
				labels: {
					style: {
						colors: '#777'
					}
				}
			},
			title: {
				text: '',
				align: 'left',
				style: {
					fontSize: '18px'
				}
			}

		}

		var chartBar = new ApexCharts(document.querySelector('#bar'), optionsBar);
		chartBar.render();
	}

	if ($('#chart').length > 0) {
		var options = {
			series: [14, 23, 21, 17, 15, 10, 12, 17, 21],
			chart: {
				type: 'polarArea',
			},
			labels: ['A+', 'A', 'B', 'B+', 'C', 'C+', 'D', 'D+', 'E'],
			stroke: {
				colors: ['#fff']
			},
			fill: {
				opacity: 0.8
			},
			responsive: [{
				breakpoint: 480,
				options: {
					chart: {
						width: 200
					},
					legend: {
						position: 'bottom'
					}
				}
			}]
		};

		var chart = new ApexCharts(document.querySelector("#chart"), options);
		chart.render();
	}

	if ($('#chart2').length > 0) {
		var options = {
			series: [{
				name: 'Class 10A',
				data: [44, 55, 57]
			}, {
				name: 'Class 10B',
				data: [76, 85, 10]
			}, {
				name: 'Class 10C',
				data: [35, 41, 36]
			}],
			chart: {
				type: 'bar',
				height: 350
			},
			plotOptions: {
				bar: {
					horizontal: false,
					columnWidth: '55%',
					endingShape: 'rounded'
				},
			},
			dataLabels: {
				enabled: false
			},
			stroke: {
				show: true,
				width: 2,
				colors: ['transparent']
			},
			xaxis: {
				categories: ['Maths', 'Physics', 'Chemistry'],
			},
			yaxis: {
				title: {
					text: 'Attendance'
				}
			},
			fill: {
				opacity: 1
			},
			tooltip: {
				y: {
					formatter: function (val) {
						return val + " marks"
					}
				}
			}
		};

		var chart = new ApexCharts(document.querySelector("#chart2"), options);
		chart.render();
	}

	if ($('#chart3').length > 0) {
		var options = {
			series: [{
				name: 'Correct',
				data: [34, 26, 20, 15, 28, 19, 10, 15]
			}],
			chart: {
				height: 350,
				type: 'bar',
			},
			plotOptions: {
				bar: {
					borderRadius: 10,
					dataLabels: {
						position: 'top', // top, center, bottom
					},
				}
			},
			dataLabels: {
				enabled: true,
				formatter: function (val) {
					return val;
				},
				offsetY: -20,
				style: {
					fontSize: '12px',
					colors: ["#304758"]
				}
			},

			xaxis: {
				categories: ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"],
				position: 'top',
				axisBorder: {
					show: false
				},
				axisTicks: {
					show: false
				},
				crosshairs: {
					fill: {
						type: 'gradient',
						gradient: {
							colorFrom: '#D8E3F0',
							colorTo: '#BED1E6',
							stops: [0, 100],
							opacityFrom: 0.4,
							opacityTo: 0.5,
						}
					}
				},
				tooltip: {
					enabled: true,
				}
			},
			yaxis: {
				axisBorder: {
					show: false
				},
				axisTicks: {
					show: false,
				},
				labels: {
					show: false,
					formatter: function (val) {
						return val;
					}
				}

			},
			title: {
				text: "Today's Quiz Analysis, 1st A",
				floating: true,
				offsetY: 330,
				align: 'center',
				style: {
					color: '#444'
				}
			}
		};

		var chart = new ApexCharts(document.querySelector("#chart3"), options);
		chart.render();

	}

	if ($('#chart4').length > 0) {
		var options = {
			series: [{
				name: 'Levels',
				data: [31, 40, 28]
			}],
			chart: {
				height: 280,
				type: 'area'
			},
			dataLabels: {
				enabled: false
			},
			stroke: {
				curve: 'smooth'
			},
		};

		var chart = new ApexCharts(document.querySelector("#chart4"), options);
		chart.render();
	}

	if ($('#chart4').length > 0) {
		var options = {
			series: [
				{
					name: "Maths",
					data: [28, 29, 33, 36, 32, 32, 33]
				},
				{
					name: "Physics",
					data: [18, 22, 30, 27, 32, 32, 30]
				},
				{
					name: "Chemistry",
					data: [12, 11, 14, 18, 17, 13, 13]
				}
			],
			chart: {
				height: 350,
				type: 'line',
				dropShadow: {
					enabled: true,
					color: '#000',
					top: 18,
					left: 7,
					blur: 10,
					opacity: 0.2
				},
				toolbar: {
					show: false
				}
			},
			colors: ['#77B6EA', '#545454', '#00ff00'],
			dataLabels: {
				enabled: true,
			},
			stroke: {
				curve: 'smooth'
			},
			title: {
				text: 'Monthly Quiz Status',
				align: 'left'
			},
			grid: {
				borderColor: '#e7e7e7',
				row: {
					colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
					opacity: 0.5
				},
			},
			markers: {
				size: 1
			},
			xaxis: {
				categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
				title: {
					text: 'Month'
				}
			},
			yaxis: {
				title: {
					text: 'Correctly Solved'
				},
				min: 5,
				max: 40
			},
			legend: {
				position: 'top',
				horizontalAlign: 'right',
				floating: true,
				offsetY: -25,
				offsetX: -5
			}
		};

		var chart = new ApexCharts(document.querySelector("#chart5"), options);
		chart.render();

	}

});