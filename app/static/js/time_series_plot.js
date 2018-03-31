var chart;

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
function requestData() {
    $.ajax({
	    url: '/../dashboard/raw_data',
		success: function(point) {
		var series = chart.series[0],
		    shift = series.data.length > 240; // shift if the series is
		// longer than 240 (240*5s = 1500s = 20 minutes of data)

		// add the point
		chart.series[0].addPoint(point, true, shift);

		// call it again after one 5s
		setTimeout(requestData, 5000);
	    },
		cache: false
		});
}

$(document).ready(function() {
	chart = new Highcharts.Chart({
		chart: {
		    renderTo: 'data-container',
		    defaultSeriesType: 'spline',
		    events: {
			load: requestData
		    }
		},
		title: {
		    text: 'Tweets per second mentioning bitcoin'
		},
		xAxis: {
		    type: 'datetime',
		    tickPixelInterval: 150,
		    maxZoom: 20 * 1000
		},
		yAxis: {
		    minPadding: 0.2,
		    maxPadding: 0.2,
		    title: {
			text: 'Tweets Per Second',
			margin: 80
		    }
		},
		series: [{
			name: 'Tweets Per Second',
			data: []
		    }]
	    });
    });