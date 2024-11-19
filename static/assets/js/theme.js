(function ($) {
	'use strict';

	/*==== swiper active   ====*/

	new Swiper('.swiper_active', {
		effect: 'defult',
		grabCursor: false,
		speed: 2000,
		direction: 'horizontal',
		slidesPerView: 1,
		spaceBetween: 30,
		freeMode: false,
		mousewheel: false,
		keyboard: true,
		loop: true,
		autoplay: {
			delay: 9000,
			disableOnInteraction: false,
		},
		pagination: {
			el: '.swiper-pagination',
			clickable: true,
			false: 'progressbar',
		},
		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		},
		scrollbar: {
			el: '.scrollbar_false',
			hide: true,
		},

	});


	/*==== WOW active js   ====*/

	new WOW().init();

	/*==== scrollUp  ====*/

	$.scrollUp({
		scrollText: '<i class="fa fa-angle-up"></i>',
		easingType: 'linear',
		scrollSpeed: 900,
		animation: 'fade'
	});

	/*==== Venubox  ====*/
	$('.venobox').venobox({

		numeratio: true,

		infinigall: true

	});

	/*==== One Page Nav  ====*/

	var top_offset = $('.one_page').height() + 0;
	$('.one_page .techsell_menu .nav_scroll').onePageNav({
		currentClass: 'current',
		changeHash: false,
		scrollSpeed: 1000,
		scrollOffset: top_offset,
		scrollThreshold: 0.5,
		filter: '',
		easing: 'swing',
	});

	$(".nav_scroll > li:first-child").addClass("current");

	/*==== sticky nav 1  ====*/
	$('.one_page').scrollToFixed({
		preFixed: function () {
			$(this).find('.scroll_fixed').addClass('prefix');
		},
		postFixed: function () {
			$(this).find('.scroll_fixed').addClass('postfix').removeClass('prefix');
		}
	});

	/*==== sticky nav 2  ====*/
	var headers1 = $('.trp_nav_area');
	$(window).on('scroll', function () {

		if ($(window).scrollTop() > 200) {
			headers1.addClass('hbg2');
		} else {
			headers1.removeClass('hbg2');
		}

	});

	/*==== Mobile Menu  ====*/
	$('.mobile-menu nav').meanmenu({
		meanScreenWidth: "990",
		meanMenuContainer: ".mobile-menu",
		onePage: true,
	});

	/*==== portfolio active ====*/

	var witrbslick = $('.portfolio_act');
	if (witrbslick.length > 0) {
		witrbslick.slick({
			infinite: true,
			autoplay: true,
			autoplaySpeed: 2000,
			speed: 1000,
			slidesToShow: 3,
			slidesToScroll: 1,
			arrows: false,
			dots: true,
			responsive: [{
					breakpoint: 1200,
					settings: {
						slidesToShow: 3,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 992,
					settings: {
						slidesToShow: 3,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 767,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
					}
				}
			]
		});
	}

	/*==== Brand active ====*/

	var witrbslick = $('.brand_active');

	if (witrbslick.length > 0) {

		witrbslick.slick({
			infinite: true,
			autoplay: true,
			default: true,
			autoplaySpeed: 3000,
			speed: 1000,
			slidesToShow: 5,
			slidesToScroll: 1,
			arrows: true,
			dots: false,
			responsive: [{
					breakpoint: 1200,
					settings: {
						slidesToShow: 5,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 992,
					settings: {
						slidesToShow: 4,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 767,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1,
					}
				}
			]
		});
	}


	/*==== testimonial active ====*/

	var witrbtslick = $('.testimonial_active');
	if (witrbtslick.length > 0) {
		witrbtslick.slick({
			infinite: true,
			autoplay: true,
			autoplaySpeed: 3000,
			speed: 1000,
			slidesToShow: 2,
			slidesToScroll: 2,
			arrows: false,
			dots: false,
			responsive: [{
					breakpoint: 1200,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 992,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 767,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
					}
				}
			]
		});
	}

	/*==== testimonial area2 active ====*/

	var witrbtslick = $('.testimonial2_active');
	if (witrbtslick.length > 0) {
		witrbtslick.slick({
			infinite: true,
			autoplay: true,
			autoplaySpeed: 3000,
			speed: 1000,
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			dots: false,
			responsive: [{
					breakpoint: 1200,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 992,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 767,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
					}
				}
			]
		});
	}


	/*==== team area active ====*/

	var witrbslick = $('.team_active');
	if (witrbslick.length > 0) {
		witrbslick.slick({
			infinite: true,
			autoplay: true,
			autoplaySpeed: 3000,
			speed: 700,
			slidesToShow: 3,
			slidesToScroll: 1,
			arrows: true,
			centerMode: false,
			centerPadding: '',
			dots: false,
			responsive: [{
					breakpoint: 1200,
					settings: {
						slidesToShow: 3,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 992,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 767,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
					}
				}
			]
		});
	}


	/*==== feature active ====*/

	var witrbslick = $('.feature_active');

	if (witrbslick.length > 0) {

		witrbslick.slick({
			infinite: true,
			autoplay: true,
			autoplaySpeed: 3000,
			speed: 1000,
			slidesToShow: 3,
			slidesToScroll: 1,
			arrows: true,
			dots: false,
			responsive: [{
					breakpoint: 1200,
					settings: {
						slidesToShow: 3,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 992,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 767,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
					}
				}
			]
		});
	}


	/*==== blog active ====*/

	var witrbslick = $('.blog_grid_active');
	if (witrbslick.length > 0) {
		witrbslick.slick({
			infinite: true,
			autoplay: true,
			autoplaySpeed: 3000,
			speed: 1000,
			slidesToShow: 3,
			slidesToScroll: 1,
			arrows: true,
			dots: false,
			responsive: [{
					breakpoint: 1200,
					settings: {
						slidesToShow: 3,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 992,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1,
					}
				},
				{
					breakpoint: 767,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
					}
				}
			]
		});
	}

	/*==== blog sidebar active ====*/

	$('.blog_sidebar_image_act').slick({

		infinite: true,
		autoplay: true,
		autoplaySpeed: 3000,
		speed: 1000,
		slidesToShow: 1,
		slidesToScroll: 1,
		centerMode: true,
		centerPadding: '',
		arrows: false,
		dots: false,
		responsive: [{
				breakpoint: 1200,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
				}
			},
			{
				breakpoint: 992,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
				}
			},
			{
				breakpoint: 768,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
				}
			}
			// You can unslick at a given breakpoint now by adding:
			// settings: "unslick"
			// instead of a settings object
		]
	});


	/*==== Portfolio Isotope  ====*/

	if ($.fn.isotope) {

		var $portfolio = $('.portfolio_active');

		$portfolio.isotope({

			itemSelector: '.grid-item',

			filter: '*',

			resizesContainer: true,

			layoutMode: 'masonry',

			transitionDuration: '0.8s'

		});


		$('.filter_menu li').on('click', function () {

			$('.filter_menu li').removeClass('current_menu_item');

			$(this).addClass('current_menu_item');

			var selector = $(this).attr('data-filter');

			$portfolio.isotope({

				filter: selector,

			});

		});

	};

	/*==== counter active ====*/

	$('.counter').counterUp({
		delay: 10,
		time: 1000
	});

	/*==== Bootstrap Accordion  ====*/

	$('.faq-part .card').each(function () {
		var $this = $(this);
		$this.on('click', function (e) {
			var has = $this.hasClass('active');
			$('.faq-part .card').removeClass('active show');
			if (has) {
				$this.removeClass('active show');
			} else {
				$this.addClass('active show');
			}
		});
	});


})(jQuery);