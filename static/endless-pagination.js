// doubleHover by artpolikarpov
$(document).ready(function() {
  doubleHover('a', 'hover');
});

var doubleHover = function(selector, hoverClass) {
  $(document).on('mouseover mouseout', selector, function(e) {
    $(selector)
      .filter('[href="' + $(this).attr('href') + '"]')
      .toggleClass(hoverClass, e.type == 'mouseover');
  });
}
