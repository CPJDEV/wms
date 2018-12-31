$(function(){
	$(".max_imize").bind("click",maximizeWHView);
	$(".min_imize").bind("click",minimizeWHView);

	initWarehouseConfiguration();
	// document.body.appendChild(createBarrel());

})

function initWarehouseConfiguration(){
    $(".view_wh").animate({"height": ($(window).height() - 150) +"px"});
	var wh_wid = $(".view_wh").width();
	var aisles = $(".aisle");
	var aisle_shelf = $(".aisle .shelf");
	$.each(aisle_shelf,function(){
		if($(this).children("li").length < 1)
			$(this).remove();
	})

	$.each(aisles,function(i){
		var aisle_shelf = $(this).children(".shelf")
		var div_ider = aisle_shelf.length > 1 ? 1.2 : .5
		$(this).css({"width":( wh_wid / (aisles.length / div_ider ) ) - 15+"px"})
	});
}

function maximizeWHView(){
    $(".view_wh").css({"position":"absolute"});
	$(".view_wh").animate({"width":"100%","height":"100%","top":"0px","left":"0","z-index":5555});
	$(".inner_wh").animate({"height":"100%"});
	$(".min_imize").show();
	setTimeout(function(){
		initWarehouseConfiguration();
	},500);
}


function minimizeWHView(){
    $(".view_wh").css({"position":"relative"});
	$(".view_wh").animate({"width":"98%","height": ($(window).height() - 150) +"px","left":"1%","z-index":5});
	$(".inner_wh").animate({"height":"100%"});
	$(this).hide();
}

var DRUM_TEXTURE = "https://keithclark.co.uk/labs/css-fps/drum2.png";

// Assembiles are for grouping faces and other assembiles
function createAssembly() {
    var assembly = document.createElement("div");
    assembly.className = "threedee assembly";
    return assembly;
}

function createFace(w, h, x, y, z, rx, ry, rz, tsrc, tx, ty) {
    var alpha = Math.cos(rx/1.5) * Math.cos(ry/2),
        grad = "linear-gradient(rgba(0,0,0," + alpha.toFixed(2) +"),rgba(0,0,0," + alpha.toFixed(2) +"))",
        face = document.createElement("div");
    face.className = "threedee face";
    face.style.cssText = PrefixFree.prefixCSS(
        "background: " + grad + ", url(" + tsrc + ") -" + tx.toFixed(2) + "px " + ty.toFixed(2) + "px;" +
        "mask-image: url(" + tsrc + ");" +
        "mask-position: -" + tx.toFixed(2) + "px " + ty.toFixed(2) + "px;" +
        "width:" + w.toFixed(2) + "px;" +
        "height:" + h.toFixed(2) + "px;" +
        "margin-top: -" + (h / 2).toFixed(2) + "px;" +
        "margin-left: -" + (w / 2).toFixed(2) + "px;" +
        "transform: translate3d(" + x.toFixed(2) + "px," + y.toFixed(2) + "px," + z.toFixed(2) + "px)" +
        "rotateX(" + rx.toFixed(2) + "rad) rotateY(" + ry.toFixed(2) + "rad) rotateY(" + rz.toFixed(2) + "rad);");
    return face;
}

function createTube(dia, height, sides, texture) {
    var tube = createAssembly();
    var sideAngle = (Math.PI / sides) * 2;
    var sideLen = dia * Math.tan(Math.PI/sides);
    for (var c = 0; c < sides; c++) {
        var x = Math.sin(sideAngle * c) * dia / 2;
        var z = Math.cos(sideAngle * c) * dia / 2;
        var ry = Math.atan2(x, z);
        tube.appendChild(createFace(sideLen + 1, height, x, 0, z, 0, ry, 0, texture, sideLen * c, 0));
    }
    return tube;
}

function createBarrel() {
    var barrel = createTube(100, 196, 25, DRUM_TEXTURE);
    barrel.appendChild(createFace(100, 100, 0, -98, 0, Math.PI / 2, 0, 0, DRUM_TEXTURE, 0, 100));
    barrel.appendChild(createFace(100, 100, 0, 98, 0, -Math.PI / 2, 0, 0, DRUM_TEXTURE, 0, 100));
    return barrel;
}

