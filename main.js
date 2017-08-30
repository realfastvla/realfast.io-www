$(document).ready(setup);

function setup() {
	$.ajax({
		url: "http://realfast.io/news",
		success: function(response) {
			var position = 0;
			var newsItems = JSON.parse(response);
			fillContent(position, newsItems);
			$("#go-forward").click(function() {
				if (position === newsItems.length - 1) {
					return;
				}
				position += 1;
				//slide next in
				$("#next").animate({
					left: 100
				}, 1000, function() {
					fillContent(position, newsItems);
					$("#next").css("left", "600px");
				});
				$("#curr").animate({
					left: -400
				}, 1000, function() {
					$("#curr").css("left", "100px");
				});
			        $("#prev").animate({
				        left: -900
				}, 1000, function() {
				        $("#prev").css("left", "-400px");
				});
			});
			$("#go-back").click(function() {
				if (position === 0) {
					return;
				}
				position -= 1;
				//slide prev in
				$("#prev").animate({
					left: 100
				}, 1000, function() {
					$("#prev").css("left", "-400px");
				});
				$("#curr").animate({
					left: 600
				}, 1000, function() {
					fillContent(position, newsItems);
					$("#curr").css("left", "100px");
				});
			        $("#next").animate({
				    left: 1100
				}, 1000, function() {
				        $("#next").css("left", "600px")
				});
			});
		}
	});
}

function fillContent(position, items) {
        $("#prev").html("")
        $("#curr").html("")
        $("#next").html("")
	if (items[position - 1]) {
		$("#prev").html(items[position - 1].html);
	}
	$("#curr").html(items[position].html);
	if (items[position + 1]) {
		$("#next").html(items[position + 1].html);
	}
}

