$(document).ready(function () {
  // Use the jQuery selector to select the <header> element
  var header = $("header");

  // Check if the <header> element was found
  if (header.length > 0) {
      // Update the text color to red (#FF0000)
      header.css("color", "#FF0000");
  }
});
