package soap.services.impl;

import java.util.ArrayList;
import java.util.List;

import soap.beans.Usuario;
import dao.UsuarioDAO;
import soap.services.definition.UsuarioService;

public class UsuarioServiceImpl implements UsuarioService {
	
	@Override
	public String altaUsuario(Usuario usuario){
		UsuarioDAO usuarioDao = new UsuarioDAO();
		String respuesta = usuarioDao.crearUsuario(usuario);
		return respuesta;
	}
	
	@Override
	public String bajaUsuario(Usuario usuario){
		UsuarioDAO usuarioDao = new UsuarioDAO();
		String respuesta = usuarioDao.eliminarUsuario(usuario);
		return respuesta;
	}

}
