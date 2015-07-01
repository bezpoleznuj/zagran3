$(document).ready(function() {
	doubleHover('a', 'hover');

  $('.main_list-items-item-price a').priceFormat();

  $('.fotorama').fotorama({
    maxwidth: '100%',
    nav: 'thumbs',
    allowfullscreen: 'true'
  });


  $('.main_list-btn_more').click()
});


// «doubleHover» by artpolikarpov
var doubleHover = function(selector, hoverClass) {
	$(document).on('mouseover mouseout', selector, function(e) {
		$(selector)
			.filter('[href="' + $(this).attr('href') + '"]')
			.toggleClass(hoverClass, e.type == 'mouseover');
	});

}
