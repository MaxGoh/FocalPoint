(function( $ ) {

		var _durationInterval;

    $.fn.time = function(action, number) {

			var duration = number;

			if ( action === "start") {
				_durationInterval = setInterval(function() {
					console.log(duration);
					if (duration == 0) {
						clearInterval(_durationInterval);
					}
					else {
						duration--;
						$("#time").text(duration)
					}
				}, 1000)
			}

			if ( action === "stop" ) {
				console.log("Timer Stop");
				clearInterval(_durationInterval);
			}

			return duration

    };

	function start() {

	}

	function stop() {
		// Stop Countdown.
	}


	function timeout(duration) {
			setTimeout(function () {
					// Do Something Here
					// Then recall the parent function to
					// create a recursive loop.
					timeout();
			}, 1000);
	}

}( jQuery ));
