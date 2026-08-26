# Devolución — Cuestionario 0

**Estudiante:** MIRAGLIA, JORGE ALBERTO
**Divergencia KL global:** ∞

---

### Moneda

- Divergencia KL: 0.5861

**Tu respuesta:** [0.3333, 0.3333, 0.3333]
> Justifique:
Los tres resultados posibles considerados son Cara, Sello y Borde, por lo que al ser todos los eventos posibles
la suma de sus probabilidades deben sumar 1:

P(Cara) + P(Sello) + P(Borde) = 1.

Como no se proporciona información adicional que permita distinguir o
privilegiar alguno de los tres resultados, aplicamos el principio de máxima
incertidumbre dada la información disponible. Esto se logra distribuyendo la
creencia en partes iguales (prior uniforme):

P(Cara) = P(Sello) = P(Borde) = 1/3.

**Respuesta de referencia:** [0.48, 0.52, 2e-07]
> Una moneda normal tiene dos caras, por lo que la probabilidad de que salga Anverso o Reverso es aproximadamente 0.5 cada una. Una vez cada 5 millones de tiradas queda en el borde.

### Cajas

- Divergencia KL: 1.585

**Tu respuesta:** [0.3333, 0.3333, 0.3333, 0]
> Justifique:
El enunciado afirma que hay 3 cajas y detras de ellas 
hay un regalo, por lo tanto Ω={Caja 0,Caja 1,Caja 2}.

i) Luego {regalo en otro lugar}=∅ y P(∅)=0
ii) Como las tres cajas son idénticas y no se proporciona información que permita
distinguir o privilegiar alguna de ellas, aplicamos el principio de máxima
incertidumbre dada la información disponible, distribuyendo la creencia en
partes iguales. P(Caja 0) = P(Caja 1) = P(Caja 2) = 1/3

**Respuesta de referencia:** [0, 0, 1, 0]
> En este caso, por casualidad, el regalo se encontraba en la tercera caja (índice 2).

### Mentir

- Divergencia KL: 0.0145

**Tu respuesta:** [0, 0, 0.99, 0, 0.01]
> Justifique:
i) La opcion 0 es una definicion incorrecta (o incompleta) porque ignora la restriccion de la informacion disponible.
ii) Las opciones 1 y 3 son incorrectas porque contradicen la definicion de maximizar la incertidumbre.
iii) La opcion 2 se ajusta bien a la definicion, estaba en duda si es o no una definicion matematica por lo cual,
busque en internet si la definicion dada en el ejercicio se puede considerar, o no, una definicion matematica. 
Esto se debe a que la definicon no esta expresada simbolicamente como por ejemplo P* = argmax_P H(P) mas ajustado a lo que
se conoce como definicion matematica.

La respuesta de google a mi pregunta, es que la opcion 2 si se considera una definicion matemtica, por lo tanto tengo alta certeza
acerca de la opcion 2, pero no certeza completa.
Asigno alta probabilidad a la opcion 2 y un poco a la opcion 4.
(Y no asigno probabilidad a la opcion 0, debido a que el enunciado pregunta por "cual" y no "cuales", asique debe elegirse 1 respuesta y la opcion 2
encaja mejor que la opcion 0 en la definicion)

**Respuesta de referencia:** [0, 0, 1, 0, 0]
> Maximizar incertidumbre (entropía) dada la información disponible (restricciones) garantiza no mentir: decir que sabemos cuando no sabemos y decir que no sabemos cuando sí sabemos.

### Universos

- Divergencia KL: 0

**Tu respuesta:** [0, 0.1667, 0.1667, 0, 0, 0.3333, 0, 0.3333, 0]
> Justifique:
i) Asigno probabilidad 0 a los eventos que no son posibles porque contradicen las hipotesis iniciales del enunciado:
Caso 1- Se abre la caja uno (Abren = 1), porque es la caja elegida por el participante y esa debe quedar en juego tenga o no el regalo dentro.
(Descarto opciones 0, 3 y 6)
Caso 2- Se abre la caja que tiene el regalo (Regalo = Abren), porque el presentador debe abrir una caja que no contenga el regalo.
(Descarto opciones 4 y 8)

ii) Luego asigno probabilidades a los distintos eventos siguiendo el concepto del juego Monty Hall.
(Regalo: r y Pista:s). Donde la primera seleccion de caja tiene igual probabilidad 1/3 cada una.
Caso 1- (Regalo = 1). En ese caso las opciones de eleccion de la caja correcta tienen
probabilidad 1/6 ya que el presentador puede elegir cualquiera de las otras dos cajas. 
Caso 2- (Regalo = 2 o Regalo = 3) las opciones donde se selecciona la caja incorrecta tienen probabilidad 1/3.
(El presentador solo tiene un unico camino posible para seleccionar la otra caja incorrecta)

**Respuesta de referencia:** [0, 0.1667, 0.1667, 0, 0, 0.3333, 0, 0.3333, 0]
> La realidad causal podría tener cualquier distribución que tenga 0 en los casos imposibles (Abren=1 es imposible porque la caja 1 está reservada; Regalo=1,Abren=1 y Regalo=2,Abren=2 y Regalo=3,Abren=3 son imposibles porque no se abre la caja con el regalo).
En este caso particular la referencia propone una realidad causal subyacente que tiene la misma distribución que la predicción de máxima incertidumbre (entropía) dada la información disponible (restricciones).

### Historia

- Divergencia KL: 1

**Tu respuesta:** [0, 0, 0, 0.5, 0.4, 0.1]
> Justifique:
Interpreto la expresión "actual sistema de razonamiento para contextos de
incertidumbre" como una referencia al sistema basado en las reglas de la
probabilidad.

Respuestas posibles:
i) Según las diapositivas de la clase, en el siglo XVIII "nace la
probabilidad (soluciones analíticas)", por lo que asigno alta creencia
a esta opción.

ii) Sin embargo, históricamente existe evidencia importante a favor del
siglo XVII. La correspondencia entre Blaise Pascal y Pierre de Fermat de 1654 suele
considerarse uno de los orígenes de la teoría matemática de la probabilidad.
Posteriormente, Christiaan Huygens publica en 1657 uno de los primeros
tratados sistemáticos sobre probabilidad. Por este motivo asigno también
una creencia alta al siglo XVII.

iii) Existen otros intentos anteriores de registros de sistemas de razonamiento de incertidumbre anteriores
al siglo 17 como por ejemplo:
(a) El poema "De Vetula" (Siglo XIII): Un poema en latín de autor desconocido que incluye la primera 
enumeración exacta de todas las formas posibles en que pueden caer tres dados (las 216 combinaciones posibles)
(b) Fra Luca Pacioli (1494): contabilidad Summa de arithmetica..., propuso por escrito una versión temprana 
del problema de los puntos (cómo repartir las apuestas si un juego se interrumpe)
Pero estos antecedentes no son necesariamente usos del "sistema actual de razonamiento" probabilistico.
por lo que asigno una creencia menor.

**Respuesta de referencia:** [0, 0, 0, 1, 0, 0]
> Según nuestro conocimiento, el primer uso fue en el siglo 18, por el señor Bayes.

### Conjunta

- Divergencia KL: 0

**Tu respuesta:** [1, 0, 0]
> Justifique:
Por la regla del producto, una distribución conjunta puede descomponerse
tomando como marginal cualquiera de sus variables y multiplicándola por
la distribución condicional del resto de las variables.

**Respuesta de referencia:** [1, 0, 0]
> Por la regla de la cadena de la probabilidad, cualquier distribución conjunta siempre puede factorizarse de manera exacta como el producto de una marginal y la condicional del resto de variables dadas las anteriores. Es una identidad algebraica universal.

### Independencia

- Divergencia KL: 0

**Tu respuesta:** [1, 0, 0]
> Justifique:
Por propiedad de independencia P(B|A) = P(B). 
Luego se multiplica en ambos lados por P(A) y se forma la igualdad P(A)P(B|A) = P(A)P(B).

**Respuesta de referencia:** [1, 0, 0]
> Si A es independiente de B, se cumple también que P(B|A) = P(B) y por lo tanto siempre se cumple la igualdad dada en el enunciado.

### Descomposiciones

- Divergencia KL: 0

**Tu respuesta:** [0, 0, 0, 0, 0, 0, 1, 0, 0]
> Justifique:
Contar las descomposiciones es exactamente contar las permutaciones de las N variables.
Si hay N variables, hay N! órdenes posibles y cada orden forma una descomposición distinta.

**Respuesta de referencia:** [0, 0, 0, 0, 0, 0, 1, 0, 0]
> Cada permutación produce una factorización única utilizando la regla de la cadena, por lo que existen N! descomposiciones posibles.

### Teorema de Bayes

- Divergencia KL: 0.074

**Tu respuesta:** [0.95, 0.05, 0]
> Justifique:
i) Para hipótesis internas a un mismo modelo, el teorema de Bayes puede
escribirse como:

P(H_i|D,M) = P(D|H_i,M)P(H_i|M) / P(D|M).

Al considerar las diferentes hipótesis H_i, el denominador P(D|M) no
depende de H_i. Por lo tanto, es constante respecto de las diferentes
hipótesis.

ii) Asigno una pequeña creencia a "A veces" debido a una posible ambigüedad en
la palabra "constante". P(D|M) no es una constante absoluta: si cambian los
datos D o el modelo M, el valor de la evidencia también puede cambiar.

**Respuesta de referencia:** [1, 0, 0]
> El denominador del Teorema de Bayes es la verosimilitud marginal, P(Datos), calculada integrando todo el espacio de hipótesis.
Debido a que la hipótesis no es un parámetro de esa función, siempre es constante para las diferentes hipótesis.

### Predicciones

- Divergencia KL: 0

**Tu respuesta:** [0, 0, 1]
> Justifique:
Por la regla del producto, la probabilidad conjunta de los datos puede
descomponerse siguiendo cualquier orden, siempre que las probabilidades
condicionales se modifiquen consistentemente con el orden elegido.

**Respuesta de referencia:** [0, 0, 1]
> Todas las descomposiciones generadas por la regla de la cadena son equivalentes y por lo tanto el orden temporal no juega ningún rol en el cálculo de la predicción conjunta.

### Valor de verdad

- Divergencia KL: 0

**Tu respuesta:** [1, 0, 0]
> Justifique:
Por la regla del producto, la predicción del conjunto de datos puede
escribirse como:
P(D|H) = P(d1|H)P(d2|d1,H)...P(dn|d1,...,d_{n-1},H).

Si cualquiera de estos factores es 0, entonces todo el producto es 0:

Por lo que, aplicando regla de bayes, P(H|D) tambien es cero. Es decir, si la hipótesis asignaba probabilidad
cero a un dato que efectivamente fue observado, pierde toda su creencia posterior y queda falseada.

**Respuesta de referencia:** [1, 0, 0]
> Si una hipótesis asigna probabilidad nula a un dato que ha sido efectivamente observado, P(D|H)=0, por la regla de la cadena la predicción conjunta va a ser 0 siempre, P(Datos|H)=0, esa hipótesis se hace falsa para siempre, la creencia a posterior de esa hipótesis va a ser 0.

### Teorías causales

- Divergencia KL: 6.644

**Tu respuesta:** [0, 0.99, 0.01, 0, 0]
> Justifique:
i) La opcion 4 se descarta porque las opciones 0, 1 y 2 0, 1 y 2 cubren todo el espacio de posibilidades de comparación entre
un modelo causal y un modelo algoritmico de IA/ML

ii) La opcion 3 tambien se le puede asignar probabilidad 0, porque los modelos causales se caractizan por su capacidad
de asignar probabilidad a los datos. Ademas si el modelo se corresponde con el verdadero proceso
causal generador, induce la distribución probabilística correcta de los datos. 
(Si son comparables ambos modelos incluso dando valores erroneos)

iii) Al comparar el rendimiento predictivo sobre datos observacionales, un modelo causal no tiene por qué ser siempre 
mejor ni siempre peor que un algoritmo de AI/ML. El rendimiento puede depender de la información disponible, 
de las variables utilizadas, de la especificación del modelo y de cómo fueron estimados sus parámetros.

**Respuesta de referencia:** [0, 0, 1, 0, 0]
> La predicción que el modelo hace de los datos, P(Datos|Modelo), en escala logarítmica y en tiempo infinito (ensamble o repeticiones del proceso) es precisamente el negativo de la entropía cruzada entre el proceso generativo de los datos P(Datos|Realidad) y las predicciones P(Datos|Modelo).
Sabemos que la entropía cruzada se minimiza cuando P(Datos|Modelo) = P(Datos|Realidad).

### Predicción e información

- Divergencia KL: 0

**Tu respuesta:** [0, 0, 1]
> Justifique:
La entropía de Shannon puede interpretarse como una medida de nuestra incertidumbre acerca del valor de X.
Mejor Prediccion o Mayor Probabilidad <-> Menor Sorpresa o Informacion de Shanon

Si sabemos que X siempre va a ocurrir P(X) = 1 entonces no hay sorpresa de Shanon, 
pero si X es un resultado poco probable, entonces el aprendizaje es mas alto con los datos observados.

La funcion es estrictamente decreciente: I(x)=−logP(x)

**Respuesta de referencia:** [0, 0, 1]
> Una predicción perfecta agrega nula información.
Cuanto mejor se predice, menos información se obtiene.
Siempre.
Nunca ocurre lo contrario.

### Modelos e información

- Divergencia KL: 0.0145

**Tu respuesta:** [0, 0.01, 0.99]
> Justifique
i) En general se comparan modelos bajo mismo conjunto de Datos (No esta especificado).
La información de Shannon acumulada por un modelo se define como
I(Datos|Modelo) = -log P(Datos|Modelo),

Cuanto mejor predice un modelo los datos observados, mayor es
P(Datos|Modelo) y, por lo tanto, menor es -log P(Datos|Modelo

ii) Si un modelo tiene mas Datos que otro, puede tener mayor informacion de Shannon acumulada e igualmente
ser mejor modelo prediciendo.

**Respuesta de referencia:** [0, 0, 1]
> Queremos el modelo causal que predice perfectamente, que no recibe ningún tipo de información de Shannon.

### Evaluación de modelos

- Divergencia KL: 0

**Tu respuesta:** [0, 1, 0]
> Justifique
Segun Koller con datos observacionales solamente, en general no se puede determinar una estructura 
causal única ni siquiera con infinitos datos; como máximo puede identificarse una clase de equivalencia.
Eso tampoco quita que a veces si pueda lograrse.
Al ser todas opciones excluyentes se elige solo la opcion 1.

**Respuesta de referencia:** [0, 1, 0]
> Es posible que dos modelos causales alternativos tengan la misma distribución conjunta.
En esos casos no podemos distinguir cuál es el modelo correcto, porque ambos hacen las mismas predicciones.

### Contrafactuales

- Divergencia KL: ∞

**Tu respuesta:** [0, 1, 0]
> Justifique
i) Siempre no pasa porque hay contrafactuales que no quedan determinados por la información factual
y los mecanismos probabilísticos disponibles.

ii) Nunca tampoco porque en ciertos modelos la información factual sí restringe suficientemente el mecanismo 
y permite calcular una distribución contrafactual.

**Respuesta de referencia:** [1, 0, 0]
> Los contrafactuales siguen una lógica causal que puede incluirse en el modelo causal usando los mecanismos causales probabilísticos.
Ese modelo extendido contiene variables factuales y contrafactuales, y permite predecir cuál hubiera sido un resultado contrafactual dada la información factual.

### Diversificación

- Divergencia KL: 0.05889

**Tu respuesta:** [0, 0, 0, 0, 0.02, 0.96, 0.02, 0, 0, 0, 0]
> Justifique:

Se evaluaron por simulación todas las proporciones posibles entre 0 y 1,
en pasos de 0.1.

Para cada proporción f asignada a Cara, el resto 1-f se asignó a Sello.
En cada tirada el capital se actualizó multiplicándolo por 3*f si salía
Cara y por 1.2*(1-f) si salía Sello.

Se simularon muchas secuencias largas de lanzamientos y se repitió cada
experimento varias veces para reducir el efecto del azar de una única
secuencia.

Al comparar el crecimiento obtenido por las distintas estrategias, la
proporción f = 0.5 produjo sistemáticamente el mejor comportamiento de
largo plazo entre las alternativas consideradas.

Por lo tanto, la simulación sugiere asignar 50% de los recursos a Cara
y 50% a Sello.

**Respuesta de referencia:** [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
> El proceso de actualización de los recursos tiene una estructura multiplicativa.
La variable libre es la proporción de recursos que asignamos a Cara y Sello.
Los pagos que ofrece la casa de apuestas, en cambio, no cambian.
Al comparar el cociente entre dos riquezas generadas mediante dos estrategias de diversificación alternativas, los pagos de la casa de apuestas se cancelan.
La ecuación a optimizar es la media geométrica de la diversificación dada la probabilidad de la moneda.
En escala logarítmica tiene la estructura de la entropía cruzada, con el signo invertido.
Y eso se maximiza cuando la diversificación es igual a la probabilidad de la moneda.

### Apuesta individual

- Divergencia KL: 0

**Tu respuesta:** [1, 0]
> Justifique:

Como Cara y Sello tienen ambos probabilidad 0.5, en una cantidad muy
grande de lanzamientos esperamos aproximadamente la misma cantidad de
Caras y Sellos.
Por cada par formado por una Cara y un Sello, los recursos se
multiplican de la siguiente forma: Capital_t2 = Capital_t1*(1.5 * 0.6) = Capital_t1*0.9
En 10000 lanzamientos esperamos aproximadamente 5000 Caras y
5000 Sellos, por lo que el capital final será aproximadamente 
Capita_final = Capital_inicial * (0.9)^5000 -> 0

**Respuesta de referencia:** [1, 0]
> Aunque la esperanza aritmética es positiva, lo que importa individualmente es la tasa de crecimiento geométrica: (1.5)^0.5 * (0.6)^0.5 = sqrt(1.5 * 0.6) = sqrt(0.9) ≈ 0.9487 < 1.
La riqueza típica decrece ~5.1% por jugada.

### Teoría de Utilidad Esperada

- Divergencia KL: ∞

**Tu respuesta:** [0, 1, 0]
> Justifique
La probabilidad de Cara y Sello es p = 0.5, pero el enunciado no
especifica la función de utilidad U(w). Por lo tanto, la conveniencia
de aceptar la apuesta depende de cómo el jugador valora su riqueza.

i) Si el jugador es neutral al riesgo, U(w) = w, etonces
E[X] = 0.5*1.5 + 0.5*0.6 = 1.05 > 1 y E[W_10000] = W_0*(1.05)^10000 > W_0.
Si le conviene jugar

ii) Si el jugador tiene utilidad logarítmica, U(w) = ln(w)
E[ln(X)] = 0.5*ln(1.5) + 0.5*ln(0.6) = 0.5*ln(0.9) < 0. 
No le conviene jugar

**Respuesta de referencia:** [0, 0, 1]
> A pesar de que la esperanza de los recursos es positiva, la tasa de crecimiento de la riqueza a largo plazo es negativa.
Esto se puede ver en dos pasos, con un Sello y una Cara.
Cuando sale Sello pasamos de 100 a 60, y luego cuando sale Cara pasamos de 60 a 90.
Y como la moneda es normal, a largo plazo vamos a tener la misma cantidad de Caras y Sellos, y la riqueza decrece siempre.

### Fondo común

- Divergencia KL: 0.074

**Tu respuesta:** [0, 0.05, 0.95]
> Justifique:
Aca hay dos escenarios posibles
i) Si son en apuestas distintas, rebalancear a partes iguales reduce la varianza. Esto reduce volatilidad y 
permite converger mas rapido en valor esperado.

ii) Si ambos participantes están expuestos exactamente al mismo resultado de la apuesta, el fondo común es indistinto, 
ya que ambos recursos se multiplican por el mismo factor y repartirlos nuevamente no modifica el resultado.

Supongo que el escenario (i) es el planteado para este escenario y el (ii) no es lo pedido por el enunciado

**Respuesta de referencia:** [0, 0, 1]
> Al poner los recursos en un fondo común y dividirlo en partes iguales, la tasa de crecimiento aumenta para todos los participantes.
A medida que el grupo es más grande, la tasa de crecimiento se parece más a la media aritmética, que es positiva, por lo que Sí conviene participar.

### Impuestos

- Divergencia KL: ∞

**Tu respuesta:** [0, 0, 1]
> Justifique:

Al dejar de aportar al fondo pero seguir recibiendo una parte igual, el jugador conserva el rendimiento
de su propio capital y además recibe una transferencia proveniente de los otros 99 integrantes.

Por lo tanto, si obtenemos Cara nuestros recursos se multiplican
aproximadamente por: 1.5 + 1.0395 = 2.5395

y si obtenemos Sello por: 0.6 + 1.0395 = 1.6395
(donde 1.0395 proviene de (99/100) * 1.05 = 1.0395)

Incluso en el caso desfavorable de Sello, los recursos aumentan
aproximadamente un 64%.

**Respuesta de referencia:** [1, 0, 0]
> Cuando dejamos de aportar al fondo común se reduce la tasa de crecimiento del grupo del cual dependemos y con ella cae nuestra tasa de crecimiento.
Esto se observa matemática y numéricamente.

## Resumen

- **Divergencia KL global:** ∞
- **Preguntas con divergencia KL infinita** (asignaste 0 a una opción con probabilidad de referencia positiva): 3 de 21
- **Preguntas sin distribución de creencias válida** (reemplazadas por máxima incertidumbre): 0 de 21