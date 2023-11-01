$(document).ready(function () {
  $("#btn_translate").on("click", function () {
      fetchTranslation();
  });

  $("#language_code").on("keyup", function (event) {
      if (event.keyCode === 13) {
          fetchTranslation();
      }
  });

  function fetchTranslation() {
      // Get the language code entered by the user
      var languageCode = $("#language_code").val();

      // Fetch the translation from the provided API service
      $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
          // Display the translation in the <div id="hello"> element
          $("#hello").text(data.hello);
      });
  }
});
