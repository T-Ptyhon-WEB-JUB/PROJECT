$(function() {
    'use srtrict';
    // ajust the height of a slider
    var winH = $(window).height();
    var headerH = $('.header-main').innerHeight();
    $('.slide, .carousel-item').height(winH - headerH);
});