$(function() {
    $("#draggable").draggable( {
      revert: "invalid"

    });
    $("#droppable").droppable({
        over: function(event, ui) {
            $(this).css("background-color", "red"); 
          },
          out: function(event, ui) {
            $(this).css("background-color", ""); 
          },
        drop: function(event, ui) {
        $(this)
          .addClass("ui-state-highlight")
          .find("p")
          .html("Dropped!");
          $(this).css("background-color", "");
      }
    });
  });
