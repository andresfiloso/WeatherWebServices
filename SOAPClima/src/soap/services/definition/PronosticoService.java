package soap.services.definition;

import soap.beans.Temperatura;

public interface PronosticoService {

	public Temperatura[] traerClima(String ciudad);
	
}
