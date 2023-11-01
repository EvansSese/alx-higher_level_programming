$(document).ready(function () {
  // Select the <header> element using the jQuery selector
  var header = $("header");

  // Select the <div id="toggle_header"> element using the jQuery selector
  var toggleHeaderDiv = $("#toggle_header");

  toggleHeaderDiv.on("click", function () {
      // Toggle the class "red" and "green" on the <header> element
      header.toggleClass("red green");
  });
});
