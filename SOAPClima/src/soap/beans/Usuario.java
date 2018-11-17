package soap.beans;

public class Usuario {
	private int idusuario;
	private String usuario;
	private String password;
	private Ciudad ciudad;
	
	public Usuario(){}
	
	public Usuario(String usuario, String password, Ciudad ciudad) {
		super();
		this.usuario = usuario;
		this.password = password;
		this.ciudad = ciudad;
	}

	public int getIdusuario() {
		return idusuario;
	}

	public void setIdusuario(int idusuario) {
		this.idusuario = idusuario;
	}

	public String getUsuario() {
		return usuario;
	}

	public void setUsuario(String usuario) {
		this.usuario = usuario;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public Ciudad getCiudad() {
		return ciudad;
	}

	public void setCiudad(Ciudad ciudad) {
		this.ciudad = ciudad;
	}

	@Override
	public String toString() {
		return "Usuario [idusuario=" + idusuario + ", usuario=" + usuario
				+ ", password=" + password + ", ciudad=" + ciudad + "]";
	}
	
	
}
