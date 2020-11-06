// Accardion menu
$(".sub-menu ul").hide();
$(".sub-menu a").click(function () {
  $(this).parent(".sub-menu").children("ul").slideToggle("100");
  $(this).find(".right").toggleClass("fa-caret-up fa-caret-down");
});

// Slider

$(function () {
  /*
  - how to call the plugin:
  $( selector ).cbpFWSlider( [options] );
  - options:
  {
    // default transition speed (ms)
    speed : 500,
    // default transition easing
    easing : 'ease'
  }
  - destroy:
  $( selector ).cbpFWSlider( 'destroy' );
  */

  $("#cbp-fwslider").cbpFWSlider();
});
