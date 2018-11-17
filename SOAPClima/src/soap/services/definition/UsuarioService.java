package soap.services.definition;

import soap.beans.Usuario;
import dao.UsuarioDAO;

public interface UsuarioService {

	public String altaUsuario(Usuario usuario);

	public String bajaUsuario(Usuario usuario);
}
