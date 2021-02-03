from film_script_formatter.film_script_formatter import FilmScriptFormatter

filmScriptFormatter = FilmScriptFormatter('examples/jojo-rabbit-script-pdf.txt')

filmScriptFormatter.actors(output = 'examples/jojo_rabbit_actors.json')