package soap.beans;

import java.util.ArrayList;
import java.util.List;

public class Pronostico {
	
	private int idCiudad;
	private List<Temperatura> temperaturas;

	public Pronostico(){
		temperaturas = new ArrayList<Temperatura>();
	}

	public int getIdCiudad() {
		return idCiudad;
	}

	public void setIdCiudad(int idCiudad) {
		this.idCiudad = idCiudad;
	}

	public List<Temperatura> getTemperaturas() {
		return temperaturas;
	}

	public void setTemperaturas(List<Temperatura> temperaturas) {
		this.temperaturas = temperaturas;
	}

	@Override
	public String toString() {
		return "Pronostico [idCiudad=" + idCiudad + ", temperaturas="
				+ temperaturas + "]";
	}
	
	
}
