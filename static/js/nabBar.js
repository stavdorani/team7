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


$(function(){
  var dtToday = new Date();
  
  var month = dtToday.getMonth() + 1;
  var day = dtToday.getDate();
  var year = dtToday.getFullYear();
  if(month < 10)
      month = '0' + month.toString();
  if(day < 10)
      day = '0' + day.toString();
  
  var minDate= year + '-' + month + '-' + day;

  $('#txtDate').attr('min', minDate);
});

function deleteRow(el) {
  if (!confirm("אתה בטוח רוצה למחוק את הטרמפ שיצרת?")) return;
  var tbl = el.parentNode.parentNode.parentNode;
  var row = el.parentNode.parentNode.rowIndex;
  tbl.deleteRow(row);
}
// example addRow
function addRow() {
  // ....
  // ....
  //onclick event
  btn.setAttribute('onclick', 'deleteRow(this)');
  cell4.appendChild(btn);
  //...
}