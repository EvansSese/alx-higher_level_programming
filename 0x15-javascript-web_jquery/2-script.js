$(document).ready(function () {
  // Select the <header> element using the jQuery selector
  var header = $("header");
  
  // Select the <div id="red_header"> element using the jQuery selector
  var redHeaderDiv = $("#red_header");

  redHeaderDiv.on("click", function () {
      // Update the text color of the <header> element to red (#FF0000)
      header.css("color", "#FF0000");
  });
});
