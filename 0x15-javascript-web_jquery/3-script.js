$(document).ready(function () {
  // Select the <header> element using the jQuery selector
  var header = $("header");
  
  // Select the <div id="red_header"> element using the jQuery selector
  var redHeaderDiv = $("#red_header");

  redHeaderDiv.on("click", function () {
      // Add the class "red" to the <header> element
      header.addClass("red");
  });
});
