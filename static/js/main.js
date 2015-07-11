$(window).load(function() {
  $("body").removeClass("preload");
});

$(document).ready(function() {
	doubleHover('a', 'hover');

  $('.main_list-items-item-price a').priceFormat({
    prefix: '',
    suffix: '&thinsp;$',
    thousandsSeparator: '&thinsp;',
    centsLimit: 0
  });

  $('.fotorama').fotorama({
    maxwidth: '100%',
    minwidth: '620px',
    height: '460px',
    nav: 'thumbs',
    loop: 'true',
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
