package soap.services.impl;


import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.List;

import org.json.JSONArray;
import org.json.JSONObject;

import soap.beans.Pronostico;
import soap.beans.Temperatura;
import soap.services.definition.PronosticoService;


public class PronosticoServiceImpl implements PronosticoService {
	
	@Override
	public Temperatura[] traerClima(String ciudad){
		String apikey = "a36d2a1bb3f074384d58c8528d14f05f";
		
		Pronostico pronostico = new Pronostico();
		List<Temperatura> temperaturas = new ArrayList<Temperatura>();
		try{
			URL url = new URL("http://api.openweathermap.org/data/2.5/forecast?q="+ciudad+"&units=metric&appid="+apikey);
			InputStream is = url.openStream();
			BufferedReader rd = new BufferedReader(new InputStreamReader(is, Charset.forName("UTF-8")));
			StringBuilder sb = new StringBuilder();
		    int cp;
		    while ((cp = rd.read()) != -1) {
		      sb.append((char) cp);
		    }
		    String jsonText = sb.toString();
		    String str = "{ \"number\": [3, 4, 5, 6] }";
		    
		    //Trabajando con el JSON obtenido
		    //Declaracion de variables
		    Temperatura temperatura = new Temperatura();
		    int tempCantidad = 0;
		    double tempAux_min = 0;
		    double tempAux_max = 0;
		    String estadoAux = "";
		    String fechaAux = "";
		    try {
		    	JSONObject json = new JSONObject(jsonText);
		    	JSONArray list = json.getJSONArray("list");
		    	int idCiudad = json.getJSONObject("city").getInt("id");
		    	String nombreCiudad = json.getJSONObject("city").getString("name");
		    	pronostico.setIdCiudad(idCiudad);
		    	//Comienzo a iterar sobre elementos del JSON
		    	for(int i=0 ; i<list.length() ; i++){
		    		if(!fechaAux.equals(list.getJSONObject(i).getString("dt_txt").substring(0, 10)) || i==list.length()-1){ //Si itera sobre el ultimo elemento
		    			//Instancio objeto temperatura con las variables que ya tengo y las agrego a la lista
		    			temperatura.setCiudad(nombreCiudad);
		    			temperatura.setFecha(fechaAux);
		    			temperatura.setTempMinima((int)(Math.round(tempAux_min/tempCantidad)));
		    			temperatura.setTempMaxima((int)(Math.round(tempAux_max/tempCantidad)));
		    			temperatura.setEstado(estadoAux);
		    			if(!fechaAux.equals("")) temperaturas.add(temperatura);
		    			//Reinicializo variables para iterar con la siguiente fecha
		    			temperatura = new Temperatura();
		    			fechaAux = list.getJSONObject(i).getString("dt_txt").substring(0, 10);
		    			tempCantidad = 0;
		    			tempAux_min = 0;
		    			tempAux_max = 0;
		    		}
		    		if(fechaAux.equals(list.getJSONObject(i).getString("dt_txt").substring(0, 10))){
		    			tempCantidad++;
		    			tempAux_min += (list.getJSONObject(i).getJSONObject("main").getDouble("temp_min"));
		    			tempAux_max += (list.getJSONObject(i).getJSONObject("main").getDouble("temp_max"));
		    			estadoAux = list.getJSONObject(i).getJSONArray("weather").getJSONObject(0).getString("description");
		    		}
		    	}
		    	//JSONArray json = new JSONArray(str);
		    } finally {
		      is.close();
		      rd.close();
		    }
		}
		catch(Exception e){
			System.out.println(e.getMessage());
		}
		return temperaturas.toArray(new Temperatura[temperaturas.size()]);
	}

}
