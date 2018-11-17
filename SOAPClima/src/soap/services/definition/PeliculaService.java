package soap.services.definition;

import soap.beans.Actor;
import soap.beans.Pelicula;

public interface PeliculaService {

	public boolean existePelicula(String titulo);

	public Pelicula[] traerPeliculasPorActor(Actor actor);
}
