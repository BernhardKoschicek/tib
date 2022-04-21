$(function () {
    $(document).scroll(function () {
        var $nav = $(".navigation");
        var $navtib = $(".navigation-tib");
        var $img = $(".brand-image");
        var $imgtib = $(".brand-image-tib");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
        $img.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
        $navtib.toggleClass('scrolled', $(this).scrollTop() > $navtib.height());
        $imgtib.toggleClass('scrolled', $(this).scrollTop() > $navtib.height());
    });
});

