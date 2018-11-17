package soap.services.impl;

import java.util.ArrayList;
import java.util.List;

import soap.beans.Actor;
import soap.beans.Pelicula;
import soap.services.definition.PeliculaService;

public class PeliculaServiceImpl implements PeliculaService {

	@Override
	public boolean existePelicula(String titulo) {
		return false;
	}

	@Override
	public Pelicula[] traerPeliculasPorActor(Actor actor) {
		System.out.println(actor.getNombre() + " - " + actor.getApellido());
		List<Pelicula> peliculas = new ArrayList<Pelicula>();
		
		Pelicula p = new Pelicula();
		p.setTitulo("Batman");
		p.setDescripcion("Accion");
		p.setFecha(2005);
		p.setIdioma("Guarani");

		Pelicula p1 = new Pelicula();
		p1.setTitulo("Superman");
		p1.setDescripcion("Drama");
		p1.setFecha(2005);
		p1.setIdioma("Inclusivo");

		peliculas.add(p1);
		peliculas.add(p);

		return peliculas.toArray(new Pelicula[peliculas.size()]);
	}

}
