$(document).ready(function () {
  // Select the <header> element using jQuery
  const $header = $("header");

  if ($header.length) {
      // Update the text color to red (#FF0000)
      $header.css("color", "#FF0000");
  }
});
