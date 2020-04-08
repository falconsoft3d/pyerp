// on ready function
  $(document).ready(function() {
	  "use strict";

	
	//---------- Preloader -section ---------------//
 
	jQuery(window).on('load', function() {
		jQuery("#status").fadeOut();
		jQuery("#preloader").delay(350).fadeOut("slow");
	});
	
	
	//-------------- VENOBOX JS -------------//
            $('.venobox').venobox({
                numeratio: true,
                titleattr: 'data-title',
                titlePosition: 'top',
                spinner: 'wandering-cubes',
                spinColor: '#dbbb0a'
            });
	
	//--------------------up scroll js-----------------------------
			
					$(window).scroll(function() {
						if ($(this).scrollTop() >= 100) {       
							$('#return-to-top').fadeIn(200);   
						} else {
							$('#return-to-top').fadeOut(200);  
						}
					});
					$('#return-to-top').on('click',function() {     
						$('body,html').animate({
							scrollTop : 0                
						}, 500);
					});
												
			//--------------- Scroll to Top end ----------------//

			
			//------------slider js code----------------//			

				function BannerSlider () {
				  var banner = $("#theme-main-banner");
				  if (banner.length) {
					  banner.camera({ //here I declared some settings, the height and the presence of the thumbnails 
						height: '920px',
						navigation: true,
						pagination: true,
						thumbnails: false,
						playPause: false,
						autoplay:true,
						pauseOnClick: false,
						hover: false,
						overlayer: true,
						loader: 'none',
						time: 5000,
						minHeight: '600px',
					  });
				  };
				}


				// -------------slider js code end -------------//

				jQuery(document).on('ready', function(){
					(function($){
						BannerSlider ();
					})(jQuery);
				});
				
				
								
				//-----------Search box jquery------------//

			$( ".searchd" ).on( "click", function() {
			  $( ".searchbox" ).addClass( "open", 1000);
			});

			$( ".close" ).on( "click", function() {
			  $( ".searchbox" ).removeClass( "open", 1000);
			});
					
					
					// Wow js
				$(window).on("load", function() {
						var wow = new WOW({
							boxClass: 'wow',
							animateClass: 'animated',
							offset: 0,
							mobile: true,
							live: true
						});
						wow.init();
					});
			
			
			
			
    //---------------- jQuery SlickNav / Onepage Mobile menu-----------//

    $('.mainmenu').slicknav({
        label: '',
        duration: 700,
        easingOpen: "easeOutBounce",
        prependTo: '#mobileMenu',
        closeOnClick: true
    });

  
	//----------- jQuery MeanMenu / Multipage Mobile menu----------//
    $('.mobile-menu nav').meanmenu({
        meanScreenWidth: "992",
        meanMenuContainer: ".mobile-menu"
    });
	
	
	//------------ Menu js for Position fixed--------------//
				$(window).scroll(function(){
					var window_top = $(window).scrollTop() + 1; 
					if (window_top > 30) {
						$('.transparent-menu').addClass('menu_fixed animated fadeIn');
					} else {
						$('.transparent-menu').removeClass('menu_fixed animated fadeIn');
					}
				});
				
		
					//------------parallex js code----------------//

			
		//---------- service slider js -----------//
	
	$(document).ready(function() {
              $('.service_slider_wrapper .owl-carousel').owlCarousel({
                loop: true,
                margin: 10,
				autoplay:false,
				smartSpeed: 1200,
                responsiveClass: true,
				navText : ['<i class="fa fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-angle-right" aria-hidden="true"></i>'],
                responsive: {
                  0: {
                    items: 1,
                    nav: true
                  },
                  600: {
                    items: 2,
                    nav: true
                  },
                  1000: {
                    items: 3,
                    nav: true,
                    loop: true,
                    margin: 20
                  }
                }
              })
            })

			//---------testimonial js----------//
			
        $(document).ready(function() {
            $('.testi_slider_wrapper .owl-carousel').owlCarousel({
                loop: true,
                margin: 10,
                autoplay: false,
                responsiveClass: true,
                smartSpeed: 1200,
              navText : ['<i class="fa fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-angle-right" aria-hidden="true"></i>'],
                responsive: {
                    0: {
                        items: 1,
                        nav: true
                    },
                    600: {
                        items: 1,
                        nav: true
                    },
                    1000: {
                        items: 1,
                        nav: true,
                        loop: true,
                        margin: 20
                    }
                }
            })
        })

			
			//----------- team slider js -------------//
	
	$(document).ready(function() {
              $('.team_slider_wrapper .owl-carousel').owlCarousel({
                loop: true,
                margin: 10,
				autoplay:false,
				smartSpeed: 1200,
                responsiveClass: true,
				navText : ['<i class="fa fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-angle-right" aria-hidden="true"></i>'],
                responsive: {
                  0: {
                    items: 1,
                    nav: true
                  },
                  600: {
                    items: 2,
                    nav: true
                  },
                  1000: {
                    items: 4,
                    nav: true,
                    loop: true,
                    margin: 20
                  }
                }
              })
            })

	
	
	//*****-----blog slidder wrapper-------******//
			$(document).ready(function() {
            $('.blog_cat_slider_wrapper .owl-carousel').owlCarousel({
                loop: true,
                margin: 10,
                autoplay: true,
                responsiveClass: true,
                smartSpeed: 1200,
                navText : ['<i class="fa fa-long-arrow-left" aria-hidden="true"></i>','<i class="fa fa-long-arrow-right" aria-hidden="true"></i>'],
                responsive: {
                    0: {
                        items: 1,
                        nav: true
                    },
                    600: {
                        items: 1,
                        nav: true
                    },
                    1000: {
                        items: 1,
                        nav: true,
                        loop: true,
                        margin: 20
                    }
                }
            })
        })
			
	
		
			
		 //------------ counter-section------------// 

    $('.counter_section').on('inview', function(event, visible, visiblePartX, visiblePartY) {
        if (visible) {
            $(this).find('.timer').each(function () {
                var $this = $(this);
                $({ Counter: 0 }).animate({ Counter: $this.text() }, {
                    duration: 2000,
                    easing: 'swing',
                    step: function () {
                        $this.text(Math.ceil(this.Counter));
                    }
                });
            });
            $(this).off('inview');
        }
    });
	
			//*******----------partner js--------*********//
		
		$(document).ready(function() {
              $('.partner_slider_wrapper .owl-carousel').owlCarousel({
                loop: true,
                margin: 10,
				autoplay:true,
				smartSpeed: 1200,
                responsiveClass: true,
				navText : ['<i class="fa fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-angle-right" aria-hidden="true"></i>'],
                responsive: {
                  0: {
                    items: 1,
                    nav: true
                  },
                  600: {
                    items: 1,
                    nav: true
                  },
                  1000: {
                    items: 1,
                    nav: true,
                    loop: true,
                    margin: 20
                  }
                }
              })
            })
			
			
			
		 // Parallax background
    $('.jarallax').jarallax({
            speed: 0.5,
    })

			
				//--------- Tweeter Slider---------------//	
							
				$('.btn-vertical-slider').on('click', function () {
					
					if ($(this).attr('data-slide') == 'next') {
						$('#myCarousel').carousel('next');
					}
					if ($(this).attr('data-slide') == 'prev') {
						$('#myCarousel').carousel('prev')
					}

				});
		
				//--------------isotope active--------------//
	

			$(window).load(function() {
				/** this is come when complete page is fully loaded, including all frames, objects and images **/
	
				var $grid = $('.grid').isotope({
				itemSelector: '.grid-item',
				stagger: 30
			  });

			  $('.filter-demo').on( 'click', '.button', function() {
				var filterValue = $(this).attr('data-filter');
				$grid.isotope({ filter: filterValue });
			  });

			  // change is-checked class on buttons

			  $('.filter').each( function( i, buttonGroup ) {
				var $buttonGroup = $( buttonGroup );
				$buttonGroup.on( 'click', '.button', function() {
				  $buttonGroup.find('.is-checked').removeClass('is-checked');
				  $( this ).addClass('is-checked');
				});
			  });
			  
			});
				
			//--------- Contact Form Submition--------------//
			
			
	function checkRequire(formId , targetResp){
		targetResp.html('');
		var email = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/;
		var url = /(http|ftp|https):\/\/[\w-]+(\.[\w-]+)+([\w.,@?^=%&amp;:\/~+#-]*[\w@?^=%&amp;\/~+#-])?/;
		var image = /\.(jpe?g|gif|png|PNG|JPE?G)$/;
		var mobile = /^[\s()+-]*([0-9][\s()+-]*){6,20}$/;
		var facebook = /^(https?:\/\/)?(www\.)?facebook.com\/[a-zA-Z0-9(\.\?)?]/;
		var twitter = /^(https?:\/\/)?(www\.)?twitter.com\/[a-zA-Z0-9(\.\?)?]/;
		var google_plus = /^(https?:\/\/)?(www\.)?plus.google.com\/[a-zA-Z0-9(\.\?)?]/;
		var check = 0;
		$('#er_msg').remove();
		var target = (typeof formId == 'object')? $(formId):$('#'+formId);
		target.find('input , textarea , select').each(function(){
			if($(this).hasClass('require')){
				if($(this).val().trim() == ''){
					check = 1;
					$(this).focus();
					targetResp.html('You missed out some fields.');
					$(this).addClass('error');
					return false;
				}else{
					$(this).removeClass('error');
				}
			}
			if($(this).val().trim() != ''){
				var valid = $(this).attr('data-valid');
				if(typeof valid != 'undefined'){
					if(!eval(valid).test($(this).val().trim())){
						$(this).addClass('error');
						$(this).focus();
						check = 1;
						targetResp.html($(this).attr('data-error'));
						return false;
					}else{
						$(this).removeClass('error');
					}
				}
			}
		});
		return check;
	}
	$(".submitForm").on("click", function() {
		var _this = $(this);
		var targetForm = _this.closest('form');
		var errroTarget = targetForm.find('.response');
		var check = checkRequire(targetForm , errroTarget);
		if(check == 0){
			var formDetail = new FormData(targetForm[0]);
			formDetail.append('form_type' , _this.attr('form-type'));
			$.ajax({
				method : 'post',
				url : 'ajax.php',
				data:formDetail,
				cache:false,
				contentType: false,
				processData: false
			}).done(function(resp){
				if(resp == 1){
					targetForm.find('input').val('');
					targetForm.find('textarea').val('');
					errroTarget.html('<p style="color:green;">Mail has been sent successfully.</p>');
				}else{
					errroTarget.html('<p style="color:red;">Something went wrong please try again latter.</p>');
				}
			});
		}
	});

	
    });