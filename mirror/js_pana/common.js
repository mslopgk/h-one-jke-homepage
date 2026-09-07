var $winH = $(window).height();
/* -----------------------------------------------------
	레디
----------------------------------------------------- */
var agt = navigator.userAgent.toLowerCase();
$(document).ready(function(){
	topVisualH();
    //ie8 별도처리
    /*
	if ( agt.indexOf("msie 8") != -1 ) {
        spaceSlider2();
        TweenMax.to( $('.slide').find('.bgImg'), .5 , {opacity:0.6, ease:Quad.easeInOut}, '0.15');
		TweenMax.to( $('.slide').find('.visualCont .title_visual'), .5, {opacity:1, left:0, ease:Quad.easeOut}, 0.2);
		TweenMax.to( $('.slide').find('.visualCont .txt'), .5, {opacity:1, left:0, ease:Quad.easeOut}, 0.2);
		TweenMax.to( $('.slide').find('.visualCont .btnArea'), .5, {opacity:1, left:0, ease:Quad.easeOut}, 0.2);
    } else {
    	spaceSlider();	
    }
    */
    spaceSlider();
	
	//공간 네비게이션
	$('.indicator li').click(function(){
		var idx = $(this).index();
		$('#spaceSlide').cycle('pause').cycle(idx);
		return false;
	});
   
	//공간 슬라이드 컨트롤
	$('#spacePause').click(function(){
		$('#spaceSlide').cycle('pause');
		$('#spacePlay').show();
		$('#spacePlay').css('display','block');
		$('#spacePause').hide();
		return false;
	});
	$('#spacePlay').click(function(){
		$('#spaceSlide').cycle('resume');
		$('#spacePause').show();
		$('#spacePlay').hide();
		return false;
	});
	

});	

$(window).load(function(){
	TweenMax.to( $('.slide01').find('.bgImg'), .8 , {opacity:0.8, ease:Quad.easeInOut}, '0.15');
	TweenMax.to( $('.slide01').find('.visualCont .title_visual'), 1, {opacity:1, left:0, delay:.4, ease:Quad.easeOut}, 0.2);
	TweenMax.to( $('.slide01').find('.visualCont .txt'), 1, {opacity:1, left:0, delay:.4, ease:Quad.easeOut}, 0.2);
	TweenMax.to( $('.slide01').find('.visualCont .btnArea'), 1, {opacity:1, left:0, delay:.6, ease:Quad.easeOut}, 0.2);
	
	$('#spaceSlide').cycle('resume');
	
//	topNotiOpen('#liveOnPopup');	//오늘의 공연 오픈
//	chkeckMainNotice();				//공지사항 오픈
	
	//공연 목록 로딩 후 배너 슬라이더 시작
	bannerSlider();
	
	//배너 슬라이드 컨트롤 클릭 이벤트 등록
	$('#bannerPause').click(function(){
		$('.bannerSlider').cycle('pause');
		$('#bannerPlay').show();
		$('#bannerPlay').css('display','block');
		$('#bannerPause').hide();
		return false;
	});
	$('#bannerPlay').click(function(){
		$('.bannerSlider').cycle('resume');
		$('#bannerPause').show();
		$('#bannerPlay').hide();
		return false;
	});
	
	//배너 슬라이드 컨트롤 위치 
	var bannW = $('#bannerNav').width();
	$('#bannerCntrol_play').css('right',bannW);
});


/* -----------------------------------------------------
	리사이즈
----------------------------------------------------- */
$(window).resize(function(){
	topVisualH();
});

/* -----------------------------------------------------
	스크롤
----------------------------------------------------- */
$(window).scroll( function(){
  var scrollTop = $(window).scrollTop();
  if ( scrollTop > 1){
  	$('#spaceSlide').cycle('pause');
  } else if ( scrollTop == 0 ) {
  	$('#spaceSlide').cycle('resume');
  }
});		

//resizetocover
if ( agt.indexOf("msie 8") != -1 ) {
	var min_w = 300; // minimum video width allowed
	var vid_w_orig;  // original video dimensions
	var vid_h_orig;

	$(function() { // runs after DOM has loaded
		
	    vid_w_orig = parseInt($('.bgImg img').width());
	    vid_h_orig = parseInt($('.bgImg img').height());

	    $(window).resize(function () { resizeToCover(); });
	    $(window).trigger('resize');
	});

	function resizeToCover() {
	    $('.bgImg').width($('.topVisual').width());
	    $('.bgImg').height($('.topVisual').height());

	    // use largest scale factor of horizontal/vertical
	    var scale_h = $('.topVisual').width() / vid_w_orig;
	    var scale_v = $('.topVisual').height() / vid_h_orig;
	    var scale = scale_h > scale_v ? scale_h : scale_v;

	    // don't allow scaled width < minimum video width
	    if (scale * vid_w_orig < min_w) {scale = min_w / vid_w_orig;};

	    // now scale the video
	    $('.bgImg img').width(scale * vid_w_orig);
	    // alert($('.bgImg img').width());
	    $('.bgImg img').height(scale * vid_h_orig);
	    // and center it by scrolling the video viewport
	    $('.bgImg').scrollLeft(($('.bgImg img').width() - $('.topVisual').width()) / 2);
	    $('.bgImg').scrollTop(($('.bgImg img').height() - $('.topVisual').height()) / 2);
	};
} 

//비쥬얼 영역 높이
function topVisualH(){
	$winH = $(window).height() - 30;
	var $topVisual = $('.topVisual');
	$topVisual.css('height', $winH);
	$('.topVisualH visualImg').css('height', $winH);
	$('#mainSpace').css('height', $winH);
};

$.fn.cycle.transitions.topSlide = function($cont, $slides, opts) {
	//var slidebg = $slides.find('.bgImg');

	//TweenMax.to( slidebg, 0, {x: 0, y:0, z:0, scale: 1});

	opts.fxFn = function(curr, next, opts, after) {
	    
		TweenMax.to($slides,0,{y:0,zIndex:0});


		$(curr).css('zIndex',10);
		$(next).css('zIndex',2);
		
		TweenMax.to( $(curr), 0.95, {

			y: -( $(curr).height()),

			ease:Expo.easeInOut,
			force3D:true,
			onComplete:function(){
				$(curr).css('zIndex',0);
				TweenMax.to( $(curr).find('.bgImg'),0,{opacity:1});
				$(curr).find('.visualCont > *').css({'left': '', 'opacity': ''});

				TweenMax.to( $(next).find('.bgImg'), .8 , {opacity:0.8, ease:Quad.easeInOut}, '0.15');

				TweenMax.to( $(next).find('.visualCont .title_visual'), 1, {opacity:1, left:0, delay:.4, ease:Quad.easeOut}, 0.2);
				TweenMax.to( $(next).find('.visualCont .txt'), 1, {opacity:1, left:0, delay:.4, ease:Quad.easeOut}, 0.2);
				TweenMax.to( $(next).find('.visualCont .btnArea'), 1, {opacity:1, left:0, delay:.6, ease:Quad.easeOut}, 0.2);

			}
			// overwrite: true

		});

		

		$(next).fadeIn(opts.fadeSpeed, function() {
			after();
		});
	}
}

//메인 공간 슬라이더
function spaceSlider(){
	$('#spaceSlide').cycle({
  		slideResize:true,
  		containerResize:false,
  		width:'100%',
  		fit:1,
		fx: 'topSlide',
		timeout:7000,
		//fadeSpeed:750, 
		before:onBefore,
		after:onAfter,
		// easeIn:'easeOutQuad',
		// easeOut:'easeOutQuad',
		pager:'#spaceSlideNav'
		//onPagerEvent:clickEvt
	}).cycle('pause');
}

//메인 공간 슬라이더 ie8
function spaceSlider2(){
	$('#spaceSlide').cycle({
    	slideResize:true,
    	containerResize:false,
    	width:'100%',
    	fit:1,
		fx: 'fade',
		timeout:6000,
		speed:500,
		//before:onBefore,
		//after:onAfter,
		pager:'#spaceSlideNav'
	}).cycle('pause');
}


//메인 공간 슬라이더 이전 애니메이션
function onBefore(curr, next, opts, ff) {
	var idxCurr = $(this).index();
	var slidebg = $('.slide').find('.bgImg');

	TweenMax.to($(next).find('.bgImg'), 0, {x: 0, y:0, z:0, scale: 1});

}

//메인 공간 슬라이더 이후 애니메이션
function onAfter(curr,next,opts){
	
	var slidebg = $('.slide').find('.bgImg');
	var bg = $(next).find('.bgImg');
	var bgW = bg.width();
	var bgH = bg.height();

	
	//$(this).find('.visualCont').stop().animate({opacity:'1',top:0},950);
	//$(this).find('.overlay').stop(true,true).animate({opacity:'.5'},550);

  TweenMax.to( bg, 10, {
	    css: {
	        scale: 1.1,
	        x: -( bgW * 0.05 ),
	        y: -( bgH * 0.05 ),
	       	z: 0.1,
	        rotationZ: "0.01deg",
	        transformOrigin: "0 0",
	        force3D: true
	    },
	    ease:Linear.easeNone,
	    force3D:true,
	    overwrite: true
	});
	

}


function onAfterBann(curr, next, opts, ff) {
	var idxCurr = $(this).index();
	$('.bannerSlider > div').removeClass('curr');
	$(this).addClass('curr');
};

// //배너 슬라이더
function bannerSlider(){	
// 	console.log("bannerSlider is called");
	$('.bannerSlider').cycle({
		fx: 'none',
		timeout:5000,
		speed:650,
		//before:onbeforeBann,
		after:onAfterBann,
		pager:'#bannerNav',
		prev:'#bannerControl .btnPrev',
  		next:'#bannerControl .btnNext'
	});
};


function resizeHeight(frm){
	frm.style.height="auto";
	contentHeight = frm.contentWindow.document.body.scrollHeight;
	frm.style.height = contentHeight + 4 + "px";
}

