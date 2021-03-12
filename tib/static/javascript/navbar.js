$(function () {
  $(document).scroll(function () {
    var $nav = $(".navigation");
    var $img = $(".brand-image");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    $img.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});
