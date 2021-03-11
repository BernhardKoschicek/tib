$(".jumbotron").css({ height: $(window).height() + "px" });

$(window).on("resize", function() {
  $(".jumbotron").css({ height: $(window).height() + "px" });
});



$(document).ready(function(){
  $('.nav-button').click(function(){
	$('body').toggleClass('nav-open');
  });
});
