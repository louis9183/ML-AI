
function onPageLoad(){
   //console.log("document loaded");
   var url = "http://127.0.0.1:5000/get_location_names"; 
       $.Get(url, function(data, status){
	//console.log("got response for get_location_namesn request")
	if(data){
		var locations = data.locations;
		var uiLocation = document.getElementById("uilocation");
		$('#uiLocations').empty();
		for (var i in locations){
			var opt = new Option(locations[i]);
			$('#uiLocations').append(opt); 
		}
	}

 }
);   
}

window.onload = onPageLoad; 