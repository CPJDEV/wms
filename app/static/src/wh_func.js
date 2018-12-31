$(function(){

	$(".max_imize").bind("click",maximizeWHView);

	initWarehouseConfiguration();
})

function initWarehouseConfiguration(){
	var wh_wid = $(".view_wh").width();
	var aisles = $(".aisle");
	var aisle_shelf = $(".aisle .shelf");
	$.each(aisle_shelf,function(){
		if($(this).children("li").length < 1)
			$(this).remove();
	})

	$.each(aisles,function(i){
		var aisle_shelf = $(this).children(".shelf")
		var div_ider = aisle_shelf.length > 1 ? .9 : .5
		$(this).css({"width":( wh_wid / (aisles.length / div_ider ) ) - 15+"px"})
	});
}

function maximizeWHView(){
	$(".view_wh").animate({"width":"100%","height":"100%","top":"0px","margin-left":"0px","z-index":5555});
	$(".inner_wh").animate({"height":"100%"});
	setTimeout(function(){
		initWarehouseConfiguration();
	},500);
}