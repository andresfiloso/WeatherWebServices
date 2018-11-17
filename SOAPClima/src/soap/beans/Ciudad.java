package soap.beans;

public class Ciudad {
	private int idCiudad;
	private String ciudad;
	private String codigo_ciudad;
	private double latitud;
	private double longitud;
	private int cantidad_busquedas;
	
	public Ciudad(){}

	public Ciudad(String ciudad, String codigo_ciudad, double latitud,
			double longitud, int cantidad_busquedas) {
		super();
		this.ciudad = ciudad;
		this.codigo_ciudad = codigo_ciudad;
		this.latitud = latitud;
		this.longitud = longitud;
		this.cantidad_busquedas = cantidad_busquedas;
	}

	public int getIdCiudad() {
		return idCiudad;
	}

	public void setIdCiudad(int idCiudad) {
		this.idCiudad = idCiudad;
	}

	public String getCiudad() {
		return ciudad;
	}

	public void setCiudad(String ciudad) {
		this.ciudad = ciudad;
	}

	public String getCodigo_ciudad() {
		return codigo_ciudad;
	}

	public void setCodigo_ciudad(String codigo_ciudad) {
		this.codigo_ciudad = codigo_ciudad;
	}

	public double getLatitud() {
		return latitud;
	}

	public void setLatitud(double latitud) {
		this.latitud = latitud;
	}

	public double getLongitud() {
		return longitud;
	}

	public void setLongitud(double longitud) {
		this.longitud = longitud;
	}

	public int getCantidad_busquedas() {
		return cantidad_busquedas;
	}

	public void setCantidad_busquedas(int cantidad_busquedas) {
		this.cantidad_busquedas = cantidad_busquedas;
	}

	@Override
	public String toString() {
		return "Ciudad [idCiudad=" + idCiudad + ", ciudad=" + ciudad
				+ ", codigo_ciudad=" + codigo_ciudad + ", latitud=" + latitud
				+ ", longitud=" + longitud + ", cantidad_busquedas="
				+ cantidad_busquedas + "]";
	}
	

}
