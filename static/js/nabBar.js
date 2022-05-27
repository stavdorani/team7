$(document).ready(function () {

  $(".nav_btn").click(function(){
    $("#nav").toggle(500);
  });

  $(window).resize(function(){
    if ($(window).width() <= 640){  
      $("#nav").css("display","none");
    } 
    if ($(window).width() >= 641){  
      $("#nav").css("display","block");
    } 
  });

});