package dao;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import soap.beans.Ciudad;
import soap.beans.Usuario;

public class UsuarioDAO {
	
	DataSource ds;
	
	public UsuarioDAO(){
		ds = new DataSource();
	}
	
	public Usuario traerUsuarioPorId(int idusuario){
		Usuario usuario = null;
		String query = "SELECT * FROM usuario WHERE idusuario="+idusuario;
		ResultSet rs = this.ds.execute(query);
		try {
			while (rs.next()){
				System.out.println("entra");
				usuario = new Usuario();
				usuario.setIdusuario(Integer.parseInt(rs.getString("idusuario")));
				usuario.setUsuario(rs.getString("usuario"));
				usuario.setPassword(rs.getString("password"));
				usuario.setPassword(rs.getString("idciudad"));
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}finally{
			this.ds.close();
		}
		return usuario;
	}
	
	public Usuario traerUsuarioPorIdCompleto(int idusuario){
		Usuario usuario = null;
		Ciudad ciudad = null;
		String query = "SELECT * FROM usuario u JOIN ciudad c ON u.idciudad=c.idciudad WHERE idusuario="+idusuario;
		ResultSet rs = this.ds.execute(query);
		try {
			while (rs.next()){
				System.out.println("entra");
				usuario = new Usuario();
				ciudad = new Ciudad();
				usuario.setIdusuario(Integer.parseInt(rs.getString("idusuario")));
				usuario.setUsuario(rs.getString("usuario"));
				usuario.setPassword(rs.getString("password"));
				ciudad.setIdCiudad(Integer.parseInt(rs.getString("idCiudad")));
				ciudad.setCiudad(rs.getString("ciudad"));
				ciudad.setCodigo_ciudad(rs.getString("codigo_ciudad"));
				ciudad.setLatitud(Double.parseDouble(rs.getString("latitud")));
				ciudad.setLongitud(Double.parseDouble(rs.getString("longitud")));
				ciudad.setCantidad_busquedas(Integer.parseInt(rs.getString("cantidad_busquedas")));
				usuario.setCiudad(ciudad);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}finally{
			this.ds.close();
		}
		return usuario;
	}
	
	public String crearUsuario(Usuario usuario){
		String respuesta = "";
		String query = "INSERT INTO usuario (usuario, password, idciudad) VALUES ('"+usuario.getUsuario()+"', '"+usuario.getPassword()+"', "+usuario.getCiudad().getIdCiudad()+")";
		try {
			int rs = this.ds.update(query);
			if (rs != 0) respuesta = "Usuario creado correctamente";
			else respuesta = "Problemas al crear el usuario";
		}
		catch(Exception e){
			System.out.println(e.getMessage());
		}
		finally{
			this.ds.close();
		}
		return respuesta;
	}
	
	public String eliminarUsuario(Usuario usuario){
		String respuesta = "";
		String query = "DELETE FROM usuario WHERE usuario='"+usuario.getUsuario()+"' and password='"+usuario.getPassword()+"'";
		try {
			int rs = this.ds.update(query);
			if (rs != 0) respuesta = "Usuario eliminado correctamente";
			else respuesta = "Problemas al eliminar el usuario";
		}finally{
			this.ds.close();
		}
		return respuesta;
	}
}
