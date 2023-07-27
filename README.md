<h1>¿Me ha afectado crecer entre Kurt Cobain y Bananarama?</h1>
<h2><i>O por qué hablar de la evolución de la cultura musical en occidente cuando podemos hablar de mí</i></h2>
Este proyecto estudia los datos recolectados en Spotify a través de su API, para comprobar si la música de Nirvana combinada con el pop más veraniego han tenido un efecto en mi personalidad musical. 
Para ello se han recolectado datos de mi cuenta desde 2013
Puedes responderte a esta misma pregunta , está en tu mano sólo necesitas sustituir el Client_id por el tuyo de Spotify. Suerte!

 <p>Spotify tiene 406 millones de usuarios activos mensuales </p>
      <p>El 30% están en Europa ...</p>
      <a href="https://es.statista.com/estadisticas/1118343/distribucion-de-usuarios-activos-mensuales-de-spotify-por-region/">Este es el reparto</a>     
      ![usuarios_spotify](https://github.com/yporquenoahora/EDA/assets/1010236/5ab3bdbc-79b0-4dc1-a37b-8fb4904e2a49)
      <image src="./imgs/usuarios_spotify.png">
      <p>Spotify tiene una API a través de la cual podemos acceder a diferentes características de cada canción</p>
      <p>No sólo nos da información sobre título, autores o género, también podemos acceder a parámetros como el tipo de acorde que predomina en la canción o las secciones que la conforman</p>
      <img src="./imgs/tabla.png"/>![tabla](https://github.com/yporquenoahora/EDA/assets/1010236/e1e1d776-3d8d-474a-b688-7f48cf15757c)
      <h1>Acordes mayores y menores</h1>
      <p>Podemos saber, por ejemplo, si una canción tiene predominio de acordes mayores</p>
      <p>Los acordes mayores transmiten optimismo, los menores, sin embargo, transmiten melancolía o tristeza</p>
      <p>Lo vamos a entender mejor a través de un ejemplo</p>
      <image src="imgs/ejemplo_acordes_mayores.png"/>
Aquí un mapa de calor que muestra la correlación entre unos parámetros y otros. 
Algunos son bastante intuitivos, como la bailabilidad y la energía, que están altamente relacionados, y todo lo contrario ocurre con el modo (mayor o menor)
<image src="imgs/corr.png"/>
<h1>Si occidente tuviera una cuenta de Spotify, ¿qué ha escuchado desde los 40?</h1>
<p>Siguiendo con los acordes, he seleccionado una de las playlist que dicen mostrar los grandes éxitos musicales desde los años 40

Esta selección está centrada en gustos y consumo occidental</p>
 <image src="imgs/generos_occidente.png"/>

Hay predominio de acordes mayores, lo que nos podíamos esperar, dado que en el mainstream suele predominar el mensaje feliz*

 <image src="imgs/acordes_mainstream.png"/>

 Es interesante explorar en qué periódos históricos predominan acordes mayores, y qué nivel de energía tiene la música más popular

 <image src="imgs/evolucion_energia.png"/>
 <image src="imgs/occidente.png"/>
 <image src="imgs/mi_lista.png"/>

 <h1>¿Qué es esto de "adult standards", porcierto?</h1>
 <p>Nada que ver con música para momentos recreativos, me temo. Resulta que se
refiere a música para nostálgicos, Nat King Cole o Frank Sinatra estarían en esta
categoría</p>

<h1>Fue entonces cuando me pregunté,
¿escucho yo algo de esto?</h1>
<p>Estos son los géneros que más he
escuchado ( nada emo para mi sorpresa)</p>

 <image src="imgs/mis_generos.png"/>
 <p>Aunque sí, parece que hay más acordes menores que en la lista maintream</p>
 <image src="imgs/mis_acordes.png"/>
 <p>¿Pero desgranando un poco también?</p>
 <image src="imgs/mis_generos_acordes.png"/>
 <p>Y aquí las que más
he escuchado
ordenadas por
popularidad</p>
 <image src="imgs/canciones.png"/>

<p> Parece que las canciones en clave menor tienen un grado de bailabilidad
alto, es decir, son enérgicas</p>
<p>Así que no soy tan emo. Me enfado más como Rage Agains the Machine
que como Thom York o Fionna Apple</p>

<h2>Mi conclusión es que me ha marcado de por vida el cruce entre Nirvana y
Bananarama.</h2>
<h2>Escucho música melancólica que se puede bailar</h2>
