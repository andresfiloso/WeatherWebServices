package soap.beans;

public class Temperatura {
	private String ciudad;
	private String fecha;
	private int tempMinima;
	private int tempMaxima;
	private String estado;
	
	public Temperatura(){}

	public Temperatura(String ciudad, String fecha, int tempMinima,
			int tempMaxima, String estado) {
		super();
		this.ciudad = ciudad;
		this.fecha = fecha;
		this.tempMinima = tempMinima;
		this.tempMaxima = tempMaxima;
		this.estado = estado;
	}

	public String getCiudad() {
		return ciudad;
	}

	public void setCiudad(String ciudad) {
		this.ciudad = ciudad;
	}

	public String getFecha() {
		return fecha;
	}

	public void setFecha(String fecha) {
		this.fecha = fecha;
	}

	public int getTempMinima() {
		return tempMinima;
	}

	public void setTempMinima(int tempMinima) {
		this.tempMinima = tempMinima;
	}

	public int getTempMaxima() {
		return tempMaxima;
	}

	public void setTempMaxima(int tempMaxima) {
		this.tempMaxima = tempMaxima;
	}

	public String getEstado() {
		return estado;
	}

	public void setEstado(String estado) {
		this.estado = estado;
	}

	@Override
	public String toString() {
		return "Temperatura [ciudad=" + ciudad + ", fecha=" + fecha
				+ ", tempMinima=" + tempMinima + ", tempMaxima=" + tempMaxima
				+ ", estado=" + estado + "]";
	}

	
	
}
