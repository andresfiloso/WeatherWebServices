var consulta = $("#searchTable").DataTable();

$("#inputBusqueda").keyup(function(){
	consulta.search($(this).val()).draw();

	

	if ($("#inputBusqueda").val() == ""){
		
		$("#search").hide();

	} else {
		$("#search").fadeIn("slow");
	}
/*
	if (e.keyCode==27){
		$("header").css({
			"height": "",
			"background": ""
		})

		$("#search").hide()
	}
*/
})


var fila = 0;
function pulsar(e) {
 	tab = document.getElementById('searchTable');
 	filas = tab.getElementsByTagName('tr');
	proc = document.getElementsByTagName('a');

 	if (e.keyCode==38 && fila>0) num=-1;
 	 else if(e.keyCode==40 && fila<filas.length-1) num=1;

	 else if (e.keyCode==13 && fila>0) window.location=(proc[fila-1]);
	 else return;
	  	filas[fila].style.background = 'white';
 	fila+=num;
 	filas[fila].style.background = 'lightgrey';

 }
