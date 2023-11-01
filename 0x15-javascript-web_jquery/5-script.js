$(document).ready(function () {
  // Select the <ul class="my_list"> element using the jQuery selector
  var myList = $("ul.my_list");
  
  // Select the <div id="add_item"> element using the jQuery selector
  var addItemDiv = $("#add_item");

  addItemDiv.on("click", function () {
      // Create a new <li> element with the text "Item"
      var newItem = $("<li>Item</li>");

      // Add the new <li> element to the <ul class="my_list"> element
      myList.append(newItem);
  });
});
