$(function() {
    'use srtrict';
    // ajust the height of a slider
    var winH = $(window).height();
    var headerH = $('.header-main').innerHeight();
    $('.slide-main').height(winH - headerH);
});