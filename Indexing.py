from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT

schema = Schema(title=TEXT(stored=True), content=TEXT,
                path=ID(stored=True), tags=KEYWORD, icon=STORED)

import os.path
from whoosh.index import create_in

if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)

from whoosh.index import open_dir

ix = open_dir("index")
writer = ix.writer()
writer.add_document(title=u"My document", content=u"This is my document!",
                    path=u"/a", tags=u"first short", icon=u"/icons/star.png")
writer.add_document(title=u"Second try", content=u"This is the second example.",
                    path=u"/b", tags=u"second short", icon=u"/icons/sheep.png")
writer.add_document(title=u"Third time's the charm", content=u"Examples are many.",
                    path=u"/c", tags=u"short", icon=u"/icons/book.png")
writer.add_document(title=u"Antonio Plaza", content=u"¡Déjala! \
 \
Toma niña, este búcaro de flores; \
tiene azucenas de gentil blancura  \
lirios fragantes y claveles rojos,   \
tiene también camelias, amaranto \
y rosas sin abrojos, \
rosas de raso, cuyo seno ofrecen \
urnas de almíbar con esencia pura, \
que en sus broches de oro se estremecen. \
 \
Admítelas, amor de mis amores, \
admítelas, mi encanto; \
las cristalinas gotas de mi llanto, \
tibio llanto que brota \
del alma de una madre que en ti piensa, \
y por eso hallarás en cada gota \
emblema santo de ternura inmensa. \
 \
Una tarde de abril, así decía, \
mi esposa sollozante, mi esposa infortunada, \
a mi hija indiferente que dormía \
en su lecho de tablas reclinada; \
y como Herminia, ¡nada!; \
nada en su egoísmo respondía \
a esa voz que me estaba asesinando. \
La madre entonces se alejó llorando, \
y ella en la tumba continuó durmiendo. \
'Déjala dije, -tu dolor comprendo. . .' \
 \
 \
Sombra \
 \
I \
 \
¿Quién eres, di, sombra errante, \
que me sigues pertinaz, \
y doquiera que la faz \
vuelvo, te miro delante? \
¿Eres la memoria estuante \
de lejano devaneo, \
o al engendrarte el deseo \
con mi propio ser batallas? \
¿Por qué sin saber do te hallas \
en todas partes te veo? \
 \
II \
 \
¿Eres éter desprendido \
de la región impalpable, \
por mandato inexplicable \
en fantasma convertido? \
¿O de mi llanto vertido \
el vaporoso ardimiento \
finge una forma en el viento, \
forma que amo y acobarda? \
¿Eres el ángel de la guarda?, \
¿eres mi remordimiento? \
 \
III \
Cuando las noches sus mares \
de sombra, en la tierra vierte \
y en mi lecho caigo inerte, \
nutrido de mil pesares; \
dejando tal vez tus lares \
fantásticos, apareces, \
y si el afán toma creces, \
me levanto como loco, \
por ver si tu sombra toco \
y al punto te desvaneces. \
 \
IV \
 \
Mi extraviada fantasía \
con distintas formas pueblas \
eres luz en las tinieblas, \
y sombra en la luz del día. \
Inspiras a mi ardentía \
amor que extraña el espanto; \
¿Por qué desde el camposanto \
me recuerdas, por mi mal, \
una historia criminal \
que santificó mi llanto? \
 \
V \
 \
Te adoro, sombra imposible, \
como el arcángel enteo, \
y aunque nada, nada creo, \
hoy me asombra lo increíble \
sombra del alma adorada. \
¿Por qué no eres ¡ay! tangible, \
sombra de la infortunada \
que mi labio en sueños nombra? \
¿por qué no me vuelvo sombra \
para fundirme en tu nada? \
 \
VI \
 \
Sombra de la amada mía, \
que brilla lánguidamente, \
como brilla una palente \
estrella, en la noche umbría. \
¿Por qué en mi audaz fantasía \
vives, memoria de ayer? \
¡Oh!, ¡quién pudiera creer \
que entre la bruma del sueño \
amara con loco empeño \
a un ser que no puede ser! \
 \
VII \
 \
Te veo unas veces estela; \
otras, estatua marmórea; \
otras, visión incorpórea; \
otras cual luna a quien cela \
denso vapor que la vela, \
y otras como esos quemantes \
rayos del sol, que anhelantes \
al entrar por el balcón, \
fingen faja de crespón \
llena de átomos brillantes. \
 \
VIII \
 \
Te adora intuitivamente, \
y vuela, si estoy dormido, \
mi espíritu desprendido \
tras tu forma transparente. \
Ojalá nunca lamente \
por tu presencia exaltada \
llegue a verte evaporada; \
porque quiero al fenecer \
dar a tu nada mi ser, \
o ser con tu nada, nada. \
 \
 \
El borracho \
 \
Generoso en la copa, ruin en todo; \
ronca la voz, inyecta la mirada, \
párpados gruesos, faz abotagada \
y siempre crudo cuando no beodo. \
Perdida la razón, goza a su modo, \
y nunca estar en su razón le agrada; \
que el vino es todo, la razón es nada, \
y sólo vive al empinar el codo. \
Cuando al inflamarle empieza el aguardiente, \
lenguaraz, atrevido y vivaracho, \
es intrépido, franco y excelente \
amigo; pero juzgo sin empacho \
que no es franco, ni amigo, ni valiente; \
porque el borracho, en fin, sólo es . . . borracho. \
 \
 \
Lágrimas y flores \
 \
 \
Soy el coplero cuyos cinismo \
ha muchos años que celebró \
en el estruendo de las orgías, \
los funerales de corazón. \
 \
Mi cráneo, que antes se enardeciera \
de los sueños con el calor, \
de lindos sueños está despierto, \
porque no es cierto lo que soñó. \
 \
Entre los sueños encantadores \
estaba oculta la decepción, \
y el desencanto con mueca horrible \
vino a burlarse de mi candor. \
 \
Soberbio entonces bajé al infierno \
de infame crápula que me abrasó \
y con sonrisa mefistofélica \
a las virtudes les di mi adiós. \
 \
Al ver que huyeron mis esperanzas, \
lleno de ira me dije: '¡oh!, \
las esperanzas son ilusiones, \
las ilusiones mentiras son' \
 \
Y con mi tedio de condenado, \
con la amargura que da el dolor, \
en malos versos le doy al mundo \
la horrible presa de que me harto. \
 \
Qué rencoroso pulso mi lira, \
lira tan negra como el carbón, \
y en cada nota que de ella salta, \
se oye el ruido que da el rencór. \
 \
Cantor histérico del torpe vicio, \
busco en el vicio la inspiración; \
y a las virtudes y a las bellezas \
jamás, Virginia, les canto yo. \
 \
Pero a ti, joven, que eres tan pura \
como el aliento de linda flor, \
te doy un canto, yo que en el dado \
perdí las flores del corazón. \
 \
Eres tú, virgen, llena de gracia, \
porque de gracia Dios te formó; \
tienes tus ojos color de cielo, \
tienes las trenzas color del sol. \
 \
Tienes un tipo muy elegante, \
cuerpo de reina, dulce la voz, \
y tu epidermis es fina y blanca \
más que la nieve del Septentrión. \
 \
Cuando en tus labios, al conocerte, \
vi una sonrisa, me pareció \
tu dentadura nido de perlas \
entre una rosa de Jericó. \
 \
Ángel sin alas, que descendiente \
de la sagrada linda región, \
por ti los cielos vistieron luto, \
por ti la tierra se engalanó. \
 \
Eres más bella que la esperanza, \
más vaporosa que la ilusión; \
y donde pones tu pie pequeño, \
pones sus labios el casto amor. \
 \
Eres la reina de las hermosas, \
porque natura te concedió \
tantos hechizos como cabellos \
tienen tus trenzas color del sol. \
 \
Eres más noble que el sacrificio; \
interesante más que el pudor; \
envidia causas a las mujeres; \
pero a los hombres admiración. \
 \
Por eso, niña, cuando te canto \
mis ilusiones, llorando estoy. . . \
perdona, virgen, si mis cantares \
de tus cantos indignos son. \
 \
Para cantarte cual tú mereces, \
preciosa rubia quisiera yo \
subir al cielo, robar su lira \
al increado poeta Dios. \
 \
 \
Una Lágrima \
 \
 \
Yo, mujer, te adoré con el delirio \
con que adoran los ángeles a Dios; \
eras, mujer, el pudoroso lirio \
que en los jardines del Edén brotó. \
 \
Eras la estrella que radió en Oriente, \
argentando mi cielo con su luz; \
eras divina cual de Dios la frente; \
eras la virgen de mis sueños, tú. \
 \
Eras la flor que en mi fatal camino \
escondida entre abrojos encontré, \
y el néctar de su cáliz purpurino, \
delirante de amor, loco apuré. \
 \
Eras de mi alma la sublime esencia; \
me fascinaste como al Inca el sol; \
eras tú de mi amor santa creencia; \
eras, en fin, mujer, mi salvación. \
 \
Bajo prisma brillante de colores \
me hiciste el universo contemplar, \
y a tu lado soñé de luz y flores \
en Edén transparente de cristal. \
 \
En éxtasis de amor, loco de celos, \
con tu imagen soñando me embriagué: \
y linda cual reina de los cielos, \
con los ojos del alma te miré. \
 \
II \
 \
¿No recuerdas, mujer, cuando de hinojos \
yo juntaba mi frente con tu frente, \
tomando un beso de tus labios rojos, \
y la luna miré, como en la fuente, \
reproducirse en tus divinos ojos? \
 \
¿No recuerdas, mujer, cuando extasiada \
al penetrar de amor en el sagrario, \
languideció tu angélica mirada? . . . \
tú eras una flor, flor perfumada; \
yo derramé la vida en tu nectario. \
 \
III \
 \
¡Mas todo es ilusión! ¡Todo se agota! \
Nace la espina con flor; ¿qué quieres? \
de ponzoña letal cayó una gota \
y el cáliz amargo de los placeres. \
 \
Los gratos sueños que la amante embriagan \
fantasmas son que al despertar se alejan; \
y si un instante al corazón halagan, \
eterna herida al corazón le dejan. \
 \
Tal es del hombre la terrible historia; \
tal de mentira su fugaz ventura: \
tras un instante de mundana gloria \
amarga hiel el corazón apura. \
 \
Por eso al fin sin esperanza, triste, \
murió mi corazón con su delirio; \
y al expirar, mujer, tú le pusiste \
la punzante corona del martirio. \
 \
Y seco yace en lecho funerario \
el pobre corazón que hiciste trizas; \
tu amor le puso el tétrico sudario, \
y un altar te levantan sus cenizas. \
 \
Tras de la dicha que veló el misterio, \
siguió cual sombra el torcedor maldito, \
trocando el cielo en triste cementerio. . . \
confórmate, mujer. . . ¡estaba escrito! \
 \
 \
A una Niña \
 \
Niña gentil que a la vida \
despertaste alegre ayer, \
como en Oriente despierta \
la luz al amanecer. \
 \
Niña, que del oro cielo \
viniste al mundo a caer, \
como aljofarada gota \
del nítido rosicler. \
 \
Y en inmaculada cuna \
te remeciste después, \
como ilusión que se mece \
del sueño al dulce vaivén. \
 \
Niña de cabellos de oro \
y de labios de clavel \
Son de rosa tus mejillas \
es de raso tu alba tez. \
 \
Es tu sonrisa inconsciente, \
de ángel tu mirada es, \
y como brilla una estrella \
brilla el candor en tu sien. \
 \
Dichosa tú que del mundo \
pasando vas el dintel, \
sin sospechar que las flores \
espinas tienen también. \
 \
En mi canto, bella niña, \
le ruego al Dios de Israel, \
que la virtud de tus años \
tierno, en otros te dé. \
 \
Para que ese mundo, nunca, \
con su lodo y fetidez, \
ensucie de tu pureza \
el blanquísimo glasé; \
 \
Qué siempre tú, mariposa \
en primoroso vergel \
hueles y en las flores halles \
ánforas ricas de miel; \
 \
Que dé calor a tus alas \
el santo sol de la fe, \
y que jamás una espina \
tus alas llegue a romper. \
 \
Desencanto \
 \
Nuestra senda regada está de llanto, \
el placer del placer es el suicidio, \
detrás de la ilusión está el fastidio \
y detrás del fastidio el desencanto. \
 \
Lleno yo de fastidio y de quebranto, \
sin fuerza ya contra la suerte lidio, \
y muerto para el mundo, sólo envidio \
a los muertos que guarda el camposanto. \
 \
El infierno sus furias desenfrena, \
viento de maldición en torno zumba, \
que a penar el destino me condena, \
 \
y he de pensar hasta que al fin sucumba; \
con el peso brutal de la cadena, \
que arrastra el hombre hasta la negra tumba.. \
 \
 \
Hojas Secas \
 \
Tú despertaste el alma descreída \
Del pobre que tranquilo y sin ventura, \
en el Gólgota horrible de la vida \
agotaba su cáliz de amargura. \
 \
Indiferente a mi fatal castigo \
me acercaba a la puerta de la parca \
Más infeliz que el último mendigo, \
más orgulloso que el primer monarca. \
 \
Pero te amé; que a tu capricho plugo \
ennegrecer mi detestable historia... \
quien nació con entrañas de verdugo \
sólo dándo tormento encuentra gloria. \
 \
Antes que te amara con delirio \
viví con mis pesares resignado; \
hoy mi vida es de sombra y de martirio; \
hoy sufro lo que sufre un condenado. \
 \
Perdió la fe mi vida pesarosa; \
sólo hay abismos a mis pies abiertos... \
quiero morir... ¡feliz el que reposa \
en el húmedo lecho de los muertos!... \
 \
Nacer, crecer, morir. He aquí el destino \
de cuanto el orbe desgraciado encierra; \
¿qué importa si al fin de mi camino \
voy a aumentar el polvo de la tierra? \
 \
¿Y qué la tempestad? ¿Qué la bonanza? \
¿Ni qué importa mi futuro incierto, \
si ha muerto el corazón, y la esperanza \
dentro del corazón también ha muerto?... \
 \
¿Sabes por qué te amé?... Creí que el destino \
te condenaba como a mí, al quebranto, \
y ebrio de amor, inmaterial, divino. \
quise mezclar mi llanto con tu llanto. \
 \
¡Ah!... ¡coqueta!... ¡coqueta!... yo veía \
en ti de la virtud excelsa palma... \
¿ignoras que la vil coquetería \
es el infame lupanar del alma? \
 \
Di, ¡por piedad! ¿qué males te he causado? \
¡Por qué me haces sufrir?... Alma de roble, \
buscar el corazón de un desgraciado \
para jugar con él, eso es... ¡innoble! \
 \
¿Me hiciste renacer al sentimiento \
para burlarte de mi ardiente llama?... \
Te amo hasta el odio, y, al odiarte siento \
que más y más el corazón te ama. \
 \
Fuiste mi fe, mi redención, mi arcángel, \
te idolatró mi corazon rendido. \
con la natura mística del ángel, \
con el vigor de Lucifer caído, \
 \
Que tengo un alma ardiente y desgraciada \
alma que mucho por amar padece; \
no sé si es miserable o elevada, \
sólo sé que a ninguna se parece. \
 \
Alma infeliz, do siempre se encontraron \
el bien y el mal en batallar eterno; \
alma que Dios y Satanás forjaron \
con luz de gloria y lumbre del infierno. \
 \
Esta alma es la mitad de un alma errante, \
que en mis sueños febriles reproduzco, \
y esa mitad que busco delirante, \
nunca la encontraré: pero... ¡la busco! \
 \
Soy viejo ya, mi vida se derrumba \
y sueño aún con plácidos amores, \
que en vez del corazón llevo una tumba, \
y los sepulcros necesitan flores. \
 \
Te creí la mitad de mi ser mismo; \
pero eres la expiación, y me parece \
ver en tu faz un atrayente abismo, \
lleno de luz que ciega y desvanece. \
 \
No eres mujer, porque la mente loca \
te ve como faceta de brillante \
eres vapor que embriaga y que sofoca. \
aérea visión, espíritu quemante. \
 \
Yo que lucho soberbio con la suerte; \
y que luchar con el demonio puedo, \
siento latir mi corazón al verte... \
ya no quiero tu amor... me causas miedo. \
 \
Tú me dejas, mujer, eterno luto; \
pero mi amor ardiente necesito \
arrancar de raíz; porque su fruto \
es furto de dolor, fruto maldito. \
 \
Quiero a los ojos arrancar la venda, \
quiero volver a mi perdida calma, \
quiero arrancar mi amor, aunque comprenda \
que al arrancar mi amor, me arranque el alma. \
 \
Flor de un día \
Yo di un eterno adiós a los placeres \
cuando la pena doblegó mi frente, \
y me soñé mujer, indiferente \
al estúpido amor de las mujeres. \
 \
En mi orgullo insensato yo creía \
que estaba el mundo para mí desierto, \
y que en lugar de corazón tenía \
una insensible lápida de muerto. \
 \
Mas despertaste tú mis ilusiones \
con embusteras frases de cariño, \
y dejaron su tumba las pasiones, \
y te entregué mi corazón de niño. \
 \
No extraño que quisieras provocarme, \
ni extraño que lograras encenderme; \
porque fuiste capaz de sospecharme, \
pero no eres capaz de comprenderme. \
 \
¿Me encendiste en amor con tus encantos, \
porque nací con alma de coplero, \
y buscaste el incienso de mis cantos?... \
¿me crees, por ventura, pebetero? \
 \
No esperes ya que tu piedad implore, \
volviendo con mi amor a importunarte; \
aunque rendido el corazón te adore, \
el orgullo me ordena abandonarte. \
 \
Yo seguiré con mi penar impío, \
mientras que gozas envidiable calma; \
tú me dejas la duda y el vacío, \
y yo, en cambio, mujer, te dejo el alma. \
 \
Porque eterno será mi amor profundo, \
que en ti pienso constante y desgraciado, \
como piensa en la vida el moribundo, \
como piensa en la gloria el condenado. \
 \
 \
A María del cielo \
 \
Y ya al pisar los últimos abrojos \
De esta maldita senda peligrosa \
Haz que ilumine espléndida mis ojos \
De tu piedad la antorcha luminosa \
                           García Gutiérrez. \
  \
 Flor de Abraham que su corola ufana \
 abrió al lucir de redención la aurora: \
 tú del cielo y del mundo soberana, \
 tú de vírgenes y ángeles Señora; \
  \
 Tú que fuiste del Verbo la elegida \
 para Madre del Verbo sin segundo, \
 y con tu sangre se nutrió la vida, \
 y con su sangre libertose el mundo: \
  \
 tú que del Hombre-Dios el sufrimiento, \
 y el estertor convulso presenciaste, \
 y en la roca del Gólgota sangriento \
 una historia de lágrimas dejaste; \
  \
 tú, que ciñes diadema resplandente, \
 y más allá de las bramantes nubes \
 habitas un palacio transparente \
 sostenido por grupo de querubes \
  \
 y es de luceros tu brillante alfombra \
 donde resides no hay tiempo ni espacio, \
 y la luz de ese sol es negra sombra \
 de aquella luz de tu inmortal palacio. \
  \
 Y llenos de ternura y de contento \
 en tus ojos los ángles se miran, \
 y mundos mil abajo de tu asiento \
 sobre sus ejes de brillantes giran; \
  \
 tú que la gloria omnipotente huellas, \
 y vírgenes y troncos en su canto \
 te aclaman soberana, y las estrellas \
 trémulas brillan en tu regio manto. \
  \
 Aquí me tienes a tus pies rendido \
 y mi rodilla nunca tocó el suelo; \
 porque nunca Señora, le he pedido \
 amor al mundo, ni piedad al cielo. \
  \
 Que si bien dentro del alma he sollozado, \
 ningún gemido reveló mi pena; \
 porque siempre soberbio y desgraciado \
 pisé del mundo la maldita arena. \
  \
 Y cero, nulo en la social partida \
rodé al acaso en páramo infecundo, \
fue mi tesoro una arpa enronquecida \
y vagué sin objeto por el mundo. \
 \
Y solo por doquier, sin un amigo, \
viajé, Señora, lleno de quebranto, \
envuelto en mis harapos de mendigo, \
sin paz el alma, ni en los ojos llanto. \
 \
Pero su orgullo el corazón arranca, \
y hoy que el pasado con horror contemplo, \
la cabeza que el crimen volvió blanca \
inclino en las baldosas de tu templo. \
 \
Si eres ¡oh Virgen! embustero mito, \
yo quiero hacer a mi razón violencia; \
porque creer en algo necesito, \
y no tengo, Señora una creencia. \
 \
¡Ay de mí! sin creencias en la vida, \
veo en la tumba la puerta de la nada, \
y no encuentro la dicha en la partida, \
ni la espero después de la jornada. \
 \
Dale, Señora, por piedad ayuda \
a mi alma que el infierno está quemando: \
el peor de los infierno... es la duda, \
y vivir no es vivir siempre dudando. \
 \
Si hay otra vida de ventura y calma, \
si no es cuento promesa tan sublime, \
entonces ¡por piedad! llévate el alma \
que en mi momia de barro se comprime. \
 \
Tú que eres tan feliz, debes ser buena; \
tú que te haces llamar Madre del hombre, \
si tu pecho no pena por mi pena, \
no mereces a fe tan dulce nombre. \
 \
El alma de una madre es generosa, \
inmenso como Dios es su cariño: \
recuerda que mi madre bondadosa \
a amarte me enseñó cuando era niño. \
 \
Y de noche en mi lecho se sentaba \
y ya desnudo arrodillar me hacía, \
y una oración sencilla recitaba, \
que durmiéndome yo la repetía. \
 \
Y sonriendo te miraba en sueños, \
inmaculada Virgen de pureza, \
y un grupo veía de arcángeles pequeños \
en torno revolar de tu cabeza. \
 \
Mi juventud, Señora, vino luego, \
y cesaron mis tiernas oraciones; \
porque en mi alma candente como el fuego, \
rugió la tempestad de las pasiones. \
 \
Es amarga y tristísima mi historia; \
en mis floridos y mejores años, \
ridículo encontró, buscando gloria, \
y en lugar del amor los desengaños. \
 \
Y yo que tantas veces te bendije, \
despechado después y sin consuelo, \
sacrílego, Señora, te maldije \
y maldije también al santo cielo. \
 \
Y con penas sin duda muy extrañas \
airado el cielo castigarme quiso \
porque puse el infierno en mis entrañas; \
porque puso en mi frente el paraíso. \
 \
Quise encontrar a mi dolor remedio \
y me lancé del vicio a la impureza, \
y en el vicio encontré cansancio y tedio, \
y me muero, Señora, de tristeza. \
 \
Y viejo ya, marchita la esperanza, \
llego a tus pies arrepentido ahora, \
Virgen que todo del Señor alcanza, \
sé tú con el Señor mi intercesora. \
 \
Dile que horrible la expiación ha sido, \
que horribles son las penas que me oprimen; \
dile también, Señora, que he sufrido \
mucho antes de saber lo que era crimen. \
 \
Si siempre he de vivir en la desgracia, \
¿por qué entonces murió por mi existencia? \
si no quiere o no puede hacerme gracia, \
¿dónde está su bondad y omnipotencia? \
 \
Perdón al que blasfema en su agonía, \
y haz que calme llorando sus enojos, \
que es horrible sufrir de noche y día \
sin que asome una lágrima a los ojos. \
 \
Quiero el llanto verter de que está henchido  \
mi pobre corazón hipertrofiado, \
que si no lloro hasta quedar rendido \
¡por Dios! que moriré desesperado. \
 \
¡Si comprendieras lo que sufro ahora!... \
¡Aire! ¡aire! ¡infeliz! ¡que me sofoco!... \
Se me revienta el corazón ... ¡Señora! \
¡Piedad!... ¡Piedad de un miserable loco! \
 \
 \
 \
No te olvido \
 \
¿Y temes que otro amor mi amor destruya? \
qué mal conoces lo que pasa en mí; \
no tengo más que un alma, que es ya tuya, \
y un solo corazón, que ya te di. \
 \
¿Y temes que placeres borrascosos \
arranquen ¡ay! del corazón la fe? \
Para mi los placeres son odiosos; \
en ti pensar es todo mi placer. \
 \
Aquí abundan mujeres deslumbrantes, \
reinas que esclavas de la moda son, \
y ataviadas de sedas y brillantes, \
sus ojos queman, como quema el sol. \
 \
De esas bellas fascinan los hechizos, \
néctar manan sus labios de carmín; \
mas con su arte y su lujo y sus postizos, \
ninguna puede compararse a ti. \
 \
A pesar de su grande poderío, \
carecen de tus gracias y virtud, \
y todas ellas juntas, ángel mío, \
valer no pueden lo que vales tú. \
 \
Es tan ingente tu sin par pureza, \
y tan ingente tu hermosura es, \
que alzar puede su templo la belleza \
con el polvo que oprimes con tu pie. \
 \
Con razón me consume negro hastío \
desde que te hallas tú lejos de aquí, \
y con razón el pensamiento mío \
sólo tiene memoria para ti. \
 \
Yo pienso en ti con ardoroso empeño, \
y siempre miro tu divina faz, \
y pronuncio tu nombre cuando sueño. \
Y pronuncio tu nombre al despertar. \
 \
Si del vaivén del mundo me retiro, \
y ávido de estudiar quiero leer, \
entre las letras ¡ay! tu imagen miro, \
tu linda imagen de mi vida ser. \
 \
Late por ti mi corazón de fuego, \
te necesito como el alma a Dios; \
eres la virgen que idolatro ciego; \
eres la gloria con que sueño yo. \
 \
 \
 \
Horas negras \
 \
Huyó la dulce sonrisa \
Nació el sarcasmo sangriento... \
                                      J. E. \
 \
Coplero a quien inspira el desencanto, \
trovador sin futuro y sin amores, \
sobre la tumba de mis sueños canto \
al colocar mi búcaro de flores. \
 \
Odia el mundo mi canto descreído, \
el estigma social tiznó mi frente... \
cárabo del dolor, cada gemido \
me concita el sarcasmo de la gente. \
 \
Sin luz el alma la ilusión desdeña, \
el pesar no la irrita ni la abate, \
y ni la frente envejecida sueña, \
y ni el leproso corazón me late. \
 \
Repugna a todos mi fatal delirio \
repelen todos mi sufrir eterno, \
que brilla en mi aureola de martirio \
la fatídica flama del infierno. \
 \
Devorado por negra pesadumbre \
lanzo en vez de sollozos carcajadas; \
porque de infame crápula en la lumbre \
arrojé mis creencias adoradas. \
 \
En aras de la fe vertí mi llanto; \
perdida ya la fe, busqué la orgía; \
pero el vicio acreció mi desencanto, \
y el vicio, la virtud, todo me hastía. \
 \
A mi gastado corazón de lodo \
nada, en fin, es capaz de conmoverlo, \
y perezoso, indiferente a todo \
no puedo ser feliz, ni quiero serlo. \
 \
Mi vida ha sido decepción horrible, \
el mundo sin piedad ha envenenado \
mi corazón que, un tiempo tan sensible, \
no sufre al encontrar un desgraciado. \
 \
Y si me duelo del dolor ajeno \
mi risa burla ese dolor profundo, \
que si a mi corazón queda algo bueno \
me da vergüenza que lo sepa el mundo. \
 \
Cuando la pena torturó mi vida, \
la cruda pena la insulté yo mismo, \
porque soberbio disfracé la herida \
con el torpe descaro del cinismo. \
 \
En el albor de juventud sensible \
amaba todo, porque fui creyente \
yo deliré buscando lo imposible \
y de mentiras se pobló mi frente. \
 \
Yo combatí con ánimo esforzado \
contra la saña de mi suerte adversa; \
pero en la lucha atleta fatigado, \
sentí agotarse mi gigante fuerza. \
 \
Me presentó pensiles engañosos \
en su espejo ese mundo fementido, \
cual presenta cambiantes primorosos \
débil burbuja en su cristal fingido. \
 \
yo también la ilusión vestí de gala \
del placer en los cármenes risueños, \
yo también de Jacob fijé la escala \
para subir al mundo de los sueños. \
 \
Soñé con la virtud cándidos lirios \
y quise, necio, de ilusión beodo, \
subir a la región de los delirios; \
pero al querer subir, caí en el lodo. \
 \
Yo rebusqué sediento de placeres, \
de amistad y de amor las emociones, \
y turbas mil de amigos y mujeres \
vinieron a matar mis afecciones. \
 \
Al ver mis sentimientos chasqueados \
burlé yo mismo mi amoroso empeño, \
y ya no alcé castillos encantados \
sobre la base efímera del sueño. \
 \
De mi pobre ilusión asesinada \
los restos profanó mi ánima impía; \
porque el cadáver de mi fe burlada \
alumbré con las luces de la orgía. \
 \
Y di culto a ese mundo estrafalario, \
y en mi gastada juventud inquieta, \
vestido de arlequín subí al calvario \
y empapé con mi llanto la careta. \
 \
En irritantes goces crapulosos \
escarneciendo mi penar ingente, \
hice cabriolas y tragué sollozos, \
y lleno de ira divertí a la gente. \
 \
Mas penitente ya, sufro callando \
y consumido de letal tristeza, \
por la vía dolorosa voy cargando \
la ridícula cruz de mi pobreza. \
 \
Histrión a quien el mundo no perdona, \
héroe de carnaval, mártir maldito, \
un birrete de loco es mi corona \
y por túnica llevo un sambenito. \
 \
Y nutrido de negras decepciones, \
avergonzado en mi vejez, reniego \
del enjambre de locas ilusiones \
que acarició mi juventud de fuego. \
 \
Ilusiones brillantes halagaban \
a mi edad juvenil que yo maldigo, \
y sediento de gloria me agitaban \
sueños de rey en lecho de mendigo. \
 \
Soñé en la gloria con delirio tanto, \
fue tal la audacia de la mente loca, \
que la gloria de Dios, único y santo, \
a mi osada ambición pareció poca. \
 \
Más Dios abate mi soberbia rara, \
y encuentro justa la expiación severa; \
que si la gloria que soñé alcanzara \
Satanás vencedor acaso fuera. \
 \
Fue mi sueño una ráfaga ilusoria; \
no existe ese laurel que busqué loco, \
que para darme mi imposible gloria \
el orbe es nada, lo infinito poco \
 \
Para pedir la gloria que yo anhelo \
es débil, impotente la palabra; \
que desván estorboso encuentro el cielo \
do el pensamiento audaz se descalabra. \
 \
Ya no me importa mi dolor presente, \
ya no me importa mi dolor pasado, \
el porvenir lo espero indiferente... \
lo mismo es ser feliz que desgraciado. \
 \
Sólo ambiciono de fastidio yerto, \
cansado ya de perdurable guerra, \
el acostarme en mi cajón de muerto \
dormir en paz debajo de la tierra. \
 \
 \
 \
Cantares \
 \
Te adoré como a una virgen \
cuando conocí tu cara; \
pero dejé de adorarte \
cuando conocí tu alma \
 \
Cuestión de vida o muerte \
son las pasiones, \
si alguien lo duda, deja \
que se apasione. \
 \
Las heridas del alma \
las cura el tiempo, \
y por eso incurables \
son en los viejos. \
 \
Los astros serán, mi vida, \
más que tus ojos hermosos; \
pero a mi más que los astros \
me gustan, linda, tus ojos. \
 \
 \
 \
Amor \
 \
¿Por qué si tus ojos miro \
me miras tú con enojos, \
cuando por ellos deliro, \
y a la luz del cielo admiro \
en el éter de tus ojos? \
 \
Cansado de padecer \
y cansado de cansarte, \
y queriendo sin querer, \
finjo amor a otra mujer \
con la ilusión de olvidarte. \
 \
No es mi estrella tan odiosa: \
que en fugaces amoríos, \
como ave de rosa en rosa \
yo voy de hermosa en hermosa \
y no lamento desvíos; \
 \
Pero el favor de las bellas  \
irrita mas la pasión \
que ardiente busca tus huellas, \
y al ir mis ojos tras ellas \
vuela a ti mi corazón. \
 \
Asi un proscrito tenía \
goces en extraño suelo \
y volvió a su patria un día \
por mirar en su agonía \
la linda luz de su cielo. \
 \
De ti proscrito y dejando \
las rosas por tus abrojos, \
vuelvo a tus pies suspirando, \
por mirar agonizando  \
la linda luz de tus ojos. \
 \
 \
 \
Dios \
 \
Espíritu de fuego sagrado y rutilante, \
tu voz la voz domina de ronca tempestad, \
y soles mil coronan tu frente de gigante, \
y brilla en tu mirada exscelsa majestad. \
 \
Señor, tú eras antes que todo lo creado, \
antes que fuera el tiempo, Señor ya eras tú, \
el ser de gloria lleno tú solo te lo has dado, \
tú solo te formaste de tu espléndida luz. \
 \
Señor, eras más grande que todo lo que existe; \
la cima de los astros es sima para ti; \
Señor, tú de la nada al orbe suspendiste, \
y pléyades brillantes colgaste en el zafir. \
 \
Es tu dosel de estrellas, de luz es tu palacio, \
irradia luz de gloria tu espíritu inmortal; \
eres quien desplegaste el viento en el espacio, \
eres quien extendiste las aguas en el mar. \
 \
Tú eres, Dios divino, el Dios omnipotente; \
los cielos y los mundos brotaron a tu voz; \
un límite le puso tu voz al mar ingente, \
y al hombre, dios pequeño, tu soplo le animó. \
 \
Retiemblan, si te irritas, los ejes de los cielos; \
el rayo se estremece, el sol cubre tu faz; \
humillan las montañas su frente hasta los suelos; \
las fieras dan rugidos, solloza el huracán. \
 \
A tu voz imperiosa los astros se oscurecen, \
se rasga de los cielos el diáfano zafir; \
los mundos se desquician, los mares desaparecen, \
el ser vuelve a la nada, si lo mandas asi. \
 \
Tú eres luz sublime del cielo y de la tierra, \
eres principio eterno de sempiterna luz; \
eres la vida sola de cuando el orbe encierra; \
ante ti todo es nada, porque eres todo tú. \
 \
Los pueblos y los reyes desfilan presurosos, \
y tiempos sobre tiempos se hacinan a tu pie; \
y en nada convertidos se pierden, silenciosos, \
en ese mar de sombra, calado del no ser. \
 \
Eres tú sólo eterno, omniscio; impenetrable, \
son nube pasajera los siglos ante ti; \
ninguno te conoce, que tú eres impalpable, \
pero doquiera se oye tu nombre bendecir. \
 \
Señor, eres el Éter que Zenón adoraba, \
el 'TODO' que Pitágoras sumiso veneró, \
el Ser indestructible que Platón deificaba, \
la Universal justicia que soñó Cicerón. \
 \
Tú eres el Jehová del pueblo de Judea, \
y del remoto chino tú eres de Xantí; \
eres el sol brillante que a Cartago recrea, \
eres del persa el fuego, en él adora a ti. \
 \
Eres el Dios que adoran los astros y las nubes, \
un himno te levantan los vientos y la mar: \
la flor te da su aroma, su canto los querubes, \
las aves te consagran su trino matinal. \
 \
Tú diste a la oropéndola su traje de colores, \
capullo a los gusanos, a las abejas miel, \
a las arañas tela y púrpura a las flores, \
cubil a los leones y las aguas al pez. \
 \
Del arca de Noé la brújula tú fuiste, \
y tu brazo detuvo el brazo de Abraham; \
libraste a Lot del fuego que en Sodoma encendiste, \
de la ballena libre salió por ti Jonás. \
 \
A Moisés de las aguas del Nilo tú salvaste, \
y le hiciste de un pueblo manumisor feliz; \
tu Código en las tablas por dárselo grabaste: \
tus rayos coronaron de luz el Sinaí. \
 \
Eres quien dio la ciencia infusa a los profetas \
que el velo del futuro lograron levantar; \
por ti ellos inspirados, sublimes y poetas, \
al orbe predijeron grandiosa una verdad. \
 \
Hiciste al Nazareno el Sabio entre los sabios, \
por ti brilló en su frente de redención la luz; \
y aunque con vil brebaje humedeció sus labios \
el héroe del martirio, el ángel de la Cruz, \
 \
oró por sus verdugos con santidad extrema, \
y en hórrido tormento morir supo cual Dios; \
por eso ante la Cruz, de oprobio un tiempo, \
humilde y de rodillas la humanidad cayó \
 \
A ti Dios de los hombres; cuya eternal historia \
escrita con tu sangre en el cadalso fue: \
sublime ajusticiado. monarca de la gloria, \
que fuiste de los hombres la víctima también; \
 \
a ti, raudal de soles que inmensos reverberan \
doquier multiplicando sus rayos mil y mil; \
a ti, la eterna dicha que los hombres esperan, \
a ti del alma eterna, eterno porvenir; \
 \
a ti, Señor, te ruego con ánima gastada, \
que de mi tumba oscura la puerta se abra ya; \
arrastro una existencia, maldita, desgraciada, \
mis horas son más negras que el alma de Satán \
 \
Pobre mártir, oscuro, coplero estrafalario, \
un cáliz de amargura también apuro yo; \
y, como Cristo el justo, también hallé un Calvario, \
y sufro aquí tormentos que nunca El conoció. \
 \
Es un presente horrible la vida que me diste, \
la vida tan amarga que yo no te pedí: \
Señor, ya no soporto la vida mustia y triste; \
devuélveme a la nada... o llévame hacia ti. \
 \
 \
 \
Sin fe y sin amor \
 \
I \
 \
Arrastro una vida \
de luto y dolor; \
a todos les choco, \
me choco hasta yo; \
y todos los hombres \
me excluyen, \
en medio de todos \
maldita excepción. \
Encina tronchada \
del viento al furor, \
mi copa gigante  \
la tierra besó. \
Murió la esperanza, \
murió el corazón,  \
que grande, hervoroso, \
un tiempo asiló \
excelsas virtudes \
y vil corrupción. \
virtudes y vicios  \
luchando perdió, \
y amorfo, sangriento, \
cadáver es hoy \
que duerme en la tumba, \
sin fe, sin amor. \
 \
II \
 \
Mis horas cubiertas \
de negro crespón \
pesadas, iguales, \
rodar miro yo. \
Esferas de sombra \
que bajan, y son \
como almas que bajan \
malditas de Dios, \
el arco, de horrores \
eterna mansión. \
Si aúlla doliente \
el alto reloj, \
yo te oigo, lo mismo \
que el grito de horror \
que arroja quien sufre \
tormento feroz: \
como eco lejano \
de agudo esquilón \
que dobla, pidiendo \
piedad al Señor, \
para un bandolero \
que en la horca expiró; \
como ese gemido, \
ese ¡ay! de dolor \
que da al reventarse \
del harpa el cordón. \
¡Qué lentas transcurren \
las horas ¡oh Dios! \
del hombre que hollando  \
punzante cambrón \
camina en la tierra, \
sin fe, sin amor! \
 \
III \
 \
Mi historia es historia \
de mártir histrión; \
sainetes y dramas \
conozco, que yo  \
he sido en el mundo \
genérico actor. \
Con frailes menores \
tranquila pasó \
mi edad inocente,  \
y el padre rector \
latín y consejos \
conmigo perdió; \
que frailes y claustro \
dejé sin temor, \
y en mil aventuras \
perdí el corazón. \
Soldado en las filas \
de Marte feroz, \
vestido de loco  \
serví de sayón. \
Chinaco más tarde, \
sin ley y sin Dios, \
escenas horribles \
miré sin horror; \
y pueblos he visto  \
que el hacha incendió, \
envueltos en llamas \
de rojo color. \
Crujir, como cruje \
rugiente crisol, \
y en negros escombros  \
de altar, mi bridón \
su huella sangrienta \
soberbio dejó. \
Por eso de todo  \
cansado ya estoy; \
conozco los goces, \
conozco el dolor, \
los salmos del coro, \
la voz del cañón, \
la faz de los campos, \
del mar el furor, \
la horrible mazmorra. \
el rico salón; \
conozco lo bueno, \
lo malo y peor; \
yo sé de banquetes, \
y de hambre sé yo; \
me son familiares \
la Regla y Colón; \
desprecios y aplausos \
el alma probó, \
el alma que vive  \
sin fe, sin amor. \
 \
IV \
 \
Más triste que tumba, \
más pobre que Job,  \
yo sufro en la tierra \
fatal expiación. \
La edad inflexible \
mi frente arrugó; \
mi cuerpo inclinado \
remeda una hoz, \
mi barba y cabellos \
de nieve ya son; \
mi espíritu ardiente, \
su fuego perdió; \
mis piernas se doblan, \
balbuce mi voz. \
¡Adiós, ilusiones \
divinas de amor, \
adiós, esperanzas, \
placeres, adiós!... \
¡Oh, muerte! yo pido  \
que des por favor \
un lecho de polvo, \
allá en un rincón, \
al pobre viandante \
que al fin se cansó, \
y llama a tu puerta  \
sin fe, sin amor. \
 \
 \
 \
Despecho \
 \
Arcanidad terrible de la vida, \
destino lleno de rigor sin nombre, \
infancia entre las sombras escondida, \
aprieta sin piedad, que das en Hombre. \
 \
No esperes con tu golpe furibundo \
avasallar mi soberano aliento: \
es grande mi tormento como el mundo; \
pero el alma es mayor que mi tormento. \
 \
Y siempre aquí, con arrogante calma \
de tus rencores la sin par fiereza \
afronto audaz, que la grandeza de alma, \
aunque pequeño soy, es mi grandeza. \
 \
Nunca al poder ni al oro me arrodillo, \
y aunque me agobie padecer tirano \
me muero de hambre; pero no me humillo... \
seré cadáver, pero no gusano. \
 \
Bien, alma ¡bien! porque jamás te humillas... \
eres inmensa en tu sufrir constante... \
¡No mendigues la gloria de rodillas, \
conquistala de pie, mártir gigante! \
 \
................. \
 \
Nací juguete de la vil fortuna \
y me acompañan en fatal camino \
la negra sombra que bañó mi cuna, \
la negra mano que marcó mi sino. \
 \
A la luz de brillantes ilusiones \
de la horrible verdad vi los arcanos, \
y fue mi alma festín de las pasiones \
como el cuerpo es festín de los gusanos; \
 \
lloré por la esperanza asesinada, \
pero tanto creció mi desventura, \
que traduje en sonora carcajada \
la suprema expresión de la amargura. \
 \
Al fin, cansado de mortal quebranto \
adopté el estoicismo por divisa: \
tanto lloré, que se agotó mi llanto, \
tanto reí que se acabó mi risa. \
 \
Sin fe, sin juventud, la despreciada \
vida infeliz indiferente rueda... \
con mi última ilusión evaporada \
¿qué me queda en el mundo? ... ¿qué me queda? \
 \
Ya no tengo sonrisa ni gemido; \
ni amo, ni aborrezco, ni ambiciono, \
que en indolencia criminal sumido \
hasta mi propio espíritu abandono. \
 \
Hora tras hora solitario pierdo \
envuelto en bruma de oriental pereza; \
es mi goce sufrir con el recuerdo, \
entregado al placer de la tristeza. \
 \
Pláceme abrir heridas mal cerradas, \
contemplando a la espalda de los años, \
ilusiones de fuego, sepultadas \
en la nieve de horribles desengaños. \
 \
II \
 \
También un tiempo ¡ay de mí! \
tras de fantasmas risueños \
desatinado corrí; \
porque la razón perdí \
entre marañas de sueños. \
 \
Lindo germen de ilusión, \
de mi espíritu gastado  \
engendró loca pasión... \
soñó con la redención \
mi frente de condenado. \
 \
En mi desencanto amé \
creyendo que no creía, \
y más desencanto hallé... \
¡imbécil! ¿por qué soñé, \
cuando soñar no debía? \
 \
Amé a una mujer, como ama \
quien amar no cree... su llanto \
alzó en mi ser una llama, \
como alza fosfórea flama \
la lluvia en el camposanto. \
 \
Pero ¡ay! de aquellas historias \
sólo guarda el corazón \
recuerdos de muertas glorias, \
memorias, sólo memorias son. \
 \
Porque mis sueños huyeron, \
y mis amores volaron, \
mis esperanzas murieron, \
y los placeres que fueron \
luto en el alma dejaron. \
 \
Hoy en negra decepción \
los desprecios y el cariño, \
mis esperanzas murieron, \
para mí los mismo son... \
en lugar de corazón \
llevo el cadáver de un niño. \
 \
III \
 \
De luz imposible mi cráneo era foco \
de luz imposible mis sueños vestí; \
pero ¡ay! que mis sueños febriles de loco \
en mares de sombra perdiéronse al fin. \
 \
El alma, la vida apenas soporta, \
la paz de las tumbas, del alma es la paz; \
yo soy un pasado que a nadie le importa; \
yo soy en la tierra cadáver social. \
 \
¡Guay del que vegeta con sueños despierto! \
dormirse soñando es muerto vivir... \
yo vivo y no sueño, cadáver despierto, \
del ser y la nada parodia infeliz. \
 \
Al cielo pregunto con ansia indecible: \
¿los mártires suben de Dios al dosel? \
el cielo se calla, y un eco terrible \
me dice: ¡No sueñes... Mentira es la fe! \
 \
Quien deja la vida de luto y hastío \
se vuelve a la nada que de ella salió, \
tras esas estrellas no hay más que vacío; \
me dice: ¡No sueñes... Mentira es la fe! \
 \
El hombre, ese imbécil gusano pequeño, \
de orgullo inflamado, se juzga inmortal; \
pero es la existencia la sombra del sueño \
del sueño que forja la nada quizá. \
 \
........................ \
 \
Señor, de la duda me asfixia el abismo, \
te ruego que mandes a mi alma infeliz \
la fe sacrosanta o el negro ateísmo... \
negar es creer... dudar es sufrir. \
 \
 \
 \
¡Siempre solo! \
 \
Si de la aurora diamantina \
se dibujan los célicos albores \
los pájaros del viento moradores \
al éter mandan su canción divina. \
 \
Y si el sol orgulloso se reclina \
sobre un lecho radiante de colores, \
llenas de amor las carminadas flores \
entreabren su corola purpurina. \
 \
Todos tienen un ser que los comprenda, \
yo al vicio y la virtud indiferente \
aislado cruzo la maldita senda, \
 \
cual se arrastra en las rocas la serpiente; \
mas tengo un alma de vivir cansada \
que ni al cielo ni al mundo pide nada. \
 \
 \
 \
Abrojos \
 \
Siempre desgraciado fui; \
Desde mi pequeña cuna, \
A la incansable fortuna \
de juguete le serví; \
La noche en que yo nací \
Tronaba la tempestad, \
Y alaridos de ansiedad \
La gente aturdida alzaba; \
Porque el cólera sembraba \
El terror y la orfandad. \
 \
II \
 \
¡La niñez ¡ – edad que vela \
el ángel de las sonrisas, \
y entre flores, juego y brisas \
sin sentir el tiempo vuela- \
Esa edad amarga estela \
Dejó sobre mar de llanto; \
Porqué sufrí tanto, tanto, \
En aquella edad de armiño, \
Que en mis recuerdos de niño \
Comienza mi desencanto. \
 \
III \
 \
Vino después otra edad, \
Y pasiones irritantes \
Se alzaron, como bramantes \
Olas, en la tempestad. \
Mas desbordé en la maldad, \
Cual se desborda un torrente, \
Y entre crápula indecente, \
Y en indecentes amores, \
Sequé del alma las flores, \
Cubrí de sombra la frente. \
 \
IV \
 \
En mi tormento prolijo, \
Al cielo a veces acudo; \
Pero ¡ay! El cielo está mudo \
Para el hombre a quien maldijo. \
En vano, en vano me aflijo \
Por la esperanza extinguida, \
Y aunque mi ya envejecida \
Frente, de pesar se abrasa, \
No vuelve la edad que pasa, \
Ni vuelve la fe perdida. \
 \
V \
 \
Tiene luto el corazón \
Como de noche el desierto, \
Y, como toque de muerto, \
Tristes mis cantares son. \
Es fúnebre panteón \
La fatigada memoria, \
Donde en ánfora mortuoria \
Vino el tiempo a recoger \
Las imágenes que ayer \
Fueron el sol de mi gloria. \
 \
VI \
 \
Nutre incisivo sarcasmo \
Mi sonrisa de amargura, \
Y es el pecho sepultura \
Donde yace el entusiasmo. \
Presa de horrible marasmo \
Desfallece el alma impía; \
Y en fatal melancolía,  \
Y en estúpido quietismo, \
Parece que en mi ser mismo \
Hay un germen de agonía. \
 \
 \
VII \
 \
Inclino con desaliento, \
Entre brumas de tristeza, \
La encanecida cabeza \
Que rasa el remordimiento. \
Y hostigado hasta el tormento, \
De la mundana balumba, \
Grito, con voz que retumba \
Cual rayo que lumbre vierte: \
¡Ábreme tus brazos, muerte! \
¡Trágate mi cuerpo, tumba! \
 \
 \
A una ramera \
 \
Mujer preciosa para el bien nacida, \
Mujer preciosa por mi mal hallada, \
Perla del solio del Señor caída \
Y en albañal inmundo sepultada; \
Cándida rosa en el Edén crecida \
Y por manos infames deshojada; \
Cisne de cuello alabastrino y blando \
En indecente bacanal cantando. \
 \
II \
 \
Objeto vil de mi pasión sublime, \
Ramera infame a quien el alma adora. \
¿Por qué el Dios ha colocado, dime, \
el candor en tu faz engañadora? \
¿Por qué el reflejo de su gloria imprime \
en tu dulce mirar? ¿Por qué atesora \
hechizos mil en tu redondo seno, \
si hay en tu corazón lodo y veneno? \
 \
III \
 \
Copa de bendición de llanto llena,  \
Do el crimen su ponzoña ha derramado; \
Ángel que el cielo abandonó sin pena, \
Y en brazos del demonio ha entregado; \
Mujer más pura que la luz serena, \
Más negra que la sombra del pecado, \
Oye y perdona si al cantarte lloro; \
Porque, ángel o demonio, yo te adoro. \
 \
IV \
 \
Por la senda del mundo yo vagaba \
Indiferente en medio de los seres; \
De la virtud y el vicio me burlaba; \
Me reí del amor de las mujeres, \
Que amar a una mujer nunca pensaba; \
Y hastiado de pesares y placeres \
Siempre vivió con el amor en guerra \
Mi ya gastado corazón de tierra. \
 \
V \
 \
Pero te vi… te vi… ¡Maldita hora \
En que te vi, mujer! Dejaste herida \
A mi alma que te adora, como adora \
El alma que de llanto está nutrida. \
Horrible sufrimiento me devora, \
Que hiciste la desgracia de mi vida. \
Mas dolor tan inmenso, tan profundo, \
No lo cambio, mujer, por todo el mundo. \
 \
VI \
 \
¿Eres demonio que arrojó el infierno \
para abrirme una herida mal cerrada? \
¿Eres un ángel que mandó el Eterno \
a velar mi existencia infortunada? \
¿Este amor tan ardiente, tan interno, \
me enaltece, mujer, o me degrada? \
No lo sé… no lo sé… yo pierdo el juicio. \
¿Eres el vicio tú? … ¡Adoro el vicio!. \
 \
VII \
 \
¡Ámame tú también! Seré tu esclavo, \
tu pobre perro que doquier te siga. \
Seré feliz si con mi sangre lavo \
Tu huella, aunque al seguirte me persiga \
Ridículo y deshonra; al cabo, al cabo, \
Nada me importa lo que el mundo diga. \
Nada me importa tu manchada historia \
Si a través de tus ojos veo la gloria. \
 \
VIII \
 \
Yo mendigo, mujer, y tú ramera, \
Descalzos por el mundo marcharemos. \
Que el mundo nos desprecie cuando quiera, \
En nuestro amor un mundo encontraremos. \
Y si horrible miseria nos espera, \
Ni de un rey por el otro la daremos; \
Que cubiertos de andrajos asquerosos, \
Dos corazones latirán dichosos. \
 \
IX \
 \
Un calvario maldito hallé en la vida \
En el que mis creencias expiraron, \
Y al abrirme los hombres una herida, \
De odio profundo el alma me llenaron. \
Por eso el alma de rencor henchida \
Odia lo que ellos aman, lo que amaron, \
Y a ti sola, mujer, a ti yo entrego \
Todo ese amor que a los mortales niego. \
 \
X \
 \
Porque nací, mujer, para adorarte \
Y la vida sin ti me es fastidiosa, \
Que mi único placer es contemplarte, \
Aunque tú halles mi pasión odiosa, \
Yo, nunca, nunca, dejaré de amarte. \
Ojalá que tuviera alguna cosa \
Más que la vida y el honor más cara, \
Y por ti sin violencia la inmolara. \
 \
XI \
 \
Sólo tengo una madre. ¡Me ama tanto! \
Sus pechos mi niñez alimentaron, \
Y mi sed apagó su tierno llanto, \
Y sus vigilias hombre me formaron. \
A ese ángel para mí tan santo, \
Última fe de creencias que pasaron, \
A ese ángel de bondad, ¡quién lo creyera!, \
Olvido por tu amor… ¡loca ramera! \
 \
XII \
 \
Sé que tu amor no me dará placer, \
Se que burlas mis grandes sacrificios. \
Eres tú la más vil de las mujeres; \
Conozco tu maldad, tus artificios. \
Pero te amo, mujer, te amo como eres; \
Amo tu perversión, amo tus vicios. \
Y aunque maldigo el fuego en que me inflamo, \
Mientras más vil te encuentro, más te amo. \
 \
 \
XIII \
 \
Quiero besar tu planta a cada instante, \
Morir contigo de placer beodo; \
Porque es tuya mi mente delirante, \
Y tuyo es mi corazón de lodo. \
Yo que soy en amores inconstante, \
Hoy me siento por ti capaz de todo. \
Por ti será mi corazón do imperas, \
Virtuoso, criminal, lo que tú quieras. \
 \
XIV \
 \
Yo me siento con fuerza muy sobrada, \
Y hasta un niño me vence sin empeño. \
¿Soy águila que duerme encadenada,  \
o vil gusano que titán me sueño? \
Yo no sé si soy mucho, o si soy nada; \
Si soy átomo grande o dios pequeño; \
Pero gusano o dios, débil o fuerte, \
Sólo sé que soy tuyo hasta la muerte. \
 \
XV \
 \
No me importa lo que eres, lo que has sido, \
Porque en vez de razón para juzgarte, \
Yo sólo tengo de ternura henchido \
Gigante corazón para adorarte. \
Seré tu redención, seré tu olvido, \
Y de ese fango vil vendré a sacarte. \
Que si los vicios en tu ser se imprimen \
Mi pasión es más grande que tu crimen. \
 \
XVI \
 \
Es tu amor nada más lo que ambiciono, \
Con tu imagen soñando me desvelo; \
De tu voz con el eco me emociono, \
Y por darte la dicha que yo anhelo \
Si fuera rey, te regalara un trono; \
Si fuera Dios, te regalara un cielo. \
Y si Dios de ese Dios tan grande fuera, \
Me arrojara a tus plantas ¡vil ramera! \
 \
 \
 \
Nada \
 \
Nadaba entre la nada. Sin empeño \
A la vida, que es nada, de improviso \
Vine a soñar que soy; porque Dios quiso  \
Entre la nada levantar un sueño. \
 \
Dios, que es el Todo y de la nada es dueño, \
Me hace un mundo soñar, porque es preciso; \
El siendo Dios, de nada un paraíso \
Formó, nadando en eternal ensueño. \
 \
¿Qué importa que en la nada confundida \
vuelva a nadar, al fin, esta soñada \
vil existencia que la nada olvida, \
nada fatal de la que fue sacada?… \
¿Qué tiene esta ilusión que llaman vida? \
-Nada en su origen. - ¿ Y en su extremo? - ¡Nada! \
 \
  \
 \
La voz del inválido \
1 \
 \
Bajo la sombra de sauz añoso \
frente a un albergue rústico y apartado, \
se hallan, un joven de naciente gozo, \
y un viejo descreído, mutilado. \
Los surcos de la frente marchitada \
las escépticas frases qué congelan, \
la irónica sonrisa y la mirada \
del viejo su pasado nos revelan. \
El apuesto garzón, el casi niño, \
con marcada humildad escucha atento \
al anciano, que lleno de cariño \
le dice así con paternal acento: \
 \
II \
 \
Conque, Andrés, ¿vas a partir? \
¿Se torna el rapaz en hombre? \
¡Bien!... Escucha y no te asombre, \
Andrés, lo que vas a oír. \
En el revuelto océano \
en que fui náufrago un día, \
quiero que lleves por guía \
la débil voz del anciano. \
No cual clérigo profundo \
evangelizarte anhelo: \
la virtud es flor del cielo \
que se marchita en el mundo. \
No de ilusiones que halagan \
te hablaré, ni de moral; \
quiero; Andrés, que no hagas mal \
ni dejes que te lo hagan. \
Franklin dijo en parte alguna, \
hablando del mundo, que: \
'Lo que salva no es la fe \
sino el no tener ninguna.' \
No creas consejos ni apólogos, \
busca siempre la verdad: \
la fe, chico, es necedad \
que llaman virtud los teólogos. \
Yo no te aconsejo el vicio, \
el que mal hace, mal halla; \
quiero que vistas con malla \
tu corazón tan novicio. \
Y ya que tus tiernos años \
están flacos de experiencia, \
escucha, Andrés, con paciencia \
la voz de los desengaños. \
También locas ilusiones \
mi juventud conmovieron, \
y las que ilusiones fueron \
son ya negras decepciones. \
Por eso en estulta calma \
niego todo con cinismo, \
porque el torpe escepticismo \
viento es que congela el alma. \
 \
* \
Tú vas a la corte. Allí \
activo en tu bien rebúllete. \
Consérvate, aséate, instrúyete, \
y vive, Andrés, para ti. \
Obra mucho y cierra el labio, \
que llega a su fin más pronto, \
con su actividad el tonto \
que con su pereza el sabio. \
Es la corte cosa brava, \
todos mal de todos piensan. \
los enemigos comienzan \
donde la nariz. acaba. \
Tú allí con muy buenos modos \
sé expansivo, sé jovial: \
de todos piensa muy mal; \
pero habla muy bien de todos. \
Que mascarada es completa \
la corte que veo con asco, \
y sufre allí más de un chasco \
quien no toma su careta. \
Allí es el afeite aseo, \
sinceridad el cinismo; \
la locura excentricismo; \
la adulación galanteo; \
Se le llama bueno al bobo, \
se llama al miedo prudencia, \
porque es difícil papel \
se llama la charla ciencia, \
se llama fianza al robo. \
Allí en duda has de poner \
la castidad del beato, \
la mansedumbre del gato, \
la virtud de la mujer. \
Allí todo es falsedad. \
'Vanidad de vanidades.' \
allí abundan nulidades \
rellenas de vanidad. \
Todos quieren que su nombre \
a los hombres envanezca, \
y no hay hombre que merezca \
llamarse siquiera hombre. \
Que de aquella sociedad, \
llena de lodo y materia, \
es muy grande su miseria \
y mayor su vanidad. \
El hombre, tenlo presente, \
en ese mundo hostigoso, \
hace un viaje muy penoso \
y no medra si no miente. \
Ese tránsito empalaga: \
que no molestan en el viaje, \
los ricos con su carruaje, \
los mendigos con su plaga. \
Y magüer razón te sobre, \
en la sociedad, buen chico, \
evita el odio del rico \
y la intimidad del pobre. \
Mas si das a la indigencia, \
nunca la humilles cruel; \
no hagas de amarga hiel \
el papel de Providencia. \
Saber dar es gran virtud, \
y dar sin tacto, locura: \
lo que se da sin finura, \
se acepta sin gratitud. \
Hay favores tan sin gracia, \
que dejan huella sensible \
en el alma, y más horrible \
hacen ellos la desgracia. \
Muchos hay que dan lo suyo \
por cálculo o vanidad, \
pero, hijo, esa caridad, \
es la virtud del orgullo. \
Nunca des con mirada doble; \
porque el hombre desgraciado \
es un objeto sagrado \
para quien tiene alma noble. \
La desgracia lenifica \
sin esperar gratitud; \
porque, Andrés, la ingratitud \
a la caridad deifica. \
 \
* \
 \
Tus apuros, si los tienes, \
cuenta al que cuente reales; \
es decir, cuenta tus males \
sólo al que los torne en bienes. \
Nunca vistas con descuido; \
porque en la corte deshonra \
más que una mancha en la honra \
un mancha en el vestido. \
Tu lujo siempre modera, \
no al lujo te entregues, no, \
mira que el lujo empezó \
por unas hojas de higuera. \
Cuida y no te faltará: \
da poco y no se te olvide \
que quien da a todo el que pide \
pide al fin a quien no da. \
Ten siempre el bolsillo a tasa, \
para que siempre algo sobre; \
porque, Andrés, el hombre pobre, \
de pobre hombre nunca pasa. \
Del placer haz poco uso, \
si ilusión quieres tener, \
que abusando del placer, \
no hay placer en el abuso. \
 \
* \
Por si acaso en sueño cálido \
buscas de Marte la gloria, \
voy e contarte la historia \
a que debo estar inválido. \
Allá en mis años mejores \
se encendió lid fratricida, \
porque a mi patria querida \
plugo cambiar de opresores. \
Del patriotismo la llama \
ardió en mi pecho de tierra. \
Marché, Andrés, en cruda guerra, \
reñí, como perro en brama. \
El éxito no fue malo: \
vencimos a los traidores, \
y volví pisando flores \
con una pierna de palo. \
Cubierto de gloria, chico, \
dejome el gobierno cruel; \
¿había de comer laurel \
como si fuera borrico? \
Otros con férvido arrojo \
la victoria celebraron. \
Oro y destino pescaron, \
y Yo quedé pobre y cojo. \
Así es la guerra maldita: \
a muchos les da oropeles, \
y carruajes y corceles, \
y a otros las piernas les quita. \
Vengué yo ajenos agravios \
y al fin ¿qué saqué?... ¡Desprecios! \
La guerra la hacen los necios \
en provecho de los sabios. \
No seas de los que combaten, \
pero odia a los que se rindan; \
pues sacan más los que brindan, \
que los tontos que se baten. \
A la guerra, Andrés, no vayas, \
y sin luchar vencerás; \
porque un brindis vale más \
que el humo de cien batallas. \
Está la patria hecha trizas \
con tanta gente malévola, \
y del brazo de Scévola \
no quedan ya ni cenizas \
Es un loco temerario \
el que anda entre los cañones: \
es mejor en los salones \
esgrimir el incensario. \
Si por figurar te apuras, \
lisonjea a los beneméritos, \
y fía más que de los méritos \
de tus buenas coyunturas. \
No te oirán si no te encorvas: \
ya que ellos tienen, Andrés, \
las orejas en los pies, \
ten el talento en las corvas. \
Para que a ciegas no andes, \
te aconsejo, por mi nombre, \
dejes tu grandeza de hombre, \
con todos los hombres grandes. \
La dignidad no conviene, \
ni la honradez, hijo de Eva; \
quien no adula no se eleva; \
el que no es vivo no tiene. \
 \
* \
 \
Si no estás en gran bonanza, \
no busques, hijo, mujer, \
el pobre ha de mantener \
solamente la esperanza. \
El amor es gran locura, \
y el bendito matrimonio, \
lazo que tiende el demonio \
y convierte en soga el cura. \
El consorcio, en conclusión, \
para un pobre es grave mal; \
y su tálamo nupcial \
túmulo es de su ilusión.  \
Nunca el marido descansa \
y sus sacrificios crecen: \
pero ellos no se agradecen,. \
porque con ellos no alcanza. \
Tú pondrás del ara encima \
tu independencia sin juicio, \
y ese inmenso sacrificio \
ninguna mujer lo estima. \
Es feliz quien por fortuna \
mujer buena tiene, Andrés: \
pero más dichoso es \
el que no tiene ninguna. \
Amor es mentida flama, \
la gratitud no parece: \
sólo, Andrés, una madre ama \
y sólo un perro agradece. \
* \
 \
Mas si tú afectos deseas, \
te lo digo con dolor, \
cree hasta en el mismo amor, \
pero en la amistad no creas. \
Con experiencia lo digo, \
Andrés, consérvalo impreso: \
un libro, un perro y un peso \
forman un completo amigo. \
los que el mundo desconocen \
dicen, sobrino, que es fama, \
que en la cárcel y en la cama \
los amigos se conocen. \
En cualquier situación seria \
tendrás número importuno \
de amigos, mas no habrá uno \
cuando estés en la miseria. \
La amistad es falso cobre, \
la amistad, óyelo, chico, \
forma la ilusión del rico \
y el desengaño del pobre. \
La amistad, en conclusión, \
la amistad, tenlo presente, \
es, sobrino, un accidente \
del oro o la posición. \
Quien fuere en la vida cero \
no tendrá un amigo, Andrés; \
si el dinero amigo es, \
sé amigo tú del dinero. \
Mejor que un peso, ten dos, \
no hagas mal por egoísmo, \
y duda hasta de ti mismo \
vete, y... ¡Bendígate Dios! \
 \
III \
 \
Un instante después, por el camino \
triste a un jinete galopar se veía, \
y un viejo de mostacho blanquecino \
con la vista al jinete perseguía. \
Cuando ni el polvo que el corcel alzara \
pudo el viejo mirar, sintió que ardiente \
gota de llanto resbaló en su cara, \
y suspirando doblegó la frente. \
'Y ¿qué será de ti? -exclamó el anciano \
Tu incierto porvenir ¿porqué me altera?. \
corre a luchar con ese mundo insano; \
vete a sufrir la suerte que te espera. \
La lucha con el mundo no te asombre, \
hombre no es el que luchar no sabe; \
porque nació para luchar el hombre \
como nació para volar el ave. \
Jamás el hombre del destino oscuro \
el negro velo levantar espere; \
envuelto entre la sombra está el futuro. \
el hombre es lo que la suerte quiere.'",
path=u"/d", tags=u"short")

writer.add_document(title=u"Guillermo Prieto", content=u"Invasión de los franceses\
\
“Mejicanos, tomad el acero,\
ya rimbomba en la playa el cañón:\
odio eterno al francés altanero,\
¡vengarse o morir con honor”.\
\
Lodo vil de ignominia horrorosa\
se arrojó de la patria a la frente:\
¿dónde está, dónde está el insolente?\
mejicanos, su sangre bebed,\
y romped del francés las entrañas,\
do la infamia cobarde se abriga:\
destrozad su bandera enemiga,\
y asentad en sus armas el pie.\
\
Si intentaren pisar nuestro suelo,\
en la mar sepultemos sus vidas,\
y en las olas, de sangre teñidas,\
luzca opaco el reflejo del sol.\
Nunca paz, mejicanos; juremos\
en los viles cebar nuestra rabia.\
¡Infeliz del que a Méjico agravia!\
gima al ver nuestro justo rencor.\
\
¡Oh qué gozo! Borremos la lujuria:\
al combate nos llama la gloria.\
Escuchad. . . ¡Ya vencimos! ¡Victoria!\
¡ay de ti, miserable francés!\
Venceremos, lo palpo, lo juro;\
¡de sangre francesas empapadas,\
nuestras manos serán levantadas\
al Eterno con vivo placer.\
\
Ya contemplo al valiente guerrero\
que hasta en sueños su mano esforzada,\
busca incierta, anhelosa, la espada\
para herir al soberbio invasor.\
Mejicanos, al campo volemos,\
en sagrado furor arda el alma;\
y al que quiera ignominia, a la calma\
lo condene ofendido el valor.\
\
\
\
La confianza del hombre\
\
Cuando la juventud despavorida,\
víctima de delirios y pasiones,\
vaga entre incertidumbre y aflicciones,\
errante en el desierto de la vida,\
\
¡sublime religión! le das asilo,\
consuelas su existir desesperado,\
en tus brazos el hombre reclinado\
no teme el porvenir, duerme tranquilo.\
\
Cuando la tempestad sus rayos lanza,\
tiembla el malvado al rebramar del viento,\
mientras del justo a Dios el firme acento\
glorifica con himnos de alabanza.\
\
Dulce es al hombre en su penoso duelo,\
cuando el tormento pertinaz le aterra,\
decir burlando a la mezquina tierra:\
“Allí es mi patria”, y señalar el cielo.\
\
Indicadme la mano que atrevida\
el velo desgarró de lo futuro:\
¿quién es aquel que penetró seguro\
el misterio insondable de otra vida?\
\
Nadie: terrible porvenir retumba,\
y el mortal ciego que en el mundo vive,\
el eco, y nada más, lejos percibe,\
que vuelve desde el seno de la tumba.\
\
Se busca el porvenir allá en el cielo,\
cree mirarle el mortal, a Dios insulta,\
y al señalarle osado, le sepulta\
el lodo vil del miserable suelo.\
\
¡Mísera humanidad, cuál es tu suerte!\
¡Cuál tu destino que lo ignora el mundo!\
¿El placer puro y el dolor profundo\
se apagan con el soplo de la muerte?\
\
Como la flor cuando el invierno asoma,\
que al frío soplo precursor del hielo,\
el tallo inclina en el humilde suelo\
sin colores, sin vida, sin aroma?\
\
¿Y aquesta alma que me anima hora,\
jamás del linde de la tumba pasa,\
cual gota que al caer sobre la brasa\
tócala, y al momento se evapora?\
\
No, jamás; nuestra noble inteligencia\
nunca perece, que las almas puras\
reflejarán por siempre en las alturas\
el brillo de la augusta omnipotencia.\
\
¿Qué dio el Eterno, el Padre de la vida,\
su lumbre a sol, su animación al mundo,\
para hacinar en él el polvo inmundo \
de nuestra humanidad envilecida?\
\
Tiemble al futuro el infeliz malvado,\
cuando a la muerte atónito sucumba,\
que no será su crimen en la tumba\
con su asqueroso cuerpo sepultado.\
\
Desprecie los horrores del averno\
y burle los misterios de la vida,\
cesará el sueño y su alma sorprendida\
se aterrará a la vista del Eterno.\
\
Y el justo, con gozo más profundo,\
verá de gloria su alma circundada,\
cuando en los negros centros de la nada\
se pierda el tiempo y se desplome el mundo.\
\
\
La inmortalidad\
(A Manuel Payno)\
\
La flor encantadora y delicada \
que sobre esbelto tallo se mecía,\
la vio ufana la luz de un solo día, \
luego desapareció.\
De ese arbusto marchito y derribado, \
ayer tal vez hermoso y floreciente, \
hoy arranca sus hojas el ambiente\
que ufano le halagó.\
\
Y al alto muro y orgullosa torre,\
que sola en el espacio alzó la frente, \
en silencio, del tiempo la corriente \
del mundo arrancó ya.\
¿Por qué, por qué insolente, hombre mezquino, \
más débil que el arbusto y que la planta,\
en vuelo audaz soberbio te levanta \
la estéril vanidad?\
\
De1 tiempo rapidísimo las alas,\
sobre nubes de imperios se extendieron, \
y se apartó la sombra, ¿ do estuvieron \
imperios y poder?\
Hombre: ¿cómo te entregas a hondo sueño, \
de la playa en la vida recostado.\
si al más ligero viento, el mar alzado \
tu cuerpo ha de envolver?\
\
Y la frágil hojilla del arbusto, \
cuando mugen terríficos los vientos, \
al caer en los marea turbulentos\
mas impresión harán\
que el golpe de cien mil generaciones, \
por la mano del tiempo derribadas, \
en las dulces y quietas oleadas\
de la ancha eternidad.\
\
Un solo grano de la limpia arena \
enturbia mas el férvido torrente,\
que esparcido del tiempo en la corriente \
del hombre el lodo vil.\
Héroe, monarca, arranca de tu labio \
el grito del orgullo que horroriza;\
es igual tu ceniza a la ceniza \
del pastor infeliz.\
\
Mas si destruye el tiempo de igual modo \
la frágil cuna, el lecho vacilante\
del anciano, y el solio de diamante \
do está la juventud;\
y si del crimen el puñal sangriento \
se rompe en los sepulcros igualmente \
que la diadema nítida y fulgente\
do está la virtud.\
\
Si a esta por siempre la mostró llorando, \
y a la maldad triunfante y denodada, \
al tocar en los bordes de la nada \
la antorcha del saber; \
¿qué importa que feroces me amenacen, \
ni que lancen gemidos los humanos,\
si yo arranco ruiseñor de sus manos \
la copa del placer?\
\
Esto dije mil veces, y encontraba \
inútil la razón, la vida yerta;\
y estéril, oscurísima, desierta \
del hombre la mansión. \
Y yo me aborrecí cuando veía\
a mi existencia entre tiniebla adusta, \
y no pude adorar la mano injusta\
del que llamaban Dios.\
\
Y burlé a los que ilusos distinguían \
sobre el sol, dominando el firmamento, \
el vasto solio y el sublime asiento\
de un genio de bondad.\
Yo allí con rabia distinguí un tirano, \
que quiso sobre el mundo levantarse, \
para ver sin estorbo aniquilarse\
la triste humanidad.\
En mi delirio horrísono exclamaba:\
si eres padre clemente y Dios piadoso, \
si es del hombre tormento doloroso \
dudar su porvenir; \
si a un solo movimiento de tu labio; \
puede rasgarse del misterio el velo, \
y hallar escrito en el inmenso cielo\
su destino infeliz;\
\
¿por qué te regocija nuestro llanto?\
¿Esa noble, tu augusta Providencia, \
al mortal le concede la existencia \
solo para el dolor?\
Mas si de lo futuro la ignorancia \
que renace en la tierra tu quisiste, \
¿para qué la razón me concediste,\
incomprensible Dios? \
\
Hacia el caos diriges 1a mirada;\
nace el sol, vive el mundo, brota el viento;\
el vasto mar refleja un firmamento \
bañado con su luz.\
Y frívolo concedes el imperio \
del orbe que tu nombre diviniza,\
a un ente vil que al toque pulveriza \
del débil ataúd?\
\
Anhelaba mi mente hasta el letargo \
de desesperación, y jamás calma;\
y siempre, siempre destrozada mi alma \
por inquietud tenaz.\
El horror de la muerte me oprimía, \
el susurro del aura me aterraba,\
y a contemplar la tumba me arrastraba \
la dudosa ansiedad.\
\
El horror expresando la mirada, \
torpe el paso, débil el aliento, \
temblando con el frío del tormento\
al sepulcro llegué.\
Una fuerza violenta, irresistible, \
me hizo inclinar al fondo la cabeza; \
y gemí de terror, y con presteza\
loe párpados cerré.\
\
En mi quebranto pronuncié convulso \
de Dios el nombre, y súbito retumba, \
y cruje, y se abre la terrible tumba\
con estruendo fatal.\
pero una luz vivísima, inefable, \
le da paso a mi atónita mirada;\
Y mi razón encuéntrase abrumada \
en gozo celestial.\
\
Con júbilo indefinible \
miré que bañó mi frente \
la luz pura, indeficiente, \
de la grande eternidad\
Vi al mortal ennoblecido \
sobre el trono del Eterno,\
y de un Dios sublime, tierno,\
la esplendente majestad.\
\
No el Dios fiero, vengativo, \
que teme y no adora el mundo, \
que creen que grita iracundo \
con la tempestad atroz;\
\
Y que devasta los campos \
en las alas del torrente, \
publicando el rayo ardiente \
su omnipotencia feroz.\
\
Cual de luciérnaga el brillo \
en la claridad del día, \
junto de Dios se perdía \
nuestro refulgente sol. \
Salud, Hacedor Supremo: \
salud, Padre de la vida,\
como el alma enternecida \
ora entona tu loor.\
\
Cuando en la tierra infeliz \
vi la virtud desdichada, \
pobre, envilecida, atada, \
del crimen negro al poder;\
no pensaba en que tu mano \
la inocencia galardona,\
que de gloria la corona \
colocas sobre su sien. \
\
Ni creí que la tormenta \
que envanece y alucina, \
en ondulación mezquina \
en el dilatado mar.\
\
Sordo al bramar la tormenta \
ciego al contemplar el cielo, \
te cubrí ¡oh Dios! con el velo \
de la lóbrega impiedad. \
Busqué criminal entonces,\
de angustia el alma agobiada, \
entre el polvo de la nada\
el lecho de la quietud.\
\
Las pasiones me arrastraron; \
no hay Dios, mis labios decían, \
y mis ojos se ofendían\
de eternidad con la luz.\
\
Si hubiera visto irrompibles \
de amor los queridos lazos, \
durmiendo al hijo en los brazos\
del afecto maternal;\
te hubiera amado, Dios mío, \
y tolerado mi suerte,\
mis ojos viendo a la muerte \
sin el llanto del pesar.\
Sólo una gota de sangre, \
o una lágrima inocente, \
del alma del delincuente \
nunca se logra borrar;\
pues la incorpora la muerte, \
la lumbre de Dios la aclara,\
y la aura copa acibara \
de aquel placer celestial. \
\
Pero ni al hombre insolente \
que con su labio blasfemo\
te ha injuriado, Ser Supremo, \
en este mundo infeliz,\
niegas tu bondad augusta; \
el no la soporta, gime\
con el aspecto sublime \
de una eternidad feliz.\
\
Aura blanda, dulces flores, \
bastos campos, lindo cielo, \
y un indecible consuelo\
que disipaba el dolor;\
yo disfruté alborozado, \
tornó el regocijo a mi alma, \
y una deliciosa calma\
ocupó mi corazón.\
\
Millares de vastos mundos \
giran, Señor, a tus plantas, \
que sostienes y que encantas\
con tu sublime bondad;\
Entre los cuales se pierden \
nuestro mundo y nuestro orgullo, \
cual de tórtola el arrullo\
cuando muge el huracán. \
Mortal, mortal atrevido,\
¿te dará la impiedad, necio, \
siquiera el odio, el desprecio \
de ese Omnipotente Dios?\
Piensas al lanzar blasfemias \
en tu honda mansión, perjuro, \
que haces retemblar el muro \
del alcázar del Criador? \
\
¿Cómo penetrar pretendes, \
contenido por ti mismo,\
en el insondable abismo \
de nuestro lóbrego ser?\
¿Quién es el hombre, responde, \
que así reclama insolente\
ser émulo y confidente \
del que prodiga el saber? \
\
Huyóse la ficción, y el alma mía, \
cuando la ofusca del dolor el velo, \
recuerda. con purísimo consuelo \
este dulce momento de alegría:\
\
tal vez, tal vez momento de delirio\
que ama mi corazón ardientemente,\
y que cuando se aleje de mi mente \
acaso en mi alma arraigará el martirio. \
Pero ¡oh Dios de bondad! por él te adoro, \
y por él , si me amaga el triste duelo, \
grito: Soy inmortal: contemplo el cielo, \
y recobro vigor y enjugo el lloro.\
\
\
\
(sin título)\
\
Yo te amo, sí, te adoro, aunque mi labio \
mil y mil veces te llamó perjura,\
aunque la copa horrenda del agravio \
me brindó los placeres tu hermosura,\
te ama mi corazón; Cuando mi mano \
destrozar quiso la feroz coyunda\
que a vil humillación me ató algún día, \
el débil corazón se resistía,\
Y aunque luché tenaz, luchaba en vano.\
\
Feliz viviera yo si siempre ufano, \
al través de mentidas ilusiones, \
hubiera contemplado tu semblante; \
si mas cauto tu labio fementido,\
si mas hábil tu hipócrita mirada,\
con el engaño mismo hubiera envuelto \
la perfidia de tu alma emponzoñada\
¿Por qué no prolongaste el dulce sueño, \
aquel sueño de angélica ventura.\
Yo respiré el placer, el aura pura\
de otra vida feliz me circuía,\
y a tu lado el torrente irresistible\
del porvenir fatal no me amagaba,\
y cual tranquilo arroyo murmuraba.\
\
Cuando entusiasta te estreché en mis brazos,\
cuando el placer entre tus lindos ojos\
con el fuego de amor resplandecía, \
cuando tu boca grata sonreía\
a mi enajenamiento, mi adorada:\
el grito de escarnio me conturba,\
te llamo ansioso, conocí mi engaño, \
y a mi rival, que irónico me indica \
con su dedo el adusto desengaño.\
\
¿Y qué, el copioso, el expresivo llanto\
que con mis manos trémulo enjugaba\
y aquella agitación, aquel quebranto\
que con anhelo tierno consolaba,\
otro amante dichoso lo causaba?\
\
Tú al verme recordabas otro amante \
que, con gozo 1o digo, no te amaba, \
otro mirabas tu a mi semblante \
con dulzura los ojos dirigías;\
y s otra ilusión feliz, viéndome ufana, \
beldad de maldición, me sonreías;\
y yo entre tanto en lóbrega congoja \
con tu dolor equívoco lloraba;\
o bien al alma con tu gozo infame \
en célico deleite se inundaba.\
¡Oh si !a espada del feroz tormento \
en tu pecho con calma revolviera\
la mano del tenaz remordimiento!... \
¡Indigno proceder! ¡atroz venganza! \
Pero es planta marchita que florea\
en mi desierta y lúgubre esperanza, \
que resta a mi existir desesperado.\
Me es estéril el canto de victoria,\
no quiero bendición, no quiero gloria, \
maldito criminal, pero tu amado.\
Si ahora tu mano ingenua me brindara\
las caricias de amor, si entre tu labio \
otra vez escuchara, vida mía,\
la grata, la dulcísima armonía \
de tu celeste voz, y si sincera \
el aura de ilusiones hechicera \
otra vez a tu vista me halagara,\
yo, idolatrado bien, te aborreciera; \
mi placer despertaran tus caricias, \
y el monstruo de la vil desconfianza \
envenenara siempre mis delicias.\
Pero al borrar tu nombre de mi mente, \
cuando el recuerdo del dolor me oprime, \
te odia mi orgullo, el labio te maldice; \
pero siempre te encuentro seductora,\
y siempre el alma con fervor te adora; \
sí, te adoro, mi bien: huyo al sosiego, \
y beso de ignominia la cadena\
cuando s tu encanto celestial me entrego.\
¡Oh fatal ilusión! ¿por qué te adoro? \
¿por qué, si la conozco fementida,\
tributo a su memoria triste lloro? \
¿por qué de mi pasión en el delirio,\
cuando miro su imagen bienhechora, \
su esbelto talle, su modesta frente, \
sus lindos ojos y su blanda risa,\
no puedo recordarla engañadora?\
¿Y bastará oponer el frágil dique \
de reflexión al bárbaro torrente \
del destino fatal, fácil olvido\
que en otro tiempo me mostró engañosa \
de la felicidad la blanca nube\
que en el aura apacible se mecía\
resbalando en el azul del cielo?\
Gallarda con el sol resplandecía,\
que ella con ansiedad me la mostraba,\
y que yo embebecido la miraba.\
¿Por qué con tal astucia del abismo,\
a que riendo ufana me llevaba,\
mi vista se paró? No la maldigo. \
Cuando la vi en el fondo, clamé en vano;\
la vi en la orilla, le tendí la mano,\
y ella volvió a tenderla, y la apartaba,\
y al irla yo a tocar la separaba,\
mostrando regocijo en mi agonía.\
¡Oh exceso de maldad! Mujer impía,\
¿cuándo mi amor sincero fue inconstante?\
¿qué vez, responde, hubiste descubierto\
a la negra traición en mi semblante?\
Dime ¿cuál es la senda bienhechora\
que me aparta de ti? Siempre te miro;\
la atmósfera inefable de tu encanto,\
peligrosa beldad, siempre respiro.\
\
La lira del amor, sin armonía\
yace sorda en mis manos; a sus cuerdas\
mi inútil llanto le robó el sonido:\
mi bien, te adoraré; pero a lo menos\
hónreme tu odio, y líbreme siquiera\
de volver a tu seno envilecido. \
\
\
El insurgente\
\
\
Desde la hermosa ribera \
se mira incierta bogar \
una barquilla ligera, \
que desafía altanera\
los horrores de la mar. \
\
Dentro se mira sentado \
un orgulloso guerrero: \
el casco despedazado,\
el vestido ensangrentado \
y a su derecha el acero.\
\
A su hijo tierno, inocente\
lleva entre sus fuertes brazos: \
baña con llanto su frente; \
pero su inquietud ardiente \
colma el niño con abrazos. \
Miró arrastrar a la muerte\
a Hidalgo y al gran Morelos; \
Y luchando con la suerte\
vio e1 Sur de su ánimo fuerte \
los patrióticos desvelos.\
\
Su bando está dispersado,\
el tirano viene atrás;\
solo salva a su hijo amado, \
y sale precipitado\
por el puerto de San Blas.\
\
\
En sus oídos aun truena\
el clamor contra el tirano:\
se alza. . . el ímpetu refrena\
porque vacila la entena,\
y extiende a su hijo la mano.\
\
De su patria idolatrada \
le arroja el destino fiero; \
sin amigos, sin su amada, \
solo con su hijo y su espada \
en el universo entero. \
\
Queda en la playa su esposa \
sin amparo, sin ventura: \
mira la mar caprichosa\
y en ella girar llorosa\
dos prendas de su ternura. \
\
Tiende 1os brazos... suspira, \
y caen con desconsuelo:\
de la playa se retira;\
mas torna, y el bravo mira \
revolear su pañuelo. \
\
Vuelve la vista el valiente\
y encuentra a su hijo dormido; \
luce la calma en su frente,\
y entona el triste insurgente \
este canto dolorido.\
\
Divino encanto de mi ternura,\
tú mi amargura\
disiparás\
En mi abandono, \
solo en los mares \
tu mis pesares\
consolarás.\
\
Tú eres mi patria,\
tú eres mi amigo.\
eres testigo\
de mi aflicción. \
Sola tu boca \
mi frente besa \
donde está impresa \
mi maldición. \
\
Hijo y tesoro\
de un tierno padre,\
tu dulce madre\
¿dónde estará?\
Dios de bondades! \
mirad su llanto, \
de su quebranto \
tened piedad.\
\
Yo en esta barca \
por mi hijo temo, \
vuelo sin remo, \
sin dirección; \
vuelo perdido \
sin saber donde, \
y ya se esconde \
la luz del sol.\
\
Pero aparece,\
¡cuánta fortuna! \
la blanca luna\
sobre el zenit.\
Hijo adorado, \
por tu inocencia\
la Omnipotencia \
me guarda a mí.\
\
Despierta el niño; la veloz barquilla\
toca triunfante la cercana tierra,\
y el atroz sobresaltó se destierra,\
y el bravo ante su Dios la frente humilla. \
La memoria empeñada en su martirio \
su situación horrible 1e presenta;\
y su patria y su amada le atormenta,\
y le sepulta en el fatal delirio, \
Inconstante y salobre su fortuna,\
como lo son las aguas de los mares, \
perturbaron los hórridos pesares \
hasta los dulces sueños de la cuna.\
Miraba ensangrentada su querida \
gimiendo ante las plantas del tirano; \
la miraba en el suelo, mejicano \
abandonada, pobre, en envilecida.\
El viento que silbaba enfurecido \
le recordaba su gemido ardiente,\
¡levantando la abatida frente \
a su esposa llamó despavorido.\
'Dulce ilusión de amor, mujer divina. \
bendigo tu memoria: yo te adoro\
Porque derramas tu copioso lloro \
por mi fortuna lúgubre y mezquina.\
\
Recuerdo que mi labio electrizado,\
después que muerte o libertad gritaba, \
en tu carrillo nácar se estampaba,\
y renacía mi vigor cansado.\
Hoy prófugo, infeliz, sin el cielo \
de Méjico, do vi la luz primera; \
nadie siente mi suerte lastimera,\
solo gimo en penoso desconsuelo.\
En otro tiempo, cuando el sol ardiente \
a el ocaso lejano declinaba,\
cuando su último rayo se apagaba\
del Popocatépetl en la alta frente: \
yo bendecía; patria idolatrada,\
tu rica tierra, tu brillante cielo; \
creí me guardarías en tu suelo\
mi última luz y mi postrer morada”.\
Pero el hijo reclama su cuidado; \
tiembla lloroso del rigor del frío;\
y ocupa su ternura y su albedrío \
en el niño inocente y desdichado.\
Los temores tal vez de alguna fiera, \
la negra noche, el árido desierto, \
tienen a su cariño vago, incierto, \
considerando lo que hacer debiera.\
Se resuelve por fin; en la barquilla, \
atada con su banda a un cocotero, \
deposita a el infante y el guerrero\
vuela donde un hogar lejano brilla.\
\
Una nube oscurece el horizonte; \
se sobresalta el bravo y retrocede,\
Y grita, y corre; mas salir no puede \
del intrincado, del oscuro monte. \
Entre tanto las olas con el viento\
se embravecen, se agitan y se chocan:\
braman, se alzan, se rompen, se sofocan; \
y está el mar en horrible movimiento.\
La voz de Dios entre las nubes truena. \
las aguas con el rayo resplandecen,\
los árboles robustos se estremecen, \
el mundo todo de pavor se llena.\
\
Inquieto vaga y furioso \
el padre despavorido, \
parecía su gemido\
a el que lanzaba la mar.\
Mientras, llora el inocente, \
grita el nombre de su padre: \
no torna: llama a la madre: \
no viene; y vuelve a llorar.\
\
El relámpago relumbra, \
la tempestad le amenaza. \
y su ímpetu despedaza\
la banda que es su sostén. \
Como la hoja arrebatada \
del huracán inclemente, \
vuela el mísero inocente\
a la mar a perecer.\
\
Cual si supiera el peligro, \
con penoso desconsuelo, \
alza las manos al cielo \
como implorando piedad. \
Así le mira su padre \
lleno de letal congoja,\
y frenético se arroja\
donde la barquilla está.\
\
Gira, lucha, a su hijo llega, \
agobiado de fatiga\
1e extiende una mano amiga. \
Crece del mar el vaivén; \
pero moverse no puede:\
estrecha a su hijo adorado,\
sonríe desesperado\
y se sumerge con él!!!\
\
\
Cómo será el mar\
\
\
Tu nombre ¡o mar! en mi interior resuena;\
despierta mi cansada fantasía:\
conmueve, engrandece al alma mía, \
de entusiasmo férvido la llena.\
\
Nada de limitado me comprime, \
cuando imagino contemplar tu seno; \
aludo, melancólico y sereno,\
o frente augusta; tu mugir sublime. \
\
Serás ¡oh mar! magnifico y grandioso \
cuando duermas risueño y sosegado; \
cuando a tu seno quieto y dilatado\
acaricie el ambiente delicioso?\
\
¿Cuando soberbio, ardiente, enfurecido \
gimiendo te abalances hasta el cielo: \
cuando haga retemblar al ancho cielo \
de tus inquietas aguas el bramido? \
\
Dulce será la luz del claro día\
si en tus diáfanas ondas reverbera; \
grata el aura y la roca que altanera \
tus impulsos vehementes desafía.\
\
Creo ver en tu imperio turbulento \
la excelsa eternidad en su palacio, \
dominando en el mundo y el espacio, \
midiendo la extensión del firmamento. \
\
De la divinidad eres idea;\
del mundo miserable poesía\
la dulce admiración del alma mía; \
con tu vista el Eterno se recrea.\
\
La rama de la playa, que distante\
en tu inquieta extensión vaga perdida, \
como el recuerdo triste de la vida\
en la mente del hombre agonizante. \
\
De la luna fulgente la luz pura,\
al través de la nube borrascosa, \
cual memoria de madre cariñosa \
en medio de 1a amarga desventura. \
\
De embarcación el mísero deshecho \
que gire por tu seno sosegado, \
como presentimiento desgraciado\
que hace agitar del navegante el pecho.\
\
Todo, todo lo harás interesante:\
¿no te habré de admirar? ¿Será vedado \
a mis oídos tu mugir sagrado\
Y siempre, siempre te tendré distante?\
\
¿La mano del dolor que me comprime, \
a perecer cautivo me destina\
entre paredes de ciudad mezquina \
sin venerar tu majestad sublime?\
\
¿O a ti, me llevará la suerte impía, \
cubierto de dolor, sin tener padre;\
sin mi dulce adorada; sin mi madre, \
lanzado, ay triste, de la patria mía?\
\
\
\
\
Al mar\
\
Te siento en mí: cuando tu voz potente\
Saludó retronando en lontananza,\
Se renovó mi ser; alcé la frente\
Nunca abatida por el hado impío\
Y vibrante brotó del pecho mío\
Un cántico de amor y de alabanza.\
\
Te encadenó el Señor en estas playas\
Cuando, Satán del mundo,\
Temerario plagiando el infinito,\
Le quisiste anegar, y en lo profundo \
Gimes ¡oh mar! en sempiterno grito.\
\
Tú también te retuerces cual remedo \
De la eterna agonía;\
También, como al ser mío,\
La soledad te cerca y el vacío;\
Y siempre en inquietud y en amargura,\
Te acaricia la luz del claro día,\
Te ven los astros de la noche oscura.\
\
A mí te vi venir, como en locura,\
Desparcido el cabello de tus ondas\
De espuma en el vaivén, como cercada\
De invisibles espíritus, llegando\
De abismos ignorados clamando\
En acentos humanos que morían\
Y el grito y el sollozo confundían.\
\
A mí te vi venir ¡oh mar divino!\
Y supe contener tanta grandeza,\
Como tiembla la gota de la lluvia\
En la hoja leve del robusto encino!\
\
Eres sublime ¡oh mar! Los horizontes\
Recogiendo las alas fatigadas,\
Se prosternan a ti desde los montes.\
\
Prendida de tus hombros la luz bella\
Forma los pliegues de tu manto inmenso.\
Entre la blanca bruma\
Se perciben los tumbos de tus ondas,\
Cual de hermosa en el seno palpitante\
Los encajes levísimos de espuma.\
\
Si te agitas, arrojas de tu seno\
En explosión tremenda las montañas, \
Y es un remedo de la brisa el trueno,\
Terrible mar, si gimen tus entrañas.\
\
¿Quién te describe ¡oh mar! cuando bravía, \
como mujer celosa,\
en medio de tu marcha procelosa\
el escollo tus iras desafía?\
\
Vas, te encrespas, te ciñes con porfía,\
Retrocedes rugiente,\
Y del tenaz luchar desesperada,\
Te precipitas en su negro seno\
Despedazando tu altanera frente.\
\
En tanto, el viento horrible,\
Arrastrando al relámpago y al rayo,\
Cimbra el espacio, rasga el negro velo\
De la tiniebla, se prosterna el mundo\
Y un siniestro contento se percibe\
¡oh mar! en lo profundo,\
cual si con esa pompa celebraras,\
entre el eterno duelo,\
tus nupcias con el cielo!\
\
Cansada de fatiga, cual si el aura\
Tierna te prodigara sus caricias,\
A su encanto dulcísimo te entregas,\
Clamas tu enojo, viertes tus sonrisas,\
Y como niña con las olas juegas\
Cuando te dan su música las brisas.\
\
Tú eres un ser de vida y de pasiones:\
Escuchas, amas, te enloqueces, lloras,\
Nos sobrecoges de terrible espanto,\
Embriagas de grandeza y enamoras.\
\
Cuando por vez primera ¡oh mar sublime!\
Me vi junto a ti, como tocando\
El borde del magnífico infinito,\
Dios, clamó el labio en entusiasta grito:\
Dios, repitió tu inquieta lontananza:\
Y dios, me pareció que proclamaban\
Las ondas, repitiendo mi alabanza.\
\
Entonces ¡ay! La juventud hervía\
En mi temprano corazón; la suerte,\
Cual guirnalda de luz, embellecía\
La frente horrible de la misma muerte.\
\
Y grande, grande el corazón, y abierto\
Al amor, a la patria y a la gloria,\
Émulo me sentí de tu grandeza\
Y mi orgullo me daba la victoria.\
Entonces ¡ay! En la ola que moría\
Reclinaba en la arena sollozando\
Recordaba el mirar de mi María,\
Sus lindos ojos y su acento blando.\
\
Si una huérfana rama atravesaba,\
Juguete de las ondas, cual yo errante,\
Lejos de su pensil y de su fuente,\
La saludaba con mi voz amante,\
La consolaba de la patria ausente.\
\
Si el pájaro perdido iba siguiendo\
Rendido de fatiga, mi navío,\
¡cuánto sufrir, Dios mío!\
Su ala se plega, aléjase la nave,\
Y se esfuerza y se abate y desfallece,\
Y convulso, arrastrándose en las ondas,\
El hijo de los bosques desaparece.\
\
En tanto, tus inmensas soledades\
La gaviota recorre, desafiando\
Las fieras tempestades.\
Entonces, en la popa, dominando\
La inmensa soledad, me parecía\
Que una voz a lo lejos me llamaba\
Y acentos misteriosos me decía:\
Y yo le preguntaba:\
¿Quién eres tú? ¿De la creación olvido,\
te quedaste tus formas esperando\
engendro indescifrable, en agonía\
entre el ser y el no ser siempre luchando?\
¿Al desunirse de la tierra el cielo\
en tus entrañas refugiaste el caos?\
¿O, mágica creación, rebelde un día,\
provocaste a tu Dios; se alzó tremendo;\
sobre tu frente derramó la nada,\
y te dejó gimiendo\
a tu muro de arena encadenada?\
\
¿O, promesa de bien, en tus cristales\
los átomos conservas que algún día,\
cuando la tierra muera,\
produzcan con encantos celestiales\
otra luz, otros seres, otro mundo,\
y entonces nuestro suelo\
a tus plantas, se llame mar profundo\
en que retrate su grandeza el cielo?\
\
Hoy llegué junto a ti como otro tiempo\
Siguiendo ¡oh Libertad! Tu blanca estela;\
Hoy llegué junto a ti cuando se hundía\
En abismos de horror y de anarquía\
La linfa de cristal de mi esperanza;\
Porque eres un poema de grandeza,\
Porque en ti el huracán sus notas vierte,\
Luz y vida coronan tu cabeza,\
Tienen por pedestal tiniebla y muerte.\
\
Nadie muere en la tierra; allí se duerme\
De tierna madre en el amante pecho:\
Velan cipreses nuestro sueño triste,\
Y riegan flores nuestro triste lecho.\
Solitaria una cruz dice al viajero\
Que pague su tributo\
De lágrimas y luto,\
En el extenso llano y el sendero.\
\
En ti se muere ¡oh mar! Ni la ceniza\
Le das al viento: en ola que sepulta \
La rica pompa de poblada nave,\
Nada conserva las mortales huellas;\
Se pierden. . . y en tu seno indiferente\
Nace la aurora y brillan las estrellas.\
\
A ti me entrego ¡oh mar! roto navío,\
Destrozado en las recias tempestades,\
Sin rumbo, sin timón, siempre anhelante\
Por el seguro puerto,\
Encerrando en mi pecho dolorido\
Las tumbas y el desierto. . .\
\
Pero humillado no; y en mi fiereza\
A ti tendiendo las convulsas manos,\
Sintiendo en ti de mi alma la grandeza\
Y ahogando mi tormento,\
Le pido a Dios la paz de mis hermanos;\
Y renuevo mi augusto juramento\
De mi odio a la traición y a los tiranos.\
\
Enero de 1877\
\
\
Ensueños\
\
Eco sin voz que conduce\
El huracán que se aleja,\
Ola que vaga refleja\
A la estrella que reluce;\
Recuerdo que me seduce\
Con engaños de alegría;\
Amorosa melodía\
Vibrando de tierno llanto, \
¿qué dices a mi quebranto,\
qué me quieres, quién te envía?\
\
Tiende su ala el pensamiento\
Buscando una sombra amiga,\
Y se rinde de fatiga\
En los mares del tormento;\
De pronto florido asiento\
Ve que en la orilla aparece,\
Y cundo ya desfallece\
Y más se acerca y le alcanza,\
Ve que su hermosa esperanza\
Es nube que desaparece.\
\
Rayo de sol que se adhiere\
A una gota pasajera,\
Que un punto luce hechicera\
Y al tocar la sombra muere.\
Dulce memoria que hiere\
Con los recuerdos de un cielo,\
Murmurios de un arroyuelo\
Que en inaccesible hondura\
Brinda al sediento frescura\
Con imposible consuelo,\
\
En inquietud, como el mar,\
Y sin dejar de sufrir,\
Ni es mi descanso dormir,\
Ni me consuela llorar.\
En vano quiero ocultar\
Lo que el pecho infeliz siente;\
Tras cada sueño aparente,\
Tras cada mentida calma,\
Hay más sombras en el alma,\
Más arrugas en la frente.\
\
Si bien entra este empeño\
En que tan doliente gimo\
La esperanza de un arrimo,\
De un halago en un ensueño, \
Si de mí no siendo dueño\
Sonreír grato me veis,\
Os ruego que recordéis\
Que estoy de dolor rendido. . .\
Pasad. . . dejadme dormido. . .\
Pasad. . . ¡no me despertéis!\
\
\
\
Cantares\
\
Yo soy quien sin amparo cruzó la vida\
En su nublada aurora, niño doliente,\
Con mi alma herida,\
El luto y la miseria sobre la frente;\
Y en mi hogar solitario y, agonizante,\
Mi madre amante.\
\
Yo soy quien vagabundo cuentos fingía,\
Y los ecos del pueblo que recogía\
Torné en cantares;\
Porque era el pueblo humilde toda mi ciencia\
Y era escudo, en mis luchas con la indigencia,\
De mis pesares.\
\
La soledad austera y el libre viento\
Le dieron a mi pecho robusto aliento,\
Fiera entereza;\
Y así tuvo mi lira cantos sentidos,\
En lo íntimo de mi alma sordos gemidos\
De mi pobreza.\
\
La nube quien volaba con alas de oro, \
La tórtola amorosa que se quejaba \
Como con lloro;\
El murmullo del aura que remedaba\
Las voces expresivas del sentimiento\
Cobijó mi acento.\
\
Y el bandolón que un barrio locuaz conmueve,\
Y el placer tempestuoso con que la plebe\
Muestra contento;\
Sus bailes, sus cantares y sus amores,\
Fueron luz arroyuelos, aves y flores\
De mi talento.\
\
Cantando ni yo mismo me sospechaba\
Que en mí, la patria hermosa con voz nacía,\
Que en mí brotaba\
Con sus penas , con sus gloria s y su alegría,\
Sus montes y sus lagos, su lindo cielo,\
Y su alma que en perfumes se esparcía.\
\
Entonces a la choza del jornalero,\
Al campo tumultuoso del guerrillero\
Llevé mis sones;\
Y no a regias beldades ni peregrinas,\
Sino a obreras modestas, a alegres chinas \
Di mis canciones.\
\
¡Oh patria idolatrada, yo en tus quebrantos,\
ensalcé con ternura tus fueros santos,\
sin arredrarme;\
tu tierra era mi carne, tu amor mi vida,\
hiel acerba en tus duelos fue mi bebida\
para embriagarme!\
\
YO tuve himnos triunfales para tus muertos,\
Mi voz sembró esperanzas en tus desiertos\
Y, complaciente,\
A la tropa cansada la consolaba,\
Y oyendo mis leyendas me reanimaba\
Riendo valiente.\
\
Hoy merezco recuerdo de ese pasado\
de luz y de tinieblas, de llanto y gloria;\
soy un despojo, un resto casi borrado \
de la memoria. . .\
\
Pero esta pobre lira que está en mis manos,\
Guarda para mi pueblo sentidos sones;\
Y acentos vengadores y maldiciones;\
A sus tiranos. . . ¡\
\
Septiembre de 1889\
\
\
Décimas Glosadas\
\
Pajarito corpulento,\
Préstame tu medecina\
Para curarme una espina\
Que tengo en el pensamiento,\
Que es traidora y me lastima.\
\
Es de muerte la aparencia\
Al dicir del hado esquivo;\
Pero está enterrado vivo\
Quien sufre males de ausencia.\
¿cómo hacerle resistencia\
a la juerza del tormento?\
Voy a remontarme al viento\
Para que tú con decoro\
Digas a mi bien que lloro,\
Pajarito corpulento.\
\
Dile que voy tentalenando\
En lo oscuro de mi vida,\
Porque es como luz perdida \
El bien por que estoy penando.\
Di que me estoy redibando\
Por su hermosura devina, \
Y, si la mirares fina,\
Pon mi ruego de por medio, \
Y dí: 'Tú eres su remedio;\
Préstame tu medecina.'\
\
El presil tiene sus flores\
Y el manantial sus frescuras,\
Y yo todas mis venturas y sus alegres amores\
Hoy me punzan los dolores\
Con terquedá tan indiana,\
Que no puedo estar ansina.\
Aigre, tierra, mar y cielo,\
¿quién quire darme un consuelo\
para curarme una espina?\
\
Es la deidad que yo adoro,\
Es mi calandria amorosa,\
Mi lluvia de hojas de rosa\
Y mi campanita de oro.\
Hoy su perdido tesoro\
Me tiene como en el viento,\
Sin abrigo, sin asiento:\
Su recuerdo de ternura\
Es como una sepultura\
Que tengo en el pensamiento.\
\
Es mirar la que era fuente\
Hoyo espantable y vacío;\
Es ver cómo mató el frío\
La mata airosa y potente;\
Es un sentir redepente\
A la muerte que se arrima,\
Es que tiene mi alma encima\
Una fantasma hechicera\
Que me sigue adonde quiera,\
Que es traidora y me lastima.\
\
\
\
Romance de la Migajita\
\
'¡Détente! Que está rendida,\
¡eh, contente, no la mates!'\
Y aunque la gente gritaba \
Corraía como el aire,\
Cuando quiso ya no pudo, \
Aunque quiso llegó tarde,\
Que estaba la Migajita\
Revolcándose en su sangre. . .\
Sus largas trenzas en tierra,\
Con la muerte al abrazarse,\
Las miramos de rodillas\
Ante el hombre, suplicante;\
Pero él le dio tres metidas \
Y una al sesgo de remache.\
De sus labios de claveles\
Salen dolientes los ayes,\
Se ven entre sus pestañas,\
Los ojos al apagarse. . .\
Y el Ronco está como piedra\
En medio de los sacrifantes,\
Que lo atan codo con codo\
Para llevarlo a la cárcel.\
\
'Ve al hespital, Migajita,\
vete con los palticantes,\
y atente a la Virgen pura\
para que tu alma se salve.\
¡Probrecita casa sin tus brazos!\
¡Pobrecita de tu madre!\
¿Y quién te lo hubiera dicho,\
tan preciosa cono un ángel, \
con tu rebozo de seda,\
con tus sartas de corales, \
con tus zapatos de raso\
que ibas llenando la calle,\
como guardando tus gracias,\
porque no se redamasen.\
\
El celo es punta de rabia,\
El celo alcanzó matarte,\
Que es veneno que hace furias\
Las mas finas voluntades.\
\
Esto dijo con conciencia\
Una siñora ya grande\
Que vido del papa al pepe\
Cómo pasó todo el lance.\
\
Y yendo y viniendo días\
La Migajita preciosa\
Fue retoñando en San Pablo;\
Pero la infeliz era otra;\
Está como pan de cera,\
El aigre la desmorona,\
Se le pintan las costillas,\
Se alevanta con congoja;\
Sólo de sus lindos ojos\
Llamas de repente brotan.\
\
'¡Muerto!. . .¡dése!' A la ventana\
la pobre herida se asoma,\
y vio que llevan difunto,\
por otra mano alevosa,\
a su Ronco que idolatra,\
que fue su amor y su gloria.\
\
Olvida que está baldada\
Y de sus penas se olvida,\
Y corre como una loca,\
Y al muerto se precipita,\
Y aulla de dolor la triste\
Llenándolo de caricias.\
\
'Madre, mi madre (le dice)\
-que su madre la seguía -,\
vendan mis aretes de oro,\
mis trasts de loza fina,\
mis dos rebozos de seda,\
\
y el rebozo de bolita;\
vendan mis tumbagas de oro,\
y de coral la soguilla,\
y mis arracadas grandes,\
guarnecidas con perlitas;\
vendan la cama de fierro,\
y el ropero y las camisas,\
y entierren con lujo a ese hombre\
porque era el bien de mi vida;\
que lo entierren con mi almohjada\
con su funda de estopilla,\
que pienso que su cabeza\
con el palo se lastima.\
\
Que le ardan cirios de cera,\
Cuatro, todos de a seis libras; \
que le pongan muchas flores,\
Que le digan muchas misas\
Mientras que me arranco el alma\
Para hacerle compañía.\
\
Tú, ampáralo con tu sombra,\
Sálvalo, Virgen María:\
Que si en esta positura\
Me puso, lo merecía;\
No porque le diera causa,\
Pues era suya mi vida'. . .\
\
Y dando mil alaridos\
La infelice Migajita,\
Se arrancaba los cabellos,\
Y aullando se retorcía.\
De pronto los gritos cesan,\
De pronto se quedó fija:\
Se acercan los platicantes,\
La encuentran sin vida y fría,\
Y el silencio se destiende\
Convirtiendo en noche el día.\
\
En el panteón de Dolores,\
Lejos, en la última fila,\
Entre unas cruces de palo\
Nuevas o medio podridas,\
Hay una cruz levantada\
De pulida cantería,\
Y en ella el nombre del Ronco,\
'Arizpe José Marías',\
y el pie, en un montón de tierra,\
medio cubierto de ortigas,\
sin que lo sospeche nadie\
reposa la Migajita,\
flor del barrio de la Palma\
y envidia de las catrinas.",
                    path=u"/c", tags=u"GP")

writer.add_document(title=u"Ignacio Manuel Altamirano", content=u"Atoyac\
\
Abrase el sol de julio las playas arenosas\
Que azota con sus tumbos embravecido el mar;\
Y opongan en su lucha las aguas orgullosas\
Al encendido rayo su ronco rebramar.\
\
Tú corres blandamente bajo la fresca sombra\
Que el mangle con sus ramas espesas te formó;\
Y duermen tus remansos en la mullida alfombra\
Que dulce Primavera de flores matizó.\
\
Tú juegas en las grutas que forman tus riberas\
De ceibas y parotas el bosque colosal;\
Y plácido murmuras al pie de las palmeras,\
Que esbeltas se retratan en tu onda de cristal.\
\
En este Edén divino, que esconde aquí la costa,\
El sol ya no penetra con rayo abrasador;\
Su luz, cayendo tibia, los árboles no agosta,\
Y en tu enramada espesa se tiñe de verdor.\
\
Aquí sólo se escuchan murmullos mil suaves,\
El blando son que forman tus linfas al correr,\
La planta cuando crece, y el canto de las aves,\
Y el aura que suspira, las ramas al mecer.\
\
Osténtanse las flores que cuelgan de tu techo\
En mil y mil guirnaldas para adornar tu sien;\
Y el gigantesco loto, que brota de tu lecho,\
Con frescos ramilletes inclínase también.\
\
Se dobla en tus orillas, cimbrándose, el papayo,\
El mango con sus pomas de oro y de carmín;\
Y en los ilamos saltan, gozoso el papagayo,\
El ronco carpintero y el dulce colorín.\
\
A veces tus cristales se apartan bulliciosos\
De tus morenas ninfas jugando en derredor;\
Y amante les prodigas abrazos misteriosos,\
Y lánguido recibes sus ósculos de amor.\
\
Y cuando el sol se oculta detrás de los palmares,\
Y en tu salvaje templo comienza a obscurecer,\
Del ave te saludan los últimos cantares\
Que lleva de los vientos el vuelo postrimer.\
\
La noche viene tibia; se cuelga ya brillando\
La blanca luna, en medio de un cielo de zafir,\
Y todo allá en los bosques se encoge y va callando,\
Y todo en tus riberas empieza ya a dormir.\
\
Entonces en tu lecho de arena, aletargado,\
Cubriéndose las palmas con lúgubre capuz,\
También te vas durmiendo, apenas alumbrado\
Del astro de la noche por la argentada luz.\
\
Y así resbalas muelle; ni turban tu reposo\
Del remo de las barcas el tímido rumor,\
Ni el repentino brinco del pez que huye medroso\
En busca de las peñas que esquiva el pescador.\
\
Ni el silbo de los grillos que se alza en los esteros,\
Ni el ronco que a los aires los caracoles dan,\
Ni el hueco vigilante que en gritos lastimeros\
Inquieta entre los juncos el sueño del caimán.\
\
En tanto los cocuyos en polvo refulgente\
Salpican los umbrosos yerbajes de huamil,\
Y las oscuras malvas de algodón naciente,\
Que crece de las cañas de maíz entre el carril.\
\
Y en tanto en la cabaña, la joven que se mece\
En la ligera hamaca y en lánguido vaivén.\
Arrúllase cantando la zamba que entristece\
Mezclado con las trovas el suspirar también.\
\
Mas de repente, al aire resuenan los bordones\
Del arpa de la costa con incitante son;\
Y agítanse y preludian la flor de las canciones,\
La dulce malagueña que alegra el corazón.\
\
Entonces, de los Barrios la turba placentera\
En pos del arpa el bosque comienza a recorrer,\
Y todo en breve es fiestas y danza en tu ribera,\
Y todo amor y cantos y risas y placer.\
\
Así transcurren breves y sin sentir las horas;\
Y de tus blandos sueños en medio del sopor\
Escuchas a tus hijas, morenas seductoras,\
Que entonan a la luna sus cántigas de amor.\
\
Las aves en sus nidos, de dicha se estremecen,\
Los floripondios se abren su esencia a derramar;\
Los céfiros despiertan, y suspirar parecen;\
Tus aguas en el álveo se sienten palpitar.\
\
¡Ay! ¿Quién en estas horas en que el insomnio ardiente\
Aviva los recuerdos del eclipsado bien,\
No busca el blando seno de la querida ausente\
Para posar los labios y reclinar la sien?\
\
Las palmas se entrelazan, la luz en sus caricias\
Destierra de tu lecho la triste oscuridad:\
Las flores a las auras inundan de delicias...\
Y sólo el alma siente su triste soledad.\
\
Adiós, callado río: tus verdes y risueñas\
Orillas, no entristezcan las quejas del pesar;\
Que oírlas sólo deben las solitarias peñas\
Que azota, con sus tumbos, embravecido el mar.\
\
Tú queda reflejando la luna en tus cristales,\
Que pasan en tus bordes tupidos a mecer\
Los verdes ahuejotes y azules carrizales,\
Que al sueño ya rendidos volviéronse a caer.\
\
Tú corre blandamente bajo la fresca sombra\
Que el mangle con sus ramas espesas te formó;\
Y duermen tus remansos en la mullida alfombra\
Que alegre Primavera de flores matizó.\
\
\
Los naranjos\
\
\
Perdiéronse las neblinas\
En los picos de la sierra,\
Y el sol derrama en la tierra\
Su torrente abrasador.\
Y se derriten las perlas\
Del argentado rocío,\
En las adelfas del río\
Y en los naranjos en flor.\
\
Del mamey el duro tronco\
Picotea el carpintero,\
Y en el frondoso manguero\
Canta su amor el turpial;\
Y buscan miel las abejas\
En las piñas olorosas,\
Y pueblan las mariposas\
El florido cafetal.\
\
Deja el baño, amada mía,\
Sal de la onda bullidora;\
Desde que alumbró la aurora\
Jugueteas loca allí.\
¿Acaso el genio que habita\
De ese río en los cristales,\
Te brinda delicias tales\
Que lo prefieres a mí?\
\
¡Ingrata! ¿por qué riendo\
Te apartas de la ribera?\
Ven pronto, que ya te espera\
Palpitando el corazón\
¿No ves que todo se agita,\
Todo despierta y florece?\
¿No ves que todo enardece\
Mi deseo y mi pasión?\
\
En los verdes tamarindos\
Se requiebran las palomas,\
Y en el nardo los aromas\
A beber las brisas van.\
¿Tu corazón, por ventura,\
Esa sed de amor no siente,\
Que así se muestra inclemente\
A mi dulce y tierno afán?\
\
¡Ah, no! perdona, bien mío;\
Cedes al fin a mi ruego;\
Y de la pasión el fuego\
Miro en tus ojos lucir.\
Ven, que tu amor, virgen bella,\
Néctar es para mi alma;\
Sin él, que mi pena calma,\
¿Cómo pudiera vivir?\
\
Ven y estréchame, no apartes\
Ya tus brazos de mi cuello,\
No ocultes el rostro bello\
Tímida huyendo de mí.\
Oprímanse nuestros labios\
En un beso eterno, ardiente,\
Y transcurran dulcemente\
Lentas las horas así.\
\
En los verdes tamarindos\
Enmudecen las palomas;\
En los nardos no hay aromas\
Para los ambientes ya.\
Tú languideces; tus ojos\
Ha cerrado la fatiga\
Y tu seno, dulce amiga,\
Estremeciéndose está.\
\
En la ribera del río,\
Todo se agosta y desmaya;\
Las adelfas de la playa\
Se adormecen de calor.\
Voy el reposo a brindarte\
De trébol en esta alfombra\
De los naranjos en flor.\
\
\
Salir de Acapulco\
\
A bordo del vapor 'St. Louis' de la línea del Pacífico.\
El 30 de octubre de 1863, a las once de la noche\
\
\
....Aun diviso tu sombra en la ribera,\
Salpicada de luces cintilantes,\
Y aun escucho a la turba vocinglera\
\
De alegres y despiertos habitantes,\
Cuyo acento lejano hasta mi oído\
Viene el terral trayendo, por instantes.\
\
Dentro de poco ¡ay Dios! Te habré perdido,\
Ultima, que pisara cariñoso,\
Tierra encantada de mi Sur querido.\
\
Me arroja mi destino tempestuoso,\
¿Adónde? No lo sé; pero yo siento\
De su mano el empuje poderoso.\
\
¿Volveré? Tal vez no; y el pensamiento\
Ni una esperanza descubrir podría \
En esta hora de huracán sangriento.\
\
Tal vez te miro el postrimero día,\
Y el alma que devoran los pesares\
Su adiós eterno, desde aquí te envía.\
\
Quédate pues, ciudad de los palmares,\
En tus noches tranquilas arrullada\
Por el acento de los roncos mares.\
\
Y a orillas de tu puerto recostada,\
Como una ninfa en el verano ardiente\
Al borde de un estanque desmayada.\
\
De la sierra el dosel cubre tu frente,\
Y las ondas del mar siempre serenas\
Acarician tus plantas dulcemente.\
\
¡Oh suerte infausta! ¡Me dejaste apenas\
De una ligera dicha los sabores,\
Y a desventura larga me condenas!\
\
Dejarte ¡oh Sur! Acrece mis dolores,\
Hoy que en tus bosques quédase escondida\
La hermosura y tierna flor de mis amores,\
\
Guárdala ¡oh Sur! Y su existencia cuida\
Y con ella alimenta mi esperanza\
¡Porque es su aroma el néctar de mi vida!\
\
Mas ya te miro huir; en lontananza\
Oigo alegre el adiós de extraña gente,\
el buque, lento en su partida avanza.\
\
Todo ríe en la cubierta indiferente;\
Sólo yo con el pecho palpitando,\
Te digo adiós con labio balbuciente.\
\
La niebla de la mar te va ocultando;\
Faro, remoto ya, tu luz semeja;\
Ruge el vapor, y el Leviatán bramando.\
\
Las anchas sombras de los montes deja.\
Presuroso atraviesa la bahía,\
Salva la entrada y a la mar se aleja;\
\
Y en la llanura lóbrega y sombría\
Abre en su carrera acelerada\
Un surco de brillante argentería.\
\
La luna, entonces, hasta aquí velada,\
Súbita brota en el zafir desnuda,\
Brillando en alta mar: Mi alma agitada\
Pensando en Dios, la inmensidad saluda.\
\
\
Recursos\
\
\
Se oprime el corazón al recordarte,\
Madre, mi único bien, mi dulce encanto;\
Se oprime el corazón y se me parte,\
Y me abrasa los párpados el llanto.\
\
Lejos de ti y en la orfandad, proscrito,\
Verte nomás en mi delirio anhelo;\
Como anhela el presito\
Ver los fulgores del perdido cielo.\
\
¡Cuánto tiempo, mi madre, ha transcurrido\
Desde ese día en que la negra suerte\
Nos separó cruel!... ¡Tanto he sufrido\
Desde entonces, oh Dios, tanto he perdido,\
Que siento helar mi corazón de muerte!\
\
¿No lloras tú también ¡oh madre mía!\
Al recordarme, al recordar el día\
En que te dije adiós, cuando en tus brazos\
Sollozaba infeliz al separarme,\
Y con el seno herido hecho pedazos,\
Aun balbucí tu nombre al alejarme?\
\
Debiste llorar mucho. Yo era niño\
Y comencé a sufrir, porque al perderte\
Perdí la dicha del primer cariño.\
Después, cuando en la noche solitaria\
Te busqué para orar, sólo vi el cielo,\
Al murmurar mi tímida plegaria,\
Mi profundo y callado desconsuelo.\
\
Era una noche obscura y silenciosa,\
Sólo cantaba el búho en la montaña;\
Sólo gemía el viento en la espadaña\
De la llanura triste y cenagosa.\
Debajo de una encina corpulenta\
Inmóvil entonces me postré de hinojos,\
Y mi frente incliné calenturienta.\
\
¡Oh! ¡cuánto pensé en ti llenos los ojos\
de lágrimas amargas! ... la existencia.\
Fue ya un martirio, y erial de abrojos\
El sendero del mundo con tu ausencia.\
\
Mi niñez pasó pronto, y se llevaba\
Mis dulces ilusiones una a una;\
No pudieron vivir, no me inspiraba\
El dulce amor que protegió mi cuna.\
Vino después la juventud insana,\
Pero me halló doliente caminando\
Lánguido en pos de la vejez temprana,\
Y las marchitas flores deshojando\
Nacidas al albor de mi mañana.\
\
Nada gocé; mi fe ya está perdida;\
El mundo es para mí triste desierto;\
Se extingue ya la lumbre de mi vida,\
Y el corazón, antes feliz, ha muerto.\
\
Me agito en la orfandad, busco un abrigo\
Donde encontrar la dicha, la ternura\
De los primeros días; ni un amigo\
Quiere partir mi negra desventura.\
Todo miro al través del desconsuelo;\
Y ni me alivia en mi dolor profundo\
El loco goce que me ofrece el mundo,\
Ni la esperanza que sonríe en el cielo.\
\
Abordo ya la tumba, madre mía,\
Me mata ya el dolor... voy a perderte,\
Y el pobre ser que acariciaste un día\
¡Presa será temprano de la muerte!\
\
Cuando te dije adiós, era yo niño:\
Diez años hace ya; mi triste alma\
Aún siente revivir su antigua calma\
Al recordar tu celestial cariño.\
\
Era yo bueno entonces, y mi frente\
Muy tersa aún tu ósculo encontraba...\
Hace años, de dolor la reja ardiente\
Allí dos surcos sin piedad trazaba.\
\
Envejecí en la juventud, señora;\
Que la vejez enferma se adelanta,\
Cuando temprano en el dolor se llora,\
Cuando temprano el mundo desencanta,\
Y el iris de la fe se descolora.\
\
Cuando contemplo en el confín del cielo,\
En la mano apoyando la mejilla,\
Mis montañas azules, esa sierra\
Que apenas a vislumbrar mi vista alcanza,\
Dios me manda el consuelo,\
Y renace mi férvida esperanza,\
Y me inclino doblando la rodilla,\
Y adoro desde aquí la hermosa tierra\
De las altas palmeras y manglares,\
De las aves hermosas, de las flores,\
De los bravos torrentes bramadores,\
Y de los anchos ríos como mares,\
Y de la brisa tibia y perfumada\
Do tu cabaña está mujer amada.\
\
Ya te veré muy pronto madre mía;\
Ya te veré muy pronto, ¡Dios lo quiera!\
Y oraremos humildes ese día\
Junto a la cruz de la montaña umbría,\
Como en los años de mi edad primera.\
Olvidaré el furor de mis pasiones.\
Me volverán rientes una a una\
De la niñez las dulces ilusiones,\
El pobre techo que abrigó mi cuna.\
Reclinaré en tu hombro mi cabeza\
Escucharás mis quejas de quebranto,\
Velarás en mis horas de tristeza\
Y enjugarás las gotas de mi llanto.\
\
Huirán mi duda, mi doliente anhelo.\
Recuerdos de mi vida desdichada;\
Que allí estarás, ¡oh ángel de consuelo!\
Pobre madre infeliz... ¡madre adorada!.\
\
\
María\
\
\
Allí en el valle fértil y risueño,\
Do nace el Lerma y, débil todavía\
Juega, desnudo de la regia pompa\
Que lo acompaña hasta la mar bravía;\
Allí donde se eleva\
El viejo xinantécatl, cuyo aliento,\
Por millares de siglos inflamado,\
Al soplo de los tiempos se ha apagado,\
Pero que altivo y majestuoso eleva\
Su frente que corona eterno hielo\
Hasta esconderla en el azul del cielo.\
\
Allí donde el favonio murmurante\
Mece los frutos de oro del manzano\
Y los rojos racimos del cerezo\
Y recoge en sus alas vagarosas\
La esencia de los nardos y las rosas.\
\
Allí por vez primera\
Un extraño temblor desconocido,\
De repente, agitado y sorprendido\
Mi adolescente corazón sintiera.\
\
Turbada fue de la niñez la calma,\
Ni supe qué pensar en ese instante\
Del ardor de mi pecho palpitante\
Ni de la tierna languidez del alma.\
\
Era el amor: mas tímido, inocente,\
Ráfaga pura del albor naciente,\
Apenas devaneo\
Del pensamiento virginal del niño;\
No la voraz hoguera del deseo,\
Sino el risueño lampo del cariño.\
\
Yo la miré una vez, virgen querida\
Despertaba cual yo, del sueño blando\
De las primeras horas de la vida:\
Pura azucena que arrojó el destino\
De mi existencia en el primer camino,\
Recibían sus pétalos temblando\
Los ósculos del aura bullidora\
Y el tierno cáliz encerraba apenas\
El blanco aliento de la tibia aurora.\
\
Cuando en ella fijé larga mirada\
De santa adoración, sus negros ojos\
De mi apartó; su frente nacarada\
Se tiñó del carmín de los sonrojos;\
Su seno se agitó por un momento,\
Y entre sus labios espiró su acento.\
\
Me amó también. Jamás amado había;\
Como yo, esta inquietud no conocía,\
Nuestros ojos ardientes se atrajeron\
Y nuestras lamas vírgenes se unieron\
Con la unión misteriosa que preside\
El hado, entre las sombras, mudo y ciego,\
Y de la dicha del vivir decide\
Para romperla sin clemencia luego.\
\
¡Ay! Que esta unión purísima debiera\
No turbarse jamás, que así la dicha\
Tal vez perenne en la existencia fuera:\
¿Cómo no ser sagrada y duradera\
si la niñez entretejió sus lazos\
Y la animó, divina, entre sus brazos\
La castidad de la pasión primera?\
\
Pero el amor es árbol delicado\
Que el aire puro de la dicha quiere,\
Y cuando de dolor el cierzo helado\
Su frente toca, se doblega y muere.\
\
¿No es verdad? ¿no es verdad, pobre María?\
¿Por qué tan pronto del pesar sañudo\
Pudo apartarnos la segura impía?\
¿Cómo tan pronto obscurecernos pudo\
La negra noche en el nacer del día?\
\
¿Por qué entonces no fuimos más felices?\
¿Por qué después no fuimos más constantes?\
¿Por qué en el débil corazón, señora,\
Se hacen eternos siglos los instantes,\
Desfalleciendo antes\
De apurar del dolor la última hora?\
\
¡Pobre María! Entonces ignorabas\
Y yo también, lo que apellida el mundo \
¡Amor... amor! Y ciega no pensabas\
Que es perfidia, interés, deleite inmundo,\
Y que tu alma pura y sin mancilla\
Que amó como los ángeles amaran\
Con fuego intenso, mas con fe sencilla,\
Iba a encontrarse sola y sin defensa\
De la maldad entre la mar inmensa.\
\
Entonces, en los días inocentes\
De nuestro amor, una mirada sola\
Fue la felicidad, los puros goces\
De nuestro corazón... el casto beso,\
La tierna y silenciosa confianza,\
La fe en el porvenir y la esperanza.\
\
Entonces... en las noches silenciosas\
¡Ay! Cuántas horas contemplamos juntos\
Con cariño las pálidas estrellas\
En el cielo sin nubes cintilando,\
Como si en nuestro amor gozaran ellas;\
O el resplandor benéfico y amigo\
De la callada luna,\
De nuestra dicha plácido testigo,\
O a las brisas balsámicas y leves\
Con placer confiamos\
Nuestros suspiros y palabras breves.\
\
¡Oh! ¿qué mal hace al cielo \
Este modesto bien, que tras él manda\
De la separación el negro duelo,\
La frialdad espantosa del olvido\
Y el amargo sabor del desengaño,\
Tristes reliquias del amor perdido?\
\
Hoy sabes qué sufrir, pobre María,\
Y sentiste al presente\
El desamor que mezcla su hiel fría\
De los placeres en la copa ardiente,\
El cansancio, la triste indiferencia,\
\
Y hasta el odio que impío\
El antes cielo azul de la existencia\
Nos convierte en un cóncavo sombrío,\
Y la duda también, duda maldita\
Que de acíbar eterno el alma llena,\
La enturbia y envenena\
Y en el caos del mal la precipita.\
\
Muy pronto, sí, nos condenó la suerte\
A no vernos jamás hasta la muerte:\
Corrió la primera lágrima encendida\
Del corazón a la primera herida,\
Mas pronto se siguió el pensar profundo, \
Del desdén la sonrisa amenazante\
Y la mirada de odio chispeante,\
Terrible reto de venganza al mundo.\
\
Mucho tiempo pasó. Tristes seguimos\
El mandato cruel del hado fiero,\
Contrarias sendas recorriendo fuimos\
Sin consuelo ni afán... Y bien, señora,\
¿Podremos sin rubor mirarnos ora?\
¡Ah! ¡qué ha quedado de la virgen bella!\
Tal vez la seducción marcó su huella\
\
En tu pálida frente ya surcada,\
Porque contemplo en tus hundidos ojos\
Señal de llanto y lívida mirada.\
Con el fulgor de acero de la ira.\
Se marchitaron los claveles rojos\
Sobre tus labios ora contraidos\
Por risa de desdén que desafía\
Tu bárbaro pesar, ¡pobre María!\
\
Y yo... yo estoy tranquilo:\
Del dolor las tremendas tempestades,\
Roncas rugieron agitando el alma;\
La erupción fue terrible y poderosa...\
Pero hoy volvió la calma\
Que se turbó un momento,\
Y aunque siente el volcán mugir violento\
El fuego adentro del, nunca se atreve\
Su cubierta a romper de dura nieve.\
\
Continuemos, mujer, nuestro camino.\
¿Dónde parar? ...¿Acaso los sabemos?\
¿Lo sabemos acaso? Que destino\
Nos lleve como ayer: ciegos vaguemos,\
Ya que ni un faro de esperanza vemos\
Llenos de duda y de pesar marchamos,\
Marchamos siempre, y a perdernos vamos\
¡Ay! De la muerte en el océano obscuro,\
¿Hay más allá riberas?... no es seguro,\
Quién sabe si las hay; mas si abordamos\
A esas riberas torvas y sombrías\
Y siempre silenciosas,\
Allí sabré tus quejas dolorosas,\
Y tú también escucharás las mías.\
\
\
A Ofelia Plisse\
\
Yo no te vi jamás; pero hubo un día\
En que un patriota y joven peregrino\
Que de esa tierra donde existes, vino\
Hasta las playas de la patria mía,\
Conmovido me habló de tu hermosura\
Que de una diosa el don llamarse puede,\
Y que admirable y rara, sólo cede\
A la santa virtud de tu alma pura.\
\
Cruzaba yo, me dijo tristemente,\
Mi camino erial desfallecido\
Temiendo sucumbir, mas de repente\
Me encontré sorprendido\
Al levantar mi dolorida frente,\
Con un carmen florido;\
Que resguardan altivos cocoteros,\
Que embalsaman obscuros limoneros,\
Y que esmaltan jazmines y amapolas,\
Y que mecen pujantes\
De dos océanos las inmensas olas.\
\
Es Panamá la bella; la cintura\
De la virgen América, allí donde\
Del mundo de Colón el cielo esconde\
La grandeza futura.\
\
Como símbolo santo, hermoso y puro\
De esa edad venturosa y anhelada,\
Cuya luz ya descubre la mirada\
Del porvenir en el confín obscuro,\
Existe una beldad, joven, risueña,\
Inteligente, dulce y seductora\
Como un amante en sus afanes sueña,\
Como un creyente en su delirio adora.\
\
Es Ofelia, la diosa de ese suelo,\
La maga de ese carmen encantado,\
De dicha imagen ideal deseado,\
El astro fulgurante de aquel cielo.\
\
La perfumada flor, la que descuella,\
De corola gentil, fresca y lozana,\
Abriéndose a la luz de la mañana\
En los jardines ístmicos, ¡es ella!\
\
Allí la admiración le erigió altares,\
Incienso le da Amor, la Poesía\
Le consagra dulcísimos cantares;\
Y un himno inmenso Libertad le envía\
Entre el ronco suspiro de los mares.\
\
Yo la vi, la adoré cual peregrino\
A quien la mano del dolor dirige;\
Adorarla y pasar fue mi destino.\
¡Ay! Yo me alejo, mi deber lo exige,\
Mas su recuerdo alumbra mi camino;\
Yo llevaré su imagen por do quiera,\
Y confundiendo en uno mis dolores\
Y en un objeto uniendo mis amores,\
Yo escribiré su nombre en mi bandera.\
\
Tú a esa tierra lejana\
En las dóciles alas de los vientos\
Envía de tu lira los acentos\
A esa beldad que he visto, soberana.\
\
Así me dijo el joven peregrino\
Y siguió con tristeza su camino.\
\
\
A orillas del mar\
\
Esos bosques de ilamos y de palmas\
Que refrescan las ondas murmurantes\
Del cristalino Técpam, al cansado\
Pero tranquilo labrador convidan\
En los ardores de la ardiente siesta\
A reposar bajo su sombra grata,\
Que él si podrá sin dolorosa lucha\
Libre de afanes entregarse al sueño.\
\
Mas yo que el alma siento combatida \
De tenaces recuerdos y cuidados\
Que sin cesar me siguen dolorosos,\
Olvido y sueño con esfuerzo inútil,\
En vano procuré la blanda alfombra\
De césped y de musgo, horrible lecho\
De arena ardiente y de espinosos cardos\
Fue para mí. De la inquietud la fiebre\
Me hace de allí apartar, y en mi tristeza,\
Vengo a buscar las solitarias dunas\
Que el ronco tumbo de la mar azota.\
\
Esta playa que abrasa un sol de fuego,\
Esta llanura inmensa que se agita,\
Del fiero Sud al irritado soplo,\
Y este cielo do van espesas nubes\
Negro dosel en su reunión formando\
Al infortunio y al pesar convienen.\
\
Aquí, los ojos en las ondas fijos,\
Pienso en la Patria ¡ay Dios! Patria infelices,\
De eterna esclavitud amenazada\
Por extranjeros déspotas. La ira\
Hierve en el fondo del honrado pecho\
Al recordar que la cobarde turba\
De menguados traidores, que en malhora\
La sangre de su seno alimentara,\
La rodilla doblando ante el injusto,\
El más injusto de los fieros reyes\
Que a la paciente Europa tiranizan,\
Un verdugo pidiera para el pueblo,\
Que al fin cansado rechazó su orgullo.\
\
¡Francia! País de corazón tan grande,\
De pensamiento generoso y libre,\
Tú que alumbraste al mundo esclavizado\
Y soplaste al alma de los pueblos,\
En los modernos siglos, ese odio\
Que va minando el trono de los reyes;\
\
Tú que recuerdas con tremenda ira\
Las orgías del inglés en tus hogares,\
Y el insultante grito del cosaco\
Al pisar el cadáver del imperio,\
¿cómo vienes ahora en tus legiones\
El lábaro feroz de la ignorancia\
Y de la injusta y negra servidumbre\
A un pueblo libre que te amó, trayendo?\
¿Tu misión olvidaste con tu historia\
Y manchas tus blasones, despreciando\
Tu pura fama, al interés vendida?\
\
\
Yo te miro República naciente\
Ahogar la débil libertad de Roma;\
Yo te miro después apresurada\
Dar un abrazo a Austria sobre Hungría;\
Yo te miro más tarde abandonando\
De los zares al fiero despotismo\
La suerte ¡ay! De la infeliz Polonia,\
Y voy a maldecirte... y me detengo.\
No eres tú, no eres tú, pueblo grandioso\
Que a la divina Libertad consagras\
\
Dentro tu corazón ardiente culto,\
Sino el tirano odioso que te oprime\
Raquítico remedo de aquel hombre\
Colosal que cayó, cuya grandeza\
De escaño sirve y pedestal y asilo\
A la ambición del mísero pequeño.\
\
Tal el nombre de César y de Augusto\
Tiranos, sí, más grandes, elevara\
La obscura mezquindad de Cayo el loco\
Del imbécil Claudio y de Enobardo infame.\
\
Tú gimes, tú también, pueblo de libres\
Encadenado ahora al soli férreo\
Que tu paciencia sufre y abomina;\
Mas su injusticia y su furor acusan \
El grito de tus nobles desterrados\
Y la voz varonil de tus tribunos\
Y la cólera santa que te agita.\
\
En tanto, de mi Patria los fecundos\
Campos abrasa el fuego de la guerra;\
Gimen sus pueblos y la sangre corre\
En los surcos que abriera laborioso\
El labrador que con horror contempla\
El paso de tus huestes destructoras.\
\
Ruge el cañón y con su acento anuncia\
La elevación de un rey en esta tierra\
De la América libre, cuyo jugo,\
Es veneno letal a los tiranos,\
Y esta nueva desgracia, todavía\
Mi triste patria a tus soldados debe.\
\
El trono del Habsburgo se levanta\
Sobre bases de sangre y de ruina,\
¿Cómo existir podrá, si sus cimientos\
el amor de los pueblos no sostiene?\
Su ejército servil corre furioso,\
A sangre y fuego su pendón llevando;\
La falacia precede tentadora,\
\
Que a las almas mezquinas avasalla;\
Y se diezman del pueblo las legiones,\
Y los pechos menguados desfallecen,\
Y en el cielo parece que se eclipsa\
¡De libertad la fulgurante estrella!\
\
¡Solemne instante de angustiosa duda\
Para el alma de cieno del cobarde!\
¡Solemne instante de entusiasmo fiero\
Para el alma ardorosa del creyente!\
¡Oh no, jamás! La Libertad es grande,\
Como grande es el Ser de donde emana.\
¿Qué pueden en si contra los reptiles?\
\
Ya encendido en el cielo el sol parece\
Entre nubes de púrpura brillando...\
¡Es el astro de Hidalgo y de Morelos\
Nuncio de guerra, de venganza y gloria,\
Y el que miró Guerrero en su infortunio,\
Faro de libertad y de esperanza,\
Y el que vio Zaragoza en Guadalupe\
La sublime victoria prometiendo!\
\
A su esplendor renuévanse la lucha,\
Crece el aliento, la desgracia amengua;\
La ancha tierra de Méjico agitada\
Se estremece al fragor de los cañones,\
Desde el confín al centro, en las altivas\
Montañas que domina el viejo Ajusco,\
Del norte en las llanuras y en las selvas\
Fieras de Michoacán y donde corren \
El Lerma undoso y el salvaje Bravo;\
De Oaxaca en las puertas que defienden \
Nobles sus hijos de entusiasmo llenos\
Y en el áspero Sur, altar grandioso\
A libertad por siempre consagrado.\
Y en las playas que azota rudo Atlante\
Y en las que habita belicoso pueblo\
Y el Pacífico baña majestuoso.\
\
Sí, donde quiera en la empeñada lucha\
Altivo el patrio pabellón ondea,\
¿Qué importa que el cobarde abandonado\
Las filas del honor corra a humillarse\
Del déspota a las plantas, tembloroso?\
¿Qué importa la miseria? ¿ qué la dura\
Intemperie y las bárbaras fatigas?\
¿Qué el aspecto terrible del cadalso?\
Este combate al miserable aparta,\
Del desamparo el fuerte no se turba\
Sólo el vil con el número bravea.\
¡Cuán hermoso es sufrir honrado y libre,\
Y al cadalso subir del despotismo\
Por la divina Libertad, cuán dulce!\
\
¡Oh! Yo te adoro Patria desdichada\
Y con tu suerte venturosa sueño,\
Me destrozan el alma tus dolores\
Tu santa indignación mi pecho sufre,\
Ya en tu defensa levanté mi acento.\
\
Tu atroz ultraje acrecentó mis odios,\
¡Hoy mis promesas sellaré con sangre\
Que en tus altares consagré mi vida!\
\
El triunfo aguarda, el porvenir sonríe,\
Pueda el destino favorable luego,\
Dar a tus hijos que combaten bravos\
Menos errores y mayor ventura.\
Pero si quiere la enemiga suerte\
De nuevo hacer que encadenada llores\
Antes que verte en servidumbre horrenda\
Pueda yo sucumbir, ¡oh Patria mía!\
\
\
\
La salida del sol\
\
\
Ya brotan del sol naciente\
los primeros resplandores,\
dorando las altas cimas\
de los encumbrados montes.\
Las neblinas de los valles \
hacia las alturas corren, \
y de las rocas se cuelgan\
o en las cañadas se esconden.\
En ascuas de oro convierten\
del astro rey los fulgores,\
del mar que duerme tranquilo\
las mansas ondas salobres.\
sus hilos tiende el rocío\
de diamantes tembladores,\
en la alfombra de los prados\
y en el manto de los bosques.\
sobre la verde ladera\
que esmaltan gallardas flores,\
elevan sus frente altiva\
los enhiestos girasoles,\
y las caléndulas rojas\
vierte al pie sus olores.\
Las amarillas retamas \
visten las colinas, donde\
se ocultan pardas y alegres\
las chozas de los pastores.\
Purpúrea el agua del río\
lame de esmeralda el bordo,\
que con sus hojas encubren\
los plátanos cimbradores;\
mientras que allá en la montaña,\
flotando en la peña enorme,\
la cascada se reviste\
de iris con los colores.\
El ganado en las llanuras\
trisca alegre, salta y corre;\
cantan las aves, y zumban\
mil insectos bullidores\
que el rayo del sol anima,\
que pronto mata la noche.\
En tanto el sol se levanta\
sobre el lejano horizonte,\
bajo la bóveda limpia\
de un cielo sereno . . . Entonces\
sus fatigosas tareas\
suspenden los labradores,\
y un santo respeto embarga\
sus sencillos corazones.\
En el valle, en la floresta, \
en el mar, en todo el orbe\
se escuchan himnos sagrados,\
misteriosas oraciones;\
porque el mundo en esta hora\
es altar inmenso, en donde \
la gratitud de los seres\
su tierno holocausto pone;\
y Dios, que todos los días\
ofrenda tan santa acoge,\
la enciende de Sol que nace\
con los puros resplandores.\
\
\
La plegaria de los niños \
\
'En la campana del puerto \
¡Tocan, hijos, la oración. . . ! \
¡De rodillas! . . . y roguemos \
a la madre del Señor\
por vuestro padre infelice, \
que ha tanto tiempo partió, \
y quizá esté luchando\
de la mar con el furor. \
Tal vez, a una tabla asido, \
¡no lo permita el buen Dios! \
náufrago, triste y hambriento, \
y al sucumbir sin valor\
los ojos al cielo alzando \
con lágrimas de aflicción, \
dirija el adiós postrero\
a los hijos de su amor. \
¡Orad, orad, hijos míos, \
la Virgen siempre escuchó \
1a plegaria de los niños\
y los ayes de dolor!'\
En una humilde cabaña, \
con piadosa devoción, \
puesta de hinojos y triste \
a sus hijos así habló:\
la mujer de un marinero\
al oír la santa voz\
de la campana del puerto \
que tocaba la oración. \
Rezaron los pobres niños\
todo quedóse en silencio \
y después sólo se oyó, \
entre apagados sollozos, \
de las olas el rumor.\
\
De repente en la bocana \
truena lejano el cañón:\
';Entra buque!', allá en la playa \
la gente ansiosa gritó.\
Los niños se levantaron; \
mas la esposa, en su dolor, \
'no es vuestro padre les dijo: \
tantas veces me engañó\
la esperanza, que hoy no puede \
alegrarse el corazón'\
\
Pero después de una pausa \
ligero un hombre subió\
por el angosto sendero, \
murmurando una canción.\
Era un marino...¡Era el padre! \
La mujer palideció\
al oírle, y de rodillas \
palpitando de emoción, \
dijo ¿Lo véis, hijos míos? \
La Virgen siempre escuchó \
la plegaria de los niños\
y los ayes de dolor",

path = u"/c", tags = u"IMA")

writer.add_document(title=u"Ignacio Rodriguez Galvan", content=u"A la muerte de mi amigo\
\
¿Por qué, el aire surcando,\
dilatándose del bronce los sonidos;\
y sin cesar vibrando\
llegan a mis oídos\
profundos y tristísimos gemidos?\
\
¿Por qué de muerte el canto\
en torno de ese féretro resuena?\
¿Por qué el fúnebre llanto?\
¿Por qué la amarga pena,\
los cirios, y el clamor que el aire llena?\
\
Te miro ante mis ojos\
postrado sin aliento, amigo mío;\
y sobre tus despojos\
su manto negro y frío\
tiende la muerte con placer impío.\
\
Y en alas de querubes,\
envuelta tu alma en esplendente velo,\
y entre rosadas nubes\
deja el impuro suelo,\
y blandamente se remonta al cielo.\
\
¡Oh, quién te acompañara!,\
y ese mundo feliz que habitas hora\
contigo disfrutara,\
y la paz seductora\
que, sin turbarse, en él eterno mora.\
\
En mi patria no viera\
sangre correr por la ciudad y llanos,\
y que entre rabia fiera\
hermanos con hermanos\
hasta hundirse el puñal pugnan insanos.\
\
Ni viera la perfidia\
de nación, que risueña nos abraza,\
y bramando de envidia\
luego nos amenaza\
y en su mente infernal nos despedaza.\
\
Ni viera hombres malvados,\
que sin temer de Dios el alto juicio,\
de la ambición guiados\
y el deshonroso vicio,\
despeñan mi nación al precipicio.\
\
Ni con feroz despecho\
la miseria, elevándose espantosa,\
cerrar contra su pecho\
la humanidad quejosa\
y devorar sus lágrimas ansiosa.\
\
Y el luto y exterminio,\
en pos del hambre descarnada y yerta,\
extender su dominio\
sobre su tierra muerta,\
y a la peste letal abrir la puerta.\
Feliz mi caro amigo,\
feliz mil veces tú, que ya en el mundo\
el dolor enemigo\
con brazo furibundo\
no rompe tus entrañas iracundo.\
\
Dichoso tú, que vives\
entre el gozo, la paz, la bienandanza\
y no, cual yo, recibes\
de amor sin esperanza\
zozobras y martirios sin mudanza.\
\
Y no sientes el yugo\
de la suerte pesar sobre tu cuello,\
ni el hombre es tu verdugo,\
ni con ansia un destello\
buscas de la verdad, sin poder vello.\
\
Cuando el mundo habitabas,\
con la voz de amistad consoladora\
las penas aliviabas\
de tu amigo, que ahora\
hundido en e1 pesar tu ausencia llora.\
\
A1 escuchar tus cantos,\
do la razón brillaba y la poesía,\
celestiales encantos\
mi corazón sentía,\
y en su mismo dolor se adormecía.\
\
Si a tu alma por ventura\
le es permitido descender al suelo,\
cuando la noche oscura\
me traiga el desconsuelo\
ven a elevar mi pensamiento al cielo.\
\
De mi agitado sueño\
las escenas de horror benigno ahuyenta;\
la imagen de mi dueño\
en vez de ellas presenta,\
y haz que tu grata voz mi oído sienta.\
\
\
Adiós, oh patria mía\
\
\
Alegre el marinero\
en voz pausada canta,\
y el ancla ya levanta\
con extraño rumor.\
De la cadena al ruido\
me agita pena impía\
Adiós, oh patria mía,\
adiós, tierra de amor.\
\
El barco suavemente\
se inclina y se remece,\
y luego se estremece\
a impulso del vapor.\
Las ruedas son cascadas\
de blanca argentería.\
Adiós, oh patria mía,\
adiós, tierra de amor.\
\
Sentado yo en la popa\
contemplo el mar inmenso,\
y en mi desdicha pienso\
y en mi tenaz dolor.\
A ti mi suerte entrego,\
a ti, Virgen María.\
Adiós, oh patria mía,\
adiós, tierra de amor.\
De fuego ardiente globo\
en las aguas se oculta:\
una onda lo sepulta\
rodando con furor.\
Rugiendo el mar anuncia\
que muere el rey del día.\
Adiós, oh patria mía,\
adiós, tierra de amor.\
\
Las olas, que se mecen\
como el niño en su cuna,\
retratan de la luna\
el rostro seductor.\
Gime la brisa triste\
cual hombre en agonía.\
Adiós, oh patria mía,\
adiós, tierra de amor.\
\
Del astro de la noche\
un rayo blandamente\
resbala por mi frente\
rugada de dolor.\
Así como hoy la luna\
en México lucía.\
Adiós, oh patria mía,\
adiós, tierra de amor.\
\
¡En México! . . . ¡Oh memoria! . . .\
¿Cuándo tu rico suelo\
y a tu azulado cielo\
veré, triste cantor?\
Sin ti, cólera y tedio\
me causa la alegría.\
Adiós, oh patria mía,\
adiós, tierra de amor.\
\
Pienso que en tu recinto\
hay quien por mí suspire,\
quien al oriente mire\
buscando a su amador.\
Mi pecho hondos gemidos\
a la brisa confía.\
Adiós, oh patria mía,\
adiós, tierra de amor.\
\
\
Profecía de Guatimoc\
\
\
Tras negros nubarrones asomaba\
Pálido rayo de luciente luna\
Tenuemente blanqueando los peñascos\
Que de Chapultepec la falda visten.\
Cenicientos a trechos, amarillos,\
O cubiertos de musgo verdinegro\
A trechos se miraban, y la vista\
De los lugares de profundas sombras\
Con terror y respeto se apartaba.\
Los corpulentos árboles ancianos,\
En cuya fuente siglos mil reposan,\
Sus canas venerables conmovían\
De viento leve al delicado soplo\
O al aleteo de nocturno cuerco,\
Que tal vez descendiendo el vuelo rápido\
Rizaba con sus alas sacudidas\
Las cristalinas aguas de la alberca,\
En donde se mecía blandamente\
La imagen de las nubes retratadas\
En su luciente espejo. La llanuras\
Y las lejanas lomas repetían\
El aullido siniestro de los lobos\
O el balar lastimoso del cordero,\
O del todo el bramido prolongado.\
¡Oh soledad, mi bien, yo te saludo!\
\
¡Cómo se eleva el corazón del triste\
cuando en tu seno bienhechor su llanto\
consigue derramar! Huyendo al mundo\
me acojo a ti. Recíbeme y piadosa\
divierte mi dolor, templa mi pena.\
Alza mi corazón al infinito,\
El velo rasga de futuros tiempos,\
Templa mi lira, y de los sacros vates\
Dame la inspiración.\
\
Nada en el mundo,\
Nada encontré que el tedio y el disgusto\
De vivir arrancara de mi pecho.\
MI pobre madre descendió a la tumba\
Y a mi padre infeliz dejé buscando\
Un lecho y pan en la piedad ajena.\
El sudor de mi faz y el llanto ardiente\
Mi sed templaron. Amistad sincera\
Busqué en los hombre, y no hallé... Mentira,\
Perfidia y falsedad hallé tan sólo.\
Busqué el amor, y una mujer, un ángel\
A mi turbada vista se presenta\
Con su rostro ofuscando a los malvados\
Que en torno la cercaban , y entre risas\
De estúpida malicia se gozaban,\
Que en sus manos sacrílegas pensando\
La flor de su quietud marchitarían\
Y de su faz las rosas... ¡Miserables!\
¿cuando la nube tempestuosa y negra\
pudo apagar del sol la lumbre pura,\
aunque un instante la ofuscó? ¿ Ni cuándo\
su irresistible luz el pardo búho\
soportar pudo?...\
\
Yo temblé de gozo, sonrió mi labio y se aclaró mi frente,\
Y brillaron mis ojos, y mis brazos\
Vacilantes buscaban el objeto\
Que tanto me asombró ... ¡Vana esperanza!\
En vez de un corazón a amar creado,\
Aridez y frialdad encontré sólo,\
Aridez y frialdad ¡indiferencia!. . .\
Y mis ensueños de placer volaron\
Y la fantasma de mi dicha huyóse,\
Y sin lumbre quedé perdido y ciego.\
\
Sin amistad y sin amor... (La ingrata\
De mí aparta la vista desdeñosa,\
Y ni la luz de sus serenos ojos\
Concede a su amador . . . En otro tiempo,\
En otro tiempo sonrió conmigo.)\
Sin amistad y sin amor, y huérfano.\
Es ya polvo mi padre, y ni abrazarlo\
Pude al morir. Y abandonado y solo\
En la tierra quedé. Mi pecho entonces\
Se oprimió más y más, y la poesía\
Fue mi gozo y placer, mi único amigo.\
Y misteriosa soledad de entonces\
Mi amada fue.\
\
¡Qué dulce, qué sublime\
es el silencio que me cerca en tono!\
¡Oh cómo es grato a mi dolor el rayo\
de moribunda luna, que halagando\
está mi yerta faz! Quizá me escuchan\
las sombras venerandas de los reyes\
que dominaron el Anáhuac, presa\
hoy de las aves de rapiña y lobos\
que ya su seno y corazón desgarran.\
-'¡Oh varón inmortal!¡Oh rey potente!\
Guatimoc valeroso y desgraciado,\
Si quebrantar las puertas del sepulcro\
Te es dado acaso ¡ven! Oye mi acento:\
Contemplar quiero tu guerrera frente,\
Quiero escuchar tu voz...'\
\
II\
\
Soneto la tierra\
Girar bajo mis pies, nieblas extrañas\
Mi vista ofuscan y hasta el cielo suben.\
Silencio reina por doquier; los campos,\
Los árboles, las aves, la natura,\
La natura parece agonizante.\
Mis miembros tiemblan, la rodillas doblo\
Y no me atrevo a levantar la vista.\
¡Oh mortal miserable! Tu ardimiento,\
tu exaltado valor es vano polvo.\
Caí por tierra sin aliento y mudo,\
Y profundo estertor del hondo pecho\
Oprimido salía.\
\
De repente\
Parece que una mano de cadáver\
Me aferra el brazo y me levanta. . . ¡Cielos!\
¿Qué estoy mirando? . . .\
-'Venerable sombra,\
huye de mí: la sepultura cóncava\
tu mansión es. ¡Aparta, aparta!\
En vano suplico y ruego; mas el alma mía\
Vuelve a su ser y el corazón ya late.\
De oro y telas cubierto y ricas piedras\
Un guerrero se ve. Cetro y penacho\
De ondeantes plumas se descubre;\
tiene potente maza a su siniestra, y arco\
Y rica aljaba de sus hombros penden . . .\
¡Qué horror! Entre las nieblas se descubren\
llenas de sangre sus tostadas plantas\
en carbón convertidas; aun se mira\
bajo sus pies brillar la viva lumbre.\
Grillos, esposas y cadenas duras\
Visten su cuerpo, y acerado anillo\
Oprime su cintura; y para colmo\
De dolor, un dogal su cuello aprieta.\
'Reconozco, exclamé, sí, reconozco\
la mano de Cortés bárbaro y crudo.\
¡Conquistador! ¡Aventurero impío!\
¿Así trata un guerrero a otro guerrero?\
¿Así un valiente a otro valiente? . . . ' Dije\
y agarrar quise del monarca el manto;\
pero él se deslizaba y aire sólo\
con los dedos toqué.\
\
-Rey del Anáhuac,\
noble varón, Guatimoctzín valiente,\
indigno soy de contemplar tu frente.\
Huye de mí. - 'No tal,' él me responde,\
Y su voz parecía\
Que del sepulcro lóbrego salía.\
-'Háblame, continuó, pero en la lengua\
del gran Netzahualcóyotl'.\
Bajé la frente y respondí: 'Lo ignoro.'\
El rey gimió en su corazón. - '¡Oh mengua\
Del gran Netzahualcóyotl.\
Bajé la frente y respondí: 'Lo ignoro.'\
El rey gimió en su corazón. -¡Oh mengua,\
Oh vergüenza!' gritó. Rugó las cejas\
Y en sus ojos brilló súbito lloro.\
-'Pero siempre te amé, rey infelice.\
Maldigo a tu asesino y a la Europa,\
La injusta Europa que tu nombre olvida.\
Vuelve, vuelve a la vida,\
Empuña luego la robusta lanza,\
De polo a polo sonará tu nombre,\
Temblarán a tu voz caducos reyes,\
El cuello rendirán a tu pujanza,\
Serán para ellos tus mandatos, leyes;\
Y en México, en París, centro de orgullo,\
Resonará la trompa de venganza.\
¿Qué e estos tiempos los guerreros veles\
cabe Cortés sañudo y Alvarado\
(varones invencibles si crueles)\
y los venciste tú, si, los venciste\
en nobleza y valor, rey desdichado!'\
\
-¡Ya mi siglo pasó. Mi pueblo todo\
jamás elevará la oscura frente\
hundida ahora en asqueroso lodo.\
Ya mi siglo pasó. DEl mar de Oriente\
Nueva familia de distinto idioma\
De distintas costumbre y semblantes,\
En hora de dolor al puerto asoma;\
Y asolando mi reino, nuevo reino\
Sobre sus ruinas míseras levanta.\
Y cayó para siempre el mexicano,\
Y ahora imprime en mi ciudad la planta\
El hijo del soberbio castellano.\
Ya mi siglo pasó'.\
\
Su voz augusta\
Sofocada quedó con los sollozos,\
Hondos gemidos arrojó del seno,\
Retemblaron sus miembros vigorosos,\
El dolor ofuscó su faz adusta\
Y la inclinó de abatimiento lleno.\
-¿Pues las pasiones que al mortal oprimen\
acosan a los muertos en la tumba?\
¿Hasta ella el grito del rencor retumba?\
¿También las almas en el cielo gimen?'\
Así hablé y respondió - 'Joven audace,\
El atrevido pensamiento enfrena.\
Piensa en ti, en tu nación; mas lo infinito\
No será manifiesto\
A los ojos del hombre: así está escrito.\
Si el destino funesto\
El denso velo destrozar pudiera\
Que la profunda eternidad te esconde,\
Más, joven infeliz, más te valiera\
Ver a tu amante en brazos de tu amigo\
Y ambos a dos el solapada acero\
Clavar en tus entrañas,\
Y reír a tu grito lastimero\
Y, sin poder, morir, sediento y flaco,\
Agonizar un siglo, ¡un siglo entero!\
\
Sentí desvanecerse mi cabeza,\
Tembló mi corazón, y mis cabellos\
Erizados se alzaron en mi frente.\
\
Miróme con terneza\
Del rey la sombra y desplegando el labio\
De esta manera prosiguió doliente:\
\
'¡Oh joven infeliz! ¡cuál tu destino,\
cuál es tu estrella impía!. . .\
Buscará la verdad tu desatino\
Sin encontrar la vía.\
\
Deseo ardiente de renombre y gloria\
Abrasará tu pecho,\
Y contigo tal vez la tu memoria\
Expirará en tu lecho.\
\
Amigo buscarás y amante pura,\
Mas a la suerte plugo\
Que hallasen en ella bárbara tortura,\
En él feroz verdugo.\
\
Y ansia devoradora\
De mecerte en las olas del océano\
Aumentará tu tedio, y será en vano,\
Aunque en dolor y rabia te despeña,\
Que el destino tirano\
Para siempre en tu suelo te asegura\
Cual fijo tronco o soterrada peña.\
\
Y entre tanto a tus ojos\
¡que terrífico lienzo se despliega!\
Llanos, montes de abrojos;\
El justo, que navega\
Y de descanso al punto nunca llega\
\
Y en palacios fastuosos\
El infame traidor, el bandolero,\
Holgando poderosos,\
Vendiendo a un usurero\
Las lágrimas de un pueblo a vil dinero.\
\
La virtud a sus puertas\
Gimiendo de fatiga y desaliento,\
Tiende las manos yertas\
Pidiendo el alimento,\
Y halla tan sólo duro tratamiento\
\
El asesino insano\
Los derechos proclama,\
Debidos al honrado ciudadano.\
\
Y más allá rastrero cortesano,\
Que ha vendido su honor, honor reclama.\
Hombre procaz, que la torpeza inflama,\
Castidad y virtud audaz predica,\
Y el hipócrita ateo\
A Dios ensalza y su poder publica.\
\
Una no firme silla\
Mira sobre cadáveres alzada. . .\
\
Ya diviso en el puerto\
Hinchadas lonas como niebla densa,\
Ya en le playa diviso\
En el aire vibrando aguda lanza,\
De gente extraña la legión inmensa.\
\
Al son del grito del feroz venganza\
Las armas crujen y el bridón relincha;\
Oprimida rechina la cureña,\
Bombas ardientes zumban,\
Vaga el sordo rumor de peña en peña\
Y hasta los montes trémulos retumban.\
\
\
¡Mirad! Mirad por los calientes aires\
mares de viva lumbre\
que se agitan y chocan rebramando;\
mirad de aquella torre el alta cumbre\
cómo tiembla y vacila y cuje y cae,\
los soberbios palacios derrumbando.\
¡Escuchad, escuchad!. . . . Hondos gemidos\
arrojan los vencidos.\
\
¡Mirad los infelices por el suelo,\
moribundos, sus cuerpos arrastrando,\
y su sed ardorosa\
en sus propias heridas apagando!\
¡Oídlos en su duelo\
maldecir su nación, su vida, el cielo!. . .\
Sangrienta está la tierra,\
Sangrienta el alta sierra,\
Sangriento el ancho mar, el hondo espacio,\
Y del innoble rey del claro día\
La faz envuelve ensangrentado velo.\
Nada perdona el bárbaro europeo:\
\
Todo lo rompe y tala y aniquila\
Con brazo furibundo.\
Ved la doncella en torpe desaliño\
Abrazar a su padre moribundo.\
Mirad sobre el cadáver asqueroso\
Del asesino aleve\
Caer sin vida el inocente niño.\
\
¡Oh vano suplicar! Es dura roca\
el hijo del Oriente:\
brotan sangre sus ojos, y a su boca\
lleva sangre caliente.\
\
Es su placer en fúnebres desiertos\
Las ciudades trocar. ¡Hazaña honrosa!\
Ve el sueño con desdén, si no reposa\
Sobre insepultos muertos.\
\
¡Ay pueblos desdichado!\
Entre tantos caudillos que te cercan\
¿quién a triunfar conducirá tu acero?\
Todos huyen cobardes, y al soldado\
En las garras del pérfido extranjero\
Dejan abandonado\
Clamando con acento lastimero:\
¿dónde cortés está? ¿dónde Alvarado?\
\
Ya eres esclavo de nación extraña,\
Tus hijos son esclavos\
A tu esposa arrebatan de tu seno. . .\
¡Ay si provocas la extranjera señal!. . .\
\
¿Lloras, pueblo infeliz y miserable?\
¿A qué sirve tu llanto?\
¿Qué vale tu lamento?\
Es tu agudo quebranto\
Para el hijo de Europa implacable\
Su más grato alimento.\
\
Y ni enjugar las lágrimas de un padre\
Concederá a tu duelo,\
Que de la venerable cabellera\
Entre signos de gozo\
Le verás arrastrado\
Al negro calabozo,\
Do por piedad demanda muerte fiera.\
¡Ay, pueblo desdichado!\
¡Dónde Cortés está? ¡dónde Alvarado?\
\
¿más qué faja de luz pura y brillante\
en el cielo se agita?\
¿Qué flamígero carro de diamante\
por los aires veloz se precipita?\
¿Cual extendido pabellón ondea?\
¿cual sonante clarín a la pelea\
el generoso corazón excita?\
\
¡Temblad, estremeceos,\
oh reyes europeos!\
Basta de tanto escandaloso crimen.\
Ya los cetros en ascuas se convierten,\
Los tronos en hogueras\
Y las coronas en serpientes fieras\
Que rencorosas vuestro cuello oprimen.\
¿Qué es de París y Londres?\
¿Qué es de tanta soberbia y poderío?\
¿Qué es sus naves de riqueza llenas?\
¿Qué de su rabia y su furor impío?\
Así preguntará triste viajero.\
Fúnebre voz responderá tan solo:\
¿Qué es de Roma y Atenas?\
\
¿Ves en desiertos de África espantosos,\
al soplar de los vientos abrasados\
qué multitud de arenas\
se elevan por los aires agitados,\
y ya truécanse en hórridos colosos,\
ya en bramadores mares procelosos?\
¡Ay de vosotros, ay, guerreros viles,\
que de la inglesa América y de Europa,\
con el vapor, o con el viento en popa,\
a México llegáis miles a miles\
y convertís el amistoso techo\
en palacio de sangre y de furores,\
y el inocente hospitalario lecho\
en morada de escándalo y de horrores!\
¡Ay de vosotros! Si pisáis altivos\
las humildes arenas de este suelo,\
no por siempre será, que la venganza\
su soplo asolador furiosa lanza\
y veloz las eleva por los aires,\
y ya las cambia en tétricos colosos\
que en sus fornidos brazos os oprimen,\
ya en abrasados mares\
que arrasan vuestros pueblos poderosos.\
\
Que aun del caos la tierra no salía\
Cuando a los pies del hacedor radiante\
Escrita estaba en sólido diamante\
Esta ley, que borrar nadie podría:\
El que del infeliz el llanto vierte,\
Amargo llanto verterá angustiado;\
El que huella al endeble, será hollado;\
El que la muerte da, recibe muerte;\
\
Y el que masa su espléndida fortuna\
Con sangre de la víctima llorosa,\
Su sangre beberá si sed lo seca,\
Sus miembros comerá si hambre lo acosa'.\
\
Brilló en el cielo matutino rayo,\
De súbito cruzó rápida llama,\
El aire convirtióse en humo denso\
Salpicado de brasas encendidas\
Cual rojos globos en oscuro cielo.\
La tierra retembló, giró tres veces\
En encontradas direcciones; hondo\
Cráter abrióse ante mi planta infirme\
Y despeñóse en él bramando un río\
De sangre espesa, que espumoso lago\
Formó en el fondo, y cuyas olas negras,\
Agitadas subiendo mis rodillas\
Bañaban sin cesar. Fantasma horrible\
De formas colosales y abultadas,\
Envolvió su cabeza en luego manto\
Y en el profundo lago sumergióse.\
Ya no ví más. . .\
\
\
¿Dó estoy? ¡Qué lazo oprime\
mi garganta? ¡ Piedad! Solo me encuentro. . .\
Mi cuerpo tembloroso húmeda yerba\
Tiene por lecho; el corazón mis manos\
Con fuerza aprietan, y mi rostro y cuero\
Tibio sudor empapa. El sol brillante,\
Tras la sierra asomando la cabeza,\
Mira a Chapultepec cual padre tierno\
Contempla al despertar a su hijo amado.\
Los rayos de su luz las peñas doran,\
Los árboles sus frentes venerables\
Inclinan blandamente, saludando\
Al astro ardiente que les da la vida.\
\
Azul está el espacio, y a los montes\
Baña color azul, claro y oscuro.\
Todo respira juventud risueña\
Y cantando los pájaros se mecen\
En las ligeras y volubles auras.\
\
Todos a gozar convida; pero a mi alma\
Manto e muerte envuelve, y gota a gota\
Sangre destila el corazón herido.\
Mi mente es negra cavidad sin fondo\
Y vaga incierto el pensamiento en ella\
Cual perdida paloma en honda grúa.\
\
¡Fue sueño o realidad? Pregunta vana. . .\
Sueño sería, que profundo sueño\
Es la voraz pasión que me consume;\
Sueño ha sido, y no más el leve gozo\
Que acarició mi faz; sueño el sonido\
De aquella sonrisa, aquel halago,\
Aquel blando mirar. . . Desperté súbito\
Y el bello Edén despareció a mis ojos\
Como oleada que la mar envía\
Y se lleva después. Sólo me resta\
Atroz recuerdo que me aprieta el alma\
Y sin cesar el corazón me roe.\
Así el fugaz placer sirve tan sólo\
Para abismar el corazón sensible,\
Así la juventud y la hermosura\
Sirven tan sólo de romper el seno\
A la cansada senectud. El hombre\
Tiene dos cosas solamente eternas:\
A Dios y la virtud, de El amada. . .\
\
Yo me sentí mecido de mis padres\
En los amante cariñosos brazos,\
Y fue sueño también. . . Mujer que adoro,\
Ven otra vez a adormecer mi alma\
Y mátame después, mas no te alejes. . .\
La amistad y el amor son mi existencia,\
Y el amor y amistad vuelven el rostro\
Y huyen de mi cual de cadáver frío.\
\
¡Venid, sueños, venid! Y ornad mi frente\
de beleño mortal: soñar deseo.\
Levantad a los muertos de sus tumbas:\
Quiero verlos sentir estremecerme. . .\
Las sensaciones mi alimento fueron,\
Sensaciones de horror y de tristeza.\
Sueño sea mi paso por el mundo,\
Hasta que nuevo sueño, dulce y grato,\
Me presente de Dios la faz sublime.\
\
¡Bailad, bailad!\
\
Bailad mientras que llora\
El pueblo dolorido,\
Bailad hasta la aurora\
Al compás del gemido\
Que a vuestra puerta el huérfano\
Hambriento lanzará.\
¡Bailad, bailad!\
\
Desnudez, ignorancia\
A nuestra prole afrenta,\
Orgullo y arrogancia\
Con altivez ostenta,\
Y embrutece su espíritu\
Torpe inmoralidad.\
\
¡Bailad, bailad!\
\
Las escuelas inunda\
Turba ignorante y fútil,\
Que su grandeza funda\
En vedarnos lo útil\
Y nos conduce hipócrita\
Por la senda del mal.\
¡Bailad, bailad!\
\
Soldados sin decoro\
Y sin saber nos celan,\
Adonde dan más oro\
Allá rápidos vuelan:\
En la batalla tórtolas,\
Buitres en la ciudad.\
¡Bailad, bailad!\
\
Y por Tejas se avanza\
El invasor astuto:\
Su grito de venganza\
Anuncia triste luto\
A la infeliz república\
Que al abismo arrastráis.\
¡Bailad, bailad!\
\
El bárbaro ya en masa\
Por nuestros campos entra,\
A fuego y sangre arrasa\
Cuando a su paso encuentra,\
Deshonra nuestras vírgenes,\
Nos asesina audaz.\
¡Bailad, bailad!\
\
Europa se aprovecha\
De nuestra inculta vida,\
Cual tigre nos acecha\
Con la garra tendida\
Y nuestra ruina próxima\
Ya celebrando está.\
¡Bailad, bailad!\
\
¿Bailad, oh campeones,\
hasta la luz vecina,\
al son de los cañones\
de Tolemaida y China,\
y de Argel a la pérdida\
veinte copas vaciad.\
¡Bailad, bailad!\
\
Vuestro cantor en tanto\
De miedo henchido, el pecho\
Se envuelve en negro manto\
En lágrimas deshecho,\
Y prepara de México\
El himno funeral.\
¡Bailad, bailad!\
\
La gota de hiel\
\
¡Jehovah! Jehovah, tu cólera me agobia!\
¿Por qué la copa del martirio llenas?\
Cansado está mi corazón de penas.\
Basta, basta, Señor.\
Hierve incendiada por el sol de Cuba\
Mi sangre toda y de cansancio expiro,\
Busco la noche, y en el lecho aspiro\
Fuego devorador.\
\
¡A, la fatiga me adormece en vano!\
Hondo sopor de mi alma se apodera\
¡y siéntanse a mi pobre cabecera\
la miseria, el dolor!\
Roncos gemidos que mi pecho lanza\
Tristes heraldos son de mis pesares,\
Ay a mi mente descienden a millares\
Fantasmas de terror.\
\
¡Es terrible tu cólera, terrible\
Jehovah, suspende tu venganza fiera\
O dame fuerzas, oh Señor, siquiera\
Para tanto sufrir.\
Incierta vaga mi extraviada mente,\
Busco y no encuentro la perdida ruta,\
Sólo descubro tenebrosa gruta\
Donde acaba el vivir.\
\
Yo sé, Señor que existes, que eres justo,\
Que está a tu vista el libro del destino,\
Y que vigilas el triunfal camino\
Del hombre pecador.\
Era tu voz la que en el mar tronaba\
Al ocultarse el sol en occidente,\
Cuando una ola rodaba tristemente\
Con extraño fragor.\
\
Era tu voz y la escuché temblando.\
Clavóse un tanto mi tenaz dolencia\
Yo adoré tu divina omnipotencia\
Como cristiano fiel.\
¡Ay, tú me ves Señor! Mi triste pecho\
cual moribunda lámpara vacila,\
y en él la suerte sin cesar destila\
una gota de hiel.\
\
\
Un crimen\
\
I.-\
\
Hubo un tiempo en que atónito miraba\
a una joven, que ardiente idolatraba,\
modelo de beldad.\
\
'Te adoro, te idolatro', me decía;\
y en su pálida frente relucía\
pudor, virginidad.\
\
Y brillaban mis ojos de contento.-\
Era su hálito puro mi alimento,\
mi concierto su voz;\
ero su rostro, su mirar mi encanto;\
era su triste y doloroso llanto\
mi tormento feroz.\
\
Como la flor en el pantano inmundo\
la arrojó el cielo despiadado al mundo\
entre angustia y dolor.\
\
Y yo corrí, volé de gozo lleno,\
y delirante recogí en mi seno\
la ternísima flor.\
\
'Huérfanos somos, sin ningún abrigo,\
y pobres, desgraciados, sin amigo;\
el cielo nos unió.\
Tu serás, dulce prenda, mi consuelo,\
y para mí será la tierra el cielo...'\
Así la dije yo.\
\
Y ella llorando se arrojó en mis brazos,\
y en deliciosos, en estrechos lazos,\
anudado me vi.\
Y en su seno purísimo y constante,\
como en la madre el delicado infante,\
tranquilo me dormí.\
\
II.-\
\
Y desperté de súbito,\
y busqué enajenado\
el ángel adorado\
de mi ternura objeto y de mi amor.\
Pero en silencio lúgubre,\
y en soledad y calma\
estaba todo; y mi alma\
fue presa de inquietud y de dolor.\
\
Me levanto frenético,\
a mi adorada llamo;\
el eco a mi reclamo\
retumbando tan solo respondió.\
Y triste, y melancólico,\
mi consuelo buscando,\
voy lento meditando\
las penas en que el cielo me arrojó.\
\
III.-\
\
¿Dó te escondes,\
mi querida?\
¿Dó mi vida,\
te hallaré?\
Si no vienes\
al instante,\
dulce amante,\
moriré.\
'Eres bella como el cielo,\
eres mi ángel, mi consuelo,\
y sin ti\
no hay contento, ni ventura,\
ni hermosura\
para mi.'\
\
De la vida\
en el camino\
mi destino\
me arrojó;\
y de duelo,\
de quebranto,\
y de espanto\
me inundó.\
\
'Eres bella como el cielo,\
eres mi ángel, mi consuelo,\
y sin ti\
no hay contento, ni ventura,\
ni hermosura\
para mi.'\
\
Pero dióme\
para guía,\
vida mía,\
tu virtud;\
Y trocóse mi tormento\
en contento\
y en salud.\
\
'Eres bella como el cielo,\
eres mi ángel, mi consuelo,\
y sin ti\
no hay contento, ni ventura,\
ni hermosura\
para mi.'\
\
La joya eres\
más hermosa,\
más preciosa\
que se vio\
en el suelo\
mexicano,\
do mi mano\
te cogió.\
\
'Eres bella como el cielo,\
eres mi ángel, mi consuelo,\
y sin ti\
no hay contento, ni ventura,\
ni hermosura\
para mi.'\
\
IV.-\
\
Mi pecho agitado de rudo tormento,\
el canto elevaba mi lánguida voz;\
y solo en respuesta notaba que el viento\
espigas y ramas movía veloz.\
\
La luna brillaba purísima y bella\
en medio al espacio de claro zafir,\
cual cándida, joven, modesta doncella\
que mira al amante gozoso venir.\
\
Tan solo escuchaba los lúgubres gritos\
de pobre aldeano que alababa al Señor;\
y mi alma oprimían los seres malditos\
que asaz provocaron del cielo el furor.\
\
En locas ideas mi mente perdida,\
pregunto a mi mismo: - ¿Por qué huye de mi?\
¡Maldita por siempre, maldita mi vida!..'\
Y un ronco gemido feroz despedí.\
\
Temblaban mis miembros, sudaba mi frente,\
espesa tiniebla mis ojos cubrió;\
y luego del seno quejido doliente,\
cual de honda caverna, vibrando salió.\
\
Mas, cielos ¡qué miro!.. ¿La vista me engaña?\
¡Es ella!.. la veo.. ¡Qué dulce placer!..\
Mas alguien... un hombre... ¡Gran Dios! la acompaña!\
Infame, traidora, perversa mujer!\
\
Le mira amorosa... le lleva a su seno..\
-¡No más! ya la daga feroz empuñé....\
y vuelo... de rabia frenética lleno\
en sangre mi diestra, mi brazo empapé!...\
\
\
La inocencia\
\
I.-\
\
Al principiar la noche silenciosa\
es más grata la estrella misteriosa\
de risueño fulgor,\
que si riela en transparente río\
la taciturna reina del vacío\
en todo su esplendor.\
\
Es más bella la fuente clara y pura\
que en delicioso prado con blandura\
deslizándose va,\
que el torrente veloz que se abalanza\
y en un abismo da.\
\
Es para mi más dulce el sol fulgente\
cuando arroja del seno del oriente\
rayo consolador,\
que si mis venas ardoroso inflama\
cuando en la tierra espléndido derrama\
su fuego abrasador.\
\
Así a mis ojos eres más hermosa,\
de mi feraz nación temprana rosa,\
niña pura y feliz,\
que la joven que erguida se levanta,\
y a cuya bella y delicada planta\
rendimos la cerviz.\
\
II.-\
\
Modelo de belleza,\
la pureza\
brilla en tu cándida faz;\
la inocencia es tu divisa,\
y tu risa\
es como un signo de paz.\
\
Alguna vez la hermosura\
con ternura\
amante me sonrió;\
dichoso ya me creía,\
y ella impía\
con falacia me burló.\
\
Mas tu sonrisa graciosa\
candorosa\
no es de amor, es de amistad;\
¡tu corazón ardiente\
inocente\
no conoce la maldad.-\
\
Oh cuán venturosa fueras,\
si vivieras\
de tu infancia sin salir:\
entonces feliz serías;\
no sabrías\
lo que es penar y sufrir.\
\
Mas la ley de la natura\
siempre dura,\
no perdona a la virtud;\
de la humanidad es dueña,\
y le enseña\
la vejez o el ataúd.\
\
Con los fatigosos años\
desengaños\
vienen del mortal en pos;\
y contra el mundo un abrigo\
y un amigo\
halla el infeliz en Dios.\
\
El no mas nos da consuelo;-\
en el suelo\
solo existe una verdad,\
y es que la inocencia gime,\
y la oprime\
triunfadora la maldad.\
\
-Tu vives, oh niña hermosa,\
cual la rosa\
en lo interior de un breñal;\
no de tu sueño despiertes,\
porque adviertes\
cuán horroroso es tu mal.\
\
Al sueño tornar querrías,\
no podrías;\
el cielo así lo ordenó;\
y tan solamente el llanto\
y el quebranto\
por patrimonio nos dio.\
\
La vida es estrecha vía,\
do nos guía\
solo el destino fatal:\
encantados proseguimos,\
mas sentimos\
de súbito frío puñal.\
\
III.-\
\
¿Ese celaje miras que se avanza\
meciéndose hechicero,\
o volando ligero\
como águila veloz?\
Aquella nube tétrica lo alcanza,\
y aquí y allá lo vuelve,\
y rugiendo lo envuelve\
con ímpetu feroz.\
\
¿Ves aquella avecilla revolando,\
que rápida se eleva,\
y su arrojo la lleva\
hasta el cielo tocar?\
Huracán espantoso rebramando,\
desde el espacio inmenso\
en remolino denso\
la hace al suelo bajar.\
\
¿Ves en las aguas de apacible río\
blandamente flotando\
y graciosa vagando\
la delicada flor?\
se acerca al fin a un vórtice bravío;\
sus olas bramadoras\
la sumergen traidoras\
en abismo de horror.\
\
Imágenes son estas de la vida:-\
es dulce, placentera,\
juguetona, ligera\
del hombre la niñez.\
En su pecho después la pena anida:\
los placeres fenecen,\
y los martirios crecen\
con furia y rapidez.\
\
IV.-\
\
Goza, goza, niña pura,\
de tus días de ventura,\
de tu inocencia feliz;\
y de tu dicha presente\
jamás se borre en tu mente\
el delicado matiz.\
\
El pesar que me fatiga\
se cambie en delicia amiga\
que me halague el corazón;\
y pueda lleno de gozo,\
de alegría, de alborozo,\
entonar grata canción.\
\
Corona de frescas rosas,\
apacibles, olorosas,\
tejerte quería yo;\
y a tiempo que la formaba,\
espina que me punzaba\
en mis manos se tornó.",
                    path=u"/c", tags=u"IRG")

writer.add_document(title=u"Jose Rosas Moreno", content=u"¡Quién pudiera vivir siempre soñando!\
\
Es la existencia un cielo,\
cuando el alma soñando embelesada,\
con amoroso anhelo,\
en los ángeles fija su mirada.\
¡Feliz el alma que a la tierra olvida\
para vivir gozando!\
¡Quién pudiera olvidarse de la vida!\
¡Quién pudiera vivir siempre soñando!\
\
En esa estrecha y mísera morada\
es un sueño engañoso la alegría;\
la gloria es humo y nada\
y el más ardiente amor gloria de un día.\
Afán eterno al corazón destroza\
cuando los sueños ¡ay! nos van dejando.\
Sólo el que sueña goza.\
¡Quién pudiera vivir siempre soñando!\
\
De su misión se olvidan las mujeres,\
los hombres viven en perpetua guerra;\
no hay amistad, ni dicha, ni placeres;\
todo es mentira ya sobre la tierra.\
Suspira el corazón inútilmente . . .\
la existencia que voy atravesando\
es hermosa entre sueños solamente.\
¡Quién pudiera vivir siempre soñando!\
\
Sin mirar el semblante a la tristeza,\
pasé de la niñez a la dulce aurora,\
contemplando entre sueños la belleza\
de ardiente juventud fascinadora.\
Pero ¡ay! se disipó mi sueño hermoso,\
y desde entonces siempre estoy llorando\
porque sólo el que sueña es venturoso.\
¡Quién pudiera vivir siempre soñando!\
\
\
El valle de mi infancia\
\
Salud, ¡oh valle hermoso! \
Albergue de placer, donde dichoso \
entre sueños espléndidos de amores, \
vi deslizarse un día,\
cual se desliza el agua entre las flores, \
los dulces años de la infancia mía. \
\
Valle umbroso, salud: hoy el viajero \
tu abrigo lisonjero\
busca ansioso con ávida mirada, \
bendice la quietud de tus vergeles, \
y reclina su frente ensangrentada \
a la sombra feliz de tus laureles. \
\
Aquí esta la montaña, allí está el río; \
allá del bosque umbrío\
la silenciosa majestad se admira; \
allí el lago retrata el firmamento; \
la fuente, más allá, lenta suspira,\
y agitando los sauces gime el viento. \
\
Allí la cruz está donde, inspirado, \
el bien del desgraciado\
imploraba con místico cariño, \
elevando a los cíelos mis plegarias, \
y estas agrestes rocas solitarias\
las mismas son que amé cuando era niño. \
\
Pero es otro el rocío, otra la brisa\
que hoy el abril te da con su sonrisa; \
otras las rosas son de encanto llenas\
que brillan entre el césped de tu alfombra, \
y otras, y otras también las azucenas\
que crecen a tu sombra.\
\
Cual las olas que pasan suspirando \
los años van pasando;\
un instante con flores se embellecen, \
un punto brilla su fulgor mentido,\
y al fin se desvanecen\
en las oscuras sombras del olvido. \
\
¿En dónde están ahora aquellas rosas \
tan puras, tan hermosas?...\
Están, ¡oh valle!, donde está la calma \
de aquellos bellos días tan risueños; \
en donde está mi amor, gloria del alma,\
y en donde están también mis dulces sueños. \
\
Yo era feliz aquí; yo me adormía\
en plácida alegría,\
por la dulce inocencia acariciado, \
sin más amor que tú, sin otro anhelo \
que amar tus flores y cruzar tu prado, \
cantar tus fuentes y mirar tu cielo. \
\
Una tarde las aves se alejaban,\
y al ver como volaban,\
sentí el alma agitarse en ansias locas \
y quise, como el águila atrevida, \
cruzar las selvas, dominar las rocas, \
y aspirar otro ambiente y otra vida: \
\
Y al huracán seguí; y al ver el mundo \
sentí en el corazón horror profundo; \
anhelé las tranquilas soledades\
donde feliz reía,\
y sentí que mi espíritu oprimía\
la atmósfera letal de las ciudades. \
\
Gozo y placer busqué, gloria y ventura; \
y sólo hallé amargura,\
inquietudes y afán, tedio y congojas; \
del viento del dolor al soplo ardiente, \
cual de tus bellos árboles las hojas, \
se secó la guirnalda de mi frente. \
\
En vano allí busqué la dulce calma \
y el casto amor del alma:\
\
sólo en la multitud con mis pesares\
me confundí gimiendo,\
y apagóse perdido entre el estruendo\
el tímido rumor de mis cantares.\
\
Esquivando el furor de la tormenta, \
cual ave voy que el huracán ahuyenta, \
y ansioso busco ahora\
en tu silencio plácido y tranquilo, \
el apacible asilo\
donde al menos en paz el alma llora. \
También, ¡oh valle!, a marchitar tus galas \
la airada tempestad tiende sus alas;\
tus flores huella y con furor se agita \
marchitando sus vívidos colores... \
¡Dichosas esas flores\
que el huracán marchita!\
\
Lejos contemplo ya la infancia mía, \
y muy lejos la tumba todavía; \
oculto afán me mata,\
mi destino en la tierra es muy incierto, \
y lúgubre a mi vista se dilata\
inmenso el porvenir como un desierto. \
\
Sin oír una voz dulce y querida,\
solo estoy en el valle de la vida, \
cual el ciprés doliente\
que en eterno abandono se consume, \
sin guirnaldas de hiedras en su frente, \
sin que le dé una flor grato perfume. \
\
Nadie piensa en mi amor, nadie me mira, \
nadie por mí suspira;\
tan sólo la tristeza con mis dolores gime,\
y entre sus brazos trémula me oprime \
y reclina en su seno mi cabeza.\
\
E1 alma ardiente que en mi afán seguía \
dulce hermana inmortal del alma mía, \
me niega su ternura,\
y sin oír mi queja,\
insensible a mi amarga desventura, \
sin enjugar mis lágrimas se aleja.\
Ya que en vano la llamo cariñoso\
para cruzar con ella el bosque umbroso,\
para contarle amante mi querella\
y dividir con ella mi alegría,\
para soñar con ella\
esta sombra de amor que dura un día. \
\
A lo mejor gozar el alma quiere\
en el sueño ideal que nunca muere, \
del infinito anhelo\
en que Dios le revela su destino, \
la esperanza feliz del bien divino\
con que existen las almas en el cielo.\
\
Aquí morir quisiera\
al rumor de tu brisa lisonjera;\
pero ¡ay! delirio, mi ansiedad es vana \
y el soplo sigo del destino airado... \
¡Quién sabe en dónde me hallaré mañana! \
¡Quién sabe en dónde moriré ignorado! \
\
Queda en paz, dulce valle, umbroso asilo, \
donde existe tranquilo,\
plácido albergue de mi amor primero. \
Ya va el sol ocultando sus fulgores, \
y adiós te dice el infeliz viajero \
empapando en sus lágrimas tus flores.\
\
 \
\
La vuelta de la aldea\
\
Ya el sol oculta su radiosa frente;\
Melancólico brilla en occidente\
Su tímido esplendor;\
Ya en las selvas la noche inquieta vaga\
Y entre las brisas lánguido se apaga\
El último cantar del ruiseñor.\
\
¡Cuánto gozo escuchando embelesado\
ese tímido acento apasionado\
que en mi niñez oí!\
Al ver de lejos la arboleda umbrosa\
¡cuál recuerdo, en la tarde silenciosa,\
la dicha que perdí!\
\
Aquí al son de las aguas bullidoras,\
De mi dulce niñez las dulces horas\
Dichoso vi pasar,\
Y aquí mil veces, al morir el día \
Vine amante después de mi alegría\
Dulces sueños de amor a recordar.\
\
Ese sauce, ese fuente, esa enramada,\
De una efímera gloria ya eclipsada\
Mudos testigos son:\
Cada árbol, cada flor, guarda una historia\
De amor y placer, cuya memoria\
Entristece y halaga el corazón.\
\
Aquí está la montaña, allí está el río;\
A mi vista se extiende el bosque umbrío\
Donde mi dicha fue.\
¡cuántas veces aquí con mis pesares \
vine a exhalar de amor tristes cantares!\
¡Cuánto de amor lloré!\
\
Acá la calle solitaria; en ella\
De mi paso en los céspedes la huella\
El tiempo ya borró.\
Allá la casa donde entrar solía\
De mi padre en la dulce compañía.\
¡Y hoy entro en su recinto sólo yo!\
\
Desde esa fuente, por la vez primera,\
Una hermosa mañana, la ribera \
A Laura vi cruzar,\
Y de aquella arboleda en la espesura,\
Una tarde de mayo, con ternura\
Una pálida flor me dio al pasar.\
\
Todo era entonces para mi risueño;\
Mas la dicha en la vida es sólo un sueño,\
Y un sueño fue mi amor.\
\
Cual eclipsa una nube al rey del día,\
La desgracia eclipsó la dicha mía\
En su primer fulgor.\
\
Desatóse estruendoso el torbellino,\
Al fin airado me arrojó el destino\
De mi natal ciudad.\
\
Así cuando es feliz entre sus flores\
¡ay del nido en que canta sus amores\
arroja al ruiseñor la tempestad.\
\
Errante y sin amor siempre he vivido;\
Siempre errante en las sombras del olvido...\
¡Cuán desgraciado soy!\
Mas la suerte conmigo es hoy piadosa;\
Ha escuchado mi queja cariñosa,\
Y aquí otra vez estoy.\
\
No se, ni espero, ni ambiciono nada;\
Triste suspira el alma destrozada\
Sus ilusiones ya:\
Mañana alumbrará la selva umbría\
La luz del nuevo sol, y la alegría\
¡jamás al corazón alumbrará!\
\
Cual hoy, la tarde en que partí doliente,\
Triste el sol derramaba en occidente\
Su moribunda luz:\
Suspiraba la brisa en la laguna\
Y alumbraban los rayos de la luna\
La solitaria cruz.\
\
Tranquilo el río reflejaba al cielo,\
Y una nube pasaba en blando vuelo\
Cual pasa la ilusión;\
Cantaba el labrador en su cabaña,\
Y el eco repetía en la montaña\
La misteriosa voz de la oración.\
\
Aquí está la montaña, allí está el río...\
Mas ¿dónde está mi fe? ¿Dónde, Dios mío,\
Dónde mi amor está?\
\
Volvieron al vergel brisas y flores,\
Volvieron otra vez los ruiseñores...\
Mi amor no volverá.\
\
¿De qué me sirven, en mi amargo duelo,\
de los bosques los lirios, y del cielo\
el mágico arrebol;\
el rumor de los céfiros suaves\
y el armonioso canto de las aves,\
si ha muerto ya de mi esperanza el sol?\
\
Del arroyo en las márgenes umbrías\
No miro ahora, como en otros días,\
A Laura sonreír.\
¡Ay! En vano la busco, en vano lloro;\
ardiente en vano su piedad imploro:\
¡jamás ha de venir!.",
                    path=u"/c", tags=u"JRM")

writer.add_document(title=u"Juan de Dios Peza", content=u"Confidencias a una estrella\
\
Sigue, sigue blanca estrella,\
Por el cielo en que naciste,\
Sin dejar ninguna huella...\
Siempre te hallaré más bella,\
Siempre te hallaré más triste.\
\
Hoy vengo con mi dolor,\
Cual antes feliz venía;\
Mas ya nunca, astro de amor,\
Ceñirás con tu fulgor\
Ni su frente ni la mía.\
\
Tú cruzas por ese cielo,\
Dando con tu luz la calma;\
Yo cruzo, por este suelo,\
Llevando en mi desconsuelo\
Lena de sombras el alma.\
\
Dame, dame tu luz bella;\
Que en esta alma sin amor,\
Tú sorprenderás estrella,\
En cada nube una huella,\
Y en cada huella un dolor.\
\
Tú que has escuchado el canto\
De mi primera pasión,\
Acompaña mi quebranto,\
Y alumbra el amargo llanto \
que brota del corazón.\
\
¡Horas del primer cariño!\
tú las miraste lucir,\
Cuando ante tu luz de armiño,\
La niña en brazos del niño\
Soñaba en el porvenir.\
\
¡Dulce amor! ¡grata ciencia!\
¡Blanca luz! ¡Delirio ardiente!\
¿Por qué huyes de la existencia,\
Cuando una dura experiencia\
Va marchitando la frente?\
\
¡Aquellos goces extraños,\
Aquel esperar en Dios, \
Sin recoger desengaños,\
Aquel pasar de los años\
Sin perturbar a los dos!\
\
Todo, todo, blanca estrella,\
Tu tibia luz alumbró;\
¡Edad de sueños aquella,\
Envidiable, dulce, bella,\
Que para siempre huyó!\
\
Celia, al expirar el día,\
Por estos sitios vendrá,\
Ya no como antes venía,\
Que aquella alma que fue mía,\
Pertenece a otra alma ya.\
\
Antes ¡ay! ¡cuánto embeleso!\
Sollozando de placer,\
Dejaba en mi frente un beso;\
Por eso, estrella; por eso\
No quiero volverla a ver.\
\
Ahora, dulce y cariñosa,\
En otro sus ojos fijos,\
Tendrá su boca amorosa\
La majestad de la esposa\
Para besar a sus hijos.\
\
Con tus rayos blanquecinos\
Alumbra siempre su hogar;\
Aparta nuestros caminos,\
Y ¡ay! que sus ojos divinos\
No aprendan nunca a llorar.\
\
Si sigues, tú, blanca estrella,\
Por el cielo en que naciste,\
Sin dejar ninguna huella...\
Siempre te hallaré más bella,\
Siempre me verás mas triste.\
\
\
\
Sin sobre\
\
Abro tu carta y reconozco ufano\
Tu letra fácil, tu dicción hermosa;\
Tú la trazaste con tu propia mano\
Pues el papel trasciende a tuberosa.\
\
Al escribirla estabas intranquila\
Y ya estoy sospechando tus desvelos\
Los médicos me han dicho, que vacila\
El pulso con la fiebre de los celos.\
\
Veo tus líneas torcidas, descuidadas,\
Y esto halaga mis propios pareceres\
Porque sé que no estando enamoradas\
Nunca escriben sin falsa las mujeres.\
\
¡Con el arrojo de tus veinte abriles,\
Has escrito un aumento que me mata!\
Siempre ha sido en las cartas femeniles\
Importante o terrible la postdata.\
\
No me vuelvas a ver. Ya no te quiero,\
Esto me dices con desdén profundo:\
Yo traduzco: ven pronto que me muerto,\
De algo me sirve conocer el mundo.\
\
Dices que consolando tu tristeza\
Vas al campo a llorar penas de amores\
Así podrá tener Naturaleza\
Coronas de diamantes en las flores.\
\
Pero no viertas llanto por tus penas\
Que siempre se evaporan bajo el cielo;\
Las lluvias del desierto en las arenas\
Y el llanto, entre las blondas del pañuelo.\
\
Las horas de silencio son tan largas,\
Que comprendo la angustia con que gimes;\
Las verdades del alma son amargas,\
Y las mentiras del amor, sublimes.\
\
Inquieres con tesón si a cada instante\
Busco tu imagen o su culto pierdo,\
¿Dónde está, niña cándida, el amante\
Que diga en estas cosas: no me acuerdo?\
\
Quien convertir pretenda de improviso\
El amor terrenal en culto eterno,\
Necesita labrar un Paraíso\
Sobre la obscura cima del infierno.\
\
¿Ves ese Sol que llena de alegría\
El cielo, el mar, el bosque y las llanuras?\
El trae a los mortales cada día\
Nuevas dichas y nuevas amarguras.\
\
Cada alma tiene libro que atesora\
sus efectos en él, sin vano alarde;\
¡Cuánto nombre se agrega en cada aurora!\
¡Cuánto nombre se borra en cada tarde!\
\
¿Quién sabe por qué anhela lo que anhela?\
¿Quién será siempre el mismo, siendo humano?\
Dicha, amor, esperanza, todo vuela\
Sobre ese amargo y turbulento Océano.\
\
Y así preguntas con afán sincero:\
¿Por qué me quieres?... voy a responderte:\
Yo te quiero mujer porque te quiero;\
No tengo otra razón para quererte.\
\
¿Tú te conformarás con tal respuesta,\
Que de mi propio corazón recibo?\
Tal vez la encuentre sin razón; pero ésta\
Es la única razón por qué te escribo.\
\
Que yo no vuelva a verte... me propones\
Y aunque mi mente vacilante queda,\
En vista de tu sexo y tus razones\
Allá iré lo más pronto que pueda.\
\
Reír llorando\
\
Viendo a Garrick, actor de la Inglaterra,\
el pueblo al aplaudirlo le decía:\
Eres el más gracioso de la tierra y el más feliz.\
Y el cómico reía.\
\
Víctimas del spleen los altos lores,\
en sus noches más negras y pesadas,\
iban a ver al rey de los actores\
y cambiaban su spleen en carcajadas.\
\
Una vez ante un médico famoso,\
llegose un hombre de mirar sombrío:\
-Sufro -le dijo- un mal tan espantoso\
como esta palidez del rostro mío.\
\
Nada me causa encanto ni atractivo;\
no me importan mi nombre ni mi suerte;\
en un eterno spleen muriendo vivo,\
y es mi única pasión la de la muerte.\
\
-Viajad y os distaeréis. -Tanto he viajado\
-Las lecturas buscad -Tanto he leido-\
Que os ame una mujer - ¡Si soy amado!\
-Un título adquirid -Noble he nacido.\
\
¿Pobre seréis quizá? -Tengo riquezas\
- ¿De lisonjas gustáis ? - ¡Tantas escucho!\
-¿Que tenéis de familia?...-Mis tristezas\
-¿Vais a los cementerios?... -Mucho, mucho.\
\
¿De vuestra vida actual tenéis testigos?\
- Sí, mas no dejo que me impongan yugos;\
yo les llamo a los muertos mis amigos;\
y les llamo a los vivos mis verdugos.\
\
-Me deja- agrega el médico -perplejo\
vuestro mal, y no debo acobardaros;\
Tomad hoy por receta este consejo:\
sólo viendo a Garrick podéis curaros.\
\
-¿A Garrick ? -Sí, a Garrick...La más remisa\
y austera sociedad lo busca ansiosa;\
todo aquel que lo ve muere de risa;\
¡tiene una gracia artística asombrosa !\
\
-Y a mí me hará reir?-Ah, sí, os lo juro !;\
él, sí, nada más él...Mas qué os inquieta?...\
-Así -dijo el enfermo -no me curo:\
¡Yo soy Garrick ! Cambiádme la receta.\
\
¡Cúantos hay que, cansados de la vida,\
enfermos de pesar, muertos de tedio,\
hacen reir como el autor suicida\
sin encontrar para su mal remedio!\
\
¡Ay ! ¡ Cuántas veces al reír se llora!..\
¡Nadie en lo alegre de la risa fíe,\
porque en los seres que el dolor devora\
el alma llora cuando el rostro rie!\
\
Si se muere la fe, si huye la calma,\
si sólo abrojos nuestras plantas pisa\
lanza a la faz la tempestad del alma\
un relámpago triste: la sonrisa.\
\
El carnaval del mundo engaña tanto;\
que las vidas son breves mascaradas;\
aquí aprendemos a reír con llanto\
y también a llorar con carcajadas.\
\
\
\
Fusiles y Muñecas \
\
CUADRO REALISTA\
\
Juan y Margot, dos ángeles hermanos\
Que embellecen mi hogar con sus cariños\
Se entretienen con juegos tan humanos\
Que parecen personas desde niños.\
\
Mientras Juan, de tres años, es soldado\
Y monta en una caña endeble y hueca,\
Besa Margot con labios de granado\
Los labios de cartón de su muñeca.\
\
Lucen los dos sus inocentes galas,\
Y alegres sueñan en tan dulces lazos;\
El, que cruza sereno entre las balas;\
Ella, que arrulla un niño entre sus brazos.\
\
Puesto al hombro el fusil de hoja de lata,\
El kepis de papel sobre la frente,\
Alienta el niño en su inocencia grata\
El orgullo viril de ser valiente.\
\
Quizá piensa, en sus juegos infantiles,\
Que en este mundo que su afán recrea,\
Son como el suyo todos los fusiles\
Con que la torpe humanidad pelea.\
\
Que pesan poco, que sin odios lucen,\
Que es igual el más débil el más fuerte,\
Y que, si se disparan, no producen\
Humo, fragor, consternación y muerte.\
\
¡Oh, misteriosa condición humana!\
Siempre lo opuesto buscas en la tierra;\
Ya delira Margot por ser anciana,\
Y Juan, que vive en paz, ama la guerra.\
\
Mirándoles jugar me aflijo y callo:\
¿Cuál será sobre el mundo su fortuna?\
Sueña el niño con armas y caballo,\
La niña con velar junto a la cuna.\
\
El uno corre de entusiasmo ciego,\
La niña arrulla a su muñeca inerme,\
Y mientas grita el uno: Fuego! fuego,\
La otra murmura triste: Duerme, duerme.\
\
A mi lado ante juegos tan extraños\
Concha, la primogénita, me mira:\
¡Es toda una persona de ses años\
Que charla, que comenta y que suspira!\
\
¿Por qué inclina su lánguida cabeza\
Mientras deshoja inquieta algunas flores?\
¿Será la que ha heredado mi tristeza?\
¿Será la que comprende mis dolores?\
\
Cuando me rindo del dolor al peso,\
Cuando la negra duda me avasalla,\
Se me cuelga del cuello, me da un beso,\
Se le saltan las lágrimas y calla.\
\
Sueltas sus trenzas claras y sedosas,\
Y oprimiendo mi mano entre sus manos,\
Parece que medita en muchas cosas\
Al mirar cómo juegan sus hermanos.\
\
Margot, que canta en madre transformada,\
Y arrulla a un hijo que jamás se queja,\
Ni tiene que llorar desengañada,\
Ni el hijo crece, ni se vuelve vieja.\
\
Y este guerrero audaz de tres abriles\
Que ya se finge apuesto caballero,\
No logra en sus campañas infantiles\
Manchar con sangre y lágrimas su acero.\
\
¡Inocencia! ¡Niñez! ¡Dichosos nombres!\
Amo tus goces, busco tus cariños;\
Cómo han de ser los sueños de los hombres,\
Más dulces que los sueños de los niños!\
\
¡Oh, mis hijos! No quiera la fortuna\
Turbar jamás vuestra inocente calma,\
No dejéis esa espada ni esa cuna:\
¡Cuando son de verdad, matan el alma!\
\
\
\
A México\
En las últimas desgracias de España.\
\
Allá del revuelto mar\
Tras los secos arenales,\
Donde sus limpios cristales\
Las ondas van a estrellar,\
Donde en lucha singular\
Disputando a la Fortuna\
Las ciudades una a una,\
De sus guerreros el brío,\
Mostraron su poderío\
La cruz y la media luna;\
\
En esa tierra encantada,\
Que esconde, en perpetuo Abril,\
Las lágrimas de Boabdil\
En las vegas de Granada;\
Donde el ave enamorada\
Repite entre los vergeles\
El canto de los gomeles,\
Y cuelga su frágil nido\
Del minarete prendido\
Entre ojivas y caireles;\
\
Donde soñados ultrajes\
Vengaron fieros zegríes,\
Regando los alelíes,\
Con sangre de abencerrajes;\
donde entre muros de encajes\
Y torres de filigrana,\
Lloró la hermosa sultana\
Amorosos sentimientos\
A los rítmicos acentos\
De una trova castellana;\
\
Allá donde nueva luz\
Alumbró, limpia y serena,\
Sobre la morisca almena\
El símbolo de la cruz;\
En ese suelo andaluz,\
Cuyos cármenes hollando,\
Y en otro mundo soñando,\
Cruzaron en su corcel\
La magnánima Isabel\
Y el católico Fernando.\
\
En esa región que encierra\
Tantos recuerdos de gloria;\
En ese altar de la Historia;\
En ese edén de la tierra;\
No el azote de la guerra\
Infunde duelo y pavor,\
Ni causa fiero dolor\
Que mira asombrado el mundo\
El negro contagio inmundo;\
Allí otra plaga mayor.\
\
Surgen allí tempestades\
Del suelo entre las entrañas,\
Y vacilan las montañas,\
Y se arrasan las ciudades\
Escombros y soledades\
Son el cortijo y la aldea;\
La muerte se enseñorea,\
Y, en medio de tanta ruina,\
Se ve cual llama divina\
La Caridad que flamea.\
\
Con sordo bramido el duelo\
Todo lo enluta y recorre;\
Yace la maciza torre\
En pedazos sobre el suelo.\
Salvarse forma el anhelo\
De los espantados seres,\
Y hombres, niños y mujeres\
Las crispadas manos juntan,\
Y viendo al cielo preguntan.\
'Dinos Dios, ¿por qué nos hieres?'\
\
Recordando en sus delitos\
las bíblicas amenazas,\
Van por las calles y plazas\
Confesándolos a gritos.\
Los corazones precitos\
Se niegan a palpitar\
Y todos ven transformar\
Al golpe del terremoto,\
El abismo el verde soto,\
Y en escombros el hogar.\
\
Se abate el pesado muro\
Que adornó silvestre yedra\
Y brotan de cada piedra\
Una oración y un conjuro.\
No hay un asilo seguro;\
Ciérnese el ángel del mal;\
Cada fosa sepulcral\
Abrese ante fuerza extraña,\
Y parece que en España\
Comienza el juicio final.\
\
Y entre la nube sombría\
Que el denso polvo levanta,\
El coro terrible espanta\
De los gritos de agonía.\
Y entre aquella vocería,\
Con rostro desencajado,\
El padre busca espantado,\
Con ayes desgarradores\
El nido de sus amores,\
Entre escombros sepultado.\
\
Convulsa, pálida errante,\
Sobre el suelo que se agita\
La madre se precipita\
Por la angustia delirante;\
Vuela en pos del hijo amante;\
El rostro al abismo asoma\
Lo llama llorando, y toma\
Por voz del hijo querido,\
La que acompaña al crujido\
De un techo que se desploma.\
\
En repentina orfandad,\
Trémulas las manos tienden\
Los niños, que no comprenden\
Su espantosa soledad.\
Tan sólo la caridad\
Velará después por ellos,\
Curando con sus destellos\
su miseria y su aflicción:\
¡Cómo no amarlos, si son\
Tan inocentes, tan bellos!\
\
¿Qué pecho no se conmueve\
Ante cuadro tan sombrío,\
Que al corazón más bravío\
A contemplar no se atreve?\
Ante el infortunio aleve\
¿Quién no es noble? ¿quién no es bueno?\
¿Quién de piedad no está lleno,\
Cuando es la virtud mayor,\
Aun más que el propio dolor,\
Sentir el dolor ajeno?\
\
Manda ¡oh, noble patria mía!\
La ofrenda de tus piedades\
A las hoy tristes ciudades\
De la hermosa Andalucía.\
No es favor, es hidalguía;\
Es deber, no vanidad.\
Llamen otro Caridad\
Estos óbolos del hombre,\
Tienen nombre, sólo un nombre;\
Se llaman Fraternidad.\
\
Con tierno entusiasmo santo,\
Mezcla ¡oh patria amante y buena!\
Esa pena con tu pena,\
Ese llanto con tu llanto.\
Si al mirar ese quebranto,\
Tu triste historia repasas,\
Verás que angustias no escasas\
Pasó, entre llantos prolijos,\
Por amparar a tus hijos\
Bartolomé de las Casas.\
\
\
En mi barrio\
\
Sobre la rota ventana antigua\
Con tosco alféizar, con puerta exigua,\
Que hacia la oscura callejada,\
Pasmando al vulgo como estantigua\
Tallada en piedra, la santa está.\
\
Borró la lluvia los mil colores\
Que hubo en su manto y en su dosel;\
Y recordando tiempos mejores,\
Guarda amarillas y secas flores\
De las verbenas del tiempo aquel.\
\
El polvo cubre sus aureolas,\
Las telarañas visten su faz,\
Nadie a sus plantas riega amapolas,\
Y ve la santa las calles solas,\
La casa triste, la gente en paz.\
\
Por muchos años allí prendido,\
Único adorno del tosco altar, \
Flota un guiñapo descolorido,\
Piadosa ofrenda que no ha caído\
De las desgracias al hondo mar.\
\
A arrebatarlo nadie se atreve,\
Símbolo antiguo de gran piedad,\
Mira del tiempo la marcha breve;\
Y cuando el aire lo empuja y mueve\
Dice a los años: pasad, pasad.\
\
¡Pobre guiñapo que el aire enreda!\
¡Qué amarga y muda lección me da!\
La vida pasa y el mundo rueda,\
Y siempre hay algo que se nos queda\
De tanto y tanto que se nos va.\
\
Tras esa virgen oscura piedra\
Que a nadie inspira santo fervor,\
Todo el pasado surge y me arredra;\
Escombros míos, yo soy la yedra;\
¡nidos desiertos, yo fui el amor!\
\
Altas paredes desportilladas\
Cuyos sillares sin musgo vi,\
¡cuántas memorias tenéis guardadas!\
Níveas corinas, jaulas doradas,\
Tiestos azules… ¡no estáis aquí!\
\
En mi azarosa vida revuelta\
Fue de esta casa dueño y señor,\
¿do está la ninfa, de crencha suelta,\
de grandes ojos, blanca y esbelta,\
que fue mi encanto, mi fe, mi amor?\
\
¡Oh mundo ingrato, cuántos reveses\
en ti he sufrido! La tempestad\
todos mis campos dijo sin mieses…\
La niña duerme bajo cipreses,\
Su sueño arrulla la eternidad. \
\
¡Todo ha pasado! ¡Todo ha caído!\
Sólo en mi pecho queda la fe,\
Como el guiñapo descolorido\
Que a la escultura flota prendido…\
¡Todo se ha muerto! ¡Todo se fue!\
\
Pero ¡qué amarga, profunda huella\
Llevo en mi pecho! … ¡Cuán triste estoy!…\
La fe radiante como una estrella,\
La casa alegre, la niña bella,\
El perro amigo… ¿Dónde están hoy?\
\
¡Oh calle sola, vetusta casa!\
¡angostas puertas de aquel balcón!\
Si todo muere, si todo pasa\
¿por qué esta fiebre que el pecho abrasa\
no ha consumido mi corazón?\
\
Ya no hay macetas llenas de flores\
Que convirtieran en un pensil\
Azotehuelas y corredores…\
Ya no se escuchan frases de amores,\
Ni hay golondrinas del mes de abril.\
\
Frente a la casa la cruz cristiana\
Del mismo templo donde rezó,\
Las mismas misas de la mañana,\
La misa torre con la campana\
Que entre mis brazos la despertó.\
\
Vetusta casa, mansión desierta,\
Mírame solo volviendo a ti…\
Arrodillado beso tu puerta\
Creyendo loco que aquella muerta\
Adentro espera pensando en mí.\
\
\
\
En las ruinas de Mitla\
\
Maravillas de otra edad;\
Prodigios de lo pasado;\
Páginas que no ha estudiado\
La indolente humanidad.\
¿Por qué vuestra majestad\
causa entusiasmo y pavor?\
Porque de tanto esplendor\
Y de tantas muertas galas,\
Están batiendo las alas\
Los siglos en derredor.\
\
Muda historia de granito\
Que erguida en pie te mantienes,\
¿qué nos escondes? ¿Qué tienes\
por otras razas escrito?\
Cada inmenso monolito, \
Del arte eximio trabajo,\
¿quién lo labró? ¿Quién lo trajo\
a do nadie lo derriba?\
Lo saben, Dios allá arriba;\
La soledad aquí abajo.\
\
Cada obelisco de pie\
Me dice en muda arrogancia:\
Tú eres dudas e ignorancia,\
Yo soy el arte y la fe,\
Semejan de lo que fue\
Los muros viejos guardianes…\
¡qué sacrificios! ¡qué afanes\
revela lo que contemplo!\
Labrado está cada templo\
No por hombres, por titanes.\
\
En nuestros tiempos ¿qué son\
Los ritos, usos y leyes,\
De sacerdotes y reyes\
Que aquí hicieron oración?\
Una hermosa tradición\
Cuya antigüedad arredra;\
Ruinas que viste la yedra\
Y que adorna el jaramago:\
¡la epopeya del estrago\
escrita en versos de piedra!\
\
Del palacio la grandeza;\
Del templo la pompa extraña;\
La azul y abrupta montaña\
Convertida en fortaleza;\
Todo respira tristeza,\
Olvido, luto, orfandad;\
¡aun del so l la claridad\
se torna opaca y medrosa\
en la puerta misteriosa\
de la negra eternidad!\
\
Despojo de lo ignorado,\
Busca un trono la hoja seca\
En la multitud greca\
Del frontón desportillado.\
Al penate derribado\
La ortiga encubre y escuda;\
Ya socavó mano ruda\
La perdurable muralla…\
Viajero: medita y calla…\
¡Lo insondable nos saluda!\
\
Sabio audaz, no inquieras nada,\
Que no sabrás más que yo;\
Aquí una raza vivió\
Heroica y civilizada;\
Extinta o degenerada,\
Sin renombre y sin poder,\
De su misterioso ser\
Aquí el esplendor se esconde\
Y aquí sólo Dios responde\
¡Y dios no ha de responder!\
\
\
Nieve de estío\
\
Como la historia del amor me aparta\
de las sombras que empañan mi fortuna,\
yo de esa historia recogí esta carta\
que he leído a los rayos de la luna.\
\
Yo soy una mujer muy caprichosa\
y que me juzgue a tu conciencia dejo,\
para poder saber si estoy hermosa\
recurro a la franqueza de mi espejo\
\
Hoy, después que te vi por la mañana,\
al consultar mi espejo alegremente,\
como un hilo de plata vi una cana\
perdida entre los rizos de mi frente.\
\
Abrí para arrancarla mis cabellos\
sintiendo en mi alma dolorosas luchas,\
y cuál fue mi sorpresa, al ver en ellos \
esa cana crecer con otras muchas.\
\
¿Por qué se pone mi cabello cano?\
¿Por qué está mi cabeza envejecida?\
¿Por qué cubro mis flores tan temprano\
con las primeras nieves de la vida?\
\
No lo sé. Yo soy tuya, yo te adoro,\
con fe sagrada, con el alma entera;\
pero sin esperanza sufro y lloro;\
¿tiene también el llanto primavera?\
\
Cada noche soñando un nuevo encanto\
vuelvo a la realidad desesperada;\
soy joven, en verdad, mas sufro tanto\
que siento ya mi juventud cansada.\
\
Cuando pienso en lo mucho que te quiero\
y llego a imaginar que no me quieres,\
tiemblo de celos y de orgullo muero;\
(Perdóname, así somos las mujeres).\
\
He cortado con mano cuidadosa\
esos cabellos blancos que te envío;\
son las primeras nieves de una rosa\
que imaginabas llena de rocío.\
\
Tú me has dicho: 'De todos tus hechizos, \
lo que más me cautiva y enajena,\
es la negra cascada de tus rizos\
cayendo en torno a tu faz morena'.\
\
Y yo, que aprendo todo lo que dices,\
puesto que me haces tan feliz con ello,\
he pasado mis horas más felices\
mirando cuán rizado es mi cabello.\
\
Mas hoy, no elevo dolorosa queja,\
porque de ti no temo desengaños;\
mis canas te dirán que ya está vieja\
una mujer que cuenta veintiún años.\
\
¿Serán para tu amor mis canas nieve?\
Ni a suponerlo en mis delirios llego.\
¿Quién a negarme sin piedad se atreve\
que es una nieve que brotó del fuego?\
\
¿Lo niegan los principios de la ciencia\
y una antítesis loca se parece?\
pues es una verdad de la experiencia:\
cabeza que se quema se emblanquece.\
\
Amar con fuego y existir sin calma;\
soñar sin esperanza de ventura,\
dar todo el corazón, dar toda el alma\
en un amor que es germen de amargura.\
\
Buscar la dicha llena de tristeza\
sin dejar que sea tuyo el hado impío,\
llena de blancas hebras mi cabeza\
y trae una vejez: la del hastío.\
\
Enemiga de necias presunciones\
cada cana que brota me la arranco,\
y aunque empañe tus gratas ilusiones\
te mando, ya lo ves, un rizo blanco.\
\
¿Lo guardarás? Es prenda de alta estima\
y es volcán este amor a que me entrego;\
tiene el volcán sus nieves en la cima,\
pero circula en sus entrañas fuego.\
\
\
A mis hijas\
\
Mi tristeza. es un mar; tiene su bruma \
que envuelve densa mis amargos días; \
sus olas son de lágrimas; mi pluma \
está empapada en ellas, hijas mías. \
Vosotras sois las inocentes flores \
nacidas de ese mar en la ribera;\
la sorda tempestad de mis dolores\
sirve de arrullo a vuestra edad primera. \
Nací para luchar; sereno y fuerte \
cobro vigor en el combate rudo;\
cuando pague mi audacia con la muerte, \
caeré cual gladiador sobre mi escudo. \
\
Llévenme así a vosotras; de los hombres \
ni desdeño el poder ni el odio temo; \
pongo todo mi honor en vuestros nombres \
y toda el alma en vuestro amor supremo. \
Para salir al mundo vais de prisa.\
¡Ojalá que esa vez nunca llegara!\
Pues hay que ahogar el llanto con la risa, \
para mirar al mundo cara a cara.\
\
No me imitéis a mí: yo me consuelo \
con abrir más los bordes de mi herida; \
imitad en lo noble a vuestro abuelo: \
¡Sol de virtud que iluminó mi vida!\
\
Orad y perdonad; siempre es inmensa \
después de la oración la interna calma, \
y el ser que sabe perdonar la ofensa \
sabe llevar a Dios. dentro del alma.\
\
Sea vuestro pecho de bondades nido, \
no ambicionéis lo que ninguno alcanza, \
coronad el perdón con el olvido\
y la austera virtud con la esperanza.\
\
Sin dar culto a los frívolos placeres \
que la pureza vuestra frente ciña, \
buscad alma de niña en las mujeres \
y buscad alma de ángel en la niña.\
\
Nadie nace a la infamia condenado, \
nadie hereda la culpa de un delito, \
nunca para ser siervas del pecado\
os disculpéis clamando: estaba escrito.\
\
¡Existir es luchar! No es infelice \
quien luchando, de espinas se corona; \
abajo, todo esfuerzo se maldice, \
arriba, toda culpa se perdona.\
\
Se apaga la ilusión cual lumbre fatua \
y la hermosura es flor que se marchita; \
la mujer sin piedad es una estatua \
dañosa al mundo y del hogar proscrita.\
\
No fijéis en el mal vuestras pupilas \
que víbora es el mal que todo enferma, \
y haced el bien para dormir tranquilas \
cuando yo triste en el sepulcro duerma.\
\
Nunca me han importado en este suelo \
renombre, aplausos, oropeles, gloria: \
procurar vuestro bien, tal es mi anhelo; \
amaros y sufrir tal es mi historia.\
\
Cuando el sol de mi vida tenga ocaso \
recordad mis consejos con ternura,\
y en cada pensamiento, en cada paso, \
buscad a Dios tras de la inmensa altura.\
\
Yo anhelo que, al morir, por premio santo,\
tengan de vuestro amor en los excesos:\
las flores de mi tumba vuestro llanto,\
las piedras de mi tumba vuestros besos.\
\
\
Mi padre\
\
Yo tengo en el hogar un soberano,\
único a quien venera el alma mía;\
es su corona su cabello cano,\
la honra su ley y la virtud su guía.\
En lentas horas de miseria y duelo,\
lleno de firme y varonil constancia,\
guarda la fé con que me habló del cielo\
en las horas primeras de mi infancia.\
La amarga proscripción y la tristeza\
en su alma abrieron incurable herida;\
es un anciano, y lleva en su cabeza\
el polvo del camino de la vida.\
Ve del mundo las fieras tempestades,\
de la suerte las horas desgraciadas,\
y pasa, como cristo el Tiberiades,\
de pie sobre las ondas encrespadas.\
Seca su llanto, calla sus dolores,\
y sólo en el deber sus ojos fijos,\
recoge espinas y derrama flores\
sobre la senda que trazó a sus hijos.\
Me ha dicho: 'A quien es bueno, la amargura\
jamás en llanto sus mejillas moja:\
en el mundo la flor de la ventura\
al mas ligero soplo se dehoja.\
'Haz el bien sin temer al sacrificio,\
el hombre ha de luchar sereno y fuerte,\
y halla quien odia la maldad y el vicio\
un tálamo de rosas en la muerte.\
'Si eres pobre confórmate y sé bueno;\
si eres rico protege al desgraciado,\
y lo mismo en tu hogar que en el ajeno\
guarda tu honor para vivir honrado.'\
'Ama la libertad, libre es el hombre\
y su juez más severo es la conciencia;\
tanto como tu honor guarda tu nombre,\
pues mi nombre y mi honor forman tu herencia'.\
Este código augusto, en mi alma pudo\
desde que lo escuché, quedar grabado;\
en todas las tormentas fue mi escudo,\
de todas las borrascas me ha salvado.\
Mi padre tiene en su mirar sereno\
reflejo fiel de su conciencia honrada;\
¡cuánto consejo cariñoso y bueno\
sorprendo en el fulgor de su mirada!\
La nobleza del alma es su nobleza;\
la gloria del deber forma su gloria;\
es pobre, pero encierra su pobreza\
la página más grande de su historia.\
Siendo el culto de mi alma su cariño,\
la suerte quiso que al honrar su nombre,\
fuera el amor que me inspiró de niño\
la más sagrada inspiración del hombre.\
Quiera el cielo que el canto que me inspira\
siempre sus ojos con amor lo vean,\
y de todos los versos de mi lira\
éstos los dignos de su nombre sean.\
\
\
\
\
Bebé\
\
Cuenta Bebé dos meses no cumplidos,\
pero burlando al tiempo y sus reveses,\
como todos los niños bien nacidos\
parece un señorón de 20 meses.\
\
Rubio, y con ojos como dos luceros\
lo vi con traje de color de grana\
en un escaparate de Plateros\
un domingo de Pascua en la mañana.\
\
Iban conmigo Concha y Margarita\
y al mirar las dos, ambas gritaron:\
'¡Mira padre, qué cara tan bonita!'\
y trémulas de gozo mi miraron.\
\
¿Quién al ver que en sus hijas se subleva\
la ambición de adueñarse de un muñeco,\
no se siente vencido cuando lleva\
dos duros en la bolsa del chaleco?\
\
Ha vencido pensé: si está comprado,\
y como es natural tiene otros dueños\
mis hijas perderán el encantado\
palacio de sus mágicos ensueños.\
\
Pero movido el paternal cariño,\
entré a la tienda a realizar su antojo,\
y dije al vendedor: 'Quiero ese niño\
de crenchas blondas y vestido rojo'.\
\
Abrió entonces la alcoba de cristales\
tomó a Bebé, lo puso entre mis manos,\
y convirtió a mis hijas en rivales\
porque el amor divide a los hermanos.\
\
'Para mí' -Concha me gritó importuna,\
'para mí' -me gritaba Margarita,\
y yo les grité al fin: 'para ninguna'\
con la seca aridez de un cenobita.\
\
Reinó un silencio entre las dos profundo,\
y yo recordé entonces conturbado\
este axioma tristísimo del mundo:\
'Ser rival es odiar y ser odiado'.\
\
Y así pensé: no debo en corazones\
que de la vida llaman a la puerta,\
encender con el celo esas pasiones,\
que el odio atiza y el rencor despierta.\
\
La historia del amor con dos premisas,\
iguala a la mujer y no os asombre;\
¡Un muñeco en la edad de las sonrisas,\
y en la edad de las lágrimas, un hombre!\
\
\
\
\
\
\
César En Casa\
\
Juan, aquel militar de tres abriles,\
que con gorra y fusil sueña en ser hombre,\
y que ha sido en sus guerras infantiles\
un glorioso heredero de mi nombre;\
\
ayer, por tregua al belicoso juego,\
dejando en un rincón la espada quieta,\
tomó por voluntad, no a sangre y fuego,\
mi mesa de escribir y mi gaveta.\
\
Allí guardo un laurel, y viene al caso\
repetir lo que saben mis testigos:\
esa corona de oropel y raso\
la debo, no a la gloria, a mis amigos.\
\
Con sus manos pequeñas y traviesas,\
desató el niño, de la verde guía,\
el lazo tricolor en que hay impresas\
frases que él no descifra todavía.\
\
Con la atención de un ser que se emociona\
miró las hojas con extraño gesto,\
y poniendo en mis manos la corona,\
me preguntó con intención: -'¿Qué es esto?'\
\
-'Esto es -repuse- el lauro que promete\
la gloria al genio que en su luz inunda...\
-'¿Y por qué lo tienes?' -Por juguete,\
le respondió mi convicción profunda.\
\
Viendo la forma oval, pronto el objeto\
descubre el niño, de la noble gala;\
se la ciñe, faltándome al respeto\
y hecho un héroe se aleja por la sala.\
\
¡Qué hermosa dualidad! Gloria y cariño\
con su inocente acción enlazó ufano,\
pues con el lauro semejaba el niño\
un diminuto emperador romano.\
\
hasta creí que de su faz severa\
irradiaban celestes resplandores,\
y que anhelaba en su imperial litera\
ir al Circo a buscar los gladiadores.\
\
Con su nuevo disfraz quedé asombrado\
(no extrañéis en un padre estos asombros),\
y corrí por un trapo colorado\
que puse y extendí sobre sus hombros.\
\
Mirélo así con cándido embeleso,\
me transformé en su esclavo humilde y rudo,\
y -'¡Ave César!- le dije, dame un beso,\
¡yo que muero de penas, te saludo!'\
\
-'¿César?'- me preguntó lleno de susto\
y yo sintiendo que su amor me abrasa,\
-'¡César!' -le respondí- 'César Augusto\
de mi honor, de mi honra y de mi casa'\
\
Quitéle el manto, le volví la espada,\
recogí mi corona de poeta,\
y la guardé, deshecha y empolvada,\
en el fondo sin luz de mi gaveta.\
\
\
\
\
El Cuento De Margot\
\
Vamos, Margot, repíteme esa historia\
que estabas refiriéndole a María,\
ya vi que te la sabes de memoria\
y debes enseñármela, hija mía.\
\
-La sé porque yo misma la compuse.\
-¿Y así no me la dices? Anda, ingrata.\
-¡Tengo compuestas diez! -¡Cómo! repuse,\
¿Te has vuelto a los seis años literata?\
\
-¡No, literata no! pero hago cuentos...\
-No temas que tal gusto te reproche.\
-Al ver a mis hermanos tan contentos\
yo les compongo un cuento en cada noche.\
\
-¿Y cómo dice el que contando estabas?\
-Es muy triste, papá, ¿qué no lo oíste?\
-Sólo oí que lloraban y llorabas.\
-¡Ah! sí, todos lloramos; ¡es muy triste!\
\
Imagínate un niño abandonado\
de grandes ojos de viveza llenos,\
rubio, risueño, gordo y colorado\
-Como mi hermano Juan, ni más ni menos.\
\
Figúrate una noche larga y fría,\
de muda soledad, sin luz alguna,\
y ese niño muriendo, en agonía,\
encima de la acera, no en la cuna.\
\
-¿En las heladas lozas? -Sí, en la acera.\
Es decir, en la calle... ¡Qué amargura!\
-Hubo alguien que pasando lo creyera\
un olvidado cesto de basura.\
\
Yo pasaba, lo vi, bajé mis brazos\
queriendo darle maternal abrigo\
y envuelto en un pañal hecho pedazos\
lo alcé a mi pecho y lo llevé conmigo.\
\
Lloraba tanto y tanto el angelito\
que ya estaban sus párpados muy rojos...\
y a cada nueva queja, a cada grito\
el alma me sacaba por los ojos.\
\
Me lo llevé a mi cama: entre plumones\
lo hice dormir caliente y sosegado...\
¡Cómo hubo en este mundo corazones\
capaces de dejarlo abandonado!\
\
¡Ay! yo sé por mi libro de lectura\
que estudio en mis mayores regocijos,\
que ni los tigres en la selva oscura\
dejan abandonados a sus hijos.\
\
¡Pobrecito! yo sé su mal profundo,\
le curo como madre toda pena;\
parece que este niño en este mundo\
no es hijo de mujer sino de hiena.\
\
De mi colchón en el caliente hueco\
duerme para que en lágrimas no estalle;\
y llorando Margot, mostró el muñeco\
que en cierta noche se encontró en la calle.\
\
\
\
\
\
El Nido\
\
Mira ese árbol que a los cielos\
sus ramas eleva erguido;\
en ellas columpia un nido\
en que duermen tres polluelos.\
\
Ese nido es un hogar;\
no lo rompas, no lo hieras:\
sé bueno y deja a las fieras,\
el vil placer de matar.\
\
\
\
\
En Cada Corazón Arde Una Llama\
\
En cada corazón arde una llama,\
si aún vive la ilusión y amor impera,\
pero en mi corazón desdeque te ama\
sin que viva ilusión, arde una hoguera.\
\
Oye esta confesión; te amo con miedo,\
con el miedo del alma a tu hermosura,\
y te traigo a mis sueños y no puedo\
llevarte más allá de mi amargura.\
\
¿Sabes lo que es vivir como yo vivo?\
¿Sabes lo que es llorar sin fe ni calma?\
¿Mientras se muere el corazón cautivo\
y en la cruz del dolor expira el alma?\
\
Eres al corazón lo que a las ruinas\
son los rayos del sol esplendoroso,\
donde el reptil se arropa en las esquinas\
y se avergüenza el sol del ser hermoso.\
\
Nunca podrás amarme aunque yo quiera,\
porque lo exige así mi suerte impía,\
y si esa misma suerte nos uniera\
tú fueras desgraciada por ser mía.\
\
Deja que te contemple y que te adore,\
y que escuche tu voz y que te admire,\
aunque al decirte adiós, con risas llore,\
y al volvernos a ver llore y suspire.\
\
Yo no quiero enlazar a mi destino\
tu dulce juventud de horas tranquilas,\
ni he de dar otro sol a mi camino\
que los soles que guardan tus pupilas.\
\
Enternézcame siempre tu belleza\
aunque no me des nunca tus amores,\
y no adornes con flores tu cabeza\
pues me encelan los besos de las flores.\
\
Siempre rubios, finísimos y bellos,\
madejas de oro, en céltica guirnalda,\
caigan flotando libres tus cabellos,\
como un manto de reina por tu espalda.\
\
Es cielo azul el que mi amor desea,\
la flor que más me encanta es siempre hermosa,\
que en tu talle gentil yo siempre vea\
tu veste tropical de azul y rosa.\
\
Mírame con tus ojos adormidos,\
sonriéndote graciosa y dulcemente,\
y avergüenza y maldice a mis sentidos\
mostrándome el rubor sobre tu frente.\
\
¿Yo nunca seré tuyo? ¡ay! ese día,\
oscureciera al sol duelo profundo;\
mas para ser feliz sobre este mundo\
bástame amarte sin llamarte mía.\
\
\
\
\
\
Este Era Un Rey...\
\
Ven mi Juan, y toma asiento\
en la mejor de tus sillas;\
siéntate aquí, en mis rodillas,\
y presta atención a un cuento.\
\
Así estás bien, eso es,\
muy cómodo, muy ufano,\
pero ten quieta esa mano;\
vamos, sosiega esos pies.\
\
Este era un rey... me maltrata\
el bigote ese cariño,\
Este era un rey... vamos niño,\
que me rompes la corbata.\
\
Si vieras con qué placer\
ese rey... ¡Jesús! ¡qué has hecho!\
¿Lo ves? en medio del pecho\
¡me has clavado un alfiler!\
\
¿Y mi dolor te da risa?\
escucha y tenme respeto:\
éste era un rey... deja quieto\
el cuello de mi camisa.\
\
Oír atento es la ley\
que a cumplir aquí te obligo...\
Deja mi reloj... prosigo.\
Atención: Este era un rey...\
\
Me da tormentos crueles\
tu movilidad chicuelo,\
¿ves? has regado en el suelo\
mi dinero y mis papeles.\
\
Responde: ¿me has de escuchar?\
Este era un rey... ¡qué locura!\
me tiene en grande tortura\
que te muevas sin parar.\
\
Mas ¿ya estás quieto? Sí, sí\
al fin cesa mi tormento...\
Este era un rey, oye el cuento\
inventado para ti.\
\
Y agrega el niño, que es ducho\
en tramar cuentos a fe:\
'Este era un rey...' ya lo sé\
porque lo repites mucho.\
\
Y me gusta el cuentecito\
y mira ya lo aprendí:\
'Este era un rey', ¿no es así?\
'¡Qué bonito! ¡Qué bonito!'\
\
Y de besos me da un ciento,\
y pienso al ver sus cariños:\
los cuentos para los niños,\
no requieren argumento.\
\
Basta con entender\
su espíritu de tal modo\
que nos puedan hacer todo\
lo que nos quieran hacer.\
\
Con lenguaje grato o rudo\
un niño, sin hacer caso,\
va dejando paso a paso\
a su narrador desnudo.\
\
Infeliz del que se escama\
con esas dulces locuras:\
¡si estriba en sus travesuras\
el argumento del drama!\
\
¡Oh Juan! me alegra y me agrada\
tu movilidad tan terca;\
te cuento por verte cerca\
y no por contarte nada.\
\
Y bendigo mi fortuna,\
y oye el cuento y lo sabrás;\
'Era un rey a quien jamás\
le sucedió cosa alguna'.\
\
\
\
\
\
Mi Mejor Lauro\
\
\
Con sus seis primaveras muy ufana,\
quebrando con sus pies las hojas secas,\
me recitó en el campo una mañana\
mi hija mayor : Fusiles y muñecas.\
\
Repitiendo mis versos no sabía\
que colmaba el mayor de mis antojos;\
no me culpéis si oyéndola sentía,\
lágrimas en el alma y en los ojos.\
\
¡Bien! exclamé, mi niña me interpreta\
mejor que todos aunque a nadie cuadre;\
yo juzgarla creí como poeta,\
y la estaba juzgando como padre.\
\
Llegó la estrofa aquella en que la nombro\
y bajando hacia el suelo la mirada,\
vi de pronto ponerse, con asombro,\
su faz, más que una fresa, colorada.\
\
¿Qué tienes? pregunté, ¿por qué haces eso?\
¿Por qué ya nada de tu labio escucho?\
Y ella me respondió, dándome un beso:\
-Me callo aquí, porque te quiero mucho.\
\
Nada valdrá tan cándida respuesta\
para el que en altas concepciones fijo,\
medir no pueda, en ocasión cual ésta,\
a donde alcanza el corazón de un hijo.\
\
Puedo deciros la verdad desnuda:\
como en mis versos comprendió mi duelo,\
por no hacerme sufrir quedóse muda,\
por no verme llorar, miraba al suelo.\
\
Yo, alabando el poder de su memoria,\
comprendí, perdonadme lo indiscreto,\
que los mejores lauros de la gloria\
son los que se cosechan en secreto.\
\
Vale más a mis ojos, siempre fijos\
en la eterna verdad no en falsos nombres,\
la lágrima arrancada por mis hijos\
que todos los aplausos de los hombres.\
\
Negó a mi numen su fulgor el genio,\
en el drama veraz de mis dolores\
el fondo de mi hogar es el proscenio\
y mi padre y mis hijos los lectores.\
\
No busco un lauro que mi frente ciña\
ni pide aplausos mi laúd ingrato;\
pero... ¿por qué me olvido de la niña\
que suspendió turbada su relato?\
\
Pronto volvió su faz a estar serena\
y a brillar en sus labios la sonrisa,\
porque el placer lo mismo que la pena\
pasan sobre los niños muy de prisa.\
\
-Tus versos voy a continuar diciendo-\
y con más firme voz soltóse hablando;\
¡inocente! los dijo sonriendo\
y entonces yo los escuché llorando.\
\
Al terminar, sintiendo hecho pedazos\
por el dolor mi corazón ardiente,\
me interrogó cruzándose de brazos\
y mirándome el rostro frente a frente.\
\
-¡Ay! dime padre, cuando tú escribiste\
los mismo versos que de oírme acabas\
¿porqué estabas mirándome tan triste?\
Al mirarnos jugar ¿en qué pensabas?\
\
y ¿por qué? -respondí- tan preguntona\
¿indagas los misterios de mi lira?\
-Porque soy, tú lo has dicho, una persona\
que charla, que comenta, y que suspira.\
\
-¡Brava razón! ¡Confórmame con eso!\
¿No eres la que, si el duelo me avasalla,\
se me cuelga del cuello, me da un beso,\
se le saltan las lagrimas y calla?\
\
-¡Yo soy! ¡yo soy! me contestó orgullosa,\
y haciéndome olvidar penas y agravios,\
se me colgó del cuello cariñosa,\
cerró sus ojos y besó mis labios.\
\
Corrió alegre después tras otros niños\
quebrando con sus pies las hojas secas\
y dejándome besos y cariños\
en premio de Fusiles y muñecas.\
\
\
\
\
Post-Umbra\
\
Con letras ya borradas por los años,\
en un papel que el tiempo ha carcomido,\
símbolo de pasados desengaños,\
guardo una carta que selló el olvido.\
\
La escribió una mujer joven y bella.\
¿Descubriré su nombre? ¡no!, ¡no quiero!\
pues siempre he sido, por mi buena estrella,\
para todas las damas, caballero.\
\
¿Qué ser alguna vez no esperó en vano\
algo que si se frustra, mortifica?\
Misterios que al papel lleva la mano,\
el tiempo los descubre y los publica.\
\
Aquellos que jusgáronme felice,\
en amores, que halagan mi amor propio,\
aprendan de memoria lo que dice\
la triste historia que a la letra copio:\
\
'Dicen que las mujeres sólo lloran\
cuando quieren fingir hondos pesares;\
los que tan falsa máxima atesoran,\
muy torpes deben ser, o muy vulgares.\
\
Si cayera mi llanto hasta las hojas\
donde temblando está la mano mía,\
para poder decirte mis congojas\
con lágrimas mi carta escribiría.\
\
Mas si el llanto es tan claro que no pinta,\
y hay que usar de otra tinta más obscura,\
la negra escogeré, porque es la tinta\
donde más se refleja mi amargura.\
\
Aunque no soy para sonar esquiva,\
sé que para soñar nací despierta.\
Me he sentido morir y aún estoy viva;\
tengo ansias de vivir y ya estoy muerta.\
\
Me acosan de dolor fieros vestigios,\
¡qué amargas son las lágrimas primeras!\
Pesan sobre mi vida veinte siglos,\
y apenas cumplo veinte primaveras.\
\
En esta horrible lucha en que batallo,\
aun cuando débil, tu consuelo imploro,\
quiero decir que lloro y me lo callo,\
y más risueña estoy cuanto más lloro.\
\
¿Por qué te conocí? Cuando temblando\
de pasión, sólo entonces no mentida,\
me llegaste a decir: 'te estoy amando\
con un amor que es vida de mi vida'\
\
¿Qué te respondí yo? Bajé la frente,\
triste y convulsa te estreché la mano,\
porque un amor que nace tan vehemente\
es natural que muera muy temprano.\
\
Tus versos para mí conmovedores,\
los juzgué flores puras y divinas,\
olvidando, insensata, que las flores\
todo lo pierden menos las espinas.\
\
Yo, que como mujer, soy vanidosa,\
me vi feliz creyéndome adorada,\
sin ver que la ilusión es una rosa,\
que vive solamente una alborada.\
\
¡Cuántos de los crepúsculos que admiras\
pasamos entre dulces vaguedades;\
las verdades juzgándolas mentiras\
las mentiras creyéndolas verdades!\
\
Me hablabas de tu amor, y absorta y loca,\
me imaginaba estar dentro de un cielo,\
y al contemplar mis ojos y mi boca,\
tu misma sombra me causaba celo.\
\
Al verme embelesada, al escucharte,\
clamaste, aprovechando mi embeleso:\
'déjame arrodillar para adorarte';\
y al verte de rodillas te di un beso.\
\
Te besé con arrojo, no se asombre\
un alma escrupulosa y timorata;\
la insensatez no es culpa. Besé a un hombre\
porque toda pasión es insensata.\
\
Debo aquí confesar que un beso ardiente,\
aunque robe la dicha y el sosiego,\
es el placer más grande que se siente\
cuando se tiene un corazón de fuego.\
\
Cuando toqué tus labios fue preciso\
soñar que aquél placer se hiciera eterno.\
Mujeres: es el beso un paraíso\
por donde entramos muchas al infierno.\
\
Después de aquella vez, en otras muchas,\
apasionado tú, yo enternecida,\
quedaste vencedor en esas luchas\
tan dulces en la aurora de la vida.\
\
¡Cuántas promesas, cuántos devaneos!\
el grande amor con el desdén se paga:\
Toda llama que avivan los deseos\
pronto encuentra la nieve que la apaga.\
\
Te quisiera culpar y no me atrevo,\
es, después de gozar, justo el hastío;\
yo que soy un cadáver que me muevo,\
del amor de mi madre desconfío.\
\
Me engañaste y no te hago ni un reproche,\
era tu voluntad y fue mi anhelo;\
reza, dice mi madre, en cada noche;\
y tengo miedo de invocar al cielo.\
\
Pronto voy a morir; esa es mi suerte;\
¿quién se opone a las leyes del destino?\
Aunque es camino oscuro el de la muerte,\
¿quién no llega a cruzar ese camino?\
\
En él te encontraré; todo derrumba\
el tiempo, y tú caerás bajo su peso;\
tengo que devolverte en ultratumba\
todo el mal que me diste con un beso.\
\
Mostrar a Dios podremos nuestra historia\
en aquella región quizá sombría.\
¿Mañana he de vivir en tu memoria...?\
Adiós... adiós... hasta el terrible día.'\
\
Leí estas líneas y en eterna ausencia\
esa cita fatal vivo esperando...\
Y sintiendo la noche en mi conciencia,\
guardé la carta y me quedé llorando.\
\
\
\
\
\
Un Consejo De Familia\
\
¿Quién en la miseria y el amor concilia?\
Esto más que un problema es un misterio.\
Para hablar de un asunto que es tan serio,\
hubo ayer un consejo de familia.\
\
Hizo de presidente del concejo\
un hombrecito al que la edad agobia,\
y que además del chiste de ser viejo,\
es, nada menos, padre de mi novia.\
\
A su lado, y en cómoda poltrona,\
con franco y natural desembarazo,\
estaba una señora setentona\
con un perro faldero en el regazo.\
\
Y en derredor, con rostros muy severos,\
prontos a discutir y meter baza,\
estaban cual prudentes consejeros\
seis a siete visitas de la casa.\
\
Y entre todos, causando maravilla,\
de gracia y juventud, rico tesoro,\
como un ángel, sentada en una silla\
estaba la mujer a quien adoro.\
\
Con que, vamos a ver, dijo indiscreta\
la madre, por anciana impertinente,\
¿es verdad que eres novia de un poeta?\
¿Sueñas con los laureles de su frente?\
\
-Puesto que lo sabéis, dijo la niña,\
no lo puedo negar: le quiero mucho.\
-Mereces, dijo el padre, que te riña.\
Y la anciana exclamó: -¡Cielos! ¡qué escucho!\
\
¡Blasfemia intolerable que me irrita!\
-¡Habráse visto niña descarada!\
Dijo en tono burlón una visita\
pegándose en la frente una palmada.\
\
-Los versos nada más son oropeles.\
Dijo la anciana en tono reposado,\
y apuesto que no sirven sus laureles\
ni para sazonar el estofado.\
\
¡Un novio soñador y sin dinero!\
Hija, esto sí que nadie lo perdona;\
ya que tiene corona y no sombrero,\
fuera mejor usara su corona.\
\
-Los hombres, dijo el padre, son perversos\
pero más los poetas de hoy en día.\
Quizá te piense alimentar con versos,\
y eso vas a comer ¡pobre hija mía!\
\
-O, quién sabe, agregó con triste acento\
una visita, al parecer piadosa,\
si se irán a poblar el firmamento\
o a vivir en el cáliz de una rosa.\
\
-Puede ser, interrumpe otra persona,\
que intente levantar, llegado el caso,\
a orillas de la fuente de Helicona,\
un palacio en las faldas de Parnaso.\
\
El regalo de boda, amigo mío,\
tendrá joyas riquísimas y bellas\
junto a un collar de perlas del rocío,\
el manto azul del cielo y sus estrellas.\
\
Envidia te tendrán los serafines,\
pues tendrás, deleitando tu hermosura,\
una alfombra de nardos y jazmines\
y un ruiseñor que cante en la espesura.\
\
El marido feliz te dará un beso\
diciendo: ¡tengo un ángel por esposa!\
¿Y a la hora de comer? ¡quién piensa en eso!\
¡para el poeta la comida es prosa!\
\
Un coro de estridentes carcajadas\
satíricas, terribles, infernales,\
convirtió las mejillas en granadas\
al ángel de mis sueños celestiales.\
\
-¿Conque piensas seguir esos amores,\
tú, la más infeliz de las mujeres,\
piensas con el aroma de las flores\
vivir entre la dicha y los placeres?\
\
¿A qué alta sociedad, hija querida\
te llevará ese amor del cual abusas?\
¡Ha de ser muy monótona la vida,\
sin tener más visitas que las musas!\
\
Otra risa estalló ¡bendita risa!\
Entonces ella abandonó su asiento,\
y con grave ademán y muy de prisa\
salió, sin vacilar, del aposento.\
\
Llamáronla mil veces, pero ella,\
espléndida, graciosa, soberana,\
como asoma en los cielos una estrella\
el rostro fue a asomar a la ventana.\
\
-Ven, me dijo, mitad del alma mía.\
Dicen que amarte es prueba de torpeza,\
que por pobre te olvide ¡qué ironía!\
que te deje por pobre ¡qué tristeza!\
\
Como no te comprenden, ya por eso\
destruir mis amores se concilia.\
Yo siempre seré tuya: dame un beso;\
¡se ha lucido el consejo de familia!\
\
\
\
\
A Mis Hijas\
\
Mi tristeza es un mar; tiene su bruma \
que envuelve densa mis amargos días; \
sus olas son de lágrimas; mi pluma \
está empapada en ellas, hijas mías. \
\
Vosotras sois las inocentes flores \
nacidas de ese mar en la ribera;\
la sorda tempestad de mis dolores\
sirve de arrullo a vuestra edad primera. \
\
Nací para luchar; sereno y fuerte \
cobro vigor en el combate rudo;\
cuando pague mi audacia con la muerte, \
caeré cual gladiador sobre mi escudo. \
\
Llévenme así a vosotras; de los hombres \
ni desdeño el poder ni el odio temo; \
pongo todo mi honor en vuestros nombres \
y toda el alma en vuestro amor supremo. \
\
Para salir al mundo vais de prisa.\
¡Ojalá que esa vez nunca llegara!\
Pues hay que ahogar el llanto con la risa, \
para mirar al mundo cara a cara.\
\
No me imitéis a mí: yo me consuelo \
con abrir más los bordes de mi herida; \
imitad en lo noble a vuestro abuelo: \
¡Sol de virtud que iluminó mi vida!\
\
Orad y perdonad; siempre es inmensa \
después de la oración la interna calma, \
y el ser que sabe perdonar la ofensa \
sabe llevar a Dios. dentro del alma.\
\
Sea vuestro pecho de bondades nido, \
no ambicionéis lo que ninguno alcanza, \
coronad el perdón con el olvido\
y la austera virtud con la esperanza.\
\
Sin dar culto a los frívolos placeres \
que la pureza vuestra frente ciña, \
buscad alma de niña en las mujeres \
y buscad alma de ángel en la niña.\
\
Nadie nace a la infamia condenado, \
nadie hereda la culpa de un delito, \
nunca para ser siervas del pecado\
os disculpéis clamando: estaba escrito.\
\
¡Existir es luchar! No es infelice \
quien luchando, de espinas se corona; \
abajo, todo esfuerzo se maldice, \
arriba, toda culpa se perdona.\
\
Se apaga la ilusión cual lumbre fatua \
y la hermosura es flor que se marchita; \
la mujer sin piedad es una estatua \
dañosa al mundo y del hogar proscrita.\
\
No fijéis en el mal vuestras pupilas \
que víbora es el mal que todo enferma, \
y haced el bien para dormir tranquilas \
cuando yo triste en el sepulcro duerma.\
\
Nunca me han importado en este suelo \
renombre, aplausos, oropeles, gloria: \
procurar vuestro bien, tal es mi anhelo; \
amaros y sufrir tal es mi historia.\
\
Cuando el sol de mi vida tenga ocaso \
recordad mis consejos con ternura,\
y en cada pensamiento, en cada paso, \
buscad a Dios tras de la inmensa altura.\
\
Yo anhelo que, al morir, por premio santo,\
tengan de vuestro amor en los excesos:\
las flores de mi tumba vuestro llanto,\
las piedras de mi tumba vuestros besos. ",
                    path=u"/c", tags=u"JDP")

writer.add_document(title=u"Manuel Acuña", content=u"Ante un cadaver\
\
¡Y bien! aqui estás ya... sobre la plancha\
donde el gran horizonte de la ciencia\
la extensión de sus límites ensancha.\
Aqui donde la rígida experiencia\
viene a dictar las leyes superiores\
a que está sometida la existencia.\
Aquí donde derrama sus fulgores\
ese astro a cuya luz desaparece\
la distinción de esclavos y señores.\
Aquí donde la fábula enmudece\
y la voz de los hechos se levanta\
y la superstición se desvanece.\
Aquí donde la ciencia se adelanta\
a leer la solución de ese problema\
cuyo sólo enunciado nos espanta.\
Ella que tiene la razón por lema\
y que en tus labios escuchar ansía\
la augusta voz de la verdad suprema.\
Aquí está ya... tras de la lucha impía\
en que romper al cabo conseguiste\
la cárcel que al dolor te retenía.\
La luz de tus pupilas ya no existe,\
tu máquina vital descansa inerte\
y a cumplir con su objeto se resiste.\
¡Miseria y nada mas! dirán al verte\
los que creen que el imperio de la vida\
acaba donde empieza el de la muerte.\
Y suponiendo tu misión cumplida\
se acercarán a ti, y en su mirada\
te mandarán la eterna despedida.\
Pero, ¡no!... tu misión no está acabada,\
que ni es la nada el punto en que nacemos\
ni el punto en que morimos es la nada.\
Círculo es la existencia, y mal hacemos\
cuando al querer medirla le asignamos\
la cuna y el sepulcro por extremos.\
La madre es sólo el molde en que tomamos\
nuestra forma, la forma pasajera\
con que la ingrata vida atravesamos.\
Pero ni es esa forma la primera\
que nuestro ser reviste, ni tampoco\
será su última forma cuando muera.\
Tú sin aliento ya, dentro de poco\
volverás a la tierra y a su seno\
que es de la vida universal el foco.\
Y allí, a la vida en apariencia ajeno,\
el poder de la lluvia y del verano\
fecundará de gérmenes tu cieno.\
Y al ascender de la raíz al grano,\
irás del vergel a ser testigo\
en el laboratorio soberano;\
Tal vez, para volver cambiado en trigo\
al triste hogar donde la triste esposa\
sin encontrar un pan sueña contigo.\
En tanto que las grietas de tu fosa\
verán alzarse de su fondo abierto\
la larva convertida en mariposa;\
Que en los ensayos de su vuelo incierto\
irá al lecho infeliz de tus amores\
a llevarle tus ósculos de muerto.\
Y en medio de esos cambios interiores\
tu cráneo lleno de una nueva vida,\
en vez de pensamientos dará flores,\
en cuyo cáliz brillará escondida\
la lágrima tal vez con que tu amada\
acompañó el adiós de tu partida.\
La tumba es el final de la jornada,\
porque en la tumba es donde queda muerta\
la llama en nuestro espíritu encerrada.\
Pero en esa mansión a cuya puerta\
se extingue nuestro aliento, hay otro aliento\
que de nuevo a la vida nos despierta.\
Allí acaban la fuerza y el talento,\
allí acaban los goces y los males\
allí acaban la fe y el sentimiento.\
Allí acaban los lazos terrenales,\
y mezclados el sabio y el idiota\
se hunden en la región de los iguales.\
Pero allí donde el ánimo se agota\
y perece la máquina, alli mismo\
el ser que muere es otro ser que brota.\
El poderoso y fecundante abismo\
del antiguo organismo se apodera\
y forma y hace de él otro organismo.\
Abandona a la historia justiciera\
un nombre sin cuidarse, indiferente,\
de que ese nombre se eternice o muera.\
El recoge la masa únicamente,\
y cambiando las formas y el objeto\
se encarga de que viva eternamente;\
La tumba sólo guarda un esqueleto\
mas la vida en su bóveda mortuoria\
prosigue alimentándose en secreto.\
Que al fin de esta existencia transitoria\
a la que tanto nuestro afán se adhiere,\
la materia, inmortal como la gloria,\
cambia de formas; pero nunca muere.\
\
\
Un limosna\
A mi querido amigo A.F. Cuenca.\
\
¡Entrad!... en mi aposento\
donde sólo se ven sombras,\
está una mujer muriendo\
entre insufribles congojas...\
Y a su cabecera tristes\
dos niñas bellas que lloran,\
y que entrelazan sus manos\
y que gimen y sollozan.\
Y la infeliz ya no mira\
ni tiene aliento en la boca,\
y cuando habla sólo dice\
con voz hueca y espantosa:\
'¡Yo tengo hambre! ¡Yo tengo hambre!\
Por piedad ¡Una limosna!'\
Y calla... y las niñas gimen...\
y calla... y el viento sopla...\
y llora... y nadie la escucha,\
¡que nadie escucha al que llora!\
...........................................\
¿Y la oís? - ¡Ay!, hijas mías\
vanse por fin a quedar solas...\
solas... y sin una madre\
que os alivie y que os socorra...\
solas... y sin un mendrugo\
que llevar a vuestra boca...\
Adiós... adiós... ya me muero...\
ya no tengo hambre...\
y la mísera expiraba ¡'Una limosna'!\
entre angustias y congojas,\
mientras que las pobres niñas\
casi locas, casi locas\
la besaban y lloraban\
envueltas entre las sombras.\
Después... temblando de frío\
bajo sus rasgadas ropas,\
caminaban lentamente\
por la calle oscura y sola,\
exclamando con voz triste\
al divisar una forma;\
...'¡Me muero de hambre!'\
Y la otra...\
...¡'Una limosna'!\
\
Enero de 1869.\
\
Adiós a México\
\
Escrita para la Sra. Cayrón y leída por ella \
en una función de despedida.\
\
Pues que del destino en pos\
débil contra su cadena,\
frente al deber que lo ordena\
tengo que decirte adiós;\
\
Antes que mi boca se abra\
para dar paso a este acento,\
la voz de mi sentimiento\
quiere hablarte una palabra.\
\
Que muy bien pudiera ser\
que cuando de aquí me aleje,\
al decirte adiós, te deje \
para no volverte a ver.\
\
Y asi entre el mal con que lucho\
y y que en el dolor me abisma,\
quiero decirte yo misma,\
sepas que te quiero mucho.\
\
Que enamorada de tí\
desde antes de conocerte,\
yo vine sólo por verte,\
y al verte te puse aquí.\
\
Que mi alma reconocida\
te adora con loco empeño,\
porque tu amor era el sueño\
más hermoso de mi vida.\
\
Que del libro de mi historia\
te dejo la hoja mas bella,\
porque en esa hoja destella\
tu gloria más que mi gloria.\
\
Que soñaba en no dejarte\
sino hasta el poster momento,\
partiendo mi pensamiento\
entre tu amor y el del arte.\
\
Y que hoy ante esa ilusión\
que se borra y se deshace,\
siento ¡ay de mí! que se hace\
pedazos mi corazón...\
\
Tal vez ya nunca en mi anhelo\
podré endulzar mi tristeza\
con ver sobre mi cabeza\
el esplendor de tu cielo.\
\
Tal vez ya nunca a mi oído\
resonará en la mañana,\
la voz del ave temprana\
que canta desde su nido.\
\
Y tal vez en los amores\
con que te adoro y admiro\
estas flores que hoy aspiro\
serán las últimas flores...\
\
Pero si afectos tan tiernos\
quiere el destino que deje,\
y que me aparte y me aleje\
para no volver a vernos;\
\
Bajo la luz de este día\
de encanto inefable y puro\
al darte mi adiós te juro,\
¡oh dulce México mío!\
\
Que si él con sus fuerzas trunca\
todos los humanos lazos,\
te arrancará de mis brazos\
pero de mi pecho, nunca!\
\
\
Misterio\
\
Si tu alma pura es un broche\
que para abrirse a la vida\
quiere la calma adormecida\
de las sombras de la noche;\
\
Si buscas como un abrigo\
lo más tranquilo y espeso,\
para que tu alma y tu beso\
se encuentren sólo conmigo;\
\
Y si temiendo en tus huellas \
testigos de tus amores,\
no quieres ver más que flores,\
más que montañas y estrellas;\
\
Yo sé muchas grutas, y una\
donde podrás en tu anhelo,\
ver un pedazo de cielo\
cuando aparezca la luna.\
\
Donde a tu tímido oído\
no llegarán otros sones\
que las tranquilas canciones\
de algún ruiseñor perdido.\
\
Donde a tu mágico acento\
y estremecido y de hinojos,\
veré abrirse ante mis ojos\
los mundos del sentimiento.\
\
Y donde tu alma y la mía,\
como una sola estrechadas,\
se adormirán embriagdas\
de amor y melancolía.\
\
Ven a esta gruta y en ella\
yo te daré mis desvelos,\
hasta que se hunda en los cielos\
la luz de la última estrella.\
\
Y antes que el ave temprana\
su alegre vuelo levante\
y entre los álamos cante\
la vuelta de la mañana.\
\
Yo te volveré al abrigo\
de tu estancia encantadora,\
donde el recuerdo de esa hora\
vendrás a soñar conmigo...\
\
Mientras que yo en el exceso\
de la pasión que me inspiras\
iré a soñar que me miras,\
e iré a soñar que te beso.\
\
 \
\
Nada sobre nada\
\
Poesía leída en la velada literaria\
que celebró la Sociedad 'El Porvenir'\
la noche del 3 de mayo de 1873.\
Pues, señor, dije yo, ya que es preciso\
puesto que asi lo han dicho en el programa,\
que rompa ya la bendecida prosa\
que preparado para el caso había,\
y que escriba en vez de ella alguna cosa\
asi, que parezca poesía,\
pongámonos al punto, \
ya que es forzoso y necesario, en obra,\
sin preocuparnos mucho del asunto,\
porque al fin el asunto es lo que sobra.\
Así dije, y tomando\
no el arpa ni la lira\
que la lira y el arpa\
no pasan hoy de ser una mentira,\
sino una pluma de ave\
con la que escribo yo generalmente\
violenté las arrugas de mi frente\
hasta ponerla cejijunta y grave\
y pensando en mi novia, en la adorada\
por quien suspiro y lloro sin sosiego,\
mojé mi pluma en el tintero, y luego\
puse ocho letras: 'A mi amada.'\
Su retrato, un retrato\
firmado por Valleto y compañía,\
se alzaba junto a mi plácido y grato,\
mostrándome las gracias y recato\
que tanto adornan a la amada mía;\
y como el verlo sólo\
basta para que mi alma se emocione,\
que Apolo me perdone\
si, dije aqui que me sentí un Apolo.\
Ella no es una rosa\
ni un ser ideal, ni cosa que lo valga;\
pero en verso o en prosa\
no seré yo el estúpido que salga\
con que mi novia es fea,\
cuando puedo decir que es muy hermosa\
por más que ni ella misma me lo crea;\
así es que en mi pintura\
hecha en rasgos por cierto no muy fieles,\
aumenté de tal modo su hermosura\
que casi resultaba una figura\
digna de ser pintada por Apeles.\
Después de dibujarla como he dicho,\
faltando a la verdad por el capricho,\
iba yo a colocar el fondo negro\
de su alma inexorable y desdeñosa,\
cuando al hacerlo me ocurrió una cosa\
que hundió mi plan, y de lo cual me alegro;\
porque, en último caso,\
como pensaba yo entre las paredes\
de mi cuarto sombrío,\
¿qué les importa a ustedes\
que mi amada me niegue sus mercedes,\
ni que yo tenga el corazón vacío?\
Si mi vida vegeta en la tristeza\
y el yugo del dolor ya no soporta,\
caeré de referirlo en la simpleza\
para que alguien me diga en su franqueza:\
¡'¿si viera usted que a mi nada me importa?...'!\
No, de seguro, que antes\
prefiero verme loco por tres días,\
que imitar a ese eterno Jeremías\
que se llama el señor de Cervantes.\
Y convencido de esto,\
ya que era conveniente y necesario,\
borré el título puesto,\
y buscando a mi lira otro pretexto\
escrbí este otro título: El Santuario.\
¡El santuario!... exclamé; pero y ¿qué cosa\
puedo decir de nuevo sobre el caso,\
cuando en cada volumen de poesías,\
en versos unos malos y otros buenos,\
sobre templos, santuarios y abadías?\
Para entonar sobre esto mis cantares,\
a mas de que el asunto vale poco,\
¿Qué entiendo yo de claustros ni de altares,\
ni qué se yo de sacristán tampoco?\
No, en la naturaleza\
hay asuntos mas dignos y mejores,\
y mas llenos de encantos y de belleza,\
y que he de escribir, haré una pieza\
que se llame: Los prados y las flores.\
Hablaré de la incauta mariposa\
que en incesante y atrevido vuelo,\
ya abandona el cielo por la rosa;\
ya abandona la rosa por el cielo,\
del insecto pintado y sorprendente\
que de esconderse entre las hierbas trata,\
y de el ave inocente que lo mata,\
lo cual prueba que no es tan inocente;\
hablaré... pero y luego que haya hablado\
sacando a luz el boquirrubio Febo,\
me pregunto, señor, ¿qué habré ganado,\
si al hacerlo no digo nada nuevo?...\
Con que si esto tampoco es un asunto\
digno de preocuparme una sola hora,\
dejemos sus inútiles detalles,\
ya que no hay ni un señor ni una señora\
que no sepa muy bien lo que es la aurora\
y lo que son las flores y los valles...\
Coloquemos a un lado estas materias\
que valen tan poco para el caso,\
y pues esto se ofrece a cada paso\
hablemos de la vida y sus miserias.\
Empezaré diciendo desde luego,\
que no hay virtud, creencias ni ilusiones;\
que en criminal y estúpido sosiego\
ya no late la fe en los corazones;\
que el hombre imbécil, a la gloria ciego,\
sólo piensa en el oro y los doblones,\
y concluiré en estilo gemebundo:\
¡Que haya un cadáver mas que importa al mundo!\
Y me puse a escribir, y asi en efecto,\
lo hice en ciento cincuenta octavas reales,\
cuyo único defecto,\
como se ve por lo que dicho queda,\
era que en vez de ser originales\
no pasaba de un plagio de Espronceda.\
Como era fuerza, las rompí en el acto\
desesperado de mi triste suerte,\
viendo por fin que en esto de poesía\
no hay un solo argumento ni una idea\
que no peque de fútil, o no sea\
tan vieja como el pan de cada día.\
En situación tan triste\
y estando la hora ya tan avanzada,\
¿qué hago, dije yo, para salvarme\
de este grave y horrible compromiso,\
cuando ningún asunto puede darme \
ni siquiera un adarme\
de novedad, de encanto, o de un hechizo?\
¿Hablaré de la guerra y de la gente\
que enardecida de las cumbres baja\
desafiando al contrario frente a frente,\
y habré de convertirme en un valiente\
yo que nunca he empuñado una navaja?\
No, señor, aunque estudio medicina\
y pertenezco a esa importante clase\
que no hay pueblo y lugar en donde no pase\
por ser la mas horrible y asesina,\
aparte de que en esto hay poco cierto,\
como lo prueba y mucho la experiencia,\
yo, a lo menos hasta hoy, me hallo a cubierto\
de que se alce la sombra de algún muerto\
a turbar la quietud de mi conciencia.\
Sobre los libros santos, se podría\
con meditar y con plagiar un poco,\
arreglar o escribir una poesía;\
pero ni esto es muy fácil en un día\
ni para hablar sobre esto estoy tampoco;\
porque en fiestas como esta\
donde el saber está en su templo,\
salir con el Diluvio, por ejemplo,\
fuera casi querer aguar la fiesta;\
y como yo no quiero que se diga \
que he venido a tal cosa,\
ya que en mi numen agotado me hallo\
el asunto y el plan a que yo aspiro\
rompo mi humilde cítara, me callo,\
y con perdón de ustedes me retiro.\
\
\
Un Sueño\
\
A Ch....\
¿Quieres oir un sueño?...\
Pues anoche\
ví la brisa fugaz de la espesura\
que al rozar con el broche\
de un lirio que se alzaba en la pradera\
grabó sobre él un 'beso',\
perdiéndose después rauda y ligera\
de la enramada entre el follaje espeso.\
Este es mi sueño todo,\
y si entenderlo quieres, niña bella,\
une tus labios en los labios míos\
y sabrás quién es 'él' y quien es 'ella'.\
\
\
AMOR\
¡Amar a una mujer, sentir su aliento,\
y escuchar a su lado\
lo dulce y armonioso de su acento;\
tener su boca a nuestra boca unida\
y su cuello en el nuestro reclinado,\
es el placer mas grato de la vida,\
el goce mas profundo\
que puede disfrutarse sobre el mundo!\
Porque el amor al hombre es tan preciso,\
como el agua a las flores,\
como el querube ardiente al paraíso;\
es el prisma de mágicos colores\
que transforma y convierte\
las espinas en rosas,\
y que hace bella hasta la misma muerte\
a pesar de sus formas espantosas.\
Amando a una mujer, olvida el hombre\
hasta su misma esencia,\
sus deberes mas santos y su nombre;\
no cambia por el cielo su existencia;\
y con su afán y su delirio, loco,\
acaricia sonriendo su creencia,\
y el mundo entero le parece poco...\
Quitadle al zenzontle la armonia,\
y al águila su vuelo,\
y al iluminar espléndido del día\
el azul pabellón del ancho cielo,\
y el mundo seguirá... Mas la criatura,\
del amor separada\
morirá como muere marchitada\
la rosa blanca y pura\
que el huracán feroz deja tronchada;\
como muere la nube y se deshace\
en perlas cristalinas\
cuando le hace falta un sol que la sostenga\
en la etérea región de las ondinas.\
¡Amor es Dios!, a su divino fiat\
brotó la tierra con sus gayas flores\
y sus selvas pobladas\
de abejas y de pájaros cantores,\
y con sus blancas y espumosas fuentes\
y sus limpias cascadas\
cayendo entre las rocas a torrentes;\
brotó sin canto ni armonía...\
Hasta que el beso puro de Adán y Eva,\
resonando en el viento,\
enseñó a las criaturas ese idioma,\
ese acento magnífico y sublime\
con que suspira el cisne cuando canta\
y la tórtola dulce cuando gime,\
¡Amor es Dios!, y la mujer la forma\
en que encarna su espíritu fecundo;\
él es el astro y ella su reflejo,\
él es el paraíso y ella el mundo...\
Y vivir es amar. A quien no ha sentido\
latir el corazón dentro del pecho\
del amor al impulso,\
no comprende las quejas de la brisa\
que vaga entre los lirios de la loma,\
ni de la virgen casta la sonrisa\
ni el suspiro fugaz de la paloma.\
¡Existir es amar! Quien no comprende\
esa emoción dulcisima y suave,\
esa tierna fusión de dos criaturas\
gimiendo en un gemido,\
en un goce gozando\
y latiendo en unísono latido...\
Quien no comprende ese placer supremo,\
purísimo y sonriente,\
ese miente si dice que ha vivido;\
si dice que ha gozado, miente.\
Y el amor no es el goce de un instante\
que en su lecho de seda\
nos brinda la ramera palpitante;\
no es el deleite impuro\
que hallamos al brillar una moneda\
del cieno y de la infamia entre lo oscuro;\
no es la miel que provoca\
y que deja, después que la apuramos,\
amargura en el alma y en la boca...\
Pureza y armonía,\
ángeles bellos y hadas primorosas\
en un Edén de luz y de poesía,\
en un pensil de nardos y de rosas,\
Todo es el amor.\
Mundo en que nadie\
llora o suspira sin hallar un eco;\
fanal de bienandanza\
que hace que siempre ante los ojos radie\
la viva claridad de una esperanza.\
El amor es la gloria,\
la corona esplendente\
con que sueña el genio de alma grande\
que pulsa el arpa o el acero blande,\
la virgen sonriente. \
El Petrarca sin Laura,\
no fuera el vate del sentido canto\
que hace brotar suspiros en el pecho \
y en la pupila llanto.\
Y el Dante sin Beatriz no fuera el poeta\
a veces dulce y tierno,\
y a veces grande, aterrador y ronco\
como el cantor salido del infierno...\
Y es que el amor encierra\
en su forma infinita\
cuanto de bello el universo habita,\
cuanto existe de ideal sobre la tierra.\
Amor es Dios, el lazo que mantiene\
en constante armonía\
los seres mil de la creación inmensa;\
y la mujer la diosa,\
la encarnación sublime y sacrosanta\
que la pradera con su olor inciensa\
y que la orquesta del Supremo canta,\
¡Y salve, amor! emanación divina...\
...¡Tú, más blanca y más pura\
que la luz de la estrella matutina!\
¡Salve, soplo de Dios!...\
Y cuando mi alma\
deje de ser un templo a la hermosura,\
ven a arrancarme el corazón del pecho\
ven a abrir a mis pies la sepultura\
\
Enero de 1869.\
\
Pobre flor\
\
-¿Por qué te miro así tan abatida,\
pobre flor?\
¿En dónde están las galas de tu vida\
y el color?\
Díme, ¿por qué tan triste te consumes,\
dulce bien?\
¿Quién?, ¡el delirio devorante y loco\
de un amor,\
que me fue consumiendo poco a poco\
de dolor!\
Porque amando con toda la ternura\
de la fe\
a mí no quiso amarme la criatura\
que yo amé\
Y por eso sin galas me marchito\
triste aquí,\
siempre llorando en mi dolor maldito,\
¡Siempre así!\
¡Habló la flor!...\
Yo gemí... era igual a la memoria \
de mi amor.\
\
Cabrío, febrero de 1969\
\
La ramera\
\
A mi querido amigo Manuel Roa.\
Humanidad pigmea,\
tú que proclamas la verdad y el Cristo,\
mintiendo caridad en cada idea:\
tú que, de orgullo el corazón beodo,\
por mirar a la altura \
te olvidas de que marchas sobre lodo:\
tú que diciendo hermano,\
escupes al gitano y al mendigo\
porque son un mendigo y un gitano:\
Ahí está esa mujer que gime y sufre\
con el dolor inmenso con que gimen\
los que cruzan sin fe por la existencia;\
escúpela tambien... ¡anda!... ¡no importa\
que tú hayas sido quien la hundió en el crimen\
que tú hayas sido quien mató su creencia!\
¡Pobre mujer! que abandonada y sola\
sobre el oscuro y negro precipicio,\
en lugar de una mano que la salve\
siente una mano que la impele al vicio;\
y que al bajar en su redor los ojos\
y a través de las sombras que la ocultan\
no encuentra mas que seres que la miran\
y que burlando su dolor la insultan...\
Antes era una flor... una azucena\
rica de galas y de esencias rica,\
llena de aromas y de encantos llena;\
era una flor hermosa\
que envidiaban las aves y las flores,\
y tan bella y tan pura\
como es pura la nieve del armiño,\
como es pura la flor de los amores,\
como es puro el corazón del niño.\
Las brisas le brindaban con sus besos,\
y con sus tibias perlas el rocío,\
y el bosque con sus álamos espesos,\
y con su arena y su corriente el río;\
y amada por las sombras en la noche,\
y amada por la luz en la mañana,\
vegetaba magnífica y lozana,\
tendiendo al aire su purpúreo broche;\
pero una vez el soplo del invierno\
en su furia maldita,\
pasó sobre ella y le arrancó sus hojas,\
pasó sobre ella y la dejó marchita;\
y al contemplar sin galas\
su cálice antes de perfumes lleno,\
la arrebató impaciente entre sus alas\
y fue a hundirla cadáver en el cieno.\
¡Filósofo mentido!...\
¡Apóstol miserable de una idea\
que tu cerebro vil no ha comprendido!\
Tú que la ves que gime y que solloza,\
y burlas su sollozo y su gemido...\
¿Qué hiciste de aquel ángel\
que amoroso y sonriente\
formó de tu niñez el dulce encanto!\
¿Qué hiciste de aquel ángel de otros días,\
que lloraba contigo si llorabas\
y gozaba contigo si reías...?\
¡Te acuerdas!... Lo arrancaste de la nube\
donde flotaba vaporoso y bello,\
y arrojándola al hambre,\
sin ver su angustia ni su amor siquiera,\
le convertiste de camelia en lodo:\
le transformaste de ángel en ramera!\
¡Maldito tú que pasas\
junto a las frescas rosas,\
y que sus galas sin piedad les quitas!\
¡Maldito tú que sin piedad las hieres,\
y luego las insultas por marchitas!\
¡Pobre mujer!... ¡Juguete miserable\
de su verdugo mismo!...\
Víctima condenada\
a vegetar sumida en un abismo\
mas negro que el abismo de la nada\
y a no escuchar mas eco en sus dolores,\
que el eco de la horrible carcajada\
con que el hombre le paga sus amores.\
¡Pobre mujer, a la que el hombre niega\
el derecho sublime\
de llamar hijo a su hijo!\
¡Pobre mujer que de rubor se cubre\
cuando escucha que le grita madre!\
Y que quiere besarle, y se detiene,\
porque sabe que un beso de sus besos\
se convierte en borrón donde lo imprime!\
Deja ya de llorar, pobre criatura,\
que si del mundo en la escabrosa senda,\
caminas entre fango y amargura,\
sin encontrar un ser que te comprenda,\
en el cielo los ángeles te miran,\
te compadecen, te aman,\
y lloran con el llanto lastimero\
que tus ojos bellísimos derraman.\
¡Y que se burle el hombre, y que se ría!\
¡Y que te llame harapo y te desprecie!\
Déjale tú reír, y que te insulte,\
Que ha de llegar el día\
en que la gota cristalina y pura\
se desprenda del lodo\
para elevarse nube hasta la altura.\
Y entonces en lugar de un anatema,\
en lugar de un desprecio,\
escucharás al Cristo del Calvario,\
que añadiendo tu pena\
a tus lágrimas tristes en abono\
te dirá como ha tiempo a Magdalena:\
Levántate, mujer, yo te perdono.\
\
\
Lágrimas \
\
Quum subit illius tristissima noctis imago\
quae mihi supremum tempus in urbe fuit;\
quum respeto noctem qui a tot mihi cara reliquie\
labitur es oculis nuc quoque gutta meis.\
OVIDIO.-ELEGÍ AS III.\
Aún era you muy niño, cuando un día,\
cogiendo mi cabeza entre sus manos\
y llorando a la vez que me veía\
'¡Adiós! ¡Adiós!' me dijo;\
'desde este instante un horizonte nuevo\
se presenta a tus ojos;\
vas a buscar la fuente \
donde apagar la sed que te devora;\
marcha... y cuando mañana\
al mal que aún no conoces\
ofrezca de tu llanto las primicias,\
ten valor y esperanza,\
anima el paso tardo,\
y mientras llega de tu vuelta la hora,\
ama un poco a tu padre que te adora,\
y ten valor y ... marcha... yo te aguardo'.\
Asi me dijo, y confundiendo en uno\
su sollozo y el mío,\
me dio un beso en la frente...\
sus brazos me estrecharon...\
y despues a los pálidos reflejos\
del sol que en el crepúsculo se hundía\
sólo vi una ciudad que se perdía\
con mi cuna y mis padres a lo lejos.\
El viento de la noche\
saturado de arrullos y de esencias,\
soplaba en mi redor, tranquilo y dulce\
como aliento de niño;\
tal vez llevando en sus ligeras alas\
con la tibia embriaguez de sus aromas,\
el acento fugaz y enamorado\
del silencioso beso de mi madre\
sobre el blanco lecho abandonado...\
Las campanas distantes repetían\
el toque de oraciones... una estrella\
apareció en el seno de una nube;\
tras de mi oscura huella \
la inmensidad se alzaba...\
y haciendo estremecer el infinito\
de mi dolor supremo con el grito;\
'¡Adiós, mi santo hogar', clamé llorando,\
'¡Adiós, hogar bendito,!\
en cuyo seno viven los recuerdos\
más queridos de mi alma...\
pedazo de ese azul en donde anidan\
mis ilusiones cándidas de niño...\
¡Quién sabe si mis ojos\
no volveran a verte!...\
¡Quién sabe si hoy te envío\
el adiós de la muerte!...\
Mas si el destino rudo\
ha de darme el morir bajo tu techo,\
si el ave de la selva\
ha de plegar las alas en su nido,\
¡guárdame mi tesoro, hogar querido,\
guárdame mi tesoro hasta que vuelva!'\
Las lágrimas brotaron\
a mis hinchados párpados... las sombras\
espesas y agrupadas de repente\
se abrieron de los astros a la huella...\
cruzó una luz por lo alto, alcé la frente,\
el cielo era una página y en ella\
ví esta cifra -¡Detente!\
Detente... y a mi oído\
llegó como un arrullo de paloma\
la nota de un gemido;\
algo como un suspiro de la noche\
rompiendo del silencio la honda calma;\
algo como la queja\
algo como el adiós con que los muertos,\
del amor al esfuerzo soberano,\
saludan desde el fondo de sus tumbas\
al recuerdo lejano.\
...........................................\
Al despertar de aquel supremo instante\
de letargo sombrío\
la noche de la ausencia desplegaba\
su impenetrable velo,\
sus sombras sin estrellas,\
su atmósfera de hielo...\
esa odiosa ceguez en que el ausente\
proscrito del cariño\
cumple con su destierro, suspirando\
por sus recuerdos vírgenes de niño;\
ese inmenso dolor que hace del alma\
en el terrible y solitario viaje,\
un árido desierto\
en donde es un miraje cada punto\
y en donde es un amor cada miraje...\
Y así de la ampolleta de mi vida\
se deslizaban las eternas horas\
sobre mi frente mustia y abatida,\
soñando al extenderse en lontananza,\
como una dulce estrofa desprendida\
del arpa celestial de la esperanza;\
así, cuando una vez, en el instante\
en que la blanca flor de mi delirio\
desplegaba en los aires su capullo;\
cuando mi muerta fe se estremecía\
bajo sus ropas fúnebres del duelo\
al ver flotando en el azul del cielo\
el alma de mi hogar sobre la mía;\
cuando iba ya a sonar para mis ojos\
la última hora de llanto,\
y se cambiaba en música de salve\
la música elegíaca de mi canto;\
mi corazón como la flor marchita\
que se abre a las sonrisas de la aurora\
esperando la vida de sus rayos\
también se abrió... para plegar su broche,\
y las caricias del amor abierto,\
encerrando en el fondo de su noche\
¡las caricias de un muerto!...\
En el espacio blanco y encendido\
por los trémulos rayos de la luna\
yo vi asomar su sombra...\
La gasa del sepulcro lo envolvía\
con sus espesos pliegues...\
En su frente espectral se dibujaba \
una aureola de angustia, lo que dijo\
se perdió en la región donde flotaba...\
su mano me bendijo...\
su pecho sollozaba...\
La sombra se elevó como la niebla\
que en la mañana se alza de los campos;\
cerró los ojos, supirando y luego...\
oí un adiós en la profunda calma\
de aquella inmensidad muda y tranquila,\
y al levantar de nuevo la pupila\
¡el cielo estaba negro como mi alma!\
En el reloj terrible \
donde cada dolor marca su instante,\
el destino inflexible\
señalaba la cifra palpitante\
de aquella hora imposible;\
hora triste en que el íntimo santuario\
de mis sueños de gloria,\
vio su altar solitario,\
convertido su sol en tenebrario,\
y su culto en memoria...\
Hora negra en que la urna consagrada\
para envolverlo, ¡oh, padre!\
del cariño en la esencia perfumada,\
fue un sepulcro sombrío\
donde sólo dejaste tu recuerdo\
para hacer más inmenso su vacío.\
¡Padre... perdón porque te amaba tanto,\
que en el orgullo de mi amor creía\
darte en él un escudo!\
¡Perdón porque luché contra la suerte,\
y desprenderme de tus lazos pudo!\
¡Perdón porque a tu muerte\
le arrebaté mis últimas caricias\
y te dejé morir sin que rompiendo\
mi alma los densos nublos de la ausencia,\
fuera a unirse en un beso con la tuya\
y a escuchar tu postrera confidencia!\
Sobre la blanca cuna en que de niño\
me adurmieron los cantos de la noche,\
el cielo azul flotaba, \
y siempre que mis párpados se abrían,\
hallé en ese cielo dos estrellas\
que al verme desde allí se sonreían;\
mañana que mis ojos \
se alcen de nuevo hacia el espacio umbrío\
que se mece fugaz sobre mi cuna,\
tú sabes, padre mío,\
que sobre aquella cuna hay un vacío,\
de esas dos estrellas falta una.\
Caiste... de los libros de la noche\
yo no tengo la ciencia ni la clave;\
en la tumba en que duermes\
yo no sé si el amor tiene cabida...\
yo no sé si el sepulcro\
puede amar a la vida;\
pero en la densa oscuridad que envuelve\
mi corazón para sufrir cobarde,\
yo sé que existe el germen de una hoguera\
que a tu memoria se estremece y arde...\
yo sé que es el más dulce de los nombres\
el nombre que te doy cuando te llamo,\
y que en la religión de mis recuerdos\
tú eres el dios que amo.\
Caíste de tu abismo empenetrable\
la helada niebla arroja\
su negra proyección sobre mi frente,\
crepúsculo que avanza\
derramando en el aire transparente,\
las sombras de una noche sin oriente\
y el capuz de un dolor sin esperanza.\
Padre... duérmete... mi alma estremecida\
te manda su cantar y sus adioses;\
vuela hacia ti, y flotando\
sobre la piedra fúnebre que sella\
tu huesa solitaria,\
mi amor la enciende, y sobre ti, sobre ella\
en la noche sin fin de tu sepulcro\
mi alma será una estrella.\
\
\
El reo a muerte\
\
Al eminente actor D. José Valero\
Esa noche, ardiendo el pueblo\
de animación y entusiasmo\
bajo el influjo sublime\
de tu genio soberano,\
todo era bravos y dianas,\
todo era vivas y aplausos,\
todo cariño en los ojos \
todo cariño en los labios,\
y todo flores, laureles,\
admiración y ... entretanto,\
allá muy lejos, muy lejos,\
sonando lento y pausado,\
se alzaba entre las tinieblas\
y entre el silencio un cadalso,\
sin otro eco que el latido\
del pecho del condenado\
que en diálogo con la muerte\
velaba en un subterraneo.\
aquel cadalso se alzaba\
cada vez más y más alto,\
como un espectro, sombrío\
como un vampiro, callado,\
como una tumba implacable,\
y como un monstruo, inhumano;\
se alzaba y, sin que ninguno\
oyera aquel ruido amargo,\
por los sollozos de un hombre\
solamente acompañado,\
la humanidad impasible\
bajo su mudo letargo, \
miraba crecer y alzarse\
las formas de aquel cadalso,\
cuando tú, tú que escuchaste\
sus ecos tristes y vagos\
te levantaste por ella\
con la voz del entusiasmo,\
y en presencia de aquel pueblo\
y enfrente de aquel tablado\
ceñida con tus laureles\
la hiciste hablar por tus labios,\
salvando al sol de aquel día\
del rubor de aquel cadalso.\
* * *\
Aquel que es su desamparo,\
y aún más que unos pocos días\
y aún más que unos pocos años\
pudo gozar la dulzura\
de ver a su hijo en los brazos,\
libre del infame nombre\
de hijo del ajusticiado;\
pero yo que desde niño\
aprendí lleno de espanto\
a aborrecer los verdugos\
y a maldecir los cadalsos\
dejo a la gloria que entonces\
para ensalzarte su canto,\
y del condenado a muerte\
bajo los recuerdos gratos,\
en nombre suyo, las gracias\
de la humanidad te mando.\
\
\
Oda\
\
Leida en la sesión que el Liceo Hidalgo\
celebró en honor de Doña Gertrudis Gómez de Avellaneda.\
De los tres cielos que recorre el hombre\
de la existencia en la medida impía,\
cuando la gloria me enseñó tu nombre\
yo estaba en el primero todavía.\
La pena que del pecho\
hasta el abismo lóbrego desciende,\
y del cadáver de un amor deshecho\
finge flotando en derredor del lecho\
la aparición bellísima de un duende;\
la sombra a cuyo peso aborrecido\
muere el placer y el alma se acobarda,\
tratando de evocar en el olvido\
el recuerdo dulcísimo y querido\
de los besos del ángel de la guarda;\
todo eso que en la frente \
deja un sello de luto y desconsuelo,\
cuando en el alma pálida y doliente\
no queda ni la fe que es del creyente\
la última golondrina que alza el vuelo\
todo eso que de noche\
baja hasta el corazón como una sombra,\
y que terrible y sin piedad ninguna\
sus ilusiones todas despedaza,\
aún no era sobre el cielo de mi cuna.\
Ni la pálida nube que importuna\
se levanta enseñando la amenaza.\
Dichoso con la dulce indiferencia\
del que al amor de su callado asilo\
ha vivido a la luz de la inocencia,\
acostumbrado a ver en la existencia\
la imagen de un azul siempre tranquilo,\
yo entonces ignoraba\
que, más alla de aquel humilde techo\
que sus caricias y su amor me daba,\
clamando al cielo y suspirando en vano\
desde el rincón sin luz de la vigilia,\
hubiera en otro hogar una familia\
de la que yo también era un hermano...\
Mi amor no sospechaba que existiera\
más ilusion ni cariñoso exceso\
que la mirada dulce y hechicera\
de la santa mujer que la primera \
nos anuncia a la vida con un beso...\
Y hasta que al ducle y mágico sonido\
del arpa que temblaba entre tus manos,\
dejé mi rama, abandoné mi nido\
y te segué hasta ese árbol bendecido\
donde todos los nidos son hermanos,\
fue cuando despertando de la calma\
en que flotaba la existencia mía,\
sentí asomar en lo íntimo de mi alma\
algo como la luz de un nuevo día.\
Tu voz fue la primera\
que me habló en la dulzura de ese idioma\
que canta como canta la paloma\
y gime como gime la palmera...\
las cuerdas de tu lira,\
como la voz de la primera alondra\
que llama a las demás y las despierta,\
fueron las que al arrullo de tu acento\
sonaron sobre mi alma estremecida,\
como si siendo un pájaro la vida\
quisieran despertarlo al sentimiento...\
Tu nombre va ligado en mi cariño\
con los recuerdos santos y amorosos\
de mis tiempos de niño,\
con los placeres dulces y sabrosos\
de esa época sonriente\
en la que es cada instante una promesa\
y en la que el ángel de la fe aún no besa\
las primeras arrugas de la frente;\
tu nombre es la memoria\
del pueblo y del hogar adonde un día\
fue a estremecerse el eco de tu gloria\
y el trino arrullador de tu poesía;\
la evocación de todo lo más santo\
en medio de mis noches desmayadas,\
que aún tiemblan a las dulces campanadas,\
de aquellas horas en que amaba tanto...\
Y así, cuando yo supe\
que abandonada a tu dolor morías,\
y que en tu muda y lánguida tristeza\
renunciabas a ver junto a tu lecho,\
quien, al rodar sin vida tu cabeza,\
recogiera el laurel de tu grandeza\
y el último sollozo de tu pecho;\
cuando yo supe que en la huesa insana\
te inclinabas por fin pálida y sola,\
sin que el adiós de tu alma soberana\
se enlutara la cítara cubana\
ni gimiera la cítara española;\
al darte mis adioses, los adioses\
de la eterna y postrera despedida,\
sentí que algo de triste sollozaba\
de mi dolor en el oscuro abismo,\
y que tu sombra que flotaba arriba,\
al extinguirse y al borrarse iba\
llevándose un pedazo de sí mismo,\
y entonces al poder de los recuerdos\
borrando la distancia\
tendí mis alas hacia el nido blando\
de los primeros sueños de la infancia;\
llegué al rincón modesto\
donde tus dulces páginas leía\
a la fe y al amor siempre dispuesto\
y allí de pie frente a la blanca cuna\
donde en sus flores me envolvió el destino,\
busqué en su fondo alguna\
que aún no cerrara su oloroso broche,\
y en él hallé dormida,\
ésta con la que el alma agradecida\
viene a aromar las sombras de la noche.\
Deuda en mi cariño\
contraje desde niño con tu nombre,\
esa flor es el cántico del niño\
mezclada con las lágrimas del hombre;\
esta flor es el fruto de aquel germen\
que derramaste en mi niñez dichosa,\
y que al rodar sobre la humilde fosa\
donde tus restos duermen\
entre sus piedras ásperas se arraiga\
recogiendo su jugo en tus cenizas,\
y esperando en su cáliz a que caiga\
la gota de los cielos que le traiga\
la esencia y el amor de tus sonrisas.\
\
\
A un arroyo\
\
A mi hermano Juan de Dios Peza.\
Cuando todo era flores tu camino,\
cuando todo era pájaros tu ambiente,\
cediendo de tu curso a la pendiente\
todo era en ti fugaz y repentino.\
Vino el invierno con sus nieblas vino\
el hielo que hoy estanca tu corriente,\
y en situación tan triste y diferente\
ni aún un pálido sol te da el destino.\
Y así en la vida el incesante vuelo\
mientras que todo es ilusión, avanza\
en sólo una hora cuanto mide un cielo;\
Y cuando el duelo asoma en lontananza\
entonces como tú cambiada en hielo\
no puede reflejar ni la esperanza.\
\
\
\
Soneto\
\
Porqué dejaste el mundo de dolores\
buscando en otro cielo la alegría\
que aquí, si nace, sólo dura un día\
y eso entre sombras, dudas y temores.\
\
Porqué en pos de otro mundo y de otras flores\
abandonaste esta región sombría,\
donde tu alma gigante se sentía\
condenada a continuos sinsabores.\
\
Yo vengo a decir mi enhorabuena\
al mandarte la eterna despedida\
que de dolor el corazón me llena;\
\
Que aunque cruel y muy triste tu partida,\
si la vida a los goces es ajena,\
mejor es el sepulcro que la vida.\
\
\
A asunción\
\
\
Mire usted, Asunción: aunque algún ángel\
metiéndose envidioso,\
conciba allá en el cielo el mal capricho\
de venir por la noche a hacerle el oso\
y en un acto glorioso\
llevársela de aquí, como le ha dicho\
no sé que nigromante misterioso,\
no vaya usted, por Dios, a hacerle caso,\
ni a dar con el tal ángel un mal paso;\
estése usted dormida,\
debajo de las sábanas metida,\
y deje usted que la hable\
y que la vuelva a hablar y que se endiable,\
que entonces con un dedo\
puesto sobre otro en cruz, ¡afuera miedo!\
No vaya usté a rendirse\
ante el ruego o las lágrimas y a irse. . .\
que donde usted nos deje\
por seguir en el vuelo a su Tenorio,\
después irá a llorar al purgatorio\
sin tener quien la mime, aunque se queje. . .\
Conque mucho cuidado\
si siente usted un ángel a su lado,\
que yo, como su amigo,\
con tal que usted, Asunción, me lo permita,\
le aconsejo y le digo\
que después de Rosario y Margarita\
no admita usted más ángeles consigo.\
Estése usted con ellas\
compartiendo delicias e ilusiones\
todas las horas tienen que ser bellas;\
viva usted muchos años\
(como un humilde criado le diría)\
y mañana que sola o entre extraños\
se encuentre por desgracia en este día,\
si busca usted una alma que la ame,\
llame usted a mi pecho, y con que llame,\
si no estoy muerto encontrará la mía.\
\
\
A Ch...\
\
Si supieras, niña ingrata,\
lo que mi pecho te adora;\
si supieras que me mata\
la pasión que por ti abrigo;\
tal vez, niña encantadora,\
no fueras tan cruel conmigo.\
\
Si supieras que del alma\
con tu desdén ha volado\
fugaz y triste la calma,\
y que te amo más mil veces,\
que las violetas al prado\
y que a los mares los peces;\
\
tal vez entonces, hermosa,\
oyeras el triste acento\
de mi querella amorosa;\
y atendiendo a mi reclamo,\
mitigaras mi tormento\
con un beso y un 'yo te amo'.\
\
Si supieras, dulce dueño,\
que tú eres del alma mía\
el sólo y único sueño;\
y que al mirar tus enojos,\
la ruda melancolía\
baña en lágrimas mis ojos;\
\
tal vez entonces me amaras,\
y con tus labios de niño\
mis labios secos besaras;\
y cariñosa y sonriente\
a mi constante cariño\
no fueras indiferente.\
\
Ámame, pues, niña pura\
ya que has oído el acento\
del que idolatrarte jura;\
y atendiendo a mi reclamo,\
ven y calma mi tormento\
con un beso y un 'yo te amo'.\
\
\
A la patria\
\
\
Composición recitada por una niña\
en Tacubaya de los Mártires,\
el 11 de septiembre de 1873.\
\
Ante el recuerdo bendito\
de aquella noche sagrada\
en que la patria aherrojada\
rompió al fin su esclavitud;\
ante la dulce memoria\
de aquella hora y de aquel día,\
yo siento que en el alma mía\
canta algo como un láud.\
\
Yo siento que brota en flores\
el huerto de mi ternura,\
que tiembla entre su espesura\
la estrofa de una canción;\
y al sonoroso y ardiente\
murmurar de cada nota,\
siendo algo grande que brota\
dentro de mi corazón.\
\
¡Bendita noche de gloria\
que así mi espíritu agitas,\
bendita entre benditas\
noche de la libertad!\
Hora del triunfo en que el pueblo\
vio al fin en su omnipotencia,\
al sol de la independencia\
rompiendo la oscuridad.\
\
Yo te amo. . . y al acercarme\
ante este altar de victoria\
donde la patria y la historia\
contemplan nuestro placer,\
yo vengo a unir al tributo\
que en darte el pueblo se afana\
mi canto de mexicana,\
mi corazón de mujer.\
\
\
\
El giro\
\
Romancero de la Guerra de Independencia\
\
I\
\
Medio oculta entre la selva\
como un nido entre las ramas,\
y medio hundido en el fondo\
tranquilo de una cañada,\
allá por aquellos tiempos\
hubo en Landín una casa\
que no por ser tan sencilla\
ni de un fecha tan larga,\
era menos pintoresca,\
ni tampoco menos blanca.\
Sombreaba su puerta un olmo\
de hojosas y verdes ramas,\
punto de citas de todas\
las aves de las montañas;\
y en uno de sus costados,\
brotando límpida y clara,\
estaba entre los terrones\
y entre las hierbas el agua,\
de noche siempre tranquila\
y eternamente callada.\
Apenas el sol naciente\
filtraba por sus ventanas,\
cuando estremeciendo el aire,\
sonaban dulces y claras,\
la voz de una cuna hablando\
de cuanto los niños hablan;\
la voz de una madre, rica\
de sentimientos y de alma,\
y la voz de un hombres que era\
la eterna voz de la patria,\
soñando ya con sus glorias\
y ya con sus esperanzas.\
Tez cobriza como aquellos\
primeros hijos de Anáhuac,\
que tantas veces hicieron\
temblar de miedo a la España,\
cuando la España atrevida\
midió con ellos sus armas;\
fuerte y ágil como todos\
los hijos de las montañas;\
como un labriego, robusto;\
como un patriota, entusiasta;\
como un valiente, atrevido,\
y como un joven, todo alma,\
el hombre de aquellas selvas,\
el hombre de aquella casa,\
era el eterno modelo\
de esas figuras sagradas\
que en el altar de los siglos\
hacen un Dios de una estatua.\
Veinticinco años apenas\
por ese tiempo contaba,\
y de sus nobles heridas\
la suma aún era más larga,\
que no hubo por el Bajío\
ningún combate ni hazaña\
donde su ardor no estuviera\
donde faltara su lanza,\
ni donde al grito de muerte\
sus huellas no señalara\
con el licor de sus venas\
o el de las venas extrañas.\
Y allí tranquilo y oculto\
su triste vida pasaba,\
lamentando en su impotencia\
la esclavitud de la patria\
que renunciando a la lucha,\
renunciaba a la esperanza:\
cuando una mañana, a la hora\
que el último sueño marca,\
despertó oyendo a lo lejos\
un ruido confuso de armas;\
y adivinando al instante\
la suerte que le amagaba,\
bajó del lecho al influjo\
de una decisión extraña;\
besa en los labios a su hijo,\
besa en la frente a su amada,\
clava los ojos ardientes\
en la entreabierta ventana,\
y al ver por sus enemigos\
ya casi envuelta su casa,\
salta a las rocas, y entre ellos\
se escapa por la montaña.\
\
II\
\
Aún no se alzaba del todo\
la niebla de la mañana,\
y aún no acertaban a darse\
cuenta de tamaña audacia\
los sitiadores furiosos\
que sorprenderle esperaban,\
cuando al galope y bajando\
camino de la cañada,\
vieron venir a lo lejos\
un grupo de gente armada,\
compuesto de ocho jinetes\
y el hombre que los mandaba;\
en mayor número que ellos\
y con superiores armas,\
seguros de la victoria\
fácil que se les aguarda,\
todos empuñan las riendas,\
todos afirman la lanza,\
todos ven al enemigo\
todos miden la distancia,\
y en silencio y todos ellos\
prontos a ponerse en marcha,\
sólo esperan a que llegue\
la hora de entrar en batalla.\
Los insurgentes en tanto\
viendo las huestes contrarias,\
más de coraje la encienden\
y más de amor la entusiasman,\
y ansiosos de dar su sangre\
por la salud de la patria,\
sobre el caballo inclinan,\
la floja rienda adelantan,\
y fijos los barboquejos\
y el sombrero hacia la espalda,\
entre la niebla y el polvo\
corren, y vuelan y avanzan,\
siguiendo entre los peñascos\
al hombre de la cañada.\
Y ya los de Bustamante\
su primer paso avanzaban,\
anhelando en su impaciencia\
cómo acortar la distancia\
que la interpuesta colina\
con un recodo aumentaba;\
cuando de pie en lo más alto\
de las rocas escarpadas,\
vieron alzarse a un jinete\
que con voz sonora y clara,\
'Yo soy el Giro –les dijo,\
-si al Giro es a quien aguardan;\
y el que lo busque que venga\
si tiene honor y tiene alma,\
que a todos espera el Giro\
frente a frente y cara a cara'-\
Dijo: y los fieros dragones\
al grito de '¡Viva España!'\
como un solo hombre treparon\
hasta donde el Giro estaba\
dispuesto como los suyos\
a sucumbir por la patria. . .\
Y fue la lucha, y terribles\
al dar la espantosa carga,\
insurgentes y realistas\
ardiendo en cólera y rabia,\
se entremezclaron sedientos\
de victoria y de matanza. . .\
Quiso la triste fortuna\
favorecer a la España,\
el brillo de sus fulgores\
negándole a nuestras armas,\
que ya de los insurgentes\
uno tan sólo quedaba\
a caballo todavía,\
pero ya herido y sin armas.\
Era el Giro, que entre doce\
dragones que le rodeaban,\
sin rendirse al desaliento\
ni inclinarse a la desgracia,\
luchaba y arremetía\
contra el que más se acercaba,\
convirtiendo a su caballo,\
a un tiempo en escudo y arma.\
Por fin un brazo atrevido\
clavó en su pecho una lanza,\
perder haciéndole el poco\
aliento que le quedaba;\
pero él aunque ya en el suelo,\
con fuerza siempre y con alma,\
coge la lanza, del pecho\
sin vacilar se la arranca,\
y estremecido y al grito\
de independencia y de patria,\
de pie sobre los peñascos\
a sus contrarios aguarda;\
y después de herir a todos\
los que acercársele ensayan,\
hace huir a los restantes\
que ante heroicidad tamaña\
se alejan, y desde lejos\
lo rematan a pedradas.\
\
III\
\
Mártir, que toda tu sangre\
supiste dar por la patria;\
tú, de los desconocidos\
que murieron por salvarla,\
¡gracias por tu fortaleza,\
por tu sacrificio, gracias!\
\
\
\
Hojas secas\
\
I\
\
Mañana que ya no puedan\
encontrarse nuestros ojos,\
y que vivamos ausentes,\
muy lejos uno del otro,\
que te hable de mí este libro\
como de ti me habla todo.\
\
II\
\
Cada hoja es un recuerdo\
tan triste como tierno\
de que hubo sobre ese árbol\
un cielo y un amor;\
reunidas forman todas\
el canto del invierno,\
la estrofa de las nieves\
y el himno del dolor.\
\
III\
\
Mañana a la misma hora\
en que el sol te besó por vez primera,\
sobre tu frente pura y hechicera\
caerá otra vez el beso de la aurora;\
pero ese beso que en aquel oriente\
cayó sobre tu frente solo y frío,\
mañana bajará dulce y ardiente,\
porque el beso del sol sobre tu frente\
bajará acompañado con el mío.\
\
IV\
\
En Dios le exiges a mi fe que crea,\
y que le alce un altar dentro de mí.\
¡Ah! ¡ Si basta no más con que te vea\
para que yo ame a Dios, creyendo en ti!\
\
V\
\
Si hay algún césped blando\
cubierto de rocío\
en donde siempre se alce\
dormida alguna flor,\
y en donde siempre puedas\
hallar, dulce bien mío,\
violetas y jazmines\
muriéndose de amor;\
\
yo quiero ser el césped\
florido y matizado\
donde se asienten, niña,\
las huellas de tus pies;\
yo quiero ser la brisa\
tranquila de ese prado\
para besar tus labios\
y agonizar después.\
\
Si hay algún pecho amante\
que de ternura lleno\
se agite y se estremezca\
no más para el amor,\
yo quiero ser, mi vida,\
yo quiero ser el seno\
donde tu frente inclines\
para dormir mejor.\
\
Yo quiero oír latiendo\
tu pecho junto al mío,\
yo quiero oír qué dicen\
los dos en su latir,\
y luego darte un beso\
de ardiente desvarío,\
y luego. . . arrodillarme\
mirándote dormir.\
\
VI\
\
Las doce. . . ¡adiós. . .! Es fuerza que me vaya\
y que te diga adiós. . .\
Tu lámpara está ya por extinguirse,\
y es necesario.\
-Aún no.-\
Las sombras son traidoras, y no quiero\
que al asomar el sol,\
se detengan sus rayos a la entrada\
de nuestro corazón. . .\
-Y, ¿qué importan las sombras cuando entre ellas\
queda velando Dios?\
-¿Dios? ¿Y qué puede Dios entre las sombras\
al lado del amor?\
-¿Cuando te duermas ¿me enviarás un beso?\
-¡Y mi alma!\
-¡Adiós. . . !\
-¡Adiós. . . !\
\
VII\
\
Lo que siente el árbol seco\
por el pájaro que cruza\
cuando plegando las alas\
baja hasta sus ramas mustias,\
y con sus cantos alegra\
las horas de su amargura;\
lo que siente pro el día\
la desolación nocturna\
que en medio de sus angustias,\
ve asomar con la mañana\
de sus esperanzas una;\
lo que sienten los sepulcros\
por la mano buena y pura\
que solamente obligada\
por la piedad que la impulsa,\
riega de flores y de hojas\
la blanca lapida muda,\
eso es al amarte mi alma\
lo que siente por la tuya,\
que has bajado hasta mi invierno,\
que has surgido entre mi angustia\
y que has regado de flores\
la soledad de mi tumba.\
\
Mi hojarasca son mis creencias,\
mis tinieblas son la duda,\
mi esperanza es el cadáver,\
y el mundo mi sepultura. . .\
Y como de entre esas hojas\
jamás retoña ninguna;\
como la duda es el cielo\
de una noche siempre oscura,\
y como la fe es un muerto\
que no resucita nunca,\
yo no puedo darte un nido\
donde recojas tus plumas,\
ni puedo darte un espacio\
donde enciendas tu luz pura,\
ni hacer que mi alma de muerto\
palpite unida a la tuya;\
pero si gozar contigo\
no ha de ser posible nunca,\
cuando estés triste, y en el alma\
sientas alguna amargura,\
yo te ayudaré a que llores,\
yo te ayudaré a que sufras,\
y te prestaré mis lágrimas\
cuando se acaben las tuyas.\
\
VIII\
\
1\
\
Aún más que con los labios\
hablamos con los ojos;\
con los labios hablamos de la tierra,\
con los ojos del cielo y de nosotros.\
\
2\
\
Cuando volví a mi casa\
de tanta dicha loco,\
fue cuando comprendí muy lejos de ella\
que no hay cosa más triste que estar solo.\
\
3\
\
Radiante de ventura,\
frenético de gozo,\
cogí una pluma, le escribí a mi madre,\
y al escribirle se lo dije todo.\
\
4\
\
Después, a la fatiga\
cediendo poco a poco,\
me dormí y al dormirme sentí en sueños\
que ella me daba un beso y mi madre otro.\
\
5\
\
¡Oh sueño, el de mi vida\
más santo y más hermoso!\
¡Qué dulce has de haber sido cuando aun muerto\
gozo con tu recuerdo de este modo!\
\
IX\
\
Cuando yo comprendí que te quería\
con toda la lealtad de mi corazón,\
fue aquella noche en que al abrirme tu alma\
miré hasta su interior.\
Rotas estaban tus virgíneas alas\
que ocultaba en sus pliegues un crespón\
y un ángel enlutado cerca de ellas\
lloraba como yo.\
Otro tal vez, te hubiera aborrecido\
delante de aquel cuadro aterrador;\
pero yo no miré en aquel instante\
más que mi corazón;\
y te quise tal vez por tus tinieblas,\
y te adoré, tal vez, por tu dolor,\
¡qué es muy bello poder decir que el alma\
ha servido de sol. . .!\
\
X\
\
Las lágrimas del niño\
la madre enjuga,\
las lágrimas del hombre\
las seca la mujer. . .\
¡Qué tristes las que brotan\
y bajan por la arruga,\
del hombre que está solo,\
del hijo que está ausente,\
del ser abandonado\
que llora y que no siente\
ni el beso de la cuna,\
ni el beso del placer!\
\
XI\
\
¡Cómo quieres que tan pronto\
olvide el mal que me has hecho,\
si cuando me toco el pecho\
la herida me duele más!\
Entre el perdón y el olvido\
hay una distancia inmensa;\
yo perdonaré la ofensa;\
pero olvidarla. . . . ¡jamás!\
\
XII\
\
¡Ah, gloria! ¡De qué me sirve\
tu laurel mágico y santo,\
cuando ella no enjuga el llanto\
que estoy vertiendo sobre él!\
¡De que me sirve el reflejo\
de tu soñada corona,\
¡cuando ella no me perdona\
ni en nombre de ese laurel!\
\
La que a la luz de sus ojos\
despertó mi pensamiento,\
la que al amor de su acento\
encendió en mi la pasión;\
muerta para el mundo entero\
y aun para ella misma muerta,\
solamente está despierta\
dentro de mi corazón.\
\
XIV\
\
El cielo muy negro, y como un velo\
lo envuelve en su crespón la oscuridad;\
con un sombra más sobre ese cielo\
el rayo puede desatar su vuelo\
y la nube cambiarse en tempestad.\
\
XV\
\
Oye, ven a ver las naves,\
están vestidas de luto,\
y en vez de las golondrinas\
están graznando los búhos. . .\
El órgano está callado,\
el templo solo y oscuro,\
sobre el altar. . . ¿y la virgen\
por qué tiene el rostro oculto?\
¿Ves?. . . en aquellas paredes\
están cavando un sepulcro,\
y parece como que alguien\
solloza allí, junto al muro.\
¿Por qué me miras y tiemblas?\
¿Por qué tienes tanto susto?\
¿Tú sabes quién es el muerto?\
¿Tú sabes quién fue el verdugo?\
\
\
\
\
\
INSCRIPCIÓN EN UN CRÁNEO\
\
Página en que la esfinge de la muerte\
con su enigma de sombrea nos provoca:\
¿Cómo poderte descifrar, si es poca\
toda la luz del sol para leerte?\
\
\
\
Los beodos\
\
Junto a una pulquería\
cuyo título es 'Los godos'\
disputaban dos beodos\
la tarde de cierto día.\
\
Yo pasaba por fuera\
de la taberna predicha,\
me detuve y por mi dicha\
oí la disputa entera.\
\
-Oiga, amigo, no me abroche\
tan horrenda tontería,\
yo le digo que es de día.\
-Pos' yo digo que es de noche\
\
-Pos' yo el sol es lo que miro\
y no hay estrella ninguna.\
-Pos yo digo que es la luna\
y muy grandota dialtiro'.\
\
Es que asté' ya se le escapa\
toditito don Perfeuto'\
porque ya siente el efeuto'\
del maldecido Tlamapa.\
\
-¡Qué Tlamapa, ni qué nada!\
A mí el pulque no me aprieta,\
-Pos' yo apuesto una peseta.\
-Pos' yo apuesto mi frezada'.\
\
-¿Pos' con quién nos arreglamos?\
-Pos' con cualesquiera', vale,\
-Bueno, pero no me jale.\
-Bueno, pus' entonces vamos.\
\
Y entre diciendo y haciendo\
este par de tercos beodos,\
se salieron de 'Los godos'\
casi, casi que cayendo.\
\
Y viendo pasar un coche\
al cochero se acercaron,\
y presto le preguntaron\
si era de día o de noche.\
\
Pero el salvaje cochero\
movió triste la cabeza\
y respondió con torpeza:\
señores: ¡soy forastero!\
\
\
Por eso\
\
Porque eres buena, inocente\
como un sueño de doncella,\
porque eres cándida y bella\
como un nectario naciente.\
\
Porque en tus ojos asoma\
con un dulcísimo encanto,\
todo lo hermoso y lo santo\
del alma de una paloma.\
\
Porque eres toda una esencia\
de castidad y consuelo,\
porque tu alma es todo un cielo\
de ternura y de inocencia.\
\
Porque al sol de tus virtudes\
se mira en ti realizado\
el ideal vago y soñado\
de todas las juventudes;\
\
por eso, niña hechicera,\
te adoro en mi loco exceso;\
por eso te amo, y por eso\
te he dado mi vida entera.\
\
Por eso a tu luz se inspira\
la fe de mi amor sublime;\
¡por eso solloza y gime\
como un corazón mi lira!\
\
Por eso cuando te evoca\
mi afán en tus embelesos,\
siento que un mundo de besos\
palpita sobre mi boca.\
\
Y por eso entre la calma\
de mi existencia sombría,\
mi amor no anhela más día\
que el que una mi alma con tu alma.\
\
Nocturno a Rosario\
\
I\
\
¡Pues bien! yo necesito\
decirte que te adoro\
decirte que te quiero\
con todo el corazón;\
que es mucho lo que sufro,\
que es mucho lo que lloro,\
que ya no puedo tanto\
al grito que te imploro,\
te imploro y te hablo en nombre\
de mi última ilusión.\
\
        II\
\
Yo quiero que tu sepas\
que ya hace muchos días\
estoy enfermo y pálido\
de tanto no dormir;\
que ya se han muerto todas\
las esperanzas mías,\
que están mis noches negras,\
tan negras y sombrías,\
que ya no sé ni dónde\
se alzaba el porvenir.\
\
        III\
\
De noche, cuando pongo\
mis sienes en la almohada\
y hacia otro mundo quiero\
mi espíritu volver,\
camino mucho, mucho,\
y al fin de la jornada\
las formas de mi madre\
se pierden en la nada\
y tú de nuevo vuelves\
en mi alma a aparecer.\
\
        IV\
\
Comprendo que tus besos\
jamás han de ser míos,\
comprendo que en tus ojos\
no me he de ver jamás,\
y te amo y en mis locos\
y ardientes desvaríos\
bendigo tus desdenes,\
adoro tus desvíos,\
y en vez de amarte menos\
te quiero mucho más.\
\
        V\
\
A veces pienso en darte\
mi eterna despedida,\
borrarte en mis recuerdos\
y hundirte en mi pasión\
mas si es en vano todo\
y el alma no te olvida,\
¿Qué quieres tú que yo haga,\
pedazo de mi vida?\
¿Qué quieres tu que yo haga\
con este corazón?\
\
        VI\
\
Y luego que ya estaba\
concluído tu santuario,\
tu lámpara encendida,\
tu velo en el altar;\
el sol de la mañana\
detrás del campanario,\
chispeando las antorchas,\
humeando el incensario,\
y abierta alla a lo lejos\
la puerta del hogar...\
\
        VII\
\
¡Qué hermoso hubiera sido\
vivir bajo aquel techo,\
los dos unidos siempre\
y amándonos los dos;\
tú siempre enamorada,\
yo siempre satisfecho,\
los dos una sola alma,\
los dos un solo pecho,\
y en medio de nosotros\
mi madre como un Dios!\
\
        VIII\
\
¡Figúrate qué hermosas\
las horas de esa vida!\
¡Qué dulce y bello el viaje\
por una tierra así!\
Y yo soñaba en eso,\
mi santa prometida;\
y al delirar en ello\
con alma estremecida,\
pensaba yo en ser bueno\
por tí, no mas por ti.\
\
        IX\
\
¡Bien sabe Dios que ese era\
mi mas hermoso sueño,\
mi afán y mi esperanza,\
mi dicha y mi placer;\
bien sabe Dios que en nada\
cifraba yo mi empeño,\
sino en amarte mucho\
bajo el hogar risueño\
que me envolvió en sus besos\
cuando me vio nacer!\
\
        X\
\
Esa era mi esperanza...\
mas ya que a sus fulgores\
se opone el hondo abismo\
que existe entre los dos,\
¡Adiós por la vez última,\
amor de mis amores;\
la luz de mis tinieblas,\
la esencia de mis flores;\
mi lira de poeta,\
mi juventud, adiós!\
\
\
Historia del Pensamiento\
\
Cuando a su nido vuela el ave pasajera\
a quien amparo disteis, abrigo y amistad\
es justo que os dirija su cántiga postrera,\
antes que triste deje, vuestra natal ciudad.\
\
Al pájaro viajero que abandonó su nido\
le disteis un abrigo, calmando su inquietud;\
¡oh! Tantos beneficios, jamás daré al olvido\
durable cual mi vida será mi gratitud.\
\
En prueba de ella os dejo lo que dejaros puedo,\
mis versos, siempre tristes, pero los dejo asi;\
porque pienso, a veces que entre sus letras quedo,\
porque al leerlos creo que os acordais de mí.\
\
Voy, pues, a referiros una sencilla historia.\
Que en mi alma desolada, honda impresión dejó;\
me la contaron... ¿Dónde?... es frágil mi memoria...\
Acaso el héroe de ella... o bien, la soñé yo.\
\
Era una linda rosa, brillante enredadera,\
tan pura, tan graciosa, espléndida y gentil.\
Que era el mejor adorno de la feliz pradera,\
la joya más valiosa del floreciente abril.\
\
Al pie de ella crecía un pobre pensamiento,\
pequeño, solitario, sin gracia ni color;\
pero miró a la rosa y respiro su aliento\
y concibió por ella el más profundo amor.\
\
Mirando a su querida pasaba noche y día.\
Mil veces ¡ay! Le quiso su pena declarar;\
pero tan lejos siempre, tan lejos la veía,\
que devoraba a solas su pena y su pesar.\
\
A veces le mandaba sus tímidos olores,\
pensando que llegaba hasta su amada flor;\
pero la brisa, al columpiar las flores,\
llevábase muy lejos la pena de su amor.\
\
El pobre pensamiento mil lágrimas vertía,\
desoladoras lágrimas, de acíbar y de hiel,\
mientras la joven rosa, sin ver a otras crecía,\
y mientras más crecía, más se alejaba de él.\
\
Llega un jazmín en tanto a la pradera bella,\
también él a la rosa al punto que la vio;\
pero él fue más dichoso, pudo llegar hasta ella,\
le declaró su pena, y al fin la rosa amó...\
\
¿Comprenderéis ahora al pobre pensamiento,\
al ver correspondido a su feliz rival?\
¿No comprendéis su horrible, su bárbaro tormento\
al verse condenado a suerte tan fatal?\
\
Después lo transplantaron; vivió en otras praderas\
indiferiencia, olvido y hasta placer fingió:\
miraba flores lindas, brillantes y hechiceras,\
pero su amor constante y fiel compareció.\
\
Por fin una mañana, estando muy distante,\
el céfiro contóle las bodas del jazmín;\
él escuchó sonriente, y ciego y delirante,\
loco placer fingiendo, creyó olvidar al fin.\
\
Pero al siguiente día con lágrimas le vieron\
las flores, e ignorando su oculto padecer;\
'Tú lloras, pensamiento, tú lloras', le dijeron:\
'No es nada, contestóles, es llanto de placer'.\
\
...................................................\
\
Ved la sencilla historia que os ofrecí contaros,\
acaso os entristezca pero la dejo así;\
adiós, adiós, ya parto; me atrevo a suplicaros\
que la leáis a solas y os acordéis de mí.\
\
Adiós\
\
A...\
\
Después de que el destino\
me ha hundido en las congojas\
del árbol que se muere\
crujiendo de dolor,\
truncando una por una\
las flores y las hojas\
que al beso de los cielos\
brotaron de mi amor.\
\
Después de que mis ramas\
se han roto bajo el peso\
de tanta y tanta nieve\
cayendo sin cesar,\
y que mi ardiente savia\
se ha helado con el beso\
que el ángel del invierno\
me dio al atravesar.\
\
Después... es necesario\
que tú también te alejes\
en pos de otras florestas\
y de otro cielo en pos;\
que te alces de tu nido,\
que te alces y me dejes\
sin escuchar mis ruegos\
y sin decirme adiós.\
\
Yo estaba solo y triste\
cuando la noche te hizo\
plegar las blancas alas\
para acogerte a mi,\
entonces mi ramaje\
doliente y enfermizo\
brotó sus flores todas\
tan sólo para ti.\
\
En ellas te hice el nido\
risueño en que dormías\
de amor y de ventura\
temblando en su vaivén,\
y en él te hallaban siempre\
las noches y los días\
feliz con mi cariño\
y amándote también...\
\
¡Ah! nunca en mis delirios\
creí que fuera eterno\
el sol de aquellas horas\
de encanto y frenesí;\
pero jamás tampoco\
que el soplo del invierno\
llegara entre tus cantos,\
y hallándote tú aquí...\
\
Es fuerza que te alejes...\
rompiéndome en astillas;\
ya siento entre mis ramas\
crujir el huracán,\
y heladas y temblando\
mis hojas amarillas\
se arrancan y vacilan\
y vuelan y se van...\
\
Adiós, paloma blanca\
que huyendo de la nieve\
te vas a otras regiones\
y dejas tu árbol fiel;\
mañana que termine\
mi vida oscura y breve\
ya sólo tus recuerdos\
palpitarán sobre él.\
\
Es fuerza que te alejes\
del cántico y del nido\
tú sabes bien la historia\
paloma que te vas...\
El nido es el recuerdo\
y el cántico el olvido,\
el árbol es el siempre\
y el ave es el jamás.\
\
Adiós mientras que puedes\
oír bajo este cielo\
el último ¡ay! del himno\
cantado por los dos...\
Te vas y ya levantas\
el ímpetu y el vuelo,\
te vas y ya me dejas,\
¡paloma, adiós, adiós!\
\
\
\
Al Ruiseñor Mexicano\
\
(Ángela Peralta)\
\
Hubo una selva y un nido\
y en ese nido un jilguero\
que alegre y estremecido,\
tras de un ensueño querido\
cruzó por el mundo entero.\
\
Que de su paso en las huellas\
sembró sus notas mejores,\
y que recogió con ellas\
al ir por el cielo, estrellas,\
y al ir por el mundo; flores.\
\
Del nido y de la enramada\
ninguno la historia sabe;\
porque la tierra admirada\
dejó esa historia olvidada\
por escribir la del ave.\
\
La historia de la que un día\
al remontarse en su vuelo,\
fue para la patria mía\
la estrella de mas valía\
de todas las de su cielo.\
\
La de aquella a quien el hombre\
robara el nombre galano\
que no hay a quien no le asombre\
para cambiarlo en el nombre\
de Ruiseñor Mexicano.\
\
Y de la que al ver perdido\
su nido de flores hecho,\
halló en su suelo querido\
en vez de las de su nido\
las flores de nuestro pecho.\
\
Su historia... que el pueblo ardiente\
en su homenaje mas justo\
viene a adorar reverente\
con el laurel esplendente\
que hoy ciñe sobre su busto.\
\
Sobre esa piedra bendita\
que grande entre las primeras\
es la página en que escrita\
leerán tu gloria infinita\
las edades venideras.\
\
Y que unida a la memoria\
de tus hechos soberanos,\
se alzará como una historia\
hablándoles de tu gloria\
a todos los mexicanos.\
\
Hoy al mirar tus destellos\
resplandecer de ese modo\
bien puede decirse de ellos\
que el nombre tuyo es de aquellos,\
que nunca muere del todo.\
\
\
\
\
La Brisa\
\
(Imitación)\
\
A mi querido amigo J.C. Fernandez.\
\
Aliento de la mañana\
que vas robando en tu vuelo\
la esencia pura y temprana\
que la violeta lozana\
despide en vapor al cielo:\
\
Dime, soplo de la aurora,\
brisa inconstante y ligera,\
¿vas por ventura a esta hora\
al valle que te enamora\
y que gimiendo te espera?\
\
¿O vas acaso a los nidos\
de los jilgueros cantores\
que en la espesura escondidos\
te aguardan medio adormidos\
sobre sus lechos de flores?\
\
¿O vas anunciando acaso,\
sopla del alba naciente,\
al murmurar de tu paso,\
que el muerto sol del ocaso\
se alza un niño en oriente?\
\
Recoge tus leves alas,\
brisa pura del estío,\
que los perfumes que exhalas\
vas robando entre las galas\
de las violetas del río.\
\
Detén tu fugaz carrera\
sobre las risueñas flores\
de la loma y la pradera,\
y ve a despertar ligera\
al ángel de mis amores.\
\
Y dile, brisa aromada,\
con tu murmullo sonoro,\
que ella es mi ilusión dorada,\
y que en mi pecho grabada\
como a mi vida la adoro.\
\
\
\
Ya sé por qué es\
\
Dolora a Elmira\
\
Era muy niña María,\
todavía,\
cuando me dijo una vez:\
-Oye, ¿por qué se sonríen\
las flores tan dulcemente,\
cuando las besa el ambiente\
sobre su aromada tez?\
-Ya lo sabrás mas delante\
niña amante,\
le contesté yo, y una mañana,\
la niña pura y hermosa,\
al entreabrir una rosa\
me dijo: ¡Ya sé por qué es!\
\
Y la graciosa criatura\
blanca y pura\
se ruborizó y después,\
ligera como las aves\
que cruzan por la campiña,\
corrió hacia el bosque la niña\
diciendo: ¡Ya sé por qué es!\
y yo la seguí jadeante,\
palpitante\
de ternura y de interés,\
y... oí un beso dulce y blando,\
que fue a perderse en lo espeso,\
diciendo: ¡Ya sé por qué es!\
\
Era muy joven María,\
todavía\
cuando me dijo una vez;\
-Oye ¿por qué la azucena\
se abate y llora marchita\
cuando el aura no la agita\
ni besa su blanca tez?\
¡Ya los sabrás más delante,\
niña amante,\
le contesté yo... después!\
Y mas tarde ¡ay! una noche,\
la joven de angustia llena,\
al ver triste a una azucena,\
me dijo: ¡Ya sé por qué es!\
\
Y ahogando un suspiro ardiente,\
la inocente\
me vio llorando... y después,\
corrió al bosque y en el bosque\
esperó mucho la bella,\
y al fin... se oyó una querella\
diciendo: ¡Ya sé por qué es!\
Era muy linda María,\
todavía,\
cuando me dijo una vez:\
-Oye, ¿Por qué se sonríe\
el niño en la sepultura,\
con una risa tan pura,\
con tan dulce sencillez?\
Ya lo sabrás mas delante\
niña amante,\
le contesté yo... después!\
\
Y... murió la pobre niña,\
y en vez de llorar, sonriendo,\
voló hacia el azul diciendo,\
¡Ya sé por qué es!\
\
Ya lo ves mi hermosa Elmira,\
quien delira\
sufre mucho, ya lo ves!\
Y así, ilusiones y encanto,\
ni acaricies ni mantengas,\
para que, al llorar, no tengas\
que decir:\
¡Ya sé por qué es!\
\
\
Ya verás\
\
Dolora (imitación)\
\
Goza, goza, niña pura,\
mientras en la infancia estás;\
goza, goza esa ventura\
que dura lo que una rosa.\
-Qué, ¿tan poco es lo que dura?\
-Ya verás niña graciosa,\
ya verás.\
\
Hoy es un vergel risueño\
la senda por donde vas;\
pero mañana, mi dueño,\
verás abrojos en ella.\
-Pues qué, ¿sus flores son sueño?\
-Sueño nada mas, mi bella,\
ya verás.\
\
Hoy el carmín y la grana\
coloran tu linda faz;\
pero ya verás mañana\
que el llanto sobre ella corra...\
-Qué, ¿los borra cuando mana?\
-Ya verás cómo los borra,\
ya verás.\
\
Y goza mi tierna Elmira,\
mientras disfruta de paz;\
delira, niña, delira\
con un amor que no existe\
pues qué, ¿el amor es mentira?\
-Y una mentira muy triste,\
ya verás.\
\
Hoy ves la dicha delante\
y ves la dicha detrás;\
pero esa estrella brillante\
vive y dura lo que el viento.\
-Qué, ¿nada mas dura un instante?\
-Sí, nada mas un momento,\
ya verás.\
\
Y así, no llores mi encanto,\
que mas tarde llorarás;\
mira que el pesar es tanto,\
que hasta el llanto dura poco.\
-¿Tampoco es eterno el llanto?\
-Tampoco, niña, tampoco,\
ya verás!\
\
\
La Ausencia del Olvido\
\
Dolora a Lola\
\
Iba llorando la Ausencia\
con el semblante abatido\
cuando se encontró en presencia\
del Olvido,\
que al ver su faz marchitada,\
le dijo con voz turbada:\
sin colores,\
-'Ya no llores niña bella,\
ya no llores.'\
\
Que si tu contraria estrella\
te oprime incansable y ruda\
yo te prometo mi ayuda\
contra tu mal y contra ella'.\
oyó la Ausencia llorando\
la propuesta cariñosa,\
y los ojos enjugando\
ruborosa,\
-'Admito desde el momento\
buen anciano'.\
Le dijo con dulce acento.\
'Admito lo que me ofreces\
y que en vano\
he buscado tantas veces,\
yo que triste y sin ventura,\
la copa de la amargura\
he apurado hasta las heces'\
Desde entonces, Lola bella,\
cariñosa y anhelante\
vive el Olvido con ella,\
siempre amante;\
y la Ausencia ya no gime,\
ni doliente\
recuerda el mal que la oprime;\
que un amor ha concebido\
tan ardiente\
por el anciano querido,\
que si sus penas resiste,\
suspira y llora muy triste\
cuando la deja el Olvido.\
\
 \
 \
\
Mentiras de la Existencia\
\
Dolora\
\
¡Qué triste es vivir soñando\
en un mundo que no existe!\
Y qué triste\
ir viviendo y caminando,\
sin fe en nuestros delirios,\
de la razón con los ojos,\
que si hay en la vida lirios,\
son muchos mas los abrojos.\
\
Nace el hombre, y al momento\
se lanza tras la esperanza,\
que no alcanza\
porque no se alcanza el viento;\
y corrre, corre, y no mira\
al ir en pos de la gloria\
que es la gloria una mentira\
tan bella como ilusoria.\
\
¡No ve al correr como loco\
tras la dicha y los amores,\
que son flores\
que duran poco, muy poco!\
¡No ve cuando se entusiasma\
con la fortuna que anhela,\
que es la fortuna un fantasma\
que cuando se toca vuela!\
\
Y que la vida es un sueño\
del que, si al fin despertamos,\
encontramos\
el mayor placer pequeño;\
pues son tan fuertes los males\
de la existencia en la senda,\
que corren allí a raudales\
las lágrimas en ofrenda.\
\
Los goces nacen y mueren\
como puras azucenas,\
mas las penas\
viven siempre y siempre hieren;\
y cuando vuelve la calma\
con las ilusiones bellas,\
su lugar dentro del alma\
queda ocupado por ellas.\
\
Porque al volar los amores\
dejan una herida abierta\
que es la puerta\
por donde entran los dolores;\
sucediendo en la jornada\
de nuestra azarosa vida\
que es para el pesar 'entrada'\
lo que para el bien 'salida'.\
\
Y todos sufren y lloran\
sin que una queja profieran,\
porque esperan\
¡hallar la ilusión que adoran!...\
Y no mira el hombre triste\
cuando tras la dicha corre,\
que sólo el dolor existe\
sin que haya bien que lo borre.\
\
No ve que es un fatuo fuego\
la pasión en que se abrasa,\
luz que pasa\
como relámpago, luego:\
y no ve que los deseos\
de su mente acalorada\
no son sino devaneos,\
no son más que sombra, nada.\
\
Que es el amor tan ligero\
cual la amistad que mancilla\
porque brilla\
sólo a la luz del dinero;\
y no ve cuando se lanza\
loco tras de su creencia,\
que son la fe y la esperanza,\
mentiras de la existencia.\
\
\
\
La Felicidad\
\
Un cielo azul de estrellas\
brillando en la inmensidad;\
un pájaro enamorado\
cantando en el florestal;\
por ambiente los aromas\
del jardín y el azahar;\
junto a nosotros el agua\
brotando del manantial\
nuestros corazones cerca,\
nuestros labios mucho más,\
tú levantándote al cielo\
y yo siguiéndote allá,\
ese es el amor mi vida,\
¡Esa es la felicidad!...\
\
Cruza con las mismas alas\
los mundos de lo ideal;\
apurar todos los goces,\
y todo el bien apurar;\
de lo sueños y la dicha\
volver a la realidad,\
despertando entre las flores\
de un césped primaveral;\
los dos mirándonos mucho,\
los dos besándonos más,\
ese es el amor, mi vida,\
¡Esa es la felicidad...!\
\
\
\
\
A una Flor\
\
Cuando tu broche apenas se entreabría\
para aspirar la dicha y el contento\
¿te doblas ya y cansada y sin aliento,\
te entregas al dolor y a la agonía?\
\
¿No ves, acaso, que esa sombra impía\
que ennegrece el azul del firmamento\
nube es tan sólo que al soplar el viento,\
te dejará de nuevo ver el día?...\
\
¡Resucita y levántate!... Aún no llega\
la hora de que en el fondo de tu broche\
des cabida al pesar que te doblega.\
\
Injusto para el sol es tu reproche,\
que esa sombra que pasa y que te ciega,\
es una sombra, pero aún no es la noche.\
\
\
\
A Rosario\
\
Esta hoja arrebatada a una corona\
que la fortuna colocó en mi frente\
entre el aplauso fácil e indulgente\
con que el primer ensayo se perdona.\
\
Esta hoja de un laurel que aún me emociona\
como en aquella noche, dulcemente,\
por más que mi razón comprende y siente\
que es un laurel que el mérito no abona.\
\
Tú la viste nacer, y dulce y buena\
te estremeciste como yo al encanto\
que produjo al rodar sobre la escena;\
\
Guárdala y de la ausencia en el quebranto,\
que te recuerde de mis besos, llena,\
al buen amigo que te quiere tanto.\
\
Resignación\
\
¡Sin lágrimas, sin quejas,\
sin decirlas adiós, sin un sollozo!\
cumplamos hasta lo último. . . la suerte\
nos trajo aquí con el objeto mismo,\
los dos venimos a enterrar el alma\
bajo la losa del escepticismo.\
Sin lágrimas... las lágrimas no pueden\
devolver a un cadáver la existencia;\
que caigan nuestras flores y que rueden,\
pero al rodar, siquiera que nos queden\
seca la vista y firme la conciencia.\
¡Ya lo ves! para tu alma y para mi alma\
los espacios y el mundo están desiertos...\
los dos hemos concluido,\
y de tristeza y aflicción cubiertos,\
ya no somos al fin sino dos muertos\
que buscan la mortaja del olvido.\
Niños y soñadores cuando apenas\
de dejar acabábamos la cuna,\
y nuestras vidas al dolor ajenas\
se deslizaban dulces y serenas\
como el ala de un cisne en la laguna\
cuando la aurora del primer cariño\
aún no asomaba a recoger el velo\
que la ignorancia virginal del niño\
extiende entre sus párpados y el cielo,\
tu alma como la mía,\
en su reloj adelantando la hora\
y en sus tinieblas encendiendo el día,\
vieron un panorama que se abría\
bajo el beso y la luz de aquella aurora;\
y sintiendo al mirar ese paisaje\
las alas de un esfuerzo soberano,\
temprano las abrimos, y temprano\
nos trajeron al término del viaje.\
Le dimos a la tierra\
los tintes del amor y de la rosa;\
a nuestro huerto nidos y cantares,\
a nuestro cielo pájaros y estrellas;\
agotamos las flores del camino\
para formar con ellas\
una corona al ángel del destino...\
y hoy en medio del triste desacuerdo\
de tanta flor agonizante o muerta,\
ya sólo se alza pálida y desierta\
la flor envenenada del recuerdo.\
Del libro de la vida\
la que escribimos hoy es la última hoja...\
cerrémoslo en seguida,\
y en el sepulcro de la fe perdida\
enterremos también nuestra congoja.\
Y ya que el cielo nos concede que este\
de nuestros males el postrero sea,\
para que el alma a descansar se apreste,\
aunque la última lágrima nos cueste,\
cumplamos hasta el fin con la tarea.\
Y después cuando al ángel del olvido\
hayamos entregado estas cenizas\
que guardan el recuerdo adolorido\
de tantas ilusiones hechas trizas\
y de tanto placer desvanecido,\
dejemos los espacios y volvamos\
a la tranquila vida de la tierra,\
ya que la noche del dolor temprana\
se avanza hasta nosotros y nos cierra\
los dulces horizontes del mañana.\
Dejemos los espacios, o si quieres\
que hagamos, ensayando nuestro aliento,\
un nuevo viaje a esa región bendita\
cuyo sólo recuerdo resucita\
al cadáver del alma al sentimiento,\
lancémonos entonces a ese mundo\
en donde todo es sombras y vacío,\
hagamos una luna del recuerdo\
si el sol de nuestro amor está ya frío;\
volemos, si tu quieres,\
al fondo de esas mágicas regiones,\
y fingiendo esperanzas e ilusiones,\
rompamos el sepulcro, y levantando\
nuestro atrevido y poderoso vuelo,\
formaremos un cielo entre las sombras,\
y seremos los duendes de ese cielo.",
                    path=u"/c", tags=u"MA")

writer.add_document(title=u"Manuel Maria Flores", content=u"Frío\
(Cuento Bohemio)\
\
La tarde era triste,\
la nieve caía,\
su blanco sudario\
los campos cubría;\
ni un ave volaba,\
ni oíase rumor.\
\
Apenas la nieve\
dejando su huella,\
pasaba muy triste,\
muy pálida y bella,\
la niña que ha sido\
del valle la flor.\
\
Llevaba en el cinto\
su pobre calzado;\
su hermano pequeño\
que marcha a su lado\
le dice: -'No sienten\
la nieve tus pies?'\
\
'Mis pies nada sienten\
responde con calma\
'El frío que yo siento\
lo llevo en el alma;\
y el frío de la nieve \
más duro no es'.\
\
Y dice el pequeño\
que helado tirita:\
-'¡Más frío que el de nieve!...\
¿Cuál es, hermanita?\
¡No hay otro que pueda\
decirse mayor!...\
\
-'Aquel que de muerte\
las almas taladre;\
aquel que en el alma\
me puso mi madre\
el día que a mi esposo\
me unió sin amor'.\
\
\
\
Ausencia\
\
¡Quién me diera tomar tus manos blancas\
para apretarme el corazón con ellas,\
y besarlas... besarlas, escuchando\
de tu amor las dulcísimas querellas!\
\
¡Quién me diera sentir sobre mi pecho\
reclinada tu lánguida cabeza,\
y escuchar, como enantes, tus suspiros,\
tus suspiros de amor y de tristeza!\
\
¡Quién me diera posar casto y suave\
mi cariñoso labio en tus cabellos,\
y que sintieras sollozar mi alma\
en cada beso que dejara en ellos!\
\
¡Quién me diera robar un solo rayo\
de aquella luz de tu mirar en calma,\
para tener al separarnos luego\
con qué alumbrar la soledad del alma!\
\
Oh! quién me diera ser tu misma sombra\
el mismo ambiente que tu rostro baña,\
y, por besar tus ojos celestiales,\
la lágrima que tiembla en tu pestaña.\
\
Y ser un corazón todo alegría,\
nido de luz y de divinas flores,\
en que durmiese tu alma de paloma\
el sueño virginal de sus amores.\
\
Pero en su triste soledad el alma\
es sombra y nada mas, sombra y enojos...\
¿cuándo esta noche de la negra ausencia\
disipará la aurora de tus ojos?...\
\
\
\
Mater dolorosa\
Plegaria\
A mi Hermana Marina\
\
Virgen del infortunio, doliente Madre mía,\
en busca del consuelo me postro ante tu altar.\
Mi espíritu está triste, mi vida está sombría,\
pasaron sobre mi alma las olas del pesar.\
\
Estoy en desamparo, no tengo quien me acoja;\
hay horas en mi vida de bárbara aflicción,\
y solo... siempre solo,, no tengo quien recoja\
las lágrimas secretas que llora el corazón.\
\
Es cierto que del mundo en la corriente impura\
cayeron deshojadas las rosas de mi fe,\
que en pos de mis fantasmas de juvenil locura\
corriendo delirante, Señora, te olvidé.\
\
Que me cegó el orgullo satánico del hombre,\
y en mi ánima turbada la duda pentró;\
y se olvidó mi labio de pronunciar tu nombre,\
y de mi mente loca tu imagen se borró.\
\
Es cierto... ¡pero escucha!... de niño te adoraba,\
al pie de tus altares mi madre me llevó...\
Llorando, arrodillada, la historia me cantaba,\
del Gólgota tremendo cuando Jesús murió.\
\
Y vi sobre su rostro la angustia y el quebranto,\
caía sobre tu frente la sombra de una cruz,\
tus lágrimas rodaban y negro era tu manto...\
todo de un cirio pálido a la siniestra luz.\
\
Entonces era niño, no comprendí tu duelo;\
pero te amé, Señora, ¡tú sabes que te amé!\
que dulce inmaculado, alzábase hasta el cielo\
el infantil acento de mi sencilla fe.\
\
Por esa fe de niño, por el ardiente ruego\
que al lado de mi madre con ella repetí,\
¡virgen del infortunio, cuando a tus plantas llego,\
virgen del infortunio, apiádate de mí!\
\
Tú miras, reina augusta, la senda que cruzamos;\
con llanto la regaron generaciones cien,\
a nuestra vez nosotros con llanto la regamos,\
y las que vienen luego la regarán también.\
\
A nuestro paso vamos dejando en sus abrojos\
pedazos palpitantes del roto corazón;\
y andamos... y andamos... y no hallan nuestros ojos\
ni tregua a la jornada, ni tregua a la aflicción.\
\
Mas tú eres la esperanza, la luz y el consuelo,\
tus ojos levantados suplican al Señor,\
tus manos están juntas en dirección al cielo...\
tú ruegas por nosotros, ¡oh, madre del dolor!\
\
En busca de consuelo yo vengo a tus altares\
con alma entristecida y amargo corazón;\
y pongo ante tus ojos, Señora, mis pesares,\
y en lágrimas se baña la voz de mi oración.\
\
No mires que olvidando tu imagen y tu nombre\
al viento de este mundo mis creencias arrojé.\
Acuérdate del niño y olvídate del hombre...\
mi frente está en el polvo... perdóname... pequé.\
\
¡Oh! por mi fe de niño, por el ferviente ruego,\
que al lado de mi madre con ella repetí,\
Virgen de los Dolores, cuando a tus plantas llego,\
Virgen de los Dolores, ¡apiádate de mí!\
\
\
\
\
La fortuna\
\
A Rosario P.\
\
En su curso voluble la Fortuna\
todo cuanto me diera me quitó;\
Y la Miseria pálida y hambrienta\
el umbral de mi puerta se sentó.\
\
Y llegó la Amistad la que en un día\
el festín de mis dichas presidió-\
y aunque le dije ven, ella, espantada\
al ver aquel espectro, se alejó.\
\
Amor llegó también... Sellé mi labio,\
porque temí que se alejara Amor;\
pero él sin vacilar, bañado en lágrimas,\
vino a mi presuroso... y me abrazó.\
\
Y la Miseria pálida y hambrienta\
que al umbral de mi puerta se sentó\
a la luz de aquel ángel que lloraba,\
ella... ¡la horible harpía!... se embelleció.\
\
\
\
PASIÓN\
\
¡Hablame! Que tu voz, eco del cielo,\
sobre la tierra por doquier me siga...\
con tal de oir tu voz, nada me importa\
que el desdén en tu labio me maldiga.\
\
¡Mírame!... Tus miradas me quemaron, \
y tengo sed de ese mirar, eterno...\
por ver tus ojos, que se abrase mi alma\
de esa mirada en el celeste infierno.\
\
¡Amame!... Nada soy... pero tu diestra\
sobre mi frente pálida un instante,\
puede hacer del esclavo arrodillado\
el hombre rey de corazón gigante.\
\
*\
\
Tú pasas... y la tierra voluptuosa\
se estremece de amor bajo tus huellas,\
se entibia el aire, se perfuma el prado\
y se inclinan a verte las estrellas.\
\
Quisiera ser la sombra de la noche\
para verte dormir sola y tranquila,\
y luego ser la aurora... y despertarte\
con un beso de luz en la pupila.\
\
Soy tuyo, me posees... un solo átomo\
no hay en mi ser que para ti no sea:\
dentro de mi corazón eres latido,\
y dentro de mi cerebro eres idea.\
\
*\
\
¡Oh! por mirar tu frente pensativa\
y pálido de amores tu semblante;\
por sentir el aliento de tu boca\
mi labio acariciar un solo instante;\
\
por estrechar tus manos virginales\
sobre mi corazón, yo de rodillas,\
y devorar con mis tremente besos\
lágrimas de pasión en tus mejillas;\
\
yo te diera... no sé... ¡no tengo nada!...\
-el poeta es mendigo de la tierra-\
¡toda la sangre que en mis venas arde!\
¡todo lo grande que mi mente encierra!\
\
*\
\
Mas no soy para ti... ¡Si entre tus brazos\
la suerte loca me arrojara un día,\
al terrible contacto de tus labios\
tal vez mi corazón... se rompería!\
\
Nunca será... Para mi negra vida\
la inmensa dicha del amor no existe...\
sólo nací para llevar en mi alma\
todo lo que hay de tempestuoso y triste.\
\
Y quisiera morir... ¡pero en tus brazos,\
con la embriaguez de la pasión más loca,\
y que mi ardiente vida se apagara\
al soplo de los besos de tu boca\
\
\
\
Amémonos\
\
Buscaba mi alma con afán tu alma,\
buscaba yo la virgen que mi frente\
tocaba con su labio dulcemente\
en el febril insomnio del amor.\
\
Buscaba la mujer pálida y bella\
que en sueño me visita desde niño,\
para partir con ella mi cariño,\
para partir con ella mi dolor.\
\
Como en la sacra soledad del templo\
sin var a Dios se siente su presencia,\
yo presentí en el mundo tu existencia,\
y, como a Dios, sin verte, te adoré.\
\
Y demandando sin cesar al cielo\
la dulce compañera de mi suerte,\
muy lejos yo de ti, sin conocerte\
en la ara de mi amor te levanté.\
\
No preguntaba ni sabía tu nombre,\
¿En dónde iba a encontrarte? lo ignoraba;\
pero tu imagen dentro el alma estaba,\
más bien presentimiento que ilusión.\
\
Y apenas te miré... tú eras ángel\
compañero ideal de mi desvelo,\
la casta virgen de mirar de cielo\
y de la frente pálida de amor.\
\
Y a la primera vez que nuestros ojos\
sus miradas magnéticas cruzaron,\
sin buscarse, las manos se encontraron\
y nos dijimos 'te amo' sin hablar\
\
Un sonrojo purísimo en tu frente,\
algo de palidez sobre la mía,\
y una sonrisa que hasta Dios subía...\
asi nos comprendimos... nada más.\
\
¡Amémonos, mi bien! En este mundo\
donde lágrimas tantas se derraman,\
las que vierten quizá los que se aman\
tienen yo no sé que de bendición.\
dos corazones en dichoso vuelo;\
¡Amémonos, mi bien! Tiendan sus alas\
amar es ver el entreabierto cielo\
y levantar el alma en asunción.\
\
Amar es empapar el pensamiento\
en la fragancia del Edén perdido;\
amar es... amar es llevar herido\
con un dardo celeste el corazón.\
Es tocar los dinteles de la gloria,\
es ver tus ojos, escuchar tu acento,\
en el alma sentir el firmamento\
y morir a tus pies de adoración.\
\
\
\
Adiós\
\
Adiós para siempre, mitad de mi vida,\
un alma tan sólo teníamos los dos;\
mas hoy es preciso que esta alma divida\
la amarga palabra del último adiós.\
\
¿Por qué nos separan? ¿No saben acaso\
que pasa la vida cual pasa la flor?\
cruzamos el mundo como aves de paso...\
mañana la tumba, ¿por qué hoy el dolor?\
\
¿La dicha secreta de dos que se adoran\
enoja a los cielos, y es fuerza sufrir?\
¿Tan sólo son gratas las almas que lloran\
al torvo destino?... ¿La ley es morir?...\
\
¿Quién es el destino?... Te arroja a mis brazos,\
en mi alma te imprime, te infunde en mi ser,\
y bárbaro luego me arranca a pedazos\
el alma y la vida contigo... ¿por qué?\
\
Adiós... es preciso. No llores... y parte.\
La dicha de vernos nos quitan no más;\
pero un solo instante dejar de adorarte,\
hacer que te olvide, ¿lo pueden? ¡Jamas!\
\
Con lazos eternos nos hemos unido;\
en vano el destino nos hiere a los dos...\
¡las almas que se aman no tienen olvido,\
no tienen ausencia, no tiene adiós!\
\
\
\
Soñando\
\
Anoche te soñaba, vida mía,\
estaba solo y triste en mi aposento,\
escribía... no sé qué; mas era algo\
de ternura, de amor, de sentimiento.\
Porque pensaba en ti. Quizás buscaba\
la palabra más fiel para decirte\
la infinita pasión con que te amaba.\
\
De pronto, silenciosa,\
una figura blanca y vaporosa\
a mi lado llegó... Sentí en mi cuello\
posarse dulcemente\
un brazo cariñoso, y por mi frente\
resbalar una trenza de cabello.\
Sentí sobre mis labios\
el puro soplo de un aliento blando,\
alcé mis ojos y encontré los tuyos\
que me estaban, dulcísimos, mirando.\
Pero estaban tan cerca que sentía\
en yo no sé que plácido desmayo\
que en la luz inefable de su rayo\
entraba toda tu alma hasta la mía.\
\
Después, largo, süave\
y rumoroso apenas, en mi frente\
un beso melancólico imprimiste,\
y con dulce sonrisa de tristeza\
resbalando tu mano en mi cabeza\
en voz baja, muy baja, me dijiste:\
-'Me escribes y estás triste\
porque me crees ausente, pobre amigo;\
pero ¿no sabes ya que eternamente\
aunque lejos esté, vivo contigo?'\
......................................\
Y al despertar de tan hermoso sueño\
sentí en mi corazón plácida calma;\
y me dijiste: es verdad... ¡eternamente!...\
¿cómo puede jamás estar ausente\
la que vive inmortal dentro del alma?\
\
\
\
Soñaba\
(Heine)\
\
Soñaba yo: mis párpados henchidos\
de lágrimas sentía;\
soñé que estabas en la tumba, muerta,\
y muerta te veía...\
Era un sueño no más , pero despierto\
lloraba todavía.\
\
Estaba yo soñando, y por la cara,\
el llanto me corría;\
soñé que te arrancaba de mi lado\
alguno, vida mía...\
Era un sueño no más, pero despierto\
lloraba todavía.\
\
Soñaba yo... Me ahogaban los sollozos,\
el llanto me bebía...\
Estaba yo soñando que me amabas,\
¡soñando que eras mía!\
Era un sueño no más, no más que un sueño,\
y lloro, más que nunca, todavía!\
\
\
\
En el baño\
\
Alegre y sola en el recodo blando\
que forma entre los árboles el río\
al fresco abrigo del ramaje umbrío\
se está la niña de mi amor bañando.\
\
Traviesa con las ondas jugueteando\
el busto saca del remanso frío,\
y ríe y salpica el glacial rocío\
el blanco seno, de rubor temblando.\
\
Al verla tan hermosa, entre el follaje\
el viento apenas susurrando gira,\
slata trinando el pájaro salvaje,\
\
el sol más poco a poco se retira;\
todo calla... y Amor, entre el ramaje,\
a escondidas mirándola, suspira.\
\
\
Adoración\
\
Como al ara de Dios llega el creyente,\
trémulo el labio al exhalar el ruego,\
turbado el corazón, baja la frente,\
así, mujer, a tu presencia llego.\
\
¡No de mí apartes tus divinos ojos!\
Pálida está mi frente de dolores;\
¿para qué castigar con tus enojos\
al que es tan infeliz con tus amores?\
\
Soy un esclavo que a tus pies se humilla\
y suplicante tu piedad reclama,\
que con las manos juntas se arrodilla\
para decir con miedo. . . que te ama!\
\
¡Te ama! Y el alma que el amor bendice,\
tiembla al sentirle como débil hoja.\
¡Te ama! y el corazón cuando lo dice\
en yo no se qué lagrimas se moja.\
\
¡Perdóname este amor! A mí ha venido\
como la luz a la pupila abierta,\
como viene la música al oído,\
como la vida a la esperanza muerta.\
\
Fue una chispa de tu alma desprendida\
en el beso de luz de tu mirada\
que al abrazar mi corazón en vida\
dejó mi alma a la tuya desposada.\
\
Y este amor es el aire que respiro,\
ilusión imposible que atesoro \
inefable palabra que suspiro\
y dulcísima lágrima que lloro.\
\
Es el ángel espléndido y risueño\
que con sus alas en mi frente toca,\
y que deja - ¡perdóname, es un sueño!\
El beso de los cielos en mi boca.\
\
Mujer, mujer . . . mi corazón de fuego\
de amor no sabe la palabra santa,\
pero palpita en el supremo ruego\
que vengo a sollozar ante tu planta.\
\
¿No sabes que por sólo las delicias\
de oír el canto que tu voz encierra,\
cambiara yo, dichoso, las caricias\
de todas las mujeres de la tierra?\
\
¿Que por seguir tu sombra, mi María,\
sellando el labio a la importuna queja,\
de lágrimas y besos cubriría\
la leve huella que tu planta deja?\
\
¿Que por oír en cariñoso acento\
mi pobre nombre entre tus labios rojos,\
para escucharte detendré mi aliento,\
para mirarte me pondré de hinojos?\
\
¿Que por sentir en mi dichosa frente\
tu dulce labio con pasión impreso,\
te diera yo, con mi vivir presente,\
toda mi eternidad . . . por sólo un beso?\
\
Pero si tanto amor, delirio tanto,\
tanta ternura ante mis pies traída,\
empapada con gotas de mi llanto,\
formada con la esencia de mi vida;\
si este grito de amor, íntimo, ardiente,\
no llega a ti . . . si mi pasión es loca,\
perdona los delirios de mi mente,\
perdona las palabras de mi boca.\
\
Y ya no más mi ruego sollozante\
irá a turbar tu indiferente calma . . .\
Pero mi amor hasta el postrer instante\
te daré con las lágrimas del alma.\
\
\
Bajo las palamas\
\
Morena por el sol de mediodía\
que en llama de oro fúlgido la baña,\
es la agreste beldad del alma mía,\
la rosa tropical de la montaña.\
\
Dióle la selva su belleza ardiente;\
dióle la palma su gallardo talle;\
en su pasión hay algo del torrente\
que se despeña desbordado al valle.\
\
Sus miradas son luz, noche sus ojos;\
la pasión en su rostro centellea,\
y late el beso entre sus labios rojos\
cuando desmaya su pupila hebrea.\
\
Me tiembla el corazón cuando la nombro;\
cuando sueño con ella, me embeleso;\
y en cada flor con que su senda alfombro\
pusiera un alma como pongo un beso.\
\
Allá en las soledad, entre las flores,\
nos amamos sin fin a cielo abierto,\
y tienen nuestros férvidos amores\
la inmensidad soberbia del desierto.\
\
Ella, regia, la beldad altiva,\
soñadora de castos embelesos,\
se doblega cual tierna sensitiva\
al aura ardiente de mis locos besos.\
\
Y tiene el bosque voluptuosa sombra,\
profundos y selvosos laberintos,\
y grutas perfumadas, con alfombra\
de eneldos y tapices de jacintos.\
\
Y palmas de soberbios abanicos\
mecidos por los vientos sonoros,\
aves salvajes de canoros picos\
y lejanos torrentes caudalosos.\
\
Los naranjos en flor que nos guarecen\
perfuman el ambiente, y en su alfombra \
un tálamo los musgos nos ofrecen\
de las gallardas palmas a la sombra.\
\
Por pabellón tenemos la techumbre\
del azul de los cielos soberano,\
y por antorcha de himeneo la lumbre\
del espléndido sol americano.\
\
Y se oyen tronadores los torrentes \
y las aves salvajes en conciertos,\
en tanto celebramos indolentes\
nuestros libres amores del desierto.\
\
Los labios de los dos, con fuego impresos,\
se dicen en secreto de las almas;\
después . . . desmayan lánguidos los besos . . .\
y a la sombra quedamos de las palmas.\
\
\
\
Un beso nada más\
\
Bésame con el beso de tu boca, \
cariñosa mitad del alma mía:\
un solo beso el corazón invoca, \
que la dicha de dos... me mataría.\
\
¡un beso nadamás!... Ya su perfume\
en mi alma derramándose la embriaga\
y mi alma por tu beso se consume\
y por mis labios impaciente vaga.\
\
¡Júntese con la tuya!... Ya no puedo \
lejos tenerla de tus labios rojos... \
¡Pronto... dame tus labios!... ¡tengo miedo \
de ver tan cerca tus divinos ojos!\
Hay un cielo, mujer en tus abrazos, \
siento de dicha el corazón opreso... \
¡Oh! ¡sosténme en la vida de tus brazos \
para que no me mates con tu beso!\
\
\
\
Francesa\
\
- La tierra en donde vi la luz primera\
es vecina del golfo en que suspende\
el Po, ya fatigado, su carrera.\
\
Amor, que sin sentir el alma prende,\
A éste prendó del don, que arrebatado\
Me fue de modo que aun aquí me ofende.\
\
Amor, que obliga a amar al que es amado,\
Juntónos a los dos con red tan fuerte\
Que para siempre ya nos ha ligado.\
\
Amor hiriónos con terrible suerte;\
Y está Caín de entonces esperando\
Aquí al perverso que nos dio la muerte.\
\
Palabras tan dolientes escuchando\
Incliné sobre el pecho la cabeza,\
-¿en qué - dijo el Poeta- estás pensando?-\
\
Y respondí, movido de tristeza\
-¡Ay de mí! ¡Cuánto bello pensamiento,\
Cuánto sueño de amor y de terneza\
\
Los condujeron al fatal momento! -\
Y vuelto a ellos -¡Oh, Francesca! - dije -,\
Al corazón me llega tu lamento;\
\
Y de tal modo tu dolor me aflige,\
Que las lágrimas bañan mi semblante.\
Pero tu triste voz a mí dirige,\
\
Y dime de qué modo, en cuál instante,\
Cuando tan dulcemente suspirábais,\
Y en el fondo del alma, vacilante,\
\
Tímido aún vuestro deseo guardábais.\
¿Dime de qué manera inesperada \
os reveló el Amor que os adorábais? -\
\
Ella me respondió: - ¡Desventurada!\
¡No hay pena más aguda, más impía,\
Que recordar la dicha ya pasada\
\
En medio de la bárbara agonía\
De un presente dolor! . . . Y esa tortura\
La conoce muy bien el que te guía.\
\
Mas ya que tu piedad saber procura\
El cómo aquel amor rasgó su velo,\
Llorando te diré mi desventura.\
\
Leíamos con quietud y grato anhelo\
De Lancelote el libro cierto día,\
Solos los dos y sin ningún recelo.\
\
Leíamos . . . y en tanto sucedía\
Que dulces las miradas se encontraban\
Y el color del rostro se perdía.\
\
Un solo punto nos venció. Pintaban\
Cómo, de la ventura en el exceso,\
En los labios amados apagaban\
\
Los labios del amante, con un beso,\
La dulce risa que a gozar provoca.\
Y entonces éste, que a mi lado preso\
\
Para siempre estará, con ansia loca\
Hizo en su frenesí lo que leía . . .\
Temblando de pasión besó mi boca . . .\
\
Y no leímos más en aquel día.\
\
\
\
La Noche\
\
A Juan B. Hijar y Haro\
\
¡Salve, noche sagrada! Cuando tiendes\
desde el éter profundo\
bordada con el oro de los astros\
tu lóbrega cortina sobre el mundo;\
cuando, vertiendo la urna de la sombra,\
con el blando rocío de los beleños\
vas derramando en la Creación dormida\
las negras flores de los vagos sueños,\
el fúnebre silencio y la honda clama\
que a los misterios de no ser convida,\
entonces, como flor de las tinieblas,\
para vivir en ti, se abre mi alma.\
\
Hermosa eres ¡Oh noche!\
Hermosa cuando límpida, serena,\
Rivalizando con el mismo día,\
Rueda tu luna llena,\
Joya de Dios, en la región vacía;\
Hermosa cuando opaca,\
Esa luna, ya triste, se reclina\
En la argentada nube\
Que apenas, melancólica, ilumina,\
Tan apacible en su divina calma\
Que, viéndola, los ojos se humedecen\
Y, sin saber por qué, suspira el alma.\
\
Hermosa cuando negra\
Como el seno del caos, la eterna sombra,\
Insondable y desierta,\
Chispea de estrellas, que alumbran parecen,\
Pálidos cirios, a la tierra muerta.\
¡Y más hermosa aún, cuando agitando\
su densa cabellera de tinieblas\
trenzadas con el rayo, la tormenta\
borra los astros y fulgura y brama,\
y azotando los cielos con la llama\
del relámpago lívido, revienta!\
\
Entonces, sólo entonces, el aliento\
Del huracán que ruge embravecido, \
Al rasgar la centella el firmamento,\
Al estallar el trueno, es cuando siento\
Latir mi corazón, latir henchido\
De salvaje embriaguez . . . Quieren mis ojos\
Su mirada cruzar fiera y sombría\
Con la mirada eléctrica del rayo,\
Fatídica también. . Mi pecho ansía\
Aspirar en tu atmósfera de fuego\
Tu aliento, tempestad . . . ¡Y que se pierda\
La ardiente voz de mi agitado seno\
En la explosión magnífica del trueno!\
\
¡Quiero sentir que mi cabello azota\
la ráfaga glacial; quiero en mi frente\
un beso de huracán, y que la lluvia\
venga a mezclar sus gotas con la gota\
en que tal vez mi párpado reviente!\
\
Noche de tempestad, noche sombría,\
¿acaso tú no eres\
la imagen de lo que es el alma mía?\
Tempestad de dolores y placeres,\
Inmenso corazón en agonía. . .\
\
También así, como en sereno cielo\
De blanca luz y fúlgidas estrellas,\
Miré pasar en delicioso vuelo,\
Como esas nubes que argentó la luna,\
Fantásticas y bellas\
Mis quimeras de amor y de fortuna.\
Y así también, de pronto, la tiniebla\
Mis astros apagó, rasgó la nube\
Cárdeno rayo en explosión violenta,\
Y en mi alma desataron\
El dolor y la duda su tormenta.\
\
¿Quién como yo sintió? ¿Quién de rodillas\
cayó temblando de pasión ante Ella\
¿Quién sintiendo corres por sus mejillas\
el llanto del amor, en ese llanto\
mojó los besos que dejó en su huella?\
¿Quién como yo, mirando realizada\
la ansiada dicha que alcanzó el empeño,\
al irla a disfrutar vio disiparse\
en la sombra, en la nada,\
la mentira de un sueño?\
¿Quién de la vida al seductor banquete\
llegó jamás con juventud más loca?\
La copa del festín ¿quién más acerba \
Apartó de su boca?\
\
¿Quién como yo ha sentido\
para tanto dolor el seno estrecho,\
y de tanto sollozo comprimido\
dolerle el corazón dentro del pecho?\
¿Quién a despecho de su orgullo de hombre\
ha sentido, cual yo, del alma rota\
brotar la acerba gota\
de un escondido padecer sin nombre?\
¿Quien, soñador maldito,\
al quemar, como yo, sus dioses vanos,\
por sofocar del corazón el grito\
se apretó el corazón con ambas manos?\
¿Quién como yo, mintiendo indiferencia\
y hasta risas y calma, \
atraviesa tan solo la existencia\
con una tempestad dentro del alma?\
\
¿Quien busca, como yo, tus muertas horas\
¡oh, noche! Y tus estrellas,\
fingiendo que son ellas\
las lágrimas de luz con que tú lloras?\
¿Quién ama como yo tu sombra muda,\
tu paz de muerte, y el silencio grave,\
a quien la voz de los misterios diste,\
y tus suspiros que las auras llevan,\
y tu mirada de luceros triste?\
\
Mi alma es la flor, la flor de las tinieblas,\
El cáliz del amor y los dolores,\
Y se abre, ¡oh, noche! En tu regazo frío,\
Y espera, así como las otras flores,\
Tu bienhechor rocío.\
\
Hijo yo del dolor, tu negra clama\
Es el mejor abrigo,\
Para ver en la sombra, sin testigo,\
Una noche en el cielo, otra en el alma.",
                    path=u"/c", tags=u"MMF")


writer.add_document(title=u"Salvador Diaz Miron", content=u"La oración del preso\
 \
 ¡Señor, tenme piedad, aunque a ti clame\
 sin fe! ¡perdona que te niegue o riña\
 y el ara tienda con bochorno infame!\
 \
 Vuelvo al antiguo altar. ¡No en vano ciña\
 guirnaldas a un león y desparrame\
 riego que pueda prosperar tu viña!\
 \
 ¡Líbrame por merced, como te plugo\
 a Bautista y Apóstol en Judea,\
 ya que no me suicido ni me fugo!\
 \
 ¡Inclínate al cautivo que flaquea;\
 y salvo, como Juan por el verdugo,\
 o como Pedro por el ángel sea!\
 \
 Habito un orco infecto; y en el manto\
 resulto cebo a chinche y pulga y piojo;\
 ¡y afuera el odio calumnia en tanto!\
 \
 ¿Qué mal obré para tamaño enojo?\
 El honor del poeta es nimbo santo\
 ¡y la sangre de un vil es fango rojo!\
 \
 Mi pobre padre cultivó el desierto.\
 Era un hombre de bien, un sabio artista,\
 y de vergüenza y de pesar ha muerto!\
 \
 ¡Oh mis querubes!  ¡Con turbada vista\
 columbro ahora el celestial e incierto\
 grupo que aguarda, y a quien todo atrista!\
 \
 ¡Y oigo un sordo piar de nido en rama,\
 un bullir de polluelos ante azores;\
 y el soplado tizón encumbra llama!\
 \
 ¡Dios de Israel, acude a mis amores:\
 y rían a manera de la grama,\
 que hasta batida por los pies da flores!\
 \
 Cárcel de Veracruz. Septiembre de 1895.\
 \
 \
 Canción medioeval\
 \
 ¡Oh tú de crin rubia, luenga y rizada,\
 que caída en torrente barre las losas,\
 y que volando incita las mariposas,\
 porque así luce aspecto de llamarada!\
 \
 ¡Linajuda Regina que, por taimada,\
 finges al viejo duque modelo a esposas,\
 y de sus canas dices honestas cosas,\
 más dignas de la espuma de una cascada!\
 \
 ¡Ven y place al que tiene la voz dorada,\
 y perennes ortigas y eternas rosas,\
 y en el talón espuela y al cinto espada!\
 \
 No ignores que los himnos hacen las diosas\
 ¡oh tú la de crin rubia, luenga y rizada,\
 que caida en torrente barre las losas!\
 \
 El fantasma\
 \
 Blancas y finas, y en el manto apenas\
 visibles, y con aire de azucenas,\
 las manos -que no rompen mis cadenas.\
 \
 Azules y con oro enarenados,\
 como las noches limpias de nublados,\
 los ojos - que contemplan mis pecados.\
 \
 Como albo pecho de paloma el cuello;\
 y como crin de sol barba y cabello;\
 y como plata el pie descalzo y bello.\
 \
 Dulce y triste la faz; la veste zarca...\
 Asi, del mal sobre la inmensa charca,\
 Jesús vino a mi unción, como a la barca.\
 \
 Y abrillantó a mi espíritu la cumbre\
 con fugaz cuanto rica certidumbre,\
 como con tintas de refleja lumbre.\
 \
 Y suele retornar; y me reintegra\
 la fe que salva y la ilusión que alegra;-\
 y un relámpago enciende mi alma negra.\
 \
 Cárcel de Veracruz. El 14 de diciembre de 1893\
 \
 Nox\
 \
 Noy hay almíbar ni aroma\
 como tu charla...\
 ¿Qué pastilla olorosa\
 y azucarada\
 disolverá en tu boca\
 su miel y su ámbar,\
 cuando conmigo a solas\
 ¡oh virgen! ¿hablas?\
 \
 La fiesta de tu boda\
 será mañana.\
 \
 A la nocturna gloria\
 vuelves la cara,\
 linda más que las rosas\
 de la ventana;\
 y tu guedeja blonda\
 vuela en el aura\
 y por azar me toca\
 la faz turbada...\
 \
 La fiesta de tu boda\
 será mañana.\
 \
 Un cometa en la sombra\
 prende una cábala.\
 Es emblema que llora,\
 signo que canta.\
 El astro tiene forma\
 de punto y raya:\
 representa una nota,\
 ¡pinta una lágrima!\
 \
 La fiesta de tu boda\
 será mañana.\
 \
 En invisible tropa\
 las grullas pasan,\
 batiendo en alta zona\
 potentes alas;\
 y lúgubres y roncas\
 gritan y espantan...\
 ¡parece que deploran\
 una desgracia!\
 \
 La fiesta de tu boda\
 será mañana.\
 \
 Nubecilla que flota,\
 que asciende o baja,\
 languidecida y floja,\
 solemne y blanca,\
 muestra señal simbólica\
 de doble traza:\
 ¡finge un velo de novia\
 y una mortaja!\
 \
 La fiesta de tu boda\
 será mañana.\
 \
 Junto al cendal que toma\
 figura mágica.\
 Escorpión interroga,\
 mientras que su alfa\
 es carmesí que brota...\
 nuncio que sangra...\
 ¡Y Amor y Duelo aprontan\
 distintas armas!\
 \
 La fiesta de tu boda\
 será mañana.\
 \
 ¡Ah! Si la Tierra sórdida\
 que por las vastas\
 oquedades enrolla\
 su curva esclava,\
 diese fin a sus rondas\
 y resultara\
 ¡desvanecida en borlas\
 de tenue gasa...!\
 \
 La fiesta de tu boda\
 será mañana.\
 \
 El mar con débil ola\
 tiembla en la playa,\
 y no inunda ni ahoga\
 pueblos, ni nada.\
 Del fuego de Sodoma\
 no miro brasa,\
 y la centella es rota\
 flecha en aljaba.\
 \
 La fiesta de tu boda\
 será mañana.\
 \
 ¡Oh Tirsa! Ya es la hora.\
 Valor me falta;\
 y en un trino de alondra\
 me dejo el alma.\
 Un comienzo de aurora\
 tiende su nácar,\
 y Lucifer asoma\
 su perla pálida.\
 \
 Engarce\
 \
 El misterio nocturno era divino.\
 Eudora estaba como nunca bella,\
 y tenía en los ojos la centella,\
 la luz de un gozo conquistado al vino.\
 \
 De alto balcón apostrofóme a tino;\
 y rostro al cielo departí con ella\
 tierno y audaz, como con una estrella...\
 ¡Oh qué timbre de voz trémulo y fino!\
 \
 ¡Y aquel fruto vedado e indiscreto\
 se puso el manto, se quitó el decoro,\
 y fue conmigo a responder a un reto!\
 \
 ¡Aventura feliz! -La rememoro\
 con inútil afán; y en un soneto\
 monto un suspiro como perla de oro.\
 \
 Veracruz. Julio de 1900\
 \
  \
 Lance\
 \
 Es un viejo borracho que me provoca,\
 que me cierra el camino y al diablo evoca,\
 recio, locuaz, inmundo, descalzo y fiero,\
 con terribles ojazos de un gris de acero\
 y con una calvicie de yerma roca.\
 -La testa perdió greña, razón y toca.\
 \
 Hasta el pecho la barba se le desliza,\
 como espuma de arroyo por cana y riza.\
 La diestra dura y fuerte, como una marra,\
 enseña entre uñas corvas, como de garra,\
 pipa roja con aire de cruenta triza.\
 -La mano es tan aleve como maciza.\
 \
 Paro el corcel fogoso y alzo la fusta...\
 -Occiduo el Sol corona cúspide augusta,\
 y el ebrio tiene al rubro y oblicuo rayo\
 sangre a linfas rebelde que aun pinta el sayo-.\
 Y me afirmo en el potro, y él se me asusta,\
 y el anciano derriba y en lodo incrusta.\
 \
 Idilio\
 \
 A tres leguas de un puerto bullente\
 que a desbordes y grescas anima,\
 y al que a un tiempo la gloria y el clima\
 adornan de palmas la frente,\
 hay un agrio breñal, y en la cima\
 de un alcor un casucho acubado,\
 que de lejos diviso a menudo,\
 y rindiéndose apoya un costado\
 en el tronco de un mango copudo.\
 \
 Distante, la choza resulta montera\
 con borla y el sesgo cobre una mollera.\
 \
 El sitio es ingrato, por fétido y hosco.\
 El cardón, el nopal y la ortiga\
 prosperan; y el aire trasciende a boñiga,\
 a marisco y a cieno; y el mosco\
 pulula y hostiga.\
 \
 La flora es enérgica para\
 que indemne y pujante soporte\
 la furia del soplo del Norte,\
 que de octubre a febrero no es rara,\
 Y la pródiga lumbre febea,\
 que de marzo a septiembre caldea.\
 \
 El Oriente se inflama y colora,\
 como un ópalo inmenso en un lampo,\
 y difunde sus tintes de aurora\
 por piélago y campo.\
 Y en la magia que irisa y corusca,\
 una perla de plata se ofusca.\
 \
 Un prestigio rebelde a la letra,\
 un misterio inviolable al idioma,\
 un encanto circula y penetra\
 y en el alma es edénico aroma.\
 Con el juego cromático gira,\
 en los pocos instantes que dura;\
 y hasta el pecho infernado respira\
 un olor de inocencia y ventura.\
 ¡Al través de la trágica Historia,\
 un efluvio de antigua bonanza\
 viene al hombre, como una memoria,\
 y acaso como una esperanza!\
 \
 El ponto es de azogue y apenas palpita.\
 Un pesado alcatraz ejercita\
 su instinto de caza en la fresca.\
 Grave y lento, discurre al soslayo,\
 escudriña con calma grotesca,\
 se derrumba cual muerto de un rayo,\
 sumérgese y pesca.\
 \
 Y al trotar de un rocín flaco y mocho,\
 un moreno, que ciñe moruna,\
 transita cantando cadente tontuna\
 de baile jarocho.\
 \
 Monótono y acre gangueo,\
 que un pájaro acalla, soltando un gorjeo.\
 \
 Cuanto es mudo y selecto en la hora,\
 en el vasto esplendor matutino,\
 halla voz en el ave canora,\
 ¡vibra y suena en el chorro del trino!\
 \
 Y como un monolito pagano,\
 un buey gris en un yermo altozano\
 mira fijo, pasmado y absorto,\
 la pompa del orto.\
 \
 Y a la puerta del viejo bohío\
 que oblicuando su ruina en la loma\
 se recuesta en el árbol sombrío-,\
 una rústica grácil asoma,\
 como una paloma.\
 \
 Infantil por edad y estatura,\
 sorprende ostentando sazón prematura:\
 elásticos bultos de tetas opimas;\
 y a juzgar por la equívoca traza,\
 ¡no semeja sino una rapaza\
 que reserva en el seno dos limas!\
 \
 Blondo y grifo e inculto el cabello,\
 y los labios turgentes y rojos,\
 y de tórtola el garbo del cuello,\
 y el azul del zafiro en los ojos.\
 Dientes albos, parejos, enanos,\
 que apagado coral prende y liga,\
 que recuerdan, en curvas de granos,\
 el maiz cuando tierno en la espiga.\
 La nariz es impura, y atesta\
 una carne sensual e impetuosa;\
 y en la faz, a rigores expuesta,\
 la nieve da en ámbar, la púrpura en rosa,\
 y el júbilo es gracia sin velo\
 y en cada carrillo produce un hoyuelo.\
 \
 La payita se llama Sidonia.\
 Llegó a México en una barriga:\
 en el vientre de infecta mendiga\
 que, del fango sacada en Bolonia,\
 formó parte de cierta colonia\
 y acabó de miseria y fatiga.\
 \
 La huérfana ignara y creyente\
 busca sólo en los cielos el rastro;\
 y de noche imagina que siente\
 besos ¡ay! en los hilos de un astro.\
 ¿Que ilusión es tan dulce y hermosa?\
 Dios le ha dicho: ¡'Sé plácida y bella;\
 y en el duelo que marque una fosa\
 por la fe que contemple una estrella'!\
 ¿Quién no cede al consuelo que olvida?\
 La piedad es un santo remedio;\
 y después, el ardor de la vida\
 urge y clama en la pena y el tedio\
 y al tumulto y al goce convida.\
 De la zafia el pesar se distrae-,\
 desplome de polvo y ascenso de nube.\
 ¡Del tizón la ceniza que cae\
 y el humo que sube!\
 \
 La madre reposa con sueño de piedra.\
 La muchacha medra.\
 \
 Y por siembras y apriscos divaga\
 con su padre, que duda de serlo;\
 y el infame la injuria y estraga\
 y la triste se obstina en quererlo.\
 Llena está de pasión y de bruma,\
 tiene ley en un torpe atavismo,\
 y es el cierzo del mal una pluma...\
 ¡Oh pobreza! ¡Oh incuria! ¡Oh abismo!\
 \
 Vestida con sucios jirones de paño,\
 descalza y un lirio en la greña,\
 la pastora gentil y risueña\
 camina detrás del rebaño.\
 \
 Radioso y jovial firmamento.\
 Zarcos fondos, con blancos celajes\
 como espumas y nieves al viento\
 esparcidas en copos y encajes.\
 \
 Y en la excelsa y magnífica fiesta,\
 y cual mácula errante y funesta,\
 un vil zopilote resbala,\
 tendida e inmóvil el ala.\
 \
 El Sol meridiano fulgura,\
 suspenso en el Toro;\
 y el paisaje, con varia verdura,\
 parece artificio de talla y pintura,\
 según está quieto en el oro.\
 \
 El fausto del orbe sublime\
 rutila en urgente sosiego;\
 y un derribo de paz y de fuego\
 baja y cunde y escuece y oprime.\
 \
 Ni céfiro blando que aliente, que rase,\
 que, corra, que pase.\
 \
 Entre dunas aurinas que otean-,\
 tapetes de grama serpean,\
 cortados a trechos por brazos hostiles,\
 que muestran espinas y ocultan reptiles.\
 Y en hojas y tallos un brillo de aceite\
 simula un afeite.\
 \
 La luz torna las aguas espejos;\
 y en el mar sin arrugas ni ruidos\
 reverbera con tales reflejos,\
 que ciega, causando vahidos.\
 \
 El ambiente sofoca y escalda;\
 y encendida sudando, la chica\
 se despega y sacude la falda,\
 y así se abanica.\
 \
 Los guiñapos revuelan en ondas...\
 La grey pace y trisca y ahogándose tarda.\
 Y al amparo de umbráticas frondas\
 la palurda se acoge y resguarda.\
 \
 Y un borrego con gran cornamenta\
 y pardos mechones de lana mugrienta,\
 y una oveja con bucles de armiño-,\
 la mejor en figura y aliño-,\
 se copulan con ansia que tienta.\
 \
 La zagala se turba y empina...\
 y alocada en la fiebre del celo,\
 lanza un grito de gusto y de anhelo...\
 ¡Un cambujo patán se avecina!\
 \
 Y en la excelsa y magnífica fiesta,\
 y cual mácula errante y funesta,\
 un vil zopilote resbala,\
 tendida e inmóvil el ala.\
 \
 \
 A ti\
 \
 Portas al cuello la gentil nobleza\
 del heráldico lirio; y en la mano\
 el puro corte del cincel pagano;\
 ¡y en los ojos abismos de belleza!\
 \
 Hay en tus rasgos acritud y alteza,\
 orgullo encrudecido en un arcano;\
 ¡y resulto en mi prez un vil gusano\
 que a un astro empina la bestial cabeza!\
 \
 ¡Quiero pugnar con el amor; y en vano\
 mi voluntad se agita y endereza,\
 como la grama tras el pie tirano!\
 \
 Humillas mi elación y mi fiereza;\
 ¡y resulto en mi prez un vil gusano\
 que a un astro empina la bestial cabeza!\
 \
 Xalapa. El 25 de mayo de 1901.\
 \
  \
 A ella\
 \
 Semejas esculpida en el más fino\
 hielo de cumbre sonrojado al beso\
 del Sol, y tienes ánimo travieso,\
 y eres embriagadora como el vino.\
 \
 Y mientras: no imitaste al peregrino\
 que cruza un monte de penoso acceso,\
 y párase a escuchar con embeleso\
 un pájaro que canta en el camino.\
 \
 Obrando tú como rapaz avieso,\
 correspondiste con la trampa del trino,\
 ¡por ver mi pluma y torturarme preso!\
 \
 No así al viandante que se vuelve a un pino\
 y párase a escuchar con embeleso\
 un pájaro que canta en el camino.\
 \
 Xalapa  27 de mayo de 1901.\
 \
   \
 Gris perla\
 \
 Siempre aguijo el ingenio en la lírica;\
 y él en vano al misterio se asoma\
 a buscar a la flor del Deseo\
 vaso digno del puro Ideal.\
 ¡Quién hiciera una trova tan dulce,\
 que al espíritu fuese un aroma,\
 un ungüento de suaves caricias,\
 con suspiros de luz musical!\
 \
 Por desdén a la pista plebeya,\
 la Ilusión empinada en su loma\
 quiere asir, ante límpidas nubes,\
 virtud alta en sutil material;\
 Pero el Alma en el barro se yergue,\
 y el magnífico afán se desploma-,\
 y revuelca sus nobles armiños\
 en el negro y batido fangal.\
 \
 La palabra en el metro resulta\
 baja y fútil pirueta en maroma;\
 un funámbulo erecto pontífice\
 lleva manto de pompa caudal;\
 y si el Gusto en sus ricas finezas\
 pide nuevo poder al idioma,\
 ¡aseméjase al ángel rebelde\
 que concita en el reino del mal!\
 ¡Quién hiciera una trova tan dulce,\
 que al espíritu fuese un aroma,\
 un ungüento de suaves caricias,\
 con suspiros de luz musical!\
 \
  \
 Claudia\
 \
 Con hermana y cuñado veranea\
 En quinta señoril, sobre un ribazo,\
 Asiento y gracia de salubre aldea.\
 Y no para en el rústico regazo;\
 Y es como una paloma que aletea\
 Por eludir o quebrantar un lazo.\
 \
 ¡Un amor doloroso e inconfeso\
 que le punza la sien como una espina,\
 y que le sella el labio como un beso;\
 y que no es como un fruto que se inclina\
 en débil fibra, por el grave peso,\
 y cae a la primera ventolina!\
 \
 Como helénica estatua, por la suma\
 Corrección de la forma; tez morena;\
 Negro y lustre de corvina pluma\
 En la rizada y pródiga melena;\
 Y ojos que afectan, en su gris de bruma,\
 Transparencias de linfa sobre arena.\
 \
 ¡Y qué voz! ¡Cómo vibra en cada nota!\
 Cambia de timbre y tono en un instante.\
 Emperlada y sutil fluye y borbota,\
 Cual por lecho de guijas onda errante;\
 Y en transición violenta rompe y brota\
 Con aristas que hirieran el diamante.\
 \
 ¡Hermosura infeliz! Arrostra y huella\
 fiero cráter; y a guisa de aureola,\
 ciñe y carga en la frente una centella.\
 A un deber sacrantísimo se inmola;\
 Y arde con el sigilo de una estrella\
 En los nublados indistinta y sola.\
 \
 Prueba coraza en donde sufre injuria;\
 Halla en su doble ser ímpetu y traba;\
 Y hervorosa de honor y de lujuria,\
 Y a un mismo tiempo meritoria y prava,\
 Muestra el pesar, la humillación, la furia\
 De una deidad que se sintiera esclava.\
 \
 Huye del trato y se resiste al brillo;\
 Y busca en el encierro una quimera:\
 La paz del corazón puro y sencillo.\
 ¡Como si por milagro consiguiera,\
 al golpe de la puerta en el pestillo,\
 burlar sus cuitas y dejarlas fuera!\
 \
 En pequeño batel hiende la rada,\
 Rigiendo con primor caña y escota;\
 Y dice a la tormenta: ¡'camarada'!\
 Y en el peligro y sin temerlo flota;\
 ¡Y de todo su afán no arroja nada\
 En su curso y su grito de gaviota!\
 \
 ¡Pobre mujer! Al rayo de la Luna,\
 pasea su desvelo y su histerismo,\
 lamentando el rigor de su fortuna.\
 Conversa con un faro del abismo;\
 Y a los misterios de la noche aduna\
 Su secreto, su oprobio, su heroísmo.\
 \
 ¡Admirable amazona la doncella!\
 Pide un corcel, y en el sillín de planta\
 nerviosa y ágil, cimbradora y bella;\
 y parte con un nudo en la garganta;\
 y compele y fustiga y atropella...\
 ¡y a su cruel torcedor no se adelanta!\
 \
  Porta en alto su nombre, como el lirio\
 Su estambre, la palmera su verdura,\
 Su airón el casco, su fulgor el cirio,\
 La fe su emblema y el volcán su albura\
 Y a veces los antojos de un delirio\
 Infiernan a la extraña criatura.\
 \
 Y en el espasmo súbito que al vuelo\
 De la colgante y columpiada soga\
 Muere y crispa las carnes del chicuelo-,\
 Claudia, gime, se increpa, se desfoga,\
 Y a pezones erguidos mira el cielo,\
 Y aun osa blasfemar, porque se ahoga.\
 \
 Y luego ante una efigie se arrodilla;\
 Y ¡ay! No logra en la espuma del torrente\
 Aferrarse a la rama de la orilla.\
 Plañe y ora, confusa y penitente;\
 ¡Dase a Dios, azorada y amarilla;\
 Y en un vértigo va por la corriente!\
 \
 ¡Ciega y tenaz la religión del triste\
 que demanda mercedes que no alcanza\
 y en adorar por obtener insiste!\
 ¡Cándida y portentosa confianza\
 en una providencia que no existe\
 en otra inmensidad que la esperanza!\
 \
 * * *\
 \
 Cabe un lago de múrice, - como radial corona,\
 O escudo excelso y nítido, el Sol occiduo esplende;\
 Y por el claro piélago inflada y sesga lona\
 Resbala, con un ósculo del astro que desciende.\
 \
 El mísero casucho y la soberbia granja\
 ostentan igual fausto, bermejo al par que blondo;\
 Y entre plomizas nubes aurina y crespa franja\
 Corta de Oriente a Ocaso el curvo y zarco fondo.\
 \
 ¡Mirífico el paisaje! Cromáticos vapores\
 ruedan en copos fusiles, que un hálito desliga;\
 y de arrebol purpúreos los bueyes aradores\
 surcan los mondos predios y mugen de fatiga.\
 \
 En áspera y herbosa ladera que dilata\
 sus pliegues en profuso y ameno desarrollo,\
 lanuda grey blanquea, como bullente plata\
 que sobre ponto glauco revela oculto escollo.\
 \
 En el confín las cumbres, cubiertas de celajes,\
 suspenden y subliman la extremidad agreste.\
 Así en pos de un prócer las manos de los pajes\
 levantan y sustentan la fimbria de la veste.\
 \
 El fango en la hondonada resulta pedrería;\
 los pájaros gorjean en tumultuario coro;\
 y oblicuo el trapo túrgido, el barquichuelo estría\
 un mar que arruga en rasos el índigo y el oro.\
 \
 Pero por amplio rumbo, abajo abierto adrede,\
 la nave se rellena de líquido salobre.\
 La tarde se destiñe y a la penumbra cede\
 y el magno dombo asume la pátina del cobre.\
 \
 Obscuro y vago aspecto de lira se dibuja\
 al Noroeste; rachas con lúgubre armonía\
 llegan; y el agua es cólera que gruñe y salta y puja\
 y con fragor voltea nevada serranía.\
 \
 Y cual humoso aroma venido por encanto\
 desde una catacumba que la piedad inciensa,\
 yna melancolía de iglesia y campo santo\
 se añade augusta y fúnebre a la borrasca intensa.\
 \
 Sentada en el esquife, y con sayal de luto,\
 y sueltos en dos alas convulsas los cabellos,\
 y el firmamento el rostro, ya cárdeno y enjuto,\
 la joven ve apagarse los últimos destellos.\
 \
 Y en su ánimo y orgullo, que de temblar la eximen\
 se forja en la catástrofe patrañas prodigiosas.\
 Figúrase que reina en el horror de un crimen\
 tan grande, que perturba el orden de las cosas.\
 \
 Rabia y estruendo y caos. Ni un plácido reflejo.\
 Ni rútilos encajes, ni sábanas carmíneas.\
 ¡Hostil y enorme cúpula, como de bronce viejo,\
 arquea, parda y próxima, sus implacables líneas!\
 \
 ¡Hora siniestra y larga, fatídica y suprema!\
 el bote combatido e hidrópico se hunde;\
 y cual de miedo loca, la vela en jiras trema\
 en las silbantes ráfagas; y la tiniebla cunde.\
 \
 ¡Ola que airada y túmida y resonante meces\
 en tus agruras íntimas el trágico despojo:\
 ten lástima y resérvalo al hambre de los peces,\
 o recogido y grávido publicará un sonrojo!\
 \
  \
 A Tirsa\
 \
 ¡Ah! ¿Qué mucho que al Sol que subía\
 se plagiara en divino esplendor\
 alma en quieto remanso la mía,\
 por abril, entre ramos en flor?\
 \
 No cayera por brusca pendiente,\
 y sería, como ante quizá,\
 linfa pura y festiva el torrente\
 que frenético y túrbido va.\
 \
 Envidiosos me culpan con saña\
 y me niegan al par honra y fe...\
 ¡Estupenda y horrible patraña\
 triunfa, puesto en mi cólera el pie!\
 \
 Y un consuelo has escrito a mis penas;\
 y la tinta consagra el favor,\
 si es carmín que ha corrido en tus venas\
 y por mí ha pintado un rubor.\
 \
 ¡Con qué brotes la planta retoña!\
 la fortuna es infausta y no cruel,\
 pues que al mísero escancia ponzoña\
 Y unge al vaso en el borde una miel.\
 \
 Un misterio me asombra e infatua:\
 la ternura de un buen corazón,\
 y que un viento derribe la estatua\
 y no logre apagar el blandón.\
 \
 ¿Esperanzas? La suerte me abruma.\
 A rivales mi prez causó mal,\
 y en mi afrenta redoro mi gloria\
 y en la herida reclavo el puñal.\
 \
 Sueño y rimo. La noche adelanta\
 su prestigio parece de ti.\
 A lo lejos un pájaro canta\
 y ¡ay! me dice que lloras por mí.\
 \
 Una estrella fugaz viene al suelo,\
 deshilando en la sombra un fulgor...\
 Una lágrima rueda en el cielo...\
 es de ángel que acude al dolor!\
 \
 Cárcel de Veracruz. Noviembre de 1892.\
 \
  \
 A mis versos\
 \
 Insensibles a fiestas y grimas\
 y con alas de luz de centellas,\
 pero esquivos a cautas doncellas,\
 difundíos por gentes y climas.\
 \
 No sois gemas inmunes a limas\
 y con lampos de fijas estrellas,\
 sino chispas de golpes y mellas\
 y ardéis lascas de piedras de simas.\
 \
 Pero hay siempre valer en las rimas.\
 Por que duran refranes? Por ellas,\
 y no suelen llevarlas opimas.\
 \
 Id, las mías, deformes o bellas:\
 inspirad repugnancias o estimas,\
 pero no sin dejar hondas huellas.\
 \
 index.jpg (2009 bytes)\
 \
 Epístola joco-seria\
 \
 Al Editor\
 \
 Mientras haya en ciudad y cortijo\
 gallineros que ostenten su rijo;\
 y por calles, y en lúbricos tratos,\
 ardentías de perros o gatos;\
 y en el aire y el muro y el suelo\
 moscas tiernas, a pares, en celo;\
 mi librillo en palacios y chozas\
 ha de ser inocente a las mozas.\
 \
 Pero quise pecar de discreto;\
 y en extraño y heroico soneto\
 dejo dicho a mis trovas que apiñas:\
 ¡'respetad el pudor de las niñas'!\
 Por 'Idilio' y 'Avemus', y acaso\
 algún otro desliz en el paso,\
 lo demás, que no funda querellas,\
 ¡sufrirá privación de doncellas!\
 \
 ¿A las chicas ofreces lectura\
 de un primor: la Sagrada Escritura.\
 Y Sodoma con fieros priapismos\
 amagando a los ángeles mismos\
 que se libran merced a un encanto?\
 ¿y las hijas de Lot? ¿Y el Rey Santo,\
 Betsabé y el cadáver de Urías?\
 ¿Y Tamar con Amón?  ¡Fruslerías!\
 \
 ¡Ay! Las cosas en sí quedan lejos.\
 Sólo dan al sensorio reflejos.\
 En mí el Cosmos intima señales\
 y es un haz de impresiones mentales.\
 Pero cunde al través de una lente\
 comba y tinta y jamás indolente,\
 que perturba en la imagen virgínea\
 el matiz, el calor y la línea.\
 \
 ¿Qué cristal el que filtra y altera?\
 pues mi humor peculiar, mi manera.\
 para mí, por virtud de objetivo,\
 todo existe según lo percibo.\
 Y el tamiz proporciona elemento\
 propio y lírico al gayo talento,\
 y es quien pone carácter y timbre,\
 novedad y valor a la urdimbre.\
 \
 Pese a ti, lo real no anda fuera,\
 sino en sellos del alma, y espera\
 que facundia o cincel, brocha o pluma,\
 tornen diáfano el cerco de bruma\
 externarse con metro gallardo\
 y en fiel copia es el triunfo del bardo.\
 La mentira es la muerte y la escoria.\
 La verdad es la vida y la gloria.\
 \
 Cuando pugno en las bregas del arte\
 por verter en trasunto una parte\
 del caudal que atesoro por dentro,\
 y en las voces hurañas encuentro\
 la precisa expresión y el buen giro\
 ¡que alborozo y que orgullo respiro!\
 ¡Cuán me alegra y ufana el acierto!\
 ¡Un oasis hallado al desierto!\
 \
 ¿La moral? ¡Es el ara divina!\
 mas escúchame, piensa y atina.\
 Una cosa en la práctica es fiemo,\
 es horror, ese feísimo extremo;\
 pero exacta en la intensa pintura,\
 resplandece magnífica y pura,\
 si allí el vate no insufla malicia,\
 sino un grito a la eterna justicia!\
 \
 ¿Que la nota poluta y la torva\
 vibran mucho en el son de mi troba?\
 en el mundo lo dulce y lo claro\
 son, por ley de la suerte, lo raro.\
 ¿Cómo hacerlos aquí lo frecuente?\
 No: la cámara obscura no miente.\
 Además: la tragedia sublime\
 ¡en piedad y terror, sangra y gime!\
 \
 Forma es fondo; y el fausto seduce\
 si no agranda y tampoco reduce.\
 Que un estilo no huelgue ni falte,\
 ¡por hincar en un yerro un esmalte!\
 que la veste resulte ceñida\
 al rigor de la estrecha medida,\
 aunque muestre, por gala o decoro,\
 opulencias de raso y de oro.\
 \
 ¿Qué repulsas mi código? Basta.\
 La bandera, prendida en el asta\
 y undulando a las rachas supremas,\
 luce y riza colores y lemas;\
 y debajo a que nadie los toque,\
 y blandiendo flamígero estoque,\
 una musa de fuerza y de gracia\
 yergue al sol su hermosura y su audacia!\
 \
 El pedestinado\
 \
 \
 Bajo el ronco motín que grita muerte,\
 el sagrado bajel cruje de suerte\
 que semeja reír - El genio es fuerte;\
 \
 \
 Y aún ante indicio, de locura o dolo,\
 no culpa de falaz a Marco Polo,\
 y se obstina en creer, inmenso y solo.\
 \
 Su fe suele medrar cuando vacila...\
 ¡Así la llama del hachón oscila\
 al viento, y es mayor por intranquila!\
 \
 En el ignoto piélago la nave\
 sigue al azar el ímpetu de un ave.\
 ¿A dónde va? ¡Ni el Genovés lo sabe!\
 \
 A la esperanza el mísero se aferra,\
 como a la tabla el náufrago que yerra\
 en la furia del mar. La noche cierra.\
 \
 Bien luego magnífica su corona...\
 Y es que Dios con su soplo hincha la lona,\
 ¡desde los astros de la nueva zona!\
 \
 Voz que nace al timón sube a la caña...\
 ¡El Ponto bulle con cadencia extraña\
 y parece que dice: ¡Viva España!\
 \
 Colón, en pie sobre la proa mira...\
 ¡Y en el cordaje un hálito respira\
 Y canta, como un estro en una lira!\
 \
 Franja de luna por el agua riela...\
 ¡Y al grande hombre simula rica estela,\
 rastro de victoriosa carabela!\
 \
 Música de schubert\
 \
 \
 Crin que al aire te vuela, rizada y bruna\
 parece a mis ahogos humo en fogata;\
 y del harpa desprendes la serenata\
 divinamente triste, como la luna.\
 \
 Y del celo ardoroso despides una\
 fragancia de resina; y él te dilata\
 ojo que resplandece con luz de plata,\
 como en la sombra el vidrio de la laguna.\
 \
 Mas tu mirada llega, con su fortuna,\
 nos dice dos lisonjas, va por su bata,\
 y al dormido chicuelo besa en la cuna.\
 \
 Y mientras que te tiñes en escarlata,\
 crin que al aire te vuela, rizada y bruna,\
 parece a mis ahogos humo en fogata.\
 \
 Excélsior\
 \
 \
 Conservo de la injuria,\
 no la ignominia; pero si la marca.\
 ¡Sentíme sin honor, cegué de furia,\
 y recogilo de sangrienta charca!\
 \
 Y hórrido amago suena...\
 Así la racha en el desierto zumba,\
 ¡cuando en crecientes vórtices de arena\
 corre a ceñir al árabe la bumba!\
 \
 ¡Infames! Os agravia\
 que un alma superior aliente y vibre;\
 y en vuestro miedo, trastocado en rabia,\
 vejáis cautivo al que adularais libre.\
 \
 Cruel fortuna dispensa\
 favor al odio de que hacéis alardes.\
 Estoy preso, caído, sin defensa...\
 podéis herir y escarnecer, ¡cobardes!\
 \
 Al mal dolos procuren\
 fuerza y laurel que la razón no alcanza.\
 ¡Aún se cantar; y en versos que perduren\
 publicaré a los siglos mi venganza!\
 \
 Sobre la impura huella\
 del fraude, la verdad austera y sola\
 brilla, como el silencio de una estrella\
 por encima del ruido de una ola.\
 \
 Cárcel de Veracruz, Julio de 1892.\
 \
 Cintas de sol\
 \
 I\
 \
 La joven madre perdió a su hijo,\
 se ha vuelto loca y está en su lecho,\
 eleva un brazo, descubre un pecho,\
 suma las líneas de un enredijo.\
 \
 \
 El dedo en alto y el ojo fijo,\
 cuenta las curvas de adorno al techo;\
 y muestra un rubro pezón, derecho\
 como un espasmo y ardor de rijo.\
 \
 En la vidriera cortina rala\
 tensa y purpúrea cierne curiosa\
 lumbre, que tiñe su tenue gala.\
 \
 Y roja lengua cae y se posa,\
 ¡y con delicia teme y resbala\
 en el erecto botón de rosa!\
 \
 II\
 \
 Cerca el marido forma concierto:\
 ofrece al torpe fulgor del día\
 desesperada melancolía;\
 ¡y en la cicuta prueba el desierto!\
 \
 ¡Ah! Los olivos del sacro huerto\
 guardan congoja ligera y pía.\
 El hombre sufre doble agonía:\
 ¡la esposa insana y el niño muerto!\
 \
 Y no concibe suerte mas dura,\
 y con el puño crispado azota\
 la sien, y plañe su desventura.\
 \
 Llora en un lampo la dicha rota;\
 ¡y el rayo juega con la tortura\
 y enciende un iris en cada gota!\
 \
 III\
 \
 Así la lira. ¿Qué grave duelo\
 rima el sollozo y enjoya el luto,\
 y a la insolencia paga tributo\
 y en la jactancia procura vuelo?\
 \
 ¿Qué mano digna recama el velo\
 y la ponzoña del triste fruto,\
 y al egoísmo del verso bruto\
 inmola el alma que mira el cielo?\
 \
 La poesía canta la historia;\
 y pone, ¿fértil en pompa espuria?,\
 ¡a mal de infierno burla de gloria!\
 \
 ¡Es implacable como una furia,\
 y pegadiza como una escoria,\
 e irreverente como una injuria!\
 \
 Duelo\
 \
 \
 Llego entre dos esbirros, que no dudan\
 de que a un monstruo feroz guardan y aquietan.\
 Gritos desgarradores me saludan\
 y brazos epilépticos me aprietan.\
 \
 Suspenso en el umbral callo y vacilo.\
 Alto y grueso blandón muestra y agrava\
 con lampo incierto el espantable asilo.\
 La llama teme al soplo, sesga y flava...\
 ¡Pugna por arrancarse del pabilo\
 y huir de penas que ilumina esclava!\
 \
 Sobre mezquino y enlutado lecho,\
 y en negro traje que semeja extraño,\
 y las manos unidas en el pecho,\
 y al vientre hielo y en la faz un paño,\
 el cuerpo yace inmóvil y derecho.\
 \
 Y ante la forma en que mi padre ha sido,\
 lloro, por mas que la razón me advierta\
 qué un cadáver no es trono demolido,\
 ni roto altar, sino prisión desierta.\
 \
 ¿Qué amigo que no acuda y me acompañe?\
 la turba, que penetra sin permiso,\
 rodea el catre funeral y plañe;\
 y en el cercano templo el bronce tañe\
 lento y lúgubre adiós al manumiso.\
 \
 Al pueblo el bardo es gracia y no carcoma.\
 Es como el floripondio de la linde\
 qué cándido y triunfal surge y asoma,\
 y al polvo de la senda torna y rinde\
 el noble cáliz y el piadoso aroma.\
 \
 ¡Oh ingenio que subsiste, que arribaste\
 al eminente y suspirado extremo!\
 ¿Por qué de la fortuna te quejaste\
 en los acentos del dolor supremo?\
 \
 \
 ¡Ay de mi, que rabioso en un erío\
 y a mitad de la ruta estoy parado;\
 que anhelo y lucho por cruzar un río\
 y no hallo puente, ni batel, ni vado;\
 y miro allá, por campo labrantío,\
 la fausta meta en el opuesto lado,\
 y el sol morir, con victorial decoro,\
 bajo un dosel de púrpura y de oro!\
 \
 Oigo decir de mi destino a un chusco:\
 'Talento seductor; pero perdido\
 en la sombra del mal y del olvido...\
 Perla rica en las babas de un molusco\
 encerrado en su concha y escondido\
 en el fondo de un mar lóbrego y brusco...'\
 \
 En sublime absorción hurgo la mente:\
 medito con asombro en ese paso\
 de todas las estrellas a un ocaso\
 que allende una ilusión resulta Oriente...\
 y me inclino arrobado y reverente.\
 \
 Veracruz. El 4 de enero de 1895.\
 \
 El muerto\
 \
 Como tronco en montaña venido al suelo.\
 Frente grandiosa y limpia, soberbia y pura.\
 Negras y unidas cejas, con la figura\
 del trazo curvo y fino que marca el vuelo.\
 \
 De un pájaro en un croquis que apunta un cielo.\
 Nariz igual a un pico de halcón albura\
 de canas. ¡El abeto, ya sin verdura,\
 dio en tierra y está en parte cinto de hielo!\
 \
 El ojo mal cerrado tiene abertura\
 que muestra un hosco y vítreo claror de duelo,\
 un lustre de agua en pozo yerta en su hondura.\
 \
 \
 Moscas espanto y quito con el pañuelo;\
 y en la faz del cadáver sombra insegura\
 flota esbozando un cóndor al par que un velo.\
 \
 Veracruz. El 5 de enero de 1895.\
 \
 Pepilla\
 \
 Como viste ropaje tan leve,\
 ne da pesadumbres,\
 pues el filtra y enseña vislumbres\
 de la carne de rosa y de nieve.\
 ¡Y que andar! La mocita se mueve\
 con garbo de chula.\
 viene y va, y en la marcha modula\
 yn canto de  líneas;\
 y en las formas, apenas virgíneas,\
 una gracia de sierpe le ondula.\
 \
 Como el sándalo emite una esencia,\
 la chica rebosa\
 acre aroma de opima y jugosa\
 pubertad en febril abstinencia.\
 Se revuelve con mucha violencia\
 y a veces me humilla.\
 bien aprecia su gran pantorrilla;\
 y así, no le importa\
 que propulse la falda ya corta\
 y eche a vuelo por alto la orilla.\
 \
 Con sus ojos de ardiente demonio,\
 que ven al soslayo,\
 quebrantara de un golpe de rayo\
 la virtud de cualquier San Antonio.\
 En la espuma del mar sacro al jonio,\
 deidad menos bella\
 sacudió, remedando una estrella,\
 el suelto y profuso\
 y dorado borlón, cuando impuso\
 con el iris al nácar le huella.\
 \
 Si en celoso y colérico ensayo\
 increpo y rezongo,\
 por traer al misterio del hongo\
 flor triunfal en su pompa de maya,\
 la doncella me tira del sayo\
 y a besos me aguisa;\
 pero no sin mostrarse insumisa\
 y osada y segura;\
 y con timbre de plata murmura,\
 entre granas y perlas de risa:\
 \
 'Hembra linda no pierde la gloria\
 por macho importuno:\
 debe ser a los más, y no a uno,\
 esplendor y delicia y memoria.\
 La hermosura inhonesta y notoria\
 contenta el Destino;\
 que quien hace con mágico tino\
 labor esmerada,\
 no la tiene para un mirada\
 y un placer en el breve camino'\
 \
 Música fúnebre\
 \
 Mi corazón percibe, sueña y presume.\
 y como envuelta en oro tejido en gasa,\
 la tristeza de Verdi suspira y pasa\
 en la cadencia fina como un perfume.\
 \
 Y frío de alta zona hiela y entume;\
 y luz de sol poniente colora y rasa:\
 y fe de gloria empírea pugna y fracasa,\
 ¡como en ensayos torpes un ala implume!\
 \
 El sublime concierto llena la casa;\
 y en medio de la sorda y estulta masa,\
 mi corazón percibe, suena y presume.\
 \
 Y como envuelta en oro tejido en gasa,\
 la tristeza de Verdi suspira y pasa\
 en la cadencia fina como un perfume.\
 \
 Diciembre de 1899.\
 \
 La giganta\
 \
 I\
 \
 Es un monstruo que me turba. Ojo glauco y enemigo,\
 como el vidrio de una rada con hondura que, por poca,\
 amenaza los bajeles con las unas de la roca.\
 La nariz resulta grácil y asemejase a un gran higo.\
 \
 La guedeja blonda y cruda y sujeta, como el trigo\
 en el haz. Fresca y brillante y rojísima la boca,\
 en su trazo enorme y burdo y en su risa eterna y loca.\
 Una barba con hoyuelo, como un vientre con ombligo.\
 \
 Tetas vastas, como frutos del mas pródigo papayo:\
 pero enérgicas y altivas en su mole y en su peso,\
 aunque inquietas, como gozques escondidos en el sayo.\
 \
 En la mano, linda en forma, vello rubio y ralo y tieso,\
 cuyos ápices fulguran como chispas, en el rayo\
 matinal, que les aplica fuego móvil con un beso.\
 \
  \
 \
 II\
 \
 ¡Cuales piernas! Dos columnas de capricho, bien labradas,\
 que de púas amarillas resplandecen espinosas,\
 en un pérfido que finge la vergüenza de las rosas,\
 por estar desnudo a trechos ante lúbricas miradas,\
 \
 Albos pies, que con eximias apariencias azuladas\
 tienen corte fino y puro. ¡Merecieran dignas cosas!\
 En la Hélade soberbia las envidias de las diosas,\
 ¡o a los templos de Afrodita engreír mesas y gradas!\
 \
 ¡Qué primores! Me seducen; y al encéfalo prendidos,\
 me los llevo en una imagen, con la luz que los proyecta,\
 y el designio de guardarlos de accidentes y de olvidos.\
 \
 Y con métrica hipertrofia, no al azar del gusto electa,\
 marco y fijo en un apunte la impresión de mis sentidos,\
 a presencia de la torre mujeril que los afecta.\
 \
 Ecce homo\
 \
 \
 Se que la humana fibra\
 a la emoción se libra,\
 pero que menos vibra\
 al goce que al dolor.\
 Y en arte no me ofusco;\
 y para el himno busco\
 la estética del brusco\
 estímulo mayor.\
 \
 Mas no en aleve audacia\
 demando a la falacia\
 la intensa y cruda gracia,\
 como un juglar sutil.\
 A la verdad ajusto\
 el calculado gusto,\
 bajo el pincel adusto\
 y el trágico buril.\
 \
 Y el daño es tema propio\
 a mí, que bebo en opio\
 el sueño, y hago acopio\
 de lágrimas de hiel.\
 Estudio,  peso y mido;\
 y al rudo esfuerzo pido\
 un bálsamo de olvido\
 y un ramo de laurel.\
 \
 Fatiga y pena ignotas\
 soltaron acres gotas,\
 que son espumas rotas\
 sl pie del bogador.\
 ¡Sonad en mi 'lirismo',\
 como en el Ponto mismo,\
 un vasto y fiero abismo\
 de llanto y de sudor!\
 \
 ¡Oh fe y piedad radiosas,\
 qué al polvo de las fosas\
 ponéis alas hermosas\
 con que poder volar!\
 ¡Oh dulces manos bellas,\
 qué al son de las querellas\
 venís de las estrellas\
 a ungir y acariciar!\
 \
 Ni el santo influjo vuestro\
 suaviza mi siniestro\
 destino, donde un estro\
 enrosca y alza luz.\
 Y a empuje por caída,\
 avanzo mas la vida,\
 maltrecha y abatida\
 como arrastrada cruz,\
 \
 Mi gloria esta en la nube\
 que por el cielo sube,\
 Llevando, no un querube,\
 Sino una tempestad.\
 ¡Y en el fulgor que anima\
 la yerma y blanca cima,\
 la cumbre que sublima\
 tristeza y soledad!\
 \
 Vigilia y sueño\
 \
 \
 La moza lucha con el mancebo\
 su prometido y hermoso efebo,\
 y vence a costa de un traje nuevo.\
 \
 Y huye sin mancha ni deterioro\
 en la pureza y en el decoro,\
 y es un gran lirio de nieve y oro.\
 \
 Y entre la sombra solemne y bruna,\
 yerra en el mate jardín, cual una\
 visión compuesta de aroma y luna.\
 \
 Y gana el cuarto, y ante un espejo,\
 y con orgullo de amargo dejo,\
 cambia sonrisas con un reflejo.\
 \
 Y echa cerrajas, y se desnuda,\
 y al catre asciende blanca y velluda,\
 y aun desvestida se quema y suda.\
 \
 Y a mal pabilo, tras corto ruego,\
 sopla y apaga la flor de fuego,\
 y a la negrura pide sosiego.\
 \
 Y duerme a poco. Y en un espanto,\
 y en una lumbre, Y en un encanto,\
 forja un suceso digno de un canto,\
 \
 Sueña que yace sujeta y sola\
 en un calaje que se arrebola,\
 ¡y que un querube llega y la viola!\
 \
 Ejemplo\
 \
 \
 En la rama el expuesto cadáver se pudría,\
 como un horrible fruto colgante junto al tallo,\
 rindiendo testimonio de inverosímil fallo\
 y con ritmo de péndola oscilando en la vía.\
 \
 La desnudez impúdica, la lengua que salía\
 y alto mechón en forma de una cresta de gallo,\
 dábanle aspecto bufo; y al pie de mi caballo\
 un grupo de arrapiezos holgábase y reía.\
 \
 Y el fúnebre despojo, con la cabeza gacha,\
 escandaloso y tumido en el verde patíbulo\
 desparramaba hedores en brisa como racha.\
 \
 Mecido con solemnes compases de Turíbulo.\
 y el sol iba en ascenso por un azul sin tacha,\
 y el campo era figura de una canción de Tíbulo.\
 \
 A Gloria\
  \
 \
 No intentes convencerme de torpeza\
 con los delirios de tu mente loca:\
 mi razón es al par luz y firmeza,\
 firmeza y luz como el cristal de roca.\
 \
 Semejante al nocturno peregrino,\
 mi esperanza inmortal no mira el suelo;\
 no viendo más que sombra en el camino,\
 sólo contempla el esplendor del cielo.\
 \
 Vanas son las imágenes que entraña\
 tu espíritu infantil, santuario oscuro.\
 Tu numen, como el oro en la montaña,\
 es virginal y, por lo mismo, impuro.\
 \
 A través de este vórtice que crispa,\
 y ávido de brillar, vuelo o me arrastro,\
 oruga enamorada de una chispa\
 o águila seducida por un astro.\
 \
 Inútil es que con tenaz murmullo\
 exageres el lance en que me enredo:\
 yo soy altivo, y el que alienta orgullo\
 lleva un broquel impenetrable al miedo.\
 \
 Fiando en el instinto que me empuja,\
 desprecio los peligros que señalas.\
 'El ave canta aunque la rama cruja:\
 como que sabe lo que son sus alas.'\
 \
 Erguido bajo el golpe en la porfía,\
 me siento superior a la victoria.\
 Tengo fe en mí; la adversidad podría,\
 quitarme el triunfo, pero no la gloria.\
 \
 ¡Deja que me persigan los abyectos!\
 ¡Quiero atraer la envidia aunque me abrume!\
 La flor en que se posan los insectos\
 es rica de matiz y de perfume.\
 \
 El mal es el teatro en cuyo foro\
 la virtud, esa trágica, descuella;\
 es la sibila de palabra de oro,\
 la sombra que hace resaltar la estrella.\
 \
 ¡Alumbrar es arder! ¡Estro encendido\
 será el fuego voraz que me consuma!\
 La perla brota del molusco herido\
 y Venus nace de la amarga espuma.\
 \
 Los claros timbres de que estoy ufano\
 han de salir de la calumnia ilesos.\
 Hay plumajes que cruzan el pantano\
 y no se manchan... ¡Mi plumaje es de esos!\
 \
 ¡Fuerza es que sufra mi pasión! La palma\
 crece en la orilla que el oleaje azota.\
 El mérito es el náufrago del alma:\
 ¡vivo, se hunde; pero muerto, flota!\
 \
 ¡Depón el ceño y que tu voz me arrulle!\
 ¡Consuela el corazón del que te ama!\
 ¡Dios dijo al agua del torrente: bulle!;\
 ¡y al río de la margen: embalsama!\
 \
 Confórmate, mujer! Hemos venido\
 a este valle de lágrimas que abate,\
 tú, como la paloma, para el nido,\
 y yo, como el león, para el combate.\
 \
 \
 Ojos verdes\
 \
 \
 Ojos que nunca me veis,\
 por recelo o por decoro,\
 ojos de esmeralda y oro,\
 fuerza es que me contempléis;\
 quiero que me consoléis\
 hermosos ojos que adoro;\
 ¡estoy triste y os imploro\
 puesta en tierra la rodilla!\
 ¡Piedad para el que se humilla,\
 ojos de esmeralda y oro!\
 \
 Ojos en que reverbera\
 la estrella crepuscular,\
 ojos verdes como el mar,\
 como el mar por la ribera,\
 ojos de lumbre hechicera\
 que ignoráis lo que es llorar,\
 ¡glorificad mi penar!\
 ¡No me desoléis así!\
 ¡Tened compasión de mí!\
 ¡Ojos verdes como el mar!\
 \
 Ojos cuyo amor anhelo\
 porque alegra cuanto alcanza,\
 ojos color de esperanza,\
 con lejanías de cielo:\
 ojos que a través del velo\
 radian bienaventuranza,\
 mi alma a vosotros se lanza\
 en alas de la embriaguez,\
 miradme una sola vez,\
 ojos color de esperanza.\
 \
 Cese ya vuestro desvío,\
 ojos que me dais congojas;\
 ojos con aspecto de hojas\
 empapadas de rocío.\
 Húmedo esplendor de río\
 que por esquivo me enojas.\
 Luz que la del sol sonrojas\
 y cuyos toques son besos,\
 derrámate en mí por esos\
 ojos con aspecto de hojas. \
 \
 \
 \
 A un pescador\
 \
 \
 En buen esquife tu afán madruga,\
 el firmamento luce arrebol;\
 grata la linfa no tiene arruga;\
 la blanca vela roba en su fuga\
 visos dorados al nuevo sol.\
 \
 Pero prorrumpes en canturía\
 que inculta y tosca mueve a llorar;\
 oigo la ingenua melancolía\
 ¡del que inseguro del pan del día\
 surca y arrostra pérfido mar!\
 \
 Tímida y mustia por los recelos\
 tu mujercita dirá: -Señor,\
 une las aguas, limpia los cielos;\
 cuida y conduce, por los chicuelos,\
 ¡la navecilla del pescador!\
 \
 \
 Rimas\
 \
 \
 El día con su manto\
 de vívidos colores,\
 inspira cosas dulces:\
 la risa y la ilusión.\
 Entonces la mirada\
 se inclina hacia las flores...\
 Las flores son los versos\
 ¡que el prado canta al sol!\
 \
 La noche con su sombra,\
 que deja ardientes rastros,\
 inspira cosas graves:\
 la angustia y la oración.\
 Entonces la mirada\
 se eleva hacia los astros...\
 Los astros son los versos\
 ¡que el cielo canta a Dios!\
 \
 Qué pliegue su ala de oro\
 la tarde en el vacío;\
 que pasen por mi mente\
 las ondas del Cedrón;\
 que caiga de la nube\
 la gota de rocío;\
 ¡que radien las estrellas,\
 que trine el ruiseñor!\
 \
 \
 Asonancias\
 \
 \
 Sabedlo, soberanos y vasallos,\
 próceres y mendigos:\
 nadie tendrá derecho a lo superfluo\
 mientras alguien carezca de lo estricto.\
 \
 Lo que llamamos caridad y ahora\
 es sólo un móvil íntimo,\
 será en un porvenir lejano o próximo\
 el resultado del deber escrito.\
 \
 Y la Equidad se sentará en el trono\
 de que huya el Egoísmo,\
 y a la ley del embudo, que hoy impera,\
 sucederá la ley del equilibrio.\
 \
 \
 \
 Mudanza\
 \
 \
 Ayer, el cielo azul, la mar en calma\
 y el sol ignipotente y cremesino,\
 y muchas ilusiones en mi alma\
 y flores por doquier en mi camino.\
 \
 Mi vida toda júbilos y encantos,\
 mi pecho rebosando de pureza,\
 mi carmen pleno de perfume y cantos\
 y muy lejos, muy lejos, la tristeza.\
 \
 Ayer, la inspiración rica y galana\
 llenando mi cerebro de fulgores;\
 y tú, sonriente y dulce en tu ventana,\
 hablándome de dichas y de amores.\
 \
 Ayer, cuanto era luz y poesía:\
 las albas puras y las tardes bellas\
 henchidas de sutil melancolía,\
 y las noches pletóricas de estrellas...\
 \
 Y hoy... la sombra y el ansia del desierto,\
 perdida la esperanza, y la creencia,\
 y el amor en tu espíritu ya muerto,\
 y sembrada de espinas la existencia.\
 \
 \
 Dones fatídicos\
 \
 Palma, no te enorgullezcas\
 de superar en altura\
 a los laureles y almendros\
 sobre cuyas copas triunfas.\
 La tempestad se avecina,\
 y cuando el rayo fulgura,\
 las frentes menos enhiestas\
 son las que están más seguras.\
 \
 No te ensoberbezcas, rosa,\
 porque brillas y perfumas,\
 y en el jardín y en el prado\
 reinas, excedes y ofuscas.\
 Esmalte y aroma en flores\
 son signos de desventura...\
 Manos vendrán que te arranquen\
 o insectos que te destruyan.\
 \
 Dulce planta de la selva,\
 cantor que esponjas la pluma\
 y abres el pico y exhalas\
 chorros de perlas de música.\
 No te envanezca el gorjeo,\
 calla: los hombres lo escuchan,\
 y trinos aprestan redes\
 al ave que los modula.\
 \
 Tierra, no envidies al astro\
 que te calienta y fecunda,\
 y que surgente o occiduo\
 prodiga el oro y la púrpura.\
 Tamaña magnificencia\
 nace de inmensa tortura...\
 El resplandor de un incendio\
 ¡te vivifica y alumbra!\
 \
 Cuán caro pagas, espíritu,\
 ¡el nimbo que te circunda!\
 Tener ingenio y renombre\
 es tu verdadera culpa.\
 De rencores a tu gloria\
 es cómplice la fortuna,\
 y pereces lapidado\
 con montañas de imposturas.\
 \
 Deseos\
 \
 \
 Yo quisiera salvar esa distancia\
 ese abismo fatal que nos divide,\
 y embriagarme de amor con la fragancia\
 mística y pura que tu ser despide.\
 \
 Yo quisiera ser uno de los lazos\
 con que decoras tus radiantes sienes;\
 yo quisiera en el cielo de tus brazos\
 beber la gloria que en los labios tienes.\
 \
 Yo quisiera ser agua y que en mis olas,\
 que en mis olas vinieras a bañarte,\
 para poder, como lo sueño a solas,\
 ¡a un mismo tiempo por doquier besarte!\
 \
 Yo quisiera ser lino y en tu lecho,\
 allá en la sombra, con ardor cubrirte,\
 temblar con los temblores de tu pecho\
 ¡y morir de placer al comprimirte!\
 \
 Oh, yo quisiera mucho mas! Quisiera\
 llevarte en mi como la nube al fuego,\
 mas no como la nube en su carrera\
 ¡para estallar y separarse luego!\
 \
 Yo quisiera en mi mismo confundirte,\
 confundirte en mi mismo y entrañarte;\
 yo quisiera en perfume convertirte,\
 ¡convertirte en perfume y aspirarte!\
 \
 Aspirarte en un soplo como esencia,\
 y unir a mis latidos tus latidos,\
 y unir a mi existencia tu existencia,\
 ¡y unir a mis sentidos tus sentidos!\
 \
 A Margarita\
 \
 \
 Qué radiosa es tu faz blanca y tranquila\
 ¡bajo el dosel de tu melena blonda!\
 Qué abismo tan profundo tu pupila,\
 ¡pérfida y azulada como la onda!\
 \
 El fulgor soñoliento que destella\
 en tus ojos donde hay siempre un reproche\
 viene cual la mirada de la estrella\
 de un cielo ennegrecido por la noche.\
 \
 Tu rojo labio en que la abeja sacia\
 su sed de miel, de aroma y embeleso,\
 ha sido modelada por la gracia\
 más para la oración que para el beso.\
 \
 Tu voz que ora es aguda y ora grave,\
 llena de gratitud suena en mi oído\
 como el saludo arrullador del ave\
 al sol naciente que despierta el nido.\
 \
 \
 Dea\
 \
 Recio y amplio edificio, que no brilla\
 Por la elegancia y el primor del arte.\
 Fue convento y capilla\
 Y es hospital. Elévase a la orilla\
 Del mar, hacia la parte\
 De Oriente, por la cual hay un baluarte,-\
 De dos que duran a evocar memoria\
 De antiguos tiempos de tumulto y gloria.\
 \
 Junto a ríspida rampa de granito,\
 Roña de ruinas y despojos muerde\
 Restos de la muralla de circuito,\
 Que son postrer vestigio que se pierde;\
 Y entre la playa bruna y el amparo\
 De los pacientes míseros, un clavo\
 Borda en rústico alarde alfombra verde.*\
 \
 Al Norte, recta y espaciosa vía,\
 Que a un lado y otro del arroyo cría\
 Y a despecho del régimen propaga \
 Mantos de zacatillo y verdolaga;\
 Y que a un extremo y a cerrar el fondo\
 Tiene un médano gris, enhiesto y mondo.\
 \
 Al Sur, y herboso como inculto predio,\
 Un parquecillo ruin en cuyo medio\
 Un zócalo mezquino espera en vano,\
 Con una obstinación que infunde tedio,\
 La estatua de un grande hombre mexicano.\
 \
 He ahí mi asilo y el contorno. -Cruda\
 Flegmasía me atrajo de mazmorra\
 A celda en que perezco de modorra\
 Y que, quizás por imitarme, suda.\
 Compasivo guardián que imparte ayuda;\
 Y cuando halla ocasión, me da permiso\
 De visitar un rato el paraíso.\
 Y a frescos y desnudos corredores,\
 Que rodean un cuadro un patiezuelo,\
 Salgo a ver sonreír frondas y flores,\
 Ya mostrar a la fe de mis dolores\
 Un pedacito del azul del cielo.\
 Y de gracia mi espíritu se viste;\
 Y entonces me pregunto si la suerte\
 Hará otra miel como la paz del fuerte\
 Y otro esplendor como el placer del triste.\
 \
 Holgábame una vez en tal encanto;\
 Y una moza, con rostro del delirio,\
 Pasó, blanca y derecha como un cirio,\
 Lírica y turbadora como un canto,\
 Odorífera y prócer como un lirio.\
 Parecía ilusión de la mirada.\
 Iba con paso cadencioso y lento,\
 Y alba ropa de lino almidonada,\
 Y un susurro de risa en enramada,\
 Y cual fuego la crin volando al viento.\
 Era de tarde, por abril que adoro, \
 Y en un silencio perturbado apenas;\
 Y efluvios de azahares y azucenas\
 Desleían al sol ámbar en oro.\
 \
 Quedáme absorto y lúgubre. Sufría\
 Présaga desazón. - ¡Oh imagen pía!\
 Ancha y tersa la frente sin pecado,\
 Helénica nariz, boca de fresa,\
 Zarco el ojo de antílope asustado,\
 Elación y decoro de princesa\
 Y un secreto de angustia en un nublado:\
 ¡asi te llevo en el sensorio impresa!\
 \
 Costumbre de inquirir, sabia y notoria,\
 A la que rindo y pagaré tributo,\
 Movióme a interrogar. Y oí una historia.\
 ¿A quién? A un servidor del instituto,\
 a un cubano feraz en viles tretas,\
 a un practicante crapuloso y pigre,\
 a un mancebo de sórdidas chancletas,\
 facha de orangután, gesto de tigre.\
 Pero atended. -Su relación incluye\
 Un imán de rumor de agua que fluye.\
 \
 'La doncella gentil se llama Dea.\
 Su padre, Juan Falot, vino de zuavo;\
 Y aqui, como en Italia y en Crimea,\
 Ganó prez en las lides como bravo.\
 Herido y preso en Camarón, no pudo\
 Seguir, camino a Francia, el regimiento;\
 Y ya en salud y en libertad, a rudo\
 Trabajo demandó noble sustento.\
 Cansado de labrar, y con su ahorro,\
 Adquirióse un tenducho y un ventorro.\
 Y casó con la reina del poblacho,\
 Una mujer de singular trapío,\
 Modesta y cauta sin ficción ni empacho,\
 Y enemiga mortal de todo lío.\
 Y los meses corrieron; y la esposa\
 Engordaba, soñando con querubes;\
 Y una chica nació sana y hermosa,\
 Con un cutis de pétalos de rosa\
 Y un olor como de astros y de nubes.'\
 \
 'Qué suplicio el del parto! ¡Cuál estreno!\
 Fruto de humano amor cumple lo escrito:\
 No se desgaja sin romper un seno\
 Y no respira sin lanzar un grito!\
 Fausto auroral surgió del horizonte;\
 Y a la sangrienta luz que despuntaba,\
 Y en el aroma del cercano monte,\
 Y en las perlas de un trino de sisonte,\
 ¡ay! La madre infeliz agonizaba.\
 Por hemorragia sucumbió al puerperio.\
 El cadáver cayó bajo el imperio\
 De la Química, numen de las cosas,\
 Y es en el más humilde cementerio\
 Polvo siempre fecundo en tuberosas.\
 Pero alma de valer, limpia y cristiana,\
 Yergue aliento que nunca se consume;\
 Y aquélla se fue a Dios, como un perfume,\
 Disuelta en el carmín de la mañana.'\
 \
 'El pobre viudo encaneció en un día.\
 ¡Cuán tierno y delicado a la pequeña\
 el que antes, por su indúctil ardentía,\
 resultaba feroz bajo la enseña!\
 Arrapiezo el 'bebe', y en la dulzura\
 Del mismo, y al alcance de la mano,\
 Campó sin probar gota de amargura.\
 ¡Frágil y bullidor, lindo y ufano\
 colibrí del vergel de la ventura!\
 Su aspecto de pictórico angelito,\
 Su inventiva, su charla, su despejo,\
 Aliviaban con bálsamo exquisito\
 El ulcerado corazón del viejo.'\
 \
 '¡Precoz muchacha! Con presteza suma\
 se adiestraba en su hogar, según crecía;\
 y llegó con el medro de la espuma\
 a la núbil y sacra lozanía.\
 Y en gusto y dignidad honró penates,\
 Y en cuidar su conducta puso esmero;\
 Y escuchando episodios de combates,\
 Retempló su virtud como un acero.\
 Jamás anduvo en triscas de festines;\
 Y sola con sus caras aficiones,\
 Vivió en intimidad con sus jazmines\
 Y hablábase de tú con sus gorriones.\
 Su pensamiento, si salvaba el muro,\
 Era de fijo en el espacio, allende,\
 Como el soplo sutil, cimero y puro\
 Que por alto pinar vibra y trasciende'.\
 \
 Al estro el narrador detuvo el giro,\
 Y luego continuó, tras un suspiro.\
 'Al destino la dicha es una injuria\
 y el oasis un tósigo al desierto.\
 El anciano 'enfermó' de albuminuria\
 Y con la virgen trasladóse al puerto.\
 Arriba está. Malísimo, por cierto,\
 Y de congoja convertido en furia.\
 La bella y santa joven, - que reside\
 No lejos, en unión de unas beatas-,\
 Acude con frecuencia y lo decide\
 A someterse a pócimas y natas.\
 Y bebe horrible hiel en vasta copa;\
 Y con firme palabra y sin misterio,,\
 Dice que pronto marchará a Europa \
 A gemir su orfandad a un monasterio.\
 Musca jerga y nevada muselina\
 Ofrecen a la mártir hechicera\
 Disfraz de prodigiosa golondrina,\
 Palma en inmarcesible primavera'.\
 \
 Veracruz. Hospital de San Sebastián. Mayo \
 De 1900.\
 \
 \
 La canción del paje\
 \
 Tan abierta de brazos como de piernas,\
 Tocas el harpa y ludes madera y oro.\
 Dejo al mueble la plaza por el decoro,\
 Y contemplo caricias a hurgarme tiernas.\
 \
 A tu ardor me figuras y subalternas\
 En la intención del alma que bien exploro,\
 Y en el roce del cuerpo con el sonoro\
 Y opulento artefacto que mal gobiernas.\
 \
 Y tanto me convidas, que ya me infiernas;\
 Y refrenado y mudo finjo que ignoro,\
 Para que si hay ultraje no lo disciernas.\
 \
 Por fiel a un noble amigo pierdo un tesoro...\
 Tan abierta de brazos como de piernas,\
 Tocas el harpa y ludes madera y oro.\
 \
 \
 \
 Avernus\
 \
 El recio astur, que se reputa\
 Claro y puro y tenaz como un diamante;\
 Y ella una montañesa, -diminuta\
 Como todo primor-, suelta y picante.\
 \
 Y en una quiebra, convertida en huerto,\
 Habitan, por azares, un casucho,\
 Con un mozo andaluz, guapo, despierto,\
 Y en corromper a las labriegas ducho.\
 \
 El marido es feliz. Tiene por Norte\
 El propio ensueño en la fortuna extraña:\
 Conservar el amor de la consorte,\
 Y con él y un caudal volver a España.\
 \
 ¡Oh ilusión, rica y tenue como un halo!\
 Eres gracia y piedad y no ironía.\
 El dios propicio, que sucumbe al malo,\
 Te insufla, porque brega todavía!\
 \
 ¡Espantoso el temblor, que de improviso\
 cambia el curso a las linfas, y despeña\
 la roca y el alud, y agrieta el piso,\
 y torna el pobre hogar montón de leña!\
 \
 El campesino acude; y en acento\
 Que al mismo pedernal abriera estría,\
 Arroja como un dardo el firmamento\
 Un nombre de mujer: el de María.\
 \
 ¡Luto y desolación! ¡Ruina y tortura!\
 -El mísero patán busca y remueve;\
 y, tras larga faena, se figura\
 que percibe un albor como de nieve.\
 \
 Escombra con afán y se aproxima...\
 ¡Y ve dos cuerpos cual de mate y yeso,\
 desnudos, enlazados, uno encima\
 del otro, muertos en la flor del beso!\
 \
 El Poniente descoge su escarlata;\
 Y, como signos de crudeza y lloro,\
 Selene muestra su segur de plata\
 Y Véspero su lágrima de oro.\
 \
 * * *\
 ¡Desdichado Ginés! Odia la vida,\
 y arma la diestra con agudo acero...\
 ¿En dónde los despojos del suicida\
 En sepulcro sin cruz y sin letrero.\
 \
 En fosa que la grama disimula,\
 Al pie de un árbol que resulta emblema,\
 Pues parece un dolor que gesticula\
 En una contorsión brusca y suprema.\
 \
 Del zafio, cuya forma ya no existe,\
 El espíritu aun es; - y con sus celos,\
 Igualmente inexhaustos, vaga triste\
 Y colérico y solo por los cielos.\
 \
 Y con voz de retumbo de caverna\
 Lanza en la sombra, pavoroso grito:\
 '¡Maldición para el alma, por eterna,\
 ¡ay! Porque su tormento es infinito!'\
 \
 \
 Paquito\
 \
 Cubierto de jiras,\
 Al ábrego hirsutas\
 Al par que las mechas\
 Crecidas y rubias,\
 El pobre chiquillo\
 Se postra en la tumba:\
 Y en voz de sollozos\
 Revienta y murmura:\
 'Mamá, soy Paquito;\
 No haré travesuras.'\
 \
 Y un cielo impasible\
 Despliega su curva.\
 \
 '¡Que bien que me acuerdo!\
 La tarde de lluvia;\
 Las velas grandotas\
 Que olían a curas;\
 Y tú en aquel catre\
 Tan tiesa, tan muda,\
 Tan fría, tan seria, \
 Así tan rechula!\
 'Mamá, soy Paquito;\
 No haré travesuras.'\
 \
 Y un cielo impasible\
 Despliega su curva.\
 \
 'Buscando comida,\
 revuelvo basura.\
 Si pido limosna,\
 La gente me insulta,\
 Me agarra la oreja,\
 Me dice granuja,\
 Y escapo con miedo \
 De que haya denuncia.\
 'Mamá, soy Paquito;\
 No haré travesuras.'\
 \
 Y un cielo impasible\
 Despliega su curva.\
 \
 'Los otros muchachos \
 se ríen, se burlan,\
 se meten conmigo,\
 y a poco me acusan\
 de pleito al gendarme\
 que viene a la bulla;\
 y todo, porque ando\
 con tiras y sucias.\
 'Mamá, soy Paquito;\
 No haré travesuras.'\
 \
 Y un cielo impasible\
 Despliega su curva.\
 \
 'Me acuesto en rincones\
 solito y a obscuras.\
 De noche, ya sabes,\
 Los ruidos me asustan.\
 Los perros divisan\
 Espantos y aúllan.\
 Las ratas me muerden,\
 Las piedras me punzan...\
 'Mamá, soy Paquito;\
 No haré travesuras.'\
 \
 Y un cielo impasible\
 Despliega su curva.\
 \
 'Papá no me quiere.\
 Está donde juzga \
 Y riñe a los hombres\
 Que tienen la culpa.\
 Si voy a buscarlo,\
 Él bota la pluma, \
 Se pone muy bravo,\
 Me ofrece una tunda.\
 'Mamá, soy Paquito;\
 No haré travesuras.'\
 \
 Y un cielo impasible\
 Despliega su curva.\
 \
 \
 \
 Beatus ille\
 \
 ¡Oh paz agreste! ¡Cuánto \
 a quien se acoge a ti brindas provecho!\
 ¡Con qué divino encanto\
 llenas de olvido el pecho\
 ¡ay! A torturas y a furores hecho!\
 \
 De la cándida oveja\
 Que a sombra trisca en hondonada bruna,\
 O la cabra bermeja\
 Que asoma en alta duna\
 Su hocico rojo de carmín de tuna,\
 \
 Ubre sana y henchida\
 Regala el apetito, aquí no escaso,\
 Con leche que, bebida,\
 Vale a dormir al raso\
 Y deja untado y azuloso el vaso.\
 \
 ¡Mesa digna de un justo\
 ¡Oh Gay! La tuya, que de carne y vino\
 te guarda exento el gusto,\
 y no a perder el tino\
 es ocasión, ni a víctimas destino!\
 \
 Égloga virgiliana\
 Abre y radica en tu heredad el seno,\
 Y de tu boca mana\
 En trasunto sereno\
 Y con almíbar oloroso a heno.\
 \
 Antigua prez no humilla\
 Claro vestigio a torpe muchedumbre:\
 Él en tu ingenio brilla,\
 Como postrera lumbre\
 De occiduo sol, en levantada cumbre.\
 \
 ¡Plácidos los que orean\
 mi frente, que a baldón opone orgullo,\
 hálitos que menean\
 las frondas con murmullo\
 grato al reposo, cual materno arrullo!\
 \
 Mas no Favonio engríe\
 El délfico laurel. Zozobras calma,\
 Y susurrando ríe\
 De la ceñida palma,\
 Con un desprecio que perfuma el alma!\
 \
 ¡Oh paz agreste! ¡Cuánto\
 a quien se acoge a ti brindas provecho!\
 ¡Con que divino encanto \
 llenas de olvido el pecho\
 ¡ay! A torturas y a furores hecho!\
 \
 A la culta o salvaje\
 Corriente del vivir marcas y ahondas\
 Recto y seguro encaje,\
 Que por arenas blondas\
 Al mar la lleva en sosegadas ondas.\
 \
 Sobre anónima huesa\
 Árbol piadoso y tétrico derrumba\
 'guirnalda que le pesa',\
 pompa que treme y zumba\
 y caricia y plañido es a la tumba.\
 \
 La madre tierra es leve\
 Al cadáver que allí se desmorona,\
 Que sólo a un sauce debe,\
 En los palmos que abona,\
 Copioso llanto y liberal corona.\
 \
 \
 Pinceladas\
 \
 I\
 Pardas o grises, donde no musgosas,\
 Tres tapias; y cuadrando el vergelillo,\
 Reja oculta en verdor florido en rosas,\
 Que son como de un ámbar amarillo.\
 \
 Césped. Un pozo con brocal de piedra,\
 Lirios, Nardos, Jazmines, Heliotropos.\
 Un copudo laurel que al sesgo medra,\
 Con telarañas como grandes gropos.\
 \
 Un firmamento rubio. Vésper brilla,\
 A manera de lágrima que brota\
 Y que creciente único se orilla\
 Para efundir o evaporar su gota.\
 \
 Bien lejos, y en un arco de horizonte,\
 Rica y negral vegetación abunda;\
 Y descediendo los pliegues de tal monte,\
 Y en símbolo de tierra tan fecunda,\
 \
 Volcán enhiesto y cónico alardea,\
 Como en robusta madre teta erguida\
 Que se vierte de tímida y albea\
 ¡Medio empapada en su licor de vida!\
 \
 II\
 \
 Como tenue labor, hecha con vaga\
 Nieve ideal por manos de chicuelos,\
 Y que lenta fusión merma y estraga\
 En la sublime curva de los cielos.\
 \
 Un trasunto se borra en una nube:\
 El de un ángel monstruoso por deforme.\
 Gloria. Silencio. Paz. La Luna sube\
 Del término del mar, flave y enorme.\
 \
 Asciende y disminuye y palidece;\
 Y en el cerco irisado que la enviste\
 Como de sacra majestad, parece\
 La cabeza de un dios enfermo y triste.\
 \
 Y su místico imán turba la calma\
 Y prende un ala torpe al grave anhelo,\
 Y suscita en el ponto y en el alma\
 Ciego y estéril ímpetu de vuelo.\
 \
 \
 A una araucaria\
 \
 \
 ¡Bien hayas, himno verde, que sublimas\
 en estrelladas y soberbias rimas\
 triunfante numen, y a cantar animas!\
 \
 En la punta prolífica y derecha\
 De tu plumada y elegante flecha,\
 Mirlo garrulador plañe una endecha\
 \
 Y abro el ala parnáside, y al crudo\
 Viento del agrio Cofre la sacudo,\
 Y con bárbara trova te saludo.\
 \
 Corvas uñas, que amagan como en rabos\
 De incógnitos a mí reptiles bravos,\
 Echas por hojas en alternos cabos.\
 \
 Y si la llama del rencor me ciñe\
 Corazón y laúd, la nota riñe\
 Y el verso es garra que la sangre tiñe.\
 \
 ¡Cuán peregrina con tus frondas nuevas!\
 Imán y encanto a las miradas pruebas\
 En las guirnaldas que a las nubes llevas.\
 \
 Extraño soy también, y más atraigo\
 Con prez que ostento y con baldón que raigo,\
 Y de mayor encumbramiento caigo.\
 \
 A mirífica lumbre te abandonas\
 E iridiscentes lágrimas temblonas\
 Adiamantan y emperlan tus coronas.\
 \
 Y ardo en estro de amor, y no hay rocío\
 Como el que cubre las que a Dios envío\
 Ansias de que me cure el ángel mío.\
 \
 ¡En ti mi nombre que grabé se mezca!\
 ¡Tal vez lo guardarás de que perezca!\
 ¡Sólo así podrá ser que dure y crezca!\
 \
 Xalapa. Septiembre de 1896.\
 \
 \
 Un jornalero\
 \
 Lírica gracia exorna y ennoblece\
 ¡oh proletario! Tu mansión mezquina:\
 el tiesto con la planta que florece,\
 la jaula con el pájaro que trina.\
 \
 Sospechoso el tugurio no parece,\
 Cuando hay en él, como señal divina,\
 El tiesto con la planta que florece,\
 La jaula con el pájaro que trina.\
 \
 ¡Lúgubre la morada que guarece\
 miseria que no luce, por mohína,\
 el tiesto con la planta que florece,\
 la jaula con el pájaro que trina.!\
 \
 ¡Siniestro el pobre que de hogar carece,\
 o a su triste refugio no destina\
 el tiesto con la planta que florece,\
 la jaula con el pájaro que trina.!\
 \
 \
 ¡Audacia!\
 \
 Basta de timidez. La gloria esquiva\
 Al que por miedo elude la pelea\
 Y con suspiros lánguidos rastrea,\
 Acogido a la sombra de la oliva.\
 \
 Sólo una tempestad brusca y altiva\
 Encumbra la pasión y la marea,\
 ¡Y en empinados vórtices pasea\
 El abismo de abajo en el de arriba!\
 \
 ¡Oh rebelde¡ ¡Conquista la presea;\
 goza de la hermosura inebriativa\
 y horror a los demás tu dicha sea!\
 \
 Arrostra por la gracia la diatriba,\
 ¡Y en empinados vórtices pasea\
 El abismo de abajo en el de arriba!\
 \
 \
 A la señorita Sofía Martinez\
 \
 Traigo por la cadena un bello tigre hircano\
 Que a tu neurosis, harta de júbilos de miel,\
 Inspira un acre gusto: el de pasar la mano\
 Por la incitante felpa de la vistosa piel.\
 \
 Felino que figura el estro a que sonríes,\
 El numen que me alienta, gallardo y fiero al par\
 Y que gruñendo lame tus breves borceguíes,\
 Cual por el flujo a veces en la ribera el mar!\
 \
 \
 \
 A la señortia Julia Zárate\
 \
 En la Venus de Médicis el arte\
 Previó cuanto hay en ti, menos la túnica.\
 Irreprochable desnudez imparte\
 Al mármol gracia vencedora y única.\
 \
 No te des al acaso. Dios no envía\
 La suprema beldad a cualquier gusto.\
 ¡La manda para ser en la porfía\
 botín al fuerte y galardón al justo!\
 \
 \
 \
 In hoc signo..\
 (Canción para mi hija Rosa.)\
 \
 Cautivo un gorrión estaba,\
 Y de un astro se prendó;\
 Y en su música decía:\
 'Llegue a ti mi dulce voz.'\
 \
 Por azar, o por astucia,\
 El pajarillo escapó;\
 Y al cielo se fue trinando\
 'Alas tengo y libre soy.'\
 \
 Y el ave a la rica estrella\
 Pudo subir, y cantó:\
 'Ni cadenas ni distancias\
 vedan triunfos al amor.'\
 \
 Entre dos lentes\
 (En un establecimiento fotográfico)\
 \
 Bruno el sombrero que a lucir campea\
 Con alto moño y superior plumaje.\
 Faz que vela su olímpico linaje\
 Y que de negro el tul raya y puntea.\
 \
 Azabache tejido el noble traje;\
 Y al cuello en un listón rica presea:\
 Adamantino aljófar que chispea\
 En dos aros que intrincan maridaje.\
 \
 Al pecho y relumbrando en el ropaje,\
 Áurica soga. La beldad ladea\
 El torso; mas no elude mi espionaje.\
 \
 Y con gesto hermosísimo florea\
 Faz que vela su olímpico linaje\
 ¡Y que de negro el tul raya y puntea!\
 \
 \
 Ópalo\
 \
 A la vieja necrópolis me arrimo;\
 y en el tumulto del desborde rimo\
 la postrera canción,\
 no conforme a la Lógica y al Arte,\
 sino según el verso brinca y parte\
 ¡del mismo corazón!\
 \
 Así surgida de la oculta vena\
 el agua pura se levanta y suena\
 en curva de cristal;\
 y al extremar la iridiscente ojiva, \
 toca en tierra y se alarga fugitiva,\
 ¡caprichosa y triunfal!\
 \
 ¡Cuál voy! El hombre labra su fortuna,\
 como el río su cauce; mas la cuna\
 y el medio siempre son\
 árbitros ¡Ay! Para las dos corrientes,\
 pues que dan a las linfas y a las gentes\
 ¡impulso y dirección!\
 \
 Si resulté raudal turbio de cieno\
 y espumante de cólera en un trueno,\
 en un fragor de alud,\
 la margen verdeció, y un espejismo\
 puso en mí, como prez, el otro abismo:\
 ¡el de la excelsitud!\
 \
 Entro. ¡-Hierbas y nichos y pendientes:\
 ponto con arrecifes rompientes-!\
 Alzo del polvo un lar:\
 un caracol cuyo tortuoso hueco\
 reproduce al oído, como un eco,\
 ¡el murmullo del mar!\
 \
 Ando en maleza vil donde no hay ruta;\
 y el temor a una víbora me inmuta,\
 cuando aventuro el pie.\
 -Una virtud suprema y exquisita\
 baja del firmamento y precipita\
 ¡la zozobra en la fe!\
 \
 Lleno de la esperanza de la gloria,\
 y arrostrando la inquina, y en la escoria,\
 fuelvo al éter la faz,\
 miro esplender la eternidad del cielo,\
 y reporto a mis lágrimas consuelo\
 ¡y a mis enconos paz!\
 \
 Mi espíritu de bronce con acíbar\
 se torna cera que desprende almíbar.\
 D'Annunzio dice bien:\
 la sazón lleva plácido atributo,\
 y dulcifica el alma, como el fruto,\
 ¡aunque mina el sostén!\
 \
 Con los jaspes del ónix mexicano\
 la tarde brilla en el inmenso vano,\
 en la veste de Ormuz;\
 y el pobre y aflictivo cementerio\
 refleja en su abandono y su misterio\
 ¡la policroma luz!\
 \
 Un adiós, hecho turba de colores,\
 como el de triste madre suelto en flores\
 a muerto chiquitín,\
 radia en el dombo, que prepara luto\
 y luminaria, por el sol hirsuto\
 ¡que cayó en el confín!\
 \
 Al rincón venerable llego al cabo.\
 Hurgo la herida con el propio clavo,\
 memoro trance cruel;\
 y ante un espectro gemebundo y bronco,\
 reclino intenso afán en firme tronco\
 ¡de cercano laurel!\
 \
 Trepadora vivaz orna la tumba,\
 que el estrago del tiempo se derrumba,\
 exenta de inscripción;\
 y en la cruz una ráfaga menea\
 follaje que parece que chorrea\
 ¡lastimero festón!\
 \
 Laúd solemne, sensitivo y pulcro,\
 enmudeció a la orilla del sepulcro\
 que atesta olvido tal...\
 a ti mi libro fiel ¡Oh poesía,\
 honrada solamente por la mía\
 y la de un vegetal!\
 \
 Y a vos dama gentil, soberbia y dura,\
 que guardáis en desdén y en hermosura\
 ¡un cadáver de amor!\
 planto y riego distinta enredadera\
 para que gane cumbre más severa\
 ¡ídolo superior!",
                    path=u"/c", tags=u"SDM")

writer.add_document(title=u"Sor Juana Ines de la Cruz", content=u"La Sentencia del Justo\
\
Firma Pilatos la que juzga ajena\
Sentencia, y es la suya. ˇOh caso fuerte!\
żQuién creerá que firmando ajena muerte\
el mismo juez en ella se condena?\
\
La ambición de sí tanto le enajena\
Que con el vil temor ciego no advierte\
Que carga sobre sí la infausta suerte,\
Quien al Justo sentencia a injusta pena.\
\
Jueces del mundo, detened la mano,\
Aún no firméis, mirad si son violencias\
Las que os pueden mover de odio inhumano;\
\
Examinad primero las conciencias,\
Mirad no haga el Juez recto y soberano\
Que en la ajena firméis vuestras sentencias\
\
\
\
A una Rosa\
\
Rosa divina, que en gentil cultura\
Eres con tu fragante sutileza\
Magisterio purpúreo en la belleza,\
Enseńanza nevada a la hermosura.\
\
Amago de la humana arquitectura,\
Ejemplo de la vana gentileza,\
En cuyo ser unió naturaleza\
La cuna alegre y triste sepultura.\
\
ˇCuán altiva en tu pompa, presumida\
soberbia, el riesgo de morir desdeńas,\
y luego desmayada y encogida.\
\
De tu caduco ser das mustias seńas!\
Con que con docta muerte y necia vida,\
Viviendo engańas y muriendo enseńas.\
\
\
\
Sentimientos de Ausente\
\
Amado dueńo mío,\
Escucha un rato mis cansadas quejas,\
Pues del viento las fío,\
Que breve las conduzca a tus orejas,\
Si no se desvanece el triste acento\
Como mis esperanzas en el viento.\
\
Óyeme con los ojos,\
Ya que están tan distantes los oídos,\
Y de ausentes enojos\
En ecos de mi pluma mis gemidos;\
Y ya que a ti no llega mi voz ruda,\
Óyeme sordo, pues me quejo muda.\
\
Si del campo te agradas,\
Goza de sus frescuras venturosas\
Sin que aquestas cansadas\
Lágrimas te detengan enfadosas;\
Que en él verás, si atento te entretienes\
Ejemplo de mis males y mis bienes.\
\
Si al arroyo parlero\
Ves, galán de las flores en el prado,\
Que amante y lisonjero\
A cuantas mira intima su cuidado,\
En su corriente mi dolor te avisa\
Que a costa de mi llanto tiene risa.\
\
Si ves que triste llora\
Su esperanza marchita, en ramo verde,\
Tórtola gemidora,\
En él y en ella mi dolor te acuerde,\
Que imitan con verdor y con lamento,\
Él mi esperanza y ella mi tormento.\
\
Si la flor delicada,\
Si la peńa, que altiva no consiente\
Del tiempo ser hollada,\
Ambas me imitan, aunque variamente,\
Ya con fragilidad, ya con dureza,\
Mi dicha aquélla y ésta mi firmeza.\
\
Si ves el ciervo herido\
Que baja por el monte, acelerado\
Buscando dolorido\
Alivio del mal en un arroyo helado,\
Y sediento al cristal se precipita,\
No en el alivio en el dolor me imita,\
\
Si la liebre encogida\
Huye medrosa de los galgos fieros,\
Y por salvar la vida\
No deja estampa de los pies ligeros,\
Tal mi esperanza en dudas y recelos\
Se ve acosa de villanos celos.\
\
Si ves el cielo claro,\
Tal es la sencillez del alma mía;\
Y si, de luz avaro,\
De tinieblas emboza el claro día,\
es con su oscuridad y su inclemencia,\
imagen de mi vida en esta ausencia.\
\
Así que, Fabio amado\
Saber puede mis males sin costarte\
La noticia cuidado,\
Pues puedes de los campos informarte;\
Y pues yo a todo mi dolor ajusto,\
Saber mi pena sin dejar tu gusto.\
Mas żcuándo ˇay gloria mía!\
Mereceré gozar tu luz serena?\
\
żcuándo llegará el día\
que pongas dulce fin a tanta pena?\
żcuándo veré tus ojos, dulce encanto,\
y de los míos quitarás el llanto?\
\
żCuándo tu voz sonora\
herirá mis oídos delicada,\
y el alma que te adora,\
de inundación de gozos anegada,\
a recibirte con amante prisa\
saldrá a los ojos desatada en risa?\
\
żCuándo tu luz hermosa\
revestirá de gloria mis sentidos?\
ży cuándo yo dichosa,\
mis suspiros daré por bien perdidos,\
teniendo en poco el precio de mi llanto?\
Que tanto ha de penar quien goza tanto.\
\
żCuándo de tu apacible\
rostro alegre veré el semblante afable,\
y aquel bien indecible\
a toda humana pluma inexplicable?\
Que mal se ceńirá a lo definido\
Lo que no cabe en todo lo sentido.\
\
Ven, pues, mi prenda amada,\
Que ya fallece mi cansada vida\
De esta ausencia pesada;\
Ven, pues, que mientras tarda tu venida,\
Aunque me cueste su verdor enojos,\
Regaré mi esperanza con mis ojos.\
\
\
\
Excusándose de un Silencio...\
\
Pedirte, seńora, quiero\
De mi silencio perdón,\
Si lo que ha sido atención,\
Le hace parecer grosero.\
\
Y no me podrás culpar\
Si hasta aquí mi proceder,\
Por ocuparse en querer\
Se ha olvidado de explicar.\
\
Que en mi amorosa pasión\
No fue descuido ni mengua\
Quitar el uso a la lengua\
Por dárselo al corazón.\
\
Ni de explicarme dejaba,\
Que como la pasión mía\
Acá en el alma te hablaba\
\
Y en esta idea notable\
Dichosamente vivía;\
Porque en mi mano tenía\
El fingirte favorable.\
\
Con traza tan peregrina\
Vivió mi esperanza vana\
Pues te puedo hacer humana\
Concibiéndote divina.\
\
ˇOh, cuan loco llegué a verme\
en tus dichosos amores,\
que aun fingidos tus favores\
pudieron enloquecerme!\
\
ˇOh, cuán loco llegué a verme\
en tus dichosos amores,\
que aun fingidos tus favores\
pudieron enloquecerme!\
\
ˇOh, cómo en tu Sol hermoso\
mi ardiente afecto encendido,\
por cebarse en lo lúcido,\
olvidó lo peligroso!\
\
Perdona, si atrevimiento\
Fue atreverme a tu ardor puro;\
Que no hay Sagrado seguro\
De culpas de pensamiento.\
\
De esta manera engańaba\
La loca esperanza mía,\
Y dentro de mí tenía\
Todo el bien que deseaba.\
\
Mas ya tu precepto grave\
Rompe mi silencio mudo;\
Que él solamente ser pudo\
De mi respeto la llave.\
\
Y aunque el amar tu belleza\
Es delito sin disculpa,\
Castíguense la culpa\
Primero que la tibieza.\
\
No quieras, pues, rigurosa,\
Que estando ya declarada,\
Sea de veras desdichada\
Quien fue de burlas dichosa.\
\
Si culpas mi desacato,\
Culpa también tu licencia;\
Que si es mala mi obediencia,\
No fue justo tu mandato.\
\
Y si es culpable mi intento,\
Será mi afecto preciso;\
Porque es amarte un delito\
De que nunca me arrepiento.\
\
Esto en mis afectos halló,\
Y más, que explicar no sé;\
Mas tú, de lo que callé,\
Inferirás lo que callo.\
\
\
\
Teme que su Afecto Parezca...\
\
Seńora, si la belleza\
Que en vos llego a contemplar\
Es bastante a conquistar\
La más inculta dureza,\
\
żPor qué hacéis que el sacrificio\
Que debo a vuestra luz pura\
Debiéndose a la hermosura\
Se atribuya al beneficio?\
\
Cuando es bien que glorias cante,\
De ser vos, quien me ha rendido,\
żQueréis que lo agradecido\
Se equivoque con lo amante?\
\
Vuestro favor me condena\
A otra especie de desdicha,\
Pues me quitáis con la dicha\
El mérito de la pena.\
\
Si no es que dais a entender\
Que favor tan singular,\
Aunque se puede lograr,\
No se puede merecer.\
\
Con razón, pues la hermosura\
Aun llegada a poseerse,\
Si llega a merecerse,\
Dejara de ser ventura.\
\
Que estar un digno cuidado\
Con razón correspondido,\
Es premio de lo servido,\
Y no dicha de lo amado.\
\
Que dicha se ha de llamar\
Sólo la que, a mi entender,\
Ni se puede merecer,\
Ni se pretende alcanzar.\
\
Ya que este favor excede\
Tanto a todos, al lograrse,\
Que no sólo no pagarse,\
Mas ni agradecer se puede.\
\
Pues desde el dichoso día\
Que vuestra belleza vi,\
Tal del todo me rendí,\
Que no me quedó acción mía.\
\
Con lo cual, seńora, muestro,\
y a decir mi amor se atreve,\
Que nadie pagaros debe,\
Que vos honréis lo que es vuestro.\
\
Bien se que es atrevimiento\
Pero el amor es testigo\
Que no se lo que me digo\
Por saber lo que me siento.\
\
Y en fin, perdonad por Dios,\
Seńora, que os hable así,\
Que si yo estuviera en mí\
No estuvierais en mí vos.\
\
Sólo quiero suplicaros\
Que de mí recibáis hoy,\
No sólo el alma que os doy,\
Mas la que quisiera daros.\
\
\
Amor Importuno\
\
Dos dudas en que escoger\
Tengo, y no se a cual prefiera,\
Pues vos sentís que no quiera\
Y yo sintiera querer.\
\
Con que si a cualquiera lado\
Quiero inclinarme, es forzoso\
Quedando el uno gustoso\
Que otro quede disgustado.\
\
Si daros gusto me ordena\
La obligación, es injusto\
Que por daros a vos gusto\
Haya yo de tener pena.\
\
Y no juzgo que habrá quien\
Apruebe sentencia tal,\
Como que me trate mal\
Por trataros a vos bien.\
\
Mas por otra parte siento\
Que es también mucho rigor\
Que lo que os debo en amor\
Pague en aborrecimiento.\
\
Y aun irracional parece\
Este rigor, pues se infiere,\
Si aborrezco a quien me quiere\
żqué haré con quien aborrezco?\
\
No se como despacharos,\
Pues hallo al determinarme\
Que amaros es disgustarme\
Y no amaros disgustaros;\
\
Pero dar un medio justo\
En estas dudas pretendo,\
Pues no queriendo, os ofendo,\
Y queriéndoos me disgusto.\
\
Y sea esta la sentencia,\
Porque no os podáis quejar,\
Que entre aborrecer y amar\
Se parta la diferencia,\
\
De modo que entre el rigor\
Y el llegar a querer bien,\
Ni vos encontréis desdén\
Ni yo pueda encontrar amor.\
\
Esto el discurso aconseja,\
Pues con esta conveniencia\
Ni yo quedo con violencia\
Ni vos os partís con queja.\
\
Y que estaremos infiero\
Gustosos con lo que ofrezco;\
Vos de ver que no aborrezco,\
Yo de saber que no quiero.\
\
Sólo este medio es bastante\
A ajustarnos, si os contenta,\
Que vos me logréis atenta\
Sin que yo pase a lo amante,\
\
Y así quedo en mi entender\
Esta vez bien con los dos;\
Con agradecer, con vos;\
Conmigo, con no querer.\
\
Que aunque a nadie llega a darse\
En este gusto cumplido,\
Ver que es igual el partido\
Servirá de resignarse.\
\
\
\
Oración Traducida del Latín\
\
Ante tus ojos benditos\
Las culpas manifestamos,\
Y las heridas mostramos,\
Que hicieron nuestros delitos.\
\
Si el mal, que hemos cometido,\
Viene a ser considerado,\
Menor es lo tolerado,\
Mayor es lo merecido.\
\
La conciencia nos condena,\
No hallando en ella disculpa,\
Que respecto de la culpa,\
Es muy liviana la pena.\
\
Del pecado el duro azar\
Sentimos, que padecemos\
Y nunca enmendar queremos\
La costumbre de pecar.\
\
Cuando en tus azotes suda\
Sangre la naturaleza,\
Se rinde nuestra flaqueza,\
Y la maldad no se muda.\
\
Cuando el pecado mancilla\
La mente con fiera herida,\
Padece el alma afligida,\
Y la cerviz no se humilla.\
\
La vida suelta la rienda\
En su acostumbrado error,\
Suspira por el dolor,\
Y en el obrar no se enmienda.\
\
Puestos entre dos extremos,\
En cualquiera peligramos;\
Si esperas, no la enmendamos;\
Si te vengas, nos perdemos.\
\
De la aflicción el quebranto\
Nos obliga a la contricción\
Y en pasando la aflicción,\
Se olvida también el llanto.\
\
Cuando tu castigo empieza\
Promete el temor humano;\
Y en suspendiendo la mano,\
No se cumple la promesa.\
\
Cuando nos hieres, clamamos\
Que el perdón nos des, que puedes,\
Y así que nos lo concedes.\
Otra vez te provocamos.\
\
Tienes a la humana gente\
Convicta en su confesión,\
Que si no le das perdón,\
la acabarás justamente.\
\
Concede al humilde ruego\
Sin mérito a quien criaste,\
Tú que de nada formas\
A quien te rogará luego.\
\
\
\
Nacimiento de Cristo\
\
De la más fragante rosa\
Nació la abeja más bella,\
A quien el limpio rocío\
Dio purísima materia.\
\
Nace, pues, y apenas nace,\
Cuando en la misma moneda,\
Lo que en perlas recibió\
Empieza a pagar en perlas.\
\
Que llora el alba, no es mucho\
Que es costumbre en su belleza;\
Mas żquién hay que no se admire\
De que el sol lágrimas vierta?\
\
Si es por secundar la rosa,\
Es ociosa diligencia,\
Pues no es menester rocío\
Después de nacer la abeja.\
\
Y más cuando en la clausura\
De su virginal pureza\
Ni antecedente haber pudo,\
Ni puede haber quien suceda,\
\
żPues a que fin es el llanto,\
que dulcemente riega?\
Quien no puede dar más fruto\
żqué importa que estéril sea?\
\
Mas ay, que la abeja tiene\
Tan íntima dependencia\
Siempre con la rosa, que\
Depende su vida de ella;\
\
Pues dándole néctar puro,\
Que sus fragancias engendran,\
No sólo antes le concibe\
Pero después le alimenta.\
\
Hijo y madre, en tan divinas\
Peregrinas competencias,\
Ninguno queda deudor,\
Y ambos obligados quedan.\
\
La abeja paga el rocío\
De que la rosa la engendra,\
Y ella vuelve a retornarle con\
Lo mismo que la engendra.\
\
Ayudando el uno al otro\
Con mutua correspondencia,\
La abeja a la flor fecunda,\
Y ella a la abeja sustenta.\
\
Pues si por eso es el llanto,\
Llore Jesús, norabuena,\
Que lo que expende en rocío\
Cobrará después en néctar.\
\
\
\
Ante la Ausencia\
\
Divino dueńo mío,\
si al tiempo de partirme\
tiene mi amante pecho\
alientos de quejarse,\
oye mis penas, mira mis males.\
\
Aliéntese el dolor,\
si puede lamentarse,\
y a la vista de perderte\
mi corazón exhale\
llanto a la tierra, quejas al aire.\
\
Apenas tus favores\
quisieron coronarme,\
dichoso más que todos,\
felices como nadie,\
cuando los gustos fueron pesares.\
\
Sin duda el ser dichoso\
es la culpa más grave,\
pues mi fortuna adversa\
dispone que la pague\
con que a mis ojos tus luces falten,\
\
ˇAy, dura ley de ausencia!\
żquién podrá derogarte,\
si a donde yo no quiero\
me llevas, sin llevarme,\
con alma muerta, vivo cadáver?\
\
żSerá de tus favores\
sólo el corazón cárcel\
por ser aun el silencio\
si quiero que los guarde,\
custodio indigno, sigilo frágil?\
\
Y puesto que me ausento,\
por el último vale\
te prometo rendido\
mi amor y fe constante,\
siempre quererte, nunca olvidarte.\
\
\
Expresa los Efectos del Amor Divino\
\
Traigo conmigo un cuidado\
y tan esquivo que creo\
que aunque se sentirlo tanto,\
aun yo misma no lo siento.\
\
Es amor, pero es amor\
que faltándole lo ciego,\
los ojos que tiene son\
para darle más tormento.\
\
El término no es a quo,\
que causa el pesar, que veo,\
que siendo el término el bien\
todo el dolor es el medio.\
\
Si es lícito y aun debido\
este carińo que tengo\
żpor qué me han de dar castigo\
porque pago lo que debo?\
\
ˇOh cuánta fineza, oh cuántos\
carińos he visto tiernos!\
que amor que se tiene en Dios\
es calidad sin opuestos.\
\
De lo lícito no puede\
hacer contrarios conceptos\
con que es amor que al olvido\
no puede vivir expuesto.\
\
Yo me acuerdo ˇoh nunca fuera!\
que he querido en otro tiempo\
lo que pasó de locura\
y lo que excedió de extremo.\
\
Más como era amor bastardo\
y de contrarios compuesto,\
fue fácil desvanecerse\
de achaque de su ser mesmo.\
\
Mas ahora ˇay de mi! está\
tan en su natural centro,\
que la virtud y razón\
son quien aviva su incendio.\
\
Quien tal oyere dirá\
que si es así żpor qué peno?\
Más mi corazón ansioso\
dirá que por eso mesmo.\
\
ˇOh humana flaqueza nuestra,\
adonde el más puro afecto\
aun no sabe desnudarse\
del natural sentimiento!\
\
Tan precisa es la apetencia\
que a ser amados tenemos,\
que aun sabiendo que no sirve\
nunca dejarla sabemos.\
\
Que corresponda a mi amor\
nada ańade, mas no puedo\
por más que lo solicito\
dejar yo de apetecerlo.\
\
Si es delito, ya lo digo;\
si es culpa, ya lo confieso,\
mas no puedo arrepentirme\
por más que hacerlo pretendo.\
\
Bien ha visto quien penetra\
lo interior de mis secretos\
que yo misma estoy formando\
los dolores que padezco.\
\
Bien sabe que soy yo misma\
verdugo de mis deseos,\
pues muertos entre mis ansias,\
tienen sepulcro en mi pecho.\
\
Muero żquién lo creerá? a manos\
de la cosa que más quiero,\
y el motivo de matarme\
es el amor que le tengo.\
\
Así alimentando triste\
la vida con el veneno,\
la misma muerte que vivo,\
es la vida con que muero.\
\
Pero, valor, corazón,\
porque en tan dulce tormento,\
en medio de cualquier suerte\
no dejar de amar protesto.\
\
II\
\
Mientras la gracia me excita\
por elevarse a la esfera,\
más me abate a lo profundo\
el peso de mis miserias.\
\
La virtud y la costumbre\
en el corazón pelean\
y el corazón agoniza\
en tanto que lidian ellas.\
\
Y aunque es la virtud tan fuerte,\
temo que tal vez la venzan.\
que es muy grande la costumbre\
y está la virtud muy tierna.\
\
Obscurécense el discurso\
entre confusas tinieblas\
pues żquién podrá darme luz\
si está la razón a ciegas?\
\
De mí misma soy verdugo\
y soy cárcel de mí mesma.\
żquién vio que pena y penante\
una propia cosa sean?\
\
Hago disgusto a lo mismo\
que más agradar quisiera;\
y del disgusto que doy,\
en mí resulta la pena.\
\
Amo a Dios y siento en Dios,\
y hace mi voluntad mesma\
de lo que es alivio, cruz;\
del mismo puerto, tormenta.\
\
Padezca, pues Dios lo manda,\
mas de tal manera sea\
que si son penas las culpas,\
que no sean culpas las penas.\
\
\
\
Día de Comunión\
\
Amante dulce del alma,\
bien soberano a que aspiro,\
tú que sabes las ofensas\
castigar a beneficios;\
divino imán en que adoro\
hoy que tan propicio os miro\
que me animás a la osadía\
de poder llamaros mío;\
hoy, que en unión amorosa,\
pareció a vuestro carińo,\
que si no estabais en mí\
era poco estar conmigo;\
hoy, que para examinar\
el afecto con que os sirvo,\
al corazón en persona\
habéis entrado vos mismo,\
pregunto żes amor o celos\
tan cuidadoso escrutinio?\
que quien lo registra todo\
da de sospechar indicios.\
Mas ˇay, bárbara ignorante,\
y que de errores he dicho,\
como si el estorbo humano\
obstara al lince divino!\
Para ver los corazones\
no es menester asistirlos;\
que para vos son patentes\
las entrańas del abismo.\
Con una intuición presente\
tenéis en vuestro registro,\
el infinito pasado,\
hasta el presente finito;\
luego no necesitabais,\
para ver el pecho mío,\
si lo estáis mirando sabio,\
entrar a mirarlo fino;\
luego es amor, no celos,\
lo que en vos miro.\
\
\
\
Letras Para Cantar\
\
Hirió blandamente el aire\
Con su dulce voz Narcisa,\
Y él le repitió los ecos\
Por boca de las heridas.\
\
De los celestiales Ejes\
El rápido curso fija,\
Y en los Elementos cesa\
la discordia nunca unida.\
\
Al dulce imán de su voz\
Quisieran, por asistirla,\
Firmamento ser el Móvil,\
El Sol ser estrella fija.\
\
Tan bella, sobre canora,\
Que el amor dudoso admira,\
Si se deben sus arpones\
A sus ecos, o a su vista.\
\
Porque tan confusamente\
Hiere, que no se averigua,\
si está en la voz la hermosura,\
O en los ojos la armonía.\
\
Homicidas sus facciones\
El mortal cambio ejercitan;\
Voces, que alteran los ojos\
Rayos que el labio fulmina.\
\
Quién podrá vivir seguro,\
si su hermosura Divina\
Con los ojos y las voces\
Duplicadas armas vibra.\
\
El Mar la admira Sirena,\
Y con sus marinas Ninfas\
Le da en lenguas de las Aguas\
Alabanzas cristalinas:\
Pero Fabio que es el blanco\
Adonde las flecha tira,\
Así le dijo, culpando\
De superfluas sus heridas:\
No dupliques las armas,\
Bella homicida,\
que está ociosa la muerte\
Donde no hay vida.\
\
\
Detente sombra\
\
Detente, sombra de mi bien esquivo,\
imagen del hechizo que más quiero,\
bella ilusión por quien alegre muero,\
dulce ficción por quien penosa vivo.\
\
Si al imán de tus gracias, atractivo,\
sirve mi pecho de obediente acero,\
¿para qué me enamoras lisonjero\
si has de burlarme luego fugitivo?\
\
Mas blasonar no puedes, satisfecho,\
de que triunfa de mí tu tiranía:\
que aunque dejas burlado el lazo estrecho\
\
que tu forma fantástica ceñía,\
poco importa burlar brazos y pecho\
si te labra prisión mi fantasía. \
\
 \
Redondillas\
\
Hombres necios que acusáis\
a la mujer, sin razón,\
sin ver que sois la ocasión\
de lo mismo que culpáis;\
\
si con ansia sin igual\
solicitáis su desdén,\
por qué queréis que obren bien\
si las incitáis al mal?\
\
Combatís su resistencia\
y luego, con gravedad,\
decís que fue liviandad\
lo que hizo la diligencia.\
\
Parecer quiere el denuedo\
de vuestro parecer loco,\
al niño que pone el coco\
y luego le tiene miedo.\
\
Queréis, con presunción necia,\
hallar a la que buscáis\
para prentendida, Thais,\
y en la posesión, Lucrecia.\
\
¿Qué humor puede ser más raro\
que el que, falto de consejo,\
él mismo empaña el espejo\
y siente que no esté claro?\
\
Con el favor y el desdén\
tenéis condición igual,\
quejándoos, si os tratan mal,\
burlándoos, si os quieren bien.\
\
Opinión, ninguna gana,\
pues la que más se recata,\
si no os admite, es ingrata,\
y si os admite, es liviana.\
\
Siempre tan necios andáis\
que, con desigual nivel,\
a una culpáis por cruel\
y a otra por fácil culpáis.\
\
¿Pues como ha de estar templada\
la que vuestro amor pretende?,\
¿si la que es ingrata ofende,\
y la que es fácil enfada?\
\
Mas, entre el enfado y la pena\
que vuestro gusto refiere,\
bien haya la que no os quiere\
y quejaos en hora buena.\
\
Dan vuestras amantes penas\
a sus libertades alas,\
y después de hacerlas malas\
las queréis hallar muy buenas.\
\
¿Cuál mayor culpa ha tenido\
en una pasión errada:\
la que cae de rogada,\
o el que ruega de caído?\
\
¿O cuál es de más culpar,\
aunque cualquiera mal haga;\
la que peca por la paga\
o el que paga por pecar?\
\
¿Pues, para qué os espantáis\
de la culpa que tenéis?\
Queredlas cual las hacéis\
o hacedlas cual las buscáis.\
\
Dejad de solicitar,\
y después, con más razón,\
acusaréis la afición\
de la que os fuere a rogar.\
\
Bien con muchas armas fundo\
que lidia vuestra arrogancia,\
pues en promesa e instancia\
juntáis diablo, carne y mundo.\
\
 \
Finjamos que soy feliz \
\
Finjamos que soy feliz,\
triste pensamiento, un rato;\
quizá prodréis persuadirme,\
aunque yo sé lo contrario,\
que pues sólo en la aprehensión\
dicen que estriban los daños,\
si os imagináis dichoso\
no seréis tan desdichado.\
\
Sírvame el entendimiento\
alguna vez de descanso, \
y no siempre esté el ingenio\
con el provecho encontrado.\
Todo el mundo es opiniones\
de pareceres tan varios,\
que lo que el uno que es negro\
el otro prueba que es blanco.\
\
A unos sirve de atractivo\
lo que otro concibe enfado;\
y lo que éste por alivio,\
aquél tiene por trabajo.\
\
El que está triste, censura\
al alegre de liviano;\
y el que esta alegre se burla\
de ver al triste penando.\
\
Los dos filósofos griegos\
bien esta verdad probaron:\
pues lo que en el uno risa,\
causaba en el otro llanto.\
\
Célebre su oposición\
ha sido por siglos tantos,\
sin que cuál acertó, esté \
hasta agora averiguado.\
\
Antes, en sus dos banderas\
el mundo todo alistado,\
conforme el humor le dicta,\
sigue cada cual el bando.\
\
Uno dice que de risa\
sólo es digno el mundo vario;\
y otro, que sus infortunios\
son sólo para llorados.\
\
Para todo se halla prueba\
y razón en qué fundarlo;\
y no hay razón para nada,\
de haber razón para tanto.\
\
Todos son iguales jueces;\
y siendo iguales y varios,\
no hay quien pueda decidir\
cuál es lo más acertado.\
\
Pues, si no hay quien lo sentencie,\
¿por qué pensáis, vos, errado,\
que os cometió Dios a vos\
la decisión de los casos?\
\
O ¿por qué, contra vos mismo,\
severamente inhumano,\
entre lo amargo y lo dulce,\
queréis elegir lo amargo?\
\
Si es mío mi entendimiento,\
¿por qué siempre he de encontrarlo\
tan torpe para el alivio,\
tan agudo para el daño?\
\
El discurso es un acero\
que sirve para ambos cabos:\
de dar muerte, por la punta,\
por el pomo, de resguardo.\
\
Si vos, sabiendo el peligro\
queréis por la punta usarlo,\
¿qué culpa tiene el acero\
del mal uso de la mano?\
\
No es saber, saber hacer\
discursos sutiles, vanos;\
que el saber consiste sólo\
en elegir lo más sano.\
\
Especular las desdichas\
y examinar los presagios,\
sólo sirve de que el mal\
crezca con anticiparlo.\
\
En los trabajos futuros,\
la atención, sutilizando,\
más formidable que el riesgo\
suele fingir el amago.\
\
Qué feliz es la ignorancia\
del que, indoctamente sabio,\
halla de lo que padece,\
en lo que ignora, sagrado!\
\
No siempre suben seguros\
vuelos del ingenio osados,\
que buscan trono en el fuego\
y hallan sepulcro en el llanto.\
\
También es vicio el saber,\
que si no se va atajando,\
cuando menos se conoce\
es más nocivo el estrago;\
y si el vuelo no le abaten,\
en sutilezas cebado,\
por cuidar de lo curioso\
olvida lo necesario.\
\
Si culta mano no impide\
crecer al árbol copado,\
quita la sustancia al fruto\
la locura de los ramos.\
\
Si andar a nave ligera\
no estorba lastre pesado,\
sirve el vuelo de que sea\
el precipicio más alto.\
\
En amenidad inútil,\
¿qué importa al florido campo,\
si no halla fruto el otoño,\
que ostente flores el mayo?\
\
¿De qué sirve al ingenio\
el producir muchos partos,\
si a la multitud se sigue\
el malogro de abortarlos?\
\
Y a esta desdicha por fuerza\
ha de seguirse el fracaso\
de quedar el que produce,\
si no muerto, lastimado.\
\
El ingenio es como el fuego,\
que, con la materia ingrato,\
tanto la consume más\
cuando él se ostenta más claro.\
\
Es de su propio Señor\
tan rebelado vasallo,\
que convierte en sus ofensas\
las armas de su resguardo.\
\
Este pésimo ejercicio,\
este duro afán pesado,\
a los ojos de los hombres\
dio Dios para ejercitarlos.\
\
¿Qué loca ambición nos lleva\
de nosotros olvidados?\
Si es para vivir tan poco,\
¿de qué sirve saber tanto?\
¡Oh, si como hay de saber,\
hubiera algún seminario\
o escuela donde a ignorar\
se enseñaran los trabajos!\
\
¡Qué felizmente viviera\
el que, flojamente cauto,\
burlara las amenazas\
del influjo de los astros!\
\
Aprendamos a ignorar,\
pensamiento, pues hallamos\
que cuanto añado al discurso,\
tanto le usurpo a los años.\
 \
Pues estoy condenada\
\
Pues estoy condenada,\
Fabio, a la muerte, por decreto tuyo,\
y la sentencia airada\
ni la apelo, resisto ni la huyo,\
óyeme, que no hay reo tan culpado\
a quien el confesar le sea negado.\
\
Porque te han informado,\
dices, de que mi pecho te ha ofendido,\
me has, fiero, condenado.\
¿Y pueden, en tu pecho endurecido\
más la noticia incierta, que no es ciencia,\
que de tantas verdades la experiencia?\
\
Si a otros crédito has dado,\
Fabio, ¿por qué a tus ojos se lo niegas,\
y el sentido trocado\
de la ley, al cordel mi cuello entregas,\
pues liberal me amplías los rigores\
y avaro me restringes los favores?\
\
Si a otros ojos he visto,\
mátenme, Fabio, tus airados ojos;\
si a otro cariño asisto,\
asístanme implacables tus enojos;\
y si otro amor del tuyo me divierte,\
tú, que has sido mi vida, me des muerte.\
\
Si a otro, alegre, he mirado,\
nunca alegre me mires ni te vea;\
si le hablé con agrado,\
eterno desagrado en ti posea;\
y si otro amor inquieta mi sentido,\
sáqueseme el alma tú, que mi alma has sido.\
\
Mas, supuesto que muero,\
sin resistir a mi infeliz suerte,\
que me des sólo quiero\
licencia de que escoja yo mi muerte;\
deja la muerte a mi elección medida,\
pues en la tuya pongo yo la vida.\
\
Esta tarde mi bien \
\
Esta tarde, mi bien, cuando te hablaba,\
como en tu rostro y tus acciones vía\
que con palabras no te persuadía,\
que el corazón me vieses deseaba;\
\
y Amor, que mis intentos ayudaba,\
venció lo que imposible parecía:\
pues entre el llanto, que el dolor vertía,\
el corazón deshecho destilaba.\
\
Baste ya de rigores, mi bien, baste:\
no te atormenten más celos tiranos,\
ni el vil recelo tu inquietud contraste\
\
con sombras necias, con indicios vanos,\
pues ya en líquido humor viste y tocaste\
mi corazón deshecho entre tus manos.\
\
\
Estos versos lector mío \
\
Estos versos, lector mío,\
que a tu deleite consagro,\
y sólo tienen de buenos\
conocer yo que son malos,\
ni disputártelos quiero,\
ni quiero recomendarlos,\
porque eso fuera querer\
hacer de ellos mucho caso.\
\
No agradecido te busco:\
pues no debes, bien mirado,\
estimar lo que yo nunca\
juzgué que fuera a tus manos.\
En tu libertad te pongo,\
si quisieres censurarlos;\
pues de que, al cabo, te estás\
en ella, estoy muy al cabo.\
\
No hay cosa más libre que \
el entendimiento humano;\
pues lo que Dios no violenta,\
por qué yo he de violentarlo?\
\
Di cuanto quisieres de ellos,\
que, cuanto más inhumano\
me los mordieres, entonces\
me quedas más obligado,\
pues le debes a mi musa\
el más sazonado plato\
(que es el murmurar), según\
un adagio cortesano.\
Y siempre te sirvo, pues,\
o te agrado, o no te agrado:\
si te agrado, te diviertes;\
murmuras, si no te cuadro.\
\
Bien pudiera yo decirte\
por disculpa, que no ha dado\
lugar para corregirlos\
la priesa de los traslados;\
que van de diversas letras,\
y que algunos, de muchachos,\
matan de suerte el sentido\
que es cadáver el vocablo;\
y que, cuando los he hecho,\
ha sido en el corto espacio\
que ferian al ocio las\
precisiones de mi estado;\
que tengo poca salud\
y continuos embarazos,\
tales, que aun diciendo esto,\
llevo la pluma trotando.\
\
Pero todo eso no sirve,\
pues pensarás que me jacto\
de que quizá fueran buenos\
a haberlos hecho despacio;\
y no quiero que tal creas,\
sino sólo que es el darlos\
a la luz, tan sólo por\
obedecer un mandato.\
\
Esto es, si gustas creerlo,\
que sobre eso no me mato,\
pues al cabo harás lo que\
se te pusiere en los cascos.\
Y adiós, que esto no es más de\
darte la muestra del paño:\
si no te agrada la pieza,\
no desenvuelvas el fardo.\
\
 \
Ya que para despedirme\
\
Ya que para despedirme,\
dulce idolatrado dueño,\
ni me da licencia el llanto\
ni me da lugar el tiempo,\
\
háblente los tristes rasgos,\
entre lastimosos ecos,\
de mi triste pluma, nunca\
con más justa causa negros.\
\
Y aun ésta te hablará torpe\
con las lágrimas que vierto,\
porque va borrando el agua\
lo que va dictando el fuego.\
\
Hablar me impiden mis ojos;\
y es que se anticipan ellos,\
viendo lo que he de decirte,\
a decírtelo primero.\
\
Oye la elocuencia muda\
que hay en mi dolor, sirviendo\
los suspiros, de palabras,\
las lágrimas, de conceptos.\
\
Mira la fiera borrasca\
que pasa en el mar del pecho,\
donde zozobran, turbados, \
mis confusos pensamientos.\
\
Mira cómo ya el vivir\
me sirve de afán grosero;\
que se avergüenza la vida\
de durarme tanto tiempo.\
\
Mira la muerte, que esquiva\
huye porque la deseo;\
que aun la muerte, si es buscada,\
se quiere subir de precio.\
\
Mira cómo el cuerpo amante,\
rendido a tanto tormento,\
siendo en lo demás cadáver,\
sólo en el sentir es cuerpo.\
\
Mira cómo el alma misma\
aun teme, en su ser exento,\
que quiera el dolor violar\
la inmunidad de lo eterno.\
\
En lágrimas y suspiros\
alma y corazón a un tiempo,\
aquél se convierte en agua,\
y ésta se resuelve en viento.\
\
Ya no me sirve de vida\
esta vida que poseo,\
sino de condición sola\
necesaria al sentimiento.\
\
Mas, por qué gasto razones\
en contar mi pena y dejo\
de decir lo que es preciso,\
por decir lo que estás viendo?\
\
En fin, te vas, ay de mi!\
Dudosamente lo pienso:\
pues si es verdad, no estoy viva,\
y si viva, no lo creo.\
\
Posible es que ha de haber día\
tan infausto, funesto,\
en que sin ver yo las tuyas\
esparza sus luces Febo?\
\
Posible es que ha de llegar\
el rigor a tan severo,\
que no ha de darle tu vista\
a mis pesares aliento?\
\
Ay, mi bien, ay prenda mía,\
dulce fin de mis deseos!\
Por qué me llevas el alma,\
dejándome el sentimiento?\
\
Mira que es contradicción\
que no cabe en un sujeto,\
tanta muerte en una vida,\
tanto dolor en un muerto.\
\
Mas ya que es preciso, ay triste!,\
en mi infeliz suceso,\
ni vivir con la esperanza,\
ni morir con el tormento,\
\
dame algún consuelo tú\
en el dolor que padezco;\
y quien en el suyo muere,\
viva siquiera en tu pecho.\
\
No te olvides que te adoro,\
y sírvante de recuerdo\
las finezas que me debes,\
si no las prendas que tengo.\
\
Acuérdate que mi amor,\
haciendo gala de riesgo,\
sólo por atropellarlo\
se alegraba de tenerlo.\
\
Y si mi amor no es bastante,\
el tuyo mismo te acuerdo,\
que no es poco empeño haber\
empezado ya en empeño.\
\
Acuérdate, señor mío,\
de tus nobles juramentos;\
y lo que juró la boca\
no lo desmientan tus hechos.\
\
Y perdona si en temer\
mi agravio, mi bien, te ofendo,\
que no es dolor, el dolor\
que se contiene atento.\
\
Y adiós; que con el ahogo\
que me embarga los alientos,\
ni sé ya lo que te digo\
ni lo que te escribo leo.\
\
\
Dime vencedor rapaz\
\
\
Dime vencedor Rapaz,\
vencido de mi constancia,\
¿Qué ha sacado tu arrogancia\
de alterar mi firme paz?\
Que aunque de vencer capaz\
es la punta de tu arpón,\
¿qué importa el tiro violento,\
si a pesar del vencimiento\
queda viva la razón?\
\
Tienes grande señorío;\
pero tu jurisdicción\
domina la inclinación,\
mas no pasa el albedrío.\
Y así librarme confío\
de tu loco atrevimiento,\
pues aunque rendida siento\
y presa la libertad,\
se rinde la voluntad\
pero no el consentimiento.\
\
En dos partes dividida\
tengo el alma en confusión:\
una, esclava a la pasión,\
y otra, a la razón medida.\
Guerra civil, encendida,\
aflige el pecho importuna:\
quiere vencer cada una,\
y entre fortunas tan varias,\
morirán ambas contrarias\
pero vencerá ninguna.\
\
Cuando fuera, Amor, te vía,\
no merecí de ti palma;\
y hoy, que estás dentro del alma,\
es resistir valentía.\
Córrase, pues, tu porfía,\
de los triunfos que te gano:\
pues cuando ocupas, tirano,\
el alma, sin resistillo,\
tienes vencido el Castillo\
e invencible el Castellano.\
\
Invicta razón alienta\
armas contra tu vil saña,\
y el pecho es corta campaña\
a batalla tan sangrienta.\
Y así, Amor, en vano intenta\
tu esfuerzo loco ofenderme:\
pues podré decir, al verme\
expirar sin entregarme,\
que conseguiste matarme\
mas no pudiste vencerme.\
\
\
Cogióme sin prevención\
\
Cogióme sin prevención\
Amor, astuto y tirano:\
con capa de cortesano\
se me entró en el corazón.\
Descuidada la razón\
y sin armas los sentidos,\
dieron puerta inadvertidos;\
y él, por lograr sus enojos,\
mientras suspendió los ojos\
me salteó los oídos.\
\
Disfrazado entró y mañoso;\
mas ya que dentro se vio\
del Paladión, salió\
de aquel disfraz engañoso;\
y, con ánimo furioso,\
tomando las armas luego,\
se descubrió astuto Griego\
que, iras brotando y furores,\
matando los defensores,\
puso a toda el Alma fuego.\
\
Y buscando sus violencias\
en ella al príamo fuerte,\
dio al Entendimiento muerte,\
que era Rey de las potencias;\
y sin hacer diferencias\
de real o plebeya grey,\
haciendo general ley\
murieron a sus puñales\
los discursos racionales\
porque eran hijos del Rey.\
\
A Casandra su fiereza\
buscó, y con modos tiranos,\
ató a la Razón las manos,\
que era del Alma princesa.\
En prisiones su belleza\
de soldados atrevidos,\
lamenta los no creídos\
desastres que adivinó,\
pues por más voces que dio\
no la oyeron los sentidos.\
\
Todo el palacio abrasado\
se ve, todo destruido;\
Deifobo allí mal herido,\
aquí Paris maltratado.\
Prende también su cuidado\
la modestia en Polixena;\
y en medio de tanta pena,\
tanta muerte y confusión,\
a la ilícita afición\
sólo reserva en Elena.\
\
Ya la Ciudad, que vecina\
fue al Cielo, con tanto arder,\
sólo guarda de su ser\
vestigios, en su ruina.\
Todo el amor lo extermina;\
y con ardiente furor,\
sólo se oye, entre el rumor\
con que su crueldad apoya:\
'Aquí yace un Alma Troya\
¡Victoria por el Amor!'\
\
Este amoroso tormento \
\
Este amoroso tormento \
que en mi corazón se ve, \
se que lo siento y no se \
la causa porque lo siento \
\
\
Siento una grave agonía \
por lograr un devaneo, \
que empieza como deseo \
y para en melancolía. \
\
y cuando con mas terneza \
mi infeliz estado lloro \
se que estoy triste e ignoro \
la causa de mi tristeza. ' \
\
\
Siento un anhelo tirano \
por la ocasión a que aspiro, \
y cuando cerca la miro \
yo misma aparto la mano. \
Porque si acaso se ofrece, \
después de tanto desvelo \
la desazona el recelo \
o el susto la desvanece. \
\
Y si alguna vez sin susto \
consigo tal posesión \
(cualquiera) leve ocasión \
me malogra todo el gusto. \
\
Siento mal del mismo bien \
con receloso temor \
y me obliga el mismo amor \
tal vez a mostrar desdén. \
\
\
Verde embeleso\
\
Verde embeleso de la vida humana,\
loca esperanza, frenesí dorado,\
sueño de los despiertos intrincado,\
como de sueños, de tesoros vana;\
\
alma del mundo, senectud lozana,\
decrépito verdor imaginado;\
el hoy de los dichosos esperado,\
y de los desdichados el mañana:\
\
sigan tu sombra en busca de tu día\
los que, con verdes vidrios por anteojos,\
todo lo ven pintado a su deseo;\
\
que yo, más cuerda en la fortuna mía,\
tengo en entrambas manos ambos ojos\
y solamente lo que toco veo.",
                    path=u"/c", tags=u"SJIC")

writer.add_document(title=u"Refugio Barragan de Toscano", content=u"¡Ése es el mío!\
\
Si oyes decir que en cuna de tristezas\
y a los arrullos del invierno frío,\
nutrido en el dolor y el sufrimiento\
se meció un corazón… ¡Ése es el mío!\
Si oyes contar que es anémico y enfermo\
enlutado a los velos del hastío\
al banquete se sienta de la vida\
un triste corazón… ¡Ése es el mío!\
Si sabes que rendido y fatigado\
herido al filo de rigor sombrío,\
cabe las ruinas de esperanzas yertas\
ha muerto un corazón… ¡Ése es el mío!\
\
\
Tendencias opuestas\
\
\
En el yerto jardín del pensamiento\
se abrió la flor de los recuerdos míos\
pálida como el lirio que en la tarde\
se mece al viento de otoñales fríos.\
Miróla el corazón y dijo triste:\
¡En tu perfume encontraré la vida!\
¡Y yo en cada una de tus lindas hojas\
una esperanza lloraré perdida!\
Dijo doliente el alma, y un suspiro\
de ella escapado remontóse al cielo,\
en tanto que una lágrima candente\
brotó del corazón y cayó al suelo.\
Así dos seres en el hombre luchan\
cual corrientes radiales de la nube:\
materia y corrupción el uno, baja;\
espíritu inmortal el otro, sube.\
\
\
\
Amor filial\
\
Está la niña sentada\
de la madre en las rodillas,\
graciosa como los ángeles,\
pura como los reflejos\
del sol sobre las colinas,\
risueña como los prados\
y como el aura festiva.\
Sus lindos brazos, a medias\
cubiertos por la batista,\
hoyuelados y redondos\
de la madre el cuello lían,\
mientras su boca de nácar\
breve, boruquienta y lista,\
la está besando en los ojos\
en la frente y las mejillas.\
Y cuando tan cara prenda\
la madre a besar se inclina,\
ella rehúye juguetona\
la rizada cabecita\
y esconde la blanca frente\
entre la blanca batista\
para volverla radiante\
a la madre que la mima,\
y la estrecha entre sus brazos\
y con ternura infinita,\
la prodiga mil caricias\
y en sus gracias se extasía.\
¡Feliz madre! Llena su alma\
emoción indefinida.\
Aquel amor es su cielo\
y es su encanto aquella niña.\
«Carmen, Carmen, ¿me amas mucho?»,\
dice al besar sus mejillas:\
y ella, con voz que asemeja\
suave murmullo de brisas,\
una música, una nota,\
un suspiro, una armonía,\
un rumor de castos besos,\
dice entre alegre y loquilla:\
«Como lo que hay en el cielo,\
así te amo, madre mía.\
A nadie amaré en el mundo\
como a ti, sol de mi vida».\
Con tristeza indefinible\
la madre la oye; y suspira\
al recordar que a su madre\
lo mismo contó de niña.\
\
Almas y flores\
\
En un humilde tiesto\
dos flores de la vida, se encontraron.\
Pequeña y triste, la una;\
fragante la otra y bella cual ninguna;\
¡Se vieron juntas, y a la par se amaron!\
¡Así suelen dos almas\
que al mundo fueron en distinta cuna,\
encontrarse por suerte,\
y amarse con pasión hasta la muerte,\
burlándose de sangre y de fortuna!\
\
\
Amores del campo\
\
«Ensíllate el alazán\
o la yegua champurrada,\
y anda al pueblo, Juan Antonio,\
a vender queso y bueyada.\
De paso dile a tía Nica\
que venga por su cuajada,\
que quiero darle a la probe\
tantita lechi quemada.»\
Entra al corral, Juan Antonio,\
y echa fuera la manada:\
laza el fogoso alazán\
y de un huásimo lo amarra.\
Ya está ensillado el corcel,\
ya el freno impaciente tasca,\
y ya siente del jinete\
la ligerísima carga.\
Lleva sombrero alemán\
con toquilla galonada,\
con dos grandes iniciales\
bordadas de oro y de plata.\
La calzonera de paño\
por el extremo abrochada,\
hacia la rodilla abierta,\
con botonadura blanca.\
Y fajada a la cintura\
una banda flor granada,\
y un sarape del Saltillo\
del alazán a las ancas.\
«¡Qué guapo va, Juan Antonio»,\
dice la madre encantada,\
«con sus armas, su soguilla,\
su machete y su gualdrapa.\
¡Vaya si es guapo! Pues mira,\
que aunque te canses no jallas\
tres leguas a la redonda,\
como la suya una cara.\
Que yo tengo de casarlo\
con una muchacha guapa,\
fresca como una amapola,\
como una rosa de pascua.»\
Así ponderando al hijo\
se quedan Juan y Mariana\
hasta que desaparece\
de un montecillo en la falda.\
\
\
\
El arroyo\
\
Cual la fresca primavera,\
como el granado encendida,\
viene a bañarse al arroyo\
la encantadora Lucía.\
Que es bella todos lo dicen;\
mas yo digo que es más linda\
que el arroyo en que se baña,\
que lo albores del día.\
Tiene ojos negros y ardientes,\
pestañas grandes y chinas,\
dientes que parecen perlas\
en botón de Alejandría.\
La nariz correcta y pura,\
frente grande, alabastrina,\
el pelo un poco quebrado,\
fresca y tersa la mejilla.\
Es graciosa y arrogante\
cual las palmas de Turquía,\
tan esbelta como el junco\
que crece en la serranía.\
Llega cantando al arroyo;\
deja el calzado a la orilla,\
y el pie pequeño y desnudo\
entre la arena desliza.\
Y alzando un poco la enagua\
hacia las ondas se inclina;\
y al verse tan hechicera\
sonríe la picarilla.\
Mete el pie dos o tres veces\
en las azuladas linfas,\
y entre alegre y juguetona\
otras tantas le retira.\
Enamorado el arroyo,\
quizá al verla tan loquilla,\
la baña de blancas perlas\
que el mórbido pecho agitan.\
Y al encontrarse bañada\
de brillantes que cintilan\
a la luz del sol, asoma\
a sus labios la sonrisa.\
Oculto en tanto en las ramas,\
allá de la opuesta orilla,\
Juan Antonio la contempla\
con admiración divina.\
Y al verla tan hechicera\
esta promesa se hacía:\
«Cuanto soy y cuanto tengo\
daré por tu amor, Lucía».\
Ella en tanto recelosa\
alza su mirada limpia\
y oculto tras los tacotes\
a Juan Antonio divisa.\
En encarnado se torna\
el rosa de su mejilla;\
trata de huir, mas el mozo\
se le acerca de puntillas.\
Y entre asustada y alegre\
al agua baja la vista\
en tanto que Juan Antonio\
así le dice a Lucía:\
—Tus gracias y tus monadas,\
allá de la opuesta orilla\
he mirado embebecido:\
y tan cierto que eres linda\
que celos me ha dado el agua\
en que tu hermosura miras.\
me ha dado celos el viento\
que te besó a hurtadillas,\
la arena en que el pie de niño\
juguetona zambullías.\
Y las perlas que saltaban\
y en tu seno se escondían.\
El sol que desde ese cielo\
encendida te ponía.\
y me he dicho: ¡Qué dichoso\
Juan Antonio no serías\
si pudieras ser arroyo,\
viento, arena, perlas frías,\
y sol que desde la altura\
reditieras a Lucía!\
—Galán eres y buen mozo\
—dice bajando la vista.\
—¿Quieres casarte conmigo\
dulce alma del alma mía?\
Si me das tu blanca mano,\
tu hermosura peregrina\
será el sol en que me abrace\
por la noche y por el día.\
Te llevaré a donde vaya,\
reina de la serranía,\
y en fogosos alazanes\
iremos al pueblo a misa.\
Te llevaré a la majada,\
verás ganados y crías,\
y beberás dulce lechi\
en blancas tazas de China.\
Y al calor, con tu ligera\
enagua de muselina,\
te conduciré a los bosques\
de pinos y altas encinas.\
Verás a las borregadas\
saltando entre la pedrisca\
y pastando entre la yerba\
los toros y las vaquillas.\
Y cuanto mires en torno,\
mi sultana peregrina,\
será tuyo, sólo tuyo;\
como es tuya el alma mía.\
—¿Y es cierto lo que me dices?\
¿Es verdad lo que me pintas?\
Porque mi padre me dijo,\
no hace mucho: «Mi Lucía,\
de engañar a las muchachas\
los hombres tienen manía».\
Por toda respuesta el mozo\
con donaire y gallardía,\
puso un anillo en la mano\
de la seductora niña.\
Como tímida gacela\
ella después se retira\
con el corazón flechado,\
como la grana encendida.\
Y él montando en su alazán,\
deja atrás la serranía,\
y se va al pueblo soñando\
con la imagen de Lucía.\
Prendada está la hechicera,\
se dice con alegría;\
en tanto que suspirando,\
ella el arroyo no olvida.\
Y dice: «Viendo el anillo\
que en su blanca mano brilla,\
muy pronto será envidiada\
de toda la ranchería».\
\
\
La llegada\
\
Con el guapo Juan Antonio,\
ella por fin se ha casado,\
y con música y cohetes\
los esperan en el campo.\
Desde tiempos muy remotos\
acostumbran en los ranchos\
quitarle la espuela al novio\
entre risadas y aplausos.\
E ir a bajar a la novia\
es honor tan estimado,\
que corren a verla aún lejos\
en sus fogosos caballos.\
Así es que todos aguardan\
con impaciencia en el rancho,\
y miran hacia el camino\
que a su encuentro ha de llevarlos.\
De pronto gritan: ¡Los novios!\
cada uno parte esperando,\
en aquella apuesta lucha\
ser el más afortunado.\
En una nube de polvo\
los jinetes y caballos\
de pronto quedan envueltos;\
pero ya llegan, ¡qué chasco!\
La traviesa de Lucía\
loquilla riendo al mirarlos,\
ágil como la gacela\
pega un brinco del caballo.\
Y que ¡Viva! gritan unos,\
otros celebran el garbo\
con que supo disputarles\
la victoria palmo a palmo.\
Al novio quita la espuela\
el más apuesto y gallardo,\
después vanse a la ramada\
do el mariachi está tocando.\
Grandes vasos de tequila\
se corren de mano en mano,\
y piden para los novios\
un jarabe repicado.\
Y ella terciando el rebozo,\
una punta en cada lado,\
sigue el son con tanto tino\
que parece anda volando.\
Hace el tequila su oficio,\
se ponen muy humorados,\
sigue la locura, el pleito,\
y hacen el arpón pedazos.\
Pagan luego el instrumento,\
que es costumbre, en esos casos\
quebrar, pues de lo contrario\
dicen: no sirvió el fandango.\
Concluida la tornaboda\
cada cual se va a su rancho,\
¿y los novios?, como todos;\
vida nueva y al trabajo.\
Pero su vida está exenta\
de ese hálito emponzoñado\
que se respira en las cortes,\
entre el oro y el brocado.\
Pues que no hay amor más puro,\
cariño más tierno y santo,\
que el que crece y se alimenta\
bajo las auras del campo.\
\
\
Parábola de la oveja perdida\
\
Pastaban en verde campo\
cien ovejas muy hermosas;\
una de ellas se extravió\
entre las vecinas rocas.\
El pastor la echa de menos,\
y, como las ama a todas,\
con sus gritos lastimeros\
todo el contorno alborota.\
Deja las noventa y nueve,\
sin mirar que quedan solas,\
y en busca de la extraviada\
pasa larguísimas horas.\
Al fin la encuentra, y la trae\
al rebaño donde mora;\
y haciéndole mil caricias\
alegre cántico entona.\
En la oveja descarriada,\
que el pastor lamenta y llora,\
se ve al pecador que errado\
la ley de Dios abandona.\
\
\
¡Murió el siglo! ¡Viva el siglo!\
\
Cien años hace que un día\
brilló tu primera aurora.\
Naciste bien a deshora\
y quizá en noche sombría.\
Al ofrecerte la flora\
de sus nectáreos la esencia;\
al par, con dulce cadencia,\
luciendo plumas de encaje;\
las aves en el ramaje,\
no anunciaron tu existencia.\
Mas… ¡qué importó! Los poetas\
con su numen por tesoro,\
templaron las arpas de oro,\
entre las sombras discretas;\
y en verso egregio y sonoro\
te dieron la bienvenida…\
¡Quizás les fue presentada\
tu grandeza soberana,\
y te cantaron ¡Hossana!\
con voz vibrante y sentida!\
Siglo en portentos fecundo,\
¿qué genios te bautizaron?\
¿Qué arcángeles te arrullaron?\
¿Qué sol te alumbró en el mundo?\
Eres grande, eres profundo,\
tus hechos son inmortales;\
la ciencia te dio a raudales\
los tesoros de su genio,\
y del mundo, en el proscenio,\
asombraste a los mortales.\
Vapor tomando por alas;\
electricidad, por bríos;\
bogaste en mares y ríos,\
derroche haciendo de galas.\
Del poder en las escalas,\
fuiste titán que se encumbra,\
meteoro que deslumbra\
haciendo surja la luz\
de las sombras, del capús,\
de la enlutada penumbra.\
Transportaste el pensamiento\
por los hilos de una idea;\
¡mas tu genio que aletea\
no se cansa, está sediento!\
Sueña, en su noble ardimento,\
otra palma, otra victoria;\
y así, en pos de nueva gloria,\
las imágenes alienta,\
revive escenas que asienta\
en sus páginas la historia.\
Grabar voz, timbre, cadencia,\
palabras, modulaciones;\
una fue de tus creaciones\
sublimes, sin competencia.\
Empleando ruda potencia\
puentes de hierro puliste,\
rieles de acero tendiste\
y, horadando las entrañas\
de las abruptas montañas,\
lejanas tierras uniste.\
Inventando proyectiles\
y fabricando cañones,\
diezmaste los batallones\
como el lobo, los rediles.\
¿De las cadenas serviles\
el engranaje deshaces…?\
¡Luz de libertad en haces,\
le das a la patria mía,\
hollando la tiranía\
con el pendón de las paces!\
Has querido que tus huellas\
el tiempo nunca borrara,\
y de tu pupila clara\
surgieron, cual las estrellas,\
luces ingentes y bellas,\
Cuya intensidad admira;\
y arden hoy en la alta pira\
donde descansas inerte,\
en los brazos de una muerte\
que del mundo se retira.\
¿Qué ciencia no floreció\
bajo tu imperio asombroso?\
¿Qué industria, qué arte en reposo\
bajo tu influjo quedó?\
Todo por ti renació\
a una vida de adelanto;\
y entre risas y entre llanto,\
la ignorancia desarmada,\
fue a ocultarse avergonzada,\
hecho jirones el manto.\
¡Qué herencia tan estupenda\
al siglo que viene dejas…!\
¡O se hunde en sombras añejas\
o sigue tu ilustre senda!\
Es fuerza que de ti aprenda\
legendarias maravillas,\
para que caiga hecha astillas,\
la imagen del retroceso,\
y siga en marcha el progreso\
sin envidias ni rencillas.\
¡Siglo, no te vi nacer,\
no te he cantado en pañales;\
salmodeo tus funerales\
porque te vi fallecer!\
Acaba de aparecer,\
quizá en glorias, tu segundo…\
¡Duerme en paz, siglo fecundo!\
Tu fosa cava la gloria;\
lápida te da la historia:\
¡y amplio panteón, el mundo!\
¡Siglo X X, te saludo\
sobre el cadáver del muerto!\
Llegas a la vida, incierto,\
en medio de invierno crudo.\
De honores vienes desnudo…\
mas nada importa, ¡adelante!\
En todo saldrás avante\
si creyeres, como creo,\
que sin fe, serás pigmeo;\
y con fe, serás gigante.",
                    path=u"/c", tags=u"RBT")

writer.add_document(title=u"Rosa Espino", content=u"El Escorial\
\
Resuena en el marmóreo pavimento\
Del medroso viajero la pisada, \
y repite la bóveda elevada\
El gemido tristísimo del viento.\
\
En la Historia se lanza el pensamiento,\
Vive la vida de la edad pasada,\
y se agita en el alma conturbada\
Supersticioso y vago sentimiento.\
\
Palpita aquí el recuerdo, que aquí en vano,\
Contra su propia hiel, buscó un abrigo,\
Esclavo de sí mismo, un soberano,\
\
Que la vida cruzó sin un amigo,\
Aguila que vivió como un gusano, \
Monarca que murió como un mendigo.\
\
Un Recuerdo \
\
Es un recuerdo dulce, pero triste,\
De mi temprana edad:\
Mi madre me llevaba de la mano\
Por la orilla del mar.\
\
Alzábanse las sombras de la tarde\
Como pardo cendal,\
y a gritar comenzaba en la cañada\
El huaco pertinaz.\
\
Cantaban los tropiales en el bosque\
Con dulce suavidad,\
Los penachos del mangle caballero\
Agitaba el terral.\
\
Y de la balsa entre los verdes musgos\
Acechaba el caimán,\
y bajaban los peces a sus nidos\
De concha y de coral.\
\
Zumbaban los insectos en el bosque\
En su continuo afán,\
y en medio a los filmores, dominando\
Los tumbos de la mar,\
\
Mas de improviso atravesando el viento\
Escuchose fugaz\
De las campanas de vecina aldea\
Tañido funeral.\
\
Detúvose mi madre, y en silencio\
La contemplé rezar,\
Y de llanto llenáronse sus ojos,\
Y se inmutó su faz.\
\
-¿Por qué lloras, mi madre? la decía\
Con dulce ingenuidad;\
Y ella me contestó dándome un beso:\
-Es preciso llorar,\
\
Que con lúgubre toque las campanas\
Anunciándome están\
Que un hombre, como todos, de esta vida\
Pasó a la eternidad.\
\
-¿Y tú te has de morir? la dije entonces,\
¿Tu amor me faltará?\
Y ella sin contestar, sólo lloraba,\
Y yo lloraba más.\
\
Sobre su seno recliné mi rostro,\
Y ella con dulce afán\
Enjugando mis lágrimas, decía.:\
'¡Vamos, ya está, ya está!'\
\
Pocos años después, perdí a mi madre:\
No ceso de llorar,\
Y en sueños la contemplo cada día;\
Del cielo viene ya.\
\
Llega, se acerca hasta tocar mi frente\
Su rostro celestial,\
Y con acento tierno me repite:\
'¡Vamos, ya está, ya está!'\
\
El arroyo y la flor\
\
En la margen de una fuente\
Mansa, pura y cristalina,\
Regada por la corriente,\
Mecíase blandamente\
Una rosa purpurina.\
\
Del arroyo enamorada\
Daba la rosa su aroma,\
Y él, cruzando la enramada,\
Más dulce canta á su amada\
Que el gemir de una paloma.\
\
-'¡Tan solo tu amor me alienta,'\
Dijo al arroyo la flor.\
-'¿Y si ruge la tormenta?'\
-'Por ti nada me amedrenta,\
Y moriré por tu amor.'\
\
Cerró la noche sombría,\
Alzóse la tempestad \
Y entre las selvas rugía,\
Y el relámpago surgía\
En la densa oscuridad.\
\
Iba el arroyo creciendo,\
Turbio, fiero, amenazante,\
Las riberas invadiendo,\
Y á la tierra estremeciendo\
Con impulso de gigante. \
\
-'Tuya soy,' dice la rosa\
Al sentirse arrebatada,\
'Que es la ilusión más hermosa\
'Hallar la muerte dichosa\
'Por su amor despedazada.'\
\
Lanzó el torrente un rugido,\
y con inmensa ternura,\
Sin dar la flor ni un gemido,\
Halló de amores un nido\
En su misma sepultura. \
\
Si sopla adversa la suerte,\
¡Angel de mis ilusiones!\
Antes que llegue a perderte\
Cubra nuestro amor la muerte\
Entre sus negros crespones.\
\
Gloria\
\
-¿Adónde vas, hijo mio?\
-Al combate, a la victoria,\
Suena el clarín de la gloria,\
y piensa escribir mi brío\
Mi nombre ilustre en la Historia.\
\
-Es grande tu atrevimiento.\
-Padre, el mundo lo proclama;\
Cuando la patria nos llama,\
Con tan noble sentimiento,\
¿Qué corazón no se inflama?\
\
-¿Y qué buceas, delirante,\
Tras de la ruda batalla?\
-Ver mi bandera triunfante\
Entre el polvo que levante\
El bote de la metralla.\
\
-¡Ay! hijo, temo perderte;\
Me agita la pena fiera.\
-Si me es adversa la suerte,\
Cubran mi lecho de muerte\
Los pliegues de mi bandera.\
\
-¿De dónde vienes, hijo mío?\
-Padre, torno de la guerra.\
-¿Y fue tu destino impío?\
-Libre está ya nuestra tierra,\
Y libre por nuestro brío.\
\
-¿Y alcanzaste, hijo querido? ...\
-No preguntéis, por favor:\
Después de quedar herido\
Alcancé, padre, el olvido\
Y un recuerdo de dolor.\
\
-¿Y esperas, en tu dolencia? .\
-Sólo espero, por mi mal,\
Tras vergonzosa indigencia\
La cama de un hospital\
Para acabar mi existencia.\
\
-¿Y tus sueños? -Se han borrado\
¡Ay padre! ele mi memoria.\
-Locura es, hijo, la gloria,\
Que nunca del hombre honrado\
Guarda el recuerdo la Historia.\
 \
Duda y fe\
\
Negro estaba y sombrío el firmamento,\
Y tú me lo mostrabas;\
«Así tengo, dijiste, el pensamiento,»\
Y era, porque dudabas.\
\
De bella tarde en apacible calma\
Otra vez me decías:\
«Como ese cielo azul tengo yo el alma,»)\
Y era, porque creías.\
\
Luz es la fe, mi bien; sombra la duda;\
Con mi amoroso anhelo\
Y o le daré, si tu pasión me ayuda,\
Luz a tu cielo .\
\
El chicano\
\
Sobre los robustos lomos\
De un poderoso alazán,\
Que apenas deja la huella\
De su ligero trotar,\
Apuntando la mañana\
y camino a Tehuacán,\
Va Márgaro Peñadura,\
El chinaco más cabal.\
Ancho bordado sombrero\
Cubre su morena faz,\
y matiza su sarape\
La bandera nacional.\
En el cinto la pistola,\
El mosquete en el carcax,\
Bajo la pierna la espada,\
y en la bota su puñal.\
Busca inquieto entre la bruma\
y descubre a poco más\
Pequeña casa escondida\
En las sombras de un palmar,\
y dejando su camino\
y aguijando su animal,\
En un instante el jinete\
Cerca de la casa está.\
Y como si ya impaciente\
Se cansara de aguardar,\
Da golpes en la ventana,\
Y muestra luego su faz\
Una morena, que puede\
Pasar por una beldad,\
De esas que hemos visto todos\
Y nos han hecho soñar, .\
Y que siempre se recuerdan\
Como visión ideal.\
-¡Alabo, Don Margarito!\
¿Tan temprano por acá?\
_¿Te pesa, luz de mis ojos?\
Pues ya me voy a marchar.\
-No me pesa, Dios me libre;\
Pero dicen que aquí están\
Los franceses. No hay cuidado,\
Porque vengo a explorar.\
Tuvimos ayer campaña\
y hoy quiere mi capitán\
Volver a darle a los zuavos;\
Conque adiós. ¿Por qué se va?\
Estese siquiera un rato,\
Bájese a desayunar,\
Ha tres días que no viene....\
-Linda, otra vez será,\
Que llegan los compañeros\
Y voy para Tehuacán.\
Inclinóse la doncella,\
Un beso se oyó sonar;\
Alzó el chinaco el embozo,\
Cobró su empaque marcial\
Y se perdió entre la bruma\
Galopando en su alazán.\
\
Hoy\
\
No de lo porvenir entra la densa\
Sombra, con que se vela impenetrable,\
Te finjas con empeño infatigable\
La pena atroz ó la desgracia inmensa.\
\
No del pasado la terrible ofensa\
Llames a nueva vida; que indomable,\
Al recuerdo de tiempo miserable\
Oponga el corazón tenaz defensa.\
\
Pasó el ayer, llevose su quebranto;\
El mañana no llega todavía:\
¿Por qué lo que no existe causa espanto?\
\
No oprima al corazón la fantasía\
Que en esta vida de dolor y llanto\
Le basta su pesar a cada día.\
 \
A dos golondrinas\
\
¿A dónde vais, peregrinas,\
Ligeras cruzando y solas,\
Inocentes golondrinas,\
Del mar las tendidas olas?\
\
Si acaso con vuelo incierto\
Buscáis un puerto seguro,\
Yo os daré tranquilo puerto\
Bajo un sol ardiente y puro.\
\
Y allá, si queréis creerme,\
Entre mirtos y azahares,\
Veréis mi patria que duerme\
Al ronco son de dos mares.\
\
Tended allá vuestro vuelo\
Y hallareis plácido encanto\
Donde es una fiesta el cielo,\
Donde es el idioma un canto.\
\
Sobre cascadas de flores,\
Perlas regando la aurora,\
Los alados trovadores\
La anuncian cuando colora.\
\
En los lagos de cristal\
Que blanda toca la brisa,\
Plácida luz matinal\
Ensaya dulce sonrisa.\
\
Allí en la oscura montaña\
Se mece gigante encino,\
Como flexible espadaña\
En el lago cristalino.\
\
Y flores, y aves y fuentes\
Y mares, con grato son,\
Alzando están reverentes\
Sus himnos de adoración.\
\
Y se mezclan confundidos\
En un inmenso concierto\
Murmullos, cantos, rugidos,\
Como la voz del desierto.\
\
Seguid con alegre vuelo\
Hasta esa patria viajeras; \
Veréis retratar el cielo\
Los lagos de las praderas\
\
Veréis mares azulados\
Como el puro firmamento,\
Y de perlas coronados\
Al soplo manso del viento.\
\
Veréis cruzar hechiceras\
Garzas blancas y rosadas,\
Las lucientes cordilleras,\
De las ondas encrespadas.\
\
Y en la ribera frondosa\
Del mar la brillante espuma,\
Regar la playa arenosa\
Del país de Moctezuma.\
\
Mecerse los cocoteros,\
Dando sombra regalada,\
y entre los verdes mangueros\
Pasar el aura callada.\
\
Y en desatado torrente\
La luz intensa bañar\
El bosque, el prado, la fuente,\
El lago, la sierra, el mar.\
\
Llegar con pausado vuelo\
Las noches tibias y bellas,\
En su, fantástico velo\
Tejiendo polvo de estrellas\
\
Y en el húmedo follaje\
Mil insectos luminosos\
Que brillan en el ramaje\
Ó se arrastran afanosos.\
\
Y surgir entre la sombra,\
Melancólicos, suaves,\
Con tal ternura que asombra,\
Los cantos de extrañas aves.\
\
Y sigue en grato concierto,\
De las aves al arrullo,\
Lejano, manso e incierto\
De las fuentes el murmullo.\
\
Y más que rumor, gemido .\
En los árboles gigantes,\
Fingir el viento perdido\
Entre las hojas flotantes.\
\
Seguid, pobres golondrinas,\
Buscando tan dulce cielo,\
Que encontrareis, peregrinas,\
A vuestras penas consuelo.\
\
Seguid, y con rumbo cierto\
Cruzad la cerrada bruma;\
Que os dará seguro puerto\
La patria de Moctezuma;\
\
Y dejando el mar bravío\
Alzad himnos de alabanza,\
Llevando hasta el suelo mío\
Mi recuerdo y mi esperanza .\
\
La veleta\
\
Erguida sobre el alto campanario,\
Y despreciando al rayo resonante,\
Sensible la veleta, sigue amante\
Del caprichoso viento, el rumbo vario.\
\
Ya la agita un impulso, ya el contrario\
La detiene ligera y vacilante,\
Y al rudo soplo de huracán pujante\
Responde con gemido funerario.\
\
Como ella, de la vida en el camino,\
Hallamos almas que con santo anhelo\
Siguiendo van nuestro fatal destino.\
\
Dulces fuentes de amor y de consuelo,\
Retratando en su fondo cristalino\
La tormenta ó la luz de nuestro cielo.\
\
La azucena y el huracán.\
\
-«Yo soy la azucena\
De lánguido talle,\
Que mece en el valle\
El aura sutil.\
La brisa que anuncia\
La fresca mañana,\
Me dice «Sultana,\
Hermosa y gentil.»\
\
«Yo guardo en mi seno\
Las perlas que llora .\
La cándida aurora\
Huyendo del sol;\
Y doy en mi cáliz\
Dulcísimo aroma\
Que el céfiro toma\
Cruzando veloz.»\
\
-«Yo llevo en mis alas\
Angustia y espanto,\
Y sombras y llanto,\
Terrible huracán.\
Yo traigo la muerte\
Y voy, a mi paso,\
Sembrando al acaso\
Miseria y afán.\
\
'Destruyo soberbio\
La pobre cabaña;\
La erguida montaña\
Temió mi poder.\
Del lago me irritan\
Las blancas espumas,\
Y en pálidas brumas\
Se miran perder.\
\
'Las olas pujantes\
Del mar proceloso\
Levanta orgulloso\
Mi altivo rigor.\
Y rujo en lo$ bosques,\
Y tiembla la tierra,\
Y el hombre se aterra\
Y siente el horror.'\
\
-'Te adoro por fuerte,\
Terrible te amo,\
\
Sombrío te llamo,\
Acércate a mí.\
Me arrastra a adorarte\
Tu inmensa grandeza,\
Tu noble fiereza\
Me neva hasta ti.'\
\
-'Yo adoro, azucena,\
Tu tierna hermosura,\
Tu blanda ternura,\
Tu dulce candor;\
Y forma mi encanto\
La mágica esencia,\
Que da á tu inocencia\
Tu místico amor.''\
\
-'Pues llega, que espero\
Tu plácido halago.'\
-'Yo llevo el estrago,\
Amarme, es morir.'\
-'Tu amor es mi vida, \
Tu suerte mi suerte.'\
-'Mi amor es la muerte,\
Mi sino sufrir.'\
\
-'Que pueda yo ufana\
Mirar a mi amante,\
Y muera al instante\
Gozando en mi amor.'\
\
-'A ti me encadenan\
Tiemí si mos lazos...\
Que muera en mis brazos\
La cándida flor.'\
\
*\
Rugió entonces la tormenta,\
La tierra gimió de duelo,\
Y triste v amarillenta\
Perdióse la luz del cielo.\
\
Y tras de la noche oscura\
En la tranquila mañana,\
Seco se alzó en la llanura\
El tallo de la sultana.\
\
Tú y yo\
\
Lanza el Orión su luz resplandeciente\
Y las luces de Sirio se difunden,\
Y al tocar a la tierra dulcemente\
Pálidas se confunden.\
\
Dos flores ricas de hermosura y galas\
Dan sus perfumes, que en constante anhelo\
De blanda brisa en las flotantes alas\
Suben juntos al cielo.\
\
Dos arroyos, cruzando bullidores,\
Bajan de la montaña a la llanura,\
Y en la tupida bóveda de flores\
Mezclan su linfa pura,\
\
Perfumes, luz y arroyos cristalinos, .\
Nuestras dos almas para siempre unidas,\
En uno convirtiendo sus destinos,\
Vivirán confundidas.\
\
El rocío y el llanto\
\
El llanto que la aurora derramaba\
Fecundó la pradera,\
Y mientras más lloraba,\
Más la hermosura de las flores era.\
\
*\
¡Ay, pobre humanidad! es tu destino\
Llorar en tu quebranto:\
La flor en tu camino\
Ha de brotar regada por el llanto .\
\
Las Plegarias\
El niño\
\
¡Oh virgen María,\
Botón de clave!\
Mi madre me dice\
Que te ame con fe,\
Pues cuenta que eres\
Mi madre también;\
Que el rezo del niño\
Te causa placer;\
Que cuando en las noches\
Dormidito esté, .\
Si soy un buen hijo,\
Me vendrá a ver.\
Mi madre no engaña,\
Lo sabe muy bien,\
Por eso te espero\
Y al fin te veré, .\
¡Oh virgen María,\
Botón de clave!\
\
La joven\
\
¡Madre tierna, virgen santa!\
Con el alma conmovida,\
Cruzando voy en la vida\
Por un mundo que me espanta;\
Donde quiera se levanta\
La sombra de la maldad,\
Y en la densa oscuridad\
En que el porvenir se abisma,\
Temblando voy por mí misma\
Con tan fiera tempestad.\
\
¡Virgen pura! ¡Madre amante!\
Dame tu amparo divino,\
Que es peligroso el camino\
Y voy sola y vacilante.\
La luz de tu amor constante\
Alumbre la senda mía;\
Sé tú mi antorcha, mi guía,\
Y en este mar que amedrenta\
Sálvame de la tormenta,\
¡Oh Madre! ¡Virgen María!\
\
El hombre\
[Credo.]\
Creo en ti, Señor y Dios, no porque admiro\
Al ronco mar que aprisionado ruge,\
Ó al huracán que con terrible empuje\
Lleva la tempestad en raudo giro.\
\
Creo en ti, Señor y Dios, no porque miro\
Que en los cielos la aurora se dibuje,\
Ó enhiesto el tallo de las flores cruje\
Del aura matinal con el suspiro.\
\
Creo en ti, porque mi espíritu agitado\
Nunca la duda entre sus penas lleva,\
Y tu ser en su ser siente grabado,\
\
Y cuando a ti su pensamiento eleva,\
Del infinito en pos, arrebatado,\
Sus alas tiende y hasta ti me eleva.\
\
El anciano\
\
Larga ha sido la lucha. En este mundo\
Pálida sombra soy de lo que fui;\
¡Sácame de este piélago profundo!\
¡Señor, llámame a ti!\
\
Tristes mis horas son, negros mis días,\
Me arrastro en la vejez y en el dolor:\
¿Por qué de tu presencia me desvías?\
¡Llámame a ti, Señor!\
\
Envuelven ya las nubes del olvido\
Los recuerdos del tiempo en que viví;\
Viajero por la noche sorprendido,\
¡Señor, llámame a ti!\
\
De la amarga vejez en el remanso,\
Sin más luz en la tierra que tu amor,\
Tranquilo espero mi final descanso,\
¡Llámame a ti, Señor!\
\
El alba\
\
(En la sierra)\
\
Ya amanece: el horizonte\
Dibuja pálida faja,\
Orla del manto nocturno,\
Diadema de la alborada.\
En Oriente las estrellas\
Palidecen y se apagan,\
y sopla el viento más frío\
Anunciando la mañana.\
Entre la sombra que cubre\
Las espesas enramadas,\
Trinan los madrugadores,\
y sus aromas exhalan\
El oyamel y el ocote,\
Los cedros y las lianas.\
En los ranchos silenciosos\
Alegres los gallos cantan,\
Que ya ilumina el paisaje\
Incierta la luz del alba.\
Ya se oyen desde los prados\
El tañir de la campana,\
y el balido de la oveja\
y el mugido de las vacas.\
Cruzan de tordos parleros\
Negras revueltas parvadas,\
Que descienden de los bosques\
Sobre la fresca labranza.\
Divísanse los senderos\
Que suben por la montaña,\
Relucientes y sembrados\
De pura y brillante escarcha.\
De azul se tiñen los cielos,\
Las nubecillas de grana,\
Ostentando la llanura\
Sus alfombras de esmeralda.\
Los vapores de la noche\
Huyen como nube blanca,\
Hasta posarse en las crestas\
Ó morir entre las ramas.\
Despiélen los jacalitos\
Columnas de humo azuladas,\
y el canto de los rancheros\
Que al trabajo se preparan,\
Se mezcla confusamente\
Con ese rumor que se alza\
Cuando después de la aurora\
Vivifico el sol derrama\
Sobre el mundo que despierta\
Su luz esplendente y clara.\
\
El mediodía\
\
(En la costa)\
\
Radiante el sol Meridiano\
Lanza torrentes de fuego,\
y sus ondas luminosas\
Aduermen al manso viento.\
De aquella calma profunda\
Sólo interrumpe el silencio\
El ronco mar que sus aguas\
Azota estruendoso y fiero,\
De los apartados morros\
Contra los peñascos negros,\
Que ya se cubren de espuma\
y ya aparecen enhiestos.\
Ni un barco sobre las olas,\
Ni una nube sobre el cielo:\
Parece el cielo un abismo,\
Parece el mar un desierto.\
Lánguidas cuelgan las hojas\
Del altivo cocotero,\
Lánguidas flotan las palmas\
Del cayaco gigantesco;\
Fuego circula en el aire\
y el azul del firmamento,\
Como de flotantes llamas\
Envuelve rojizo velo;\
Sobre las ondas del río\
Se inclina el mangle soberbio,\
y buscando grata sombra\
Calla el zanate parlero.\
Al abrigo de la yerba\
Los esmaltados insectos\
Enmudecen, respetando\
El silencioso misterio.\
Duerme la verdosa iguana.\
Sobre un tronco de árbol seco,\
Duerme el caimán perezoso\
A la orilla del estero.\
Los loros y guacamayas\
Se agrupan bajo los cedros,\
Inmóviles, mientras llega\
El terral húmedo y fresco.\
Huye el guaco a la cañada,\
y el tigre con paso incierto\
Sigue el rumor del arroyo\
Que sale a buscar sediento.\
Terrible es aquella calma,\
Pavoroso aquel silencio\
Que sólo el mar interrumpe\
Con su monótono estruendo.\
\
La tarde\
\
(En el Valle de México)\
\
Está moribundo el día\
y el sol poniente colora\
Las nieves del Ixtacihuatl\
Con los tintes de la rosa.\
En un cielo de turquesa\
Ligeros crespones flotan,\
Nubes de púrpura y grana\
Que oro mienten con sus orlas.\
Sobre los tendidos lagos\
Las brisas murmuradoras\
Van recogiendo el perfume\
De las frescas amapolas,\
Del mirto y del zempazuchil,\
De las clavellinas rojas,\
Del cacomite atigrado,\
De la azucena olorosa.\
En grato vaivén se agitan\
Los tulares, si les toca\
El aliento de la tarde\
Que va impregnado de aromas.\
Las flores en las chinampas\
Inclinan ya sus corolas,\
y el mirasol languidece\
De la tarde con la sombra.\
Forman alegre concierto\
Los gorriones, en las hojas\
De fresnos y capulines,\
En cuyas ramas se posan.\
El vuelo tienden las garzas\
Buscando la selva umbrosa,\
y al abrigo de las trojes\
Retíranse las palomas.\
Se oye el rumor a lo lejos\
De las reses mugidoras\
Que llegan a los establos\
Ó a los potreros retornan.\
Por el lago trasparente\
Cruzan pesadas canoas\
Ó chalupas que ligeras\
Mueven apenas las olas.\
Sembrado se mira el valle\
De haciendas, pueblos y chozas,\
y en medio de ese conjunto\
México, que se corona\
Con cien torres que reflejan\
Esa luz que seductora\
Las nieves del Ixtacithuatl\
Tiñe de carmín y rosa.\
\
La noche\
\
(En la montaña)\
\
La noche envuelve a la tierra\
Con sus negros pabellones,\
y en el espacio infinito\
Brillan miríadas de soles.\
Espléndida se levanta\
La luna en el horizonte,\
y vaporosos celajes\
Sus blancas luces recogen.\
No es la imagen de la muerte\
Dentro las selvas la noche;\
Que se alzan por todas partes\
Dulces y extraños rumores\
El eco de los torrentes\
Viene de lejano bosque,\
Mientras al brillar la luna\
Cantan, sin saberse en dónde,\
Pájaros desconocidos,\
Desconocidas canciones.\
Se oye crujir la maleza\
y luego el pesado roce\
De los tigres que en la loma\
Cruzan pujando feroces.\
Aúllan en las cañadas\
Los lobos y los coyotes,\
y brillan entre la yerba\
Mil insectos zumbadores,\
Que como estrellas perdidas,\
Fosforescentes, veloces, '\
Tan pronto surcan la tierra\
Como en las hojas se esconden,\
De los árboles soberbios\
En que cantan sus amores\
Los jilgueros en las tardes\
y en la aurora los cenzontles.\
Una ráfaga de viento \
Llega rápida y se oye \
Crujir el añoso tronco,\
y sordo luego, recorre\
Aquel rumor misterioso\
La virgen selva, y entonces\
Se interrumpen de repente\
Todos los otros rumores,\
Porque el ángel de las sombras\
Cruzando va por el bosque.\
\
La noche de la muerte\
\
¡Cómo está oscura la noche!\
¡Qué negro está el firmamento!\
Ni una antorcha sobre el mundo,\
Ni en las sombras un lucero.\
Ni un leve rumor que turbe\
Tan espantoso silencio,\
Ni un vientecillo que mueva\
Las flores del cementerio.\
Inmensas y tristes aves\
Cruzan por el cielo negro,\
y aunque no logro mirarlas,\
Puedo decir que las veo.\
¡Qué solo estoy! tengo frío;\
¡Qué solo estoy! tengo miedo;\
Estoy muy triste, muy triste,\
Muy solo porque estoy muerto,\
Ayer estaba en el mundo,\
Ayer el vital aliento\
Animaba mi existencia\
Dando vigor a mi cuerpo.\
Ahora, todos me abandonan...\
¿Quién se acuerda de los muertos?\
¡Madre! porque madre tuve!\
¡Madre! ¿Por qué estás tan lejos?\
Diera yo toda mi vida.\
Porque me dieras un beso.\
¡Mi vida? la tengo acaso?\
Sólo me queda el recuerdo,\
y es el recuerdo muy firme\
y el existir pasajero. \
Siento cruzar a mi lado\
Las almas de los que fueron,\
Que ni se atreven a hablarme\
Ni yo a llamarlas me atrevo.\
¡Cómo está oscura la noche!...\
¡Qué negro está el firmamento!...\
¡Estoy tan solo, tan solo!...\
¡Qué triste es el cementerio!\
Quisiera llorar un poco,\
Quisiera... pero no puedo.\
¡Pobre de aquel que se muere!\
¿Qué cosa pueden los muertos?\
Cómo se alza mi cariño\
Por los que en el mundo dejo:\
Ignoro si aborrecía;\
Si aborrecí no me acuerdo.\
Una mujer fue mi encanto,\
Mi luz, mi vida, mi ensueño ... \
Ella también me abandona...\
¿Quién se acuerda de los muertos?\
¡Qué soledad! ¡Cuánta sombra!\
Cuánto frío, yo me hielo!\
¿A dónde torno mis ojos\
¿A dónde guío mi empeño?\
Mi Dios, ¿por qué me abandonas?\
¿Por qué me dejas, Dios bueno?\
¿Es cierto que tú eres Dios\
De vivos y no de muertos? \
La antorcha de la esperanza\
Extinguió su santo fuego;\
Estoy solo en mi sepulcro,\
Estoy solo y tengo miedo.\
Óyeme ¡oh Dios! estoy triste,\
Muy triste en el cementerio.\
¡Tú que eres luz, dame vida;\
Tú que eres vida, consuelo!...\
¡Ah! ¿qué miro? se colora\
Espléndido el firmamento;\
Vaga armonía se escucha\
Entre las luces del cielo;\
Cruzan mirando a la tierra\
Los espíritus, envueltos\
En luminosos ropajes,\
Lanzando puros destellos.\
¡Cuánta luz! ¡cuánta ventura!\
¡Qué armonía! ¡Qué concentos!\
Ni estoy triste, ni estoy solo,\
Ni está oscuro el cementerio.\
¿y tú quién eres? ¿Qué buscas,\
Angel que tocas mi pecho?\
¿Por qué me miras tan dulce,\
Por qué tan dulce te veo?\
¡Eres la Fe! te conozco;\
Tu mano me muestra el cielo: \
Hay un camino de estrellas\
y después .... el sol eterno.\
¿Te he de seguir? Ya te sigo;\
Estoy libre, ya lo siento:\
Entre torrentes de vida\
Flota mi espíritu inquieto;\
Tierno arcángel, ya te sigo, .\
Levanta, levanta el vuelo,\
Que al buscar el infinito\
Entre las ondas de fuego,\
Himnos alzaré al que justo\
No se olvida de los muertos.\
\
Lejos de ti\
\
Lejos de ti, Señora, el pensamiento\
Tu imagen pura encuentra por doquiera,\
Entre la luz que ardiente reverbera\
En la nube que cruza el firmamento.\
\
Oigo tu voz cuando suspira el viento\
Acariciando el agua en la ribera,\
y el aroma que se alza en la pradera\
Es el ámbar, señora, de tu aliento.\
\
y si te miro en la graciosa palma,\
Si estás en el aroma de las flores,\
Si de la noche en la apacible calma\
\
Me hablan de tí no más los ruiseñores,\
¿Me puedes olvidar, alma de mi alma?\
¿Puedo olvidarte amor de mis amores?\
\
Alborada\
\
Trinando están los jilgueros,\
El aura soplando ufana,\
y pálidos y ligeros\
Huyendo van los luceros\
De la luz de la mañana.\
\
Asoman entre las brumas\
Rosas, lirios y amapolas,\
y como flotantes plumas\
Del arroyo las espumas\
Se posan en sus corolas.\
\
En la selva que despierta \
Se oye místico, suave\
Vago rumor que concierta\
Con esa armonía incierta\
Que lanza al cantar el ave.\
\
Va la fuente murmurando\
Entre la erguida espadaña,\
y el pardo cielo cruzando\
Las nieblas que van buscando\
La cresta de la montaña.\
\
Dejan el caliente nido\
Las bandas de los tropiales,\
y desde el bosque escondido\
Llegan en vuelo tendido\
A los dorados trigales.\
\
Sobre la pradera amena\
Todo es quietud, todo calma,\
y de luz y encanto llena ;\
La atmósfera está serena\
Como está tranquila el alma.\
\
¡Pienso con tanta dulzura\
En ti, vida de mi vida!\
¡Es tan grande mi ventura!\
¡Tan profunda mi ternura! '\
¡Mi fe tan correspondida!\
\
Toda pasión enmudece\
Ante esa inmensa pasión;\
Toda imagen desparece\
y toda luz palidece\
A la luz de esa ilusión.\
\
Te amo, pues amor le llaman\
Al dulce inefable anhelo\
\
Que nuestras almas derraman,\
Como los ángeles aman,\
Como ha de amarse en el cielo.\
\
Pienso en ti: quizá dichosa\
Del sueño entre las visiones,\
Oiga tu alma generosa\
Esta cántiga amorosa\
Que entonan mis ilusiones.\
\
y del cuerpo desprendida\
Por el sueño, aquí tu alma\
Dando esté vida a mi vida, '\
y a mi pasión encendida\
La fe que me da la calma.\
\
¡Aquí está! ¡sí! yo la siento;\
Por eso ven mis amores\
Más bellos el firmamento \
La luz, las nubes', el viento,\
La selva; el prado y las flores.\
\
Porque en tu amor, vida mía,\
Toda mi ilusión se encierra,\
Y sin él, siempre hallaría \
La bóveda azul, vacía,\
Desierta y sola la tierra.\
\
Amor\
\
En una fresca mañana\
y por la vega florida,\
Alegre y entretenida\
Canta una linda serrana:\
\
-'Tengo un amor tan callado,\
Tan puro, tan inocente,\
Como la mansa corriente\
Que se desliza en el prado.\
\
Jamás de los sinsabores\
Llegó la triste amargura\
A turbar su linfa pura\
Sobre su lecho de flores.\
\
y con tan amante prisa\
Corren sus ondas suaves,\
Que ni las oyen las aves,\
Ni las alcanza la brisa .\
\
No enluta noche importuna\
Sus encantos virginales,\
Que entre sus limpios cristales\
Quiebra sus rayos la luna.\
\
Amo con tan dulce calma,\
Que no sé por darle nombre, .\
Si soy el alma de un hombre\
O él es alma de mi alma.\
\
Con ese amor se engalana\
Orgulloso el pecho mío,\
Como gota de rocío\
Con el sol de la mañana.\
\
y ni la nube del celo\
Turba la luz de mi vida,\
Ni cruza vaga y perdida\
La sospecha en nuestro cielo.\
\
De la tarde misteriosa\
A los últimos fulgores,\
Le cuento yo mis amores\
A la encina y a la rosa.\
\
y voy alegre y parlera,\
Como loca en mi contento,\
y digo mi pensamiento\
Al bosque y a la pradera;\
\
Con el aura que suspira,\
Con la fuente que murmura,\
Con el ave que en la altura\
En círculo inmenso gira,\
\
Con la leda mariposa,\
Con el celaje flotante,\
Con todo, mando a mi amante\
Una memoria dichosa.\
\
y me habla del, el aroma\
Que desde los valles sube,\
y me hablan la blanca nube\
y el gemir de la paloma.\
\
y me habla en el Occidente\
El rico manto de gualda\
y la alfombra de esmeralda\
Por donde cruza el torrente.\
\
Dice su nombre a mi oído\
La brisa con dulce anhelo,\
y yo por causarla celo\
Repito el nombre querido .\
\
Entonces de gozo llena,\
Sin que tal encanto cese,\
Porque la brisa le bese .\
Grabo ese nombre en la arena.\
\
y cuando de allí me alejo,\
Vuelvo a mirar con ternura\
Que al irme se me figura\
Que hago mal porque le dejo.\
\
Paso noche de contento\
Contemplando las estrellas\
Pues miro escrita con ellas\
Su cifra en el firmamento.\
\
y en inocente deseo\
Tanto mi ilusión se exalta,\
Que si una estrella me falta\
Me parece que la veo.\
\
y así pasa mi existencia\
Tan dulce, tan sosegada,\
Que vive el alma embriagada\
De amor con tan pura esencia \
\
y este amor es tan callado,\
Tan tierno y tan inocente\
Como la limpia corriente\
Que se desliza en el prado.'\
 \
Al viento\
\
Cuando era niño, con pavor te oía\
En las puertas gemir de mi aposento;\
Doloroso, tristísimo lamento\
Dé misteriosos seres te creía.\
\
Cuando era joven, tu rumor decía\
Frases que adivinó mi pensamiento;\
y cruzando después el campamento,\
Patria, tu ronca voz me repetía.\
\
Hoy te siento azotando, en las oscuras\
Noches, de mi prisión las fuertes rejas;\
Pero hánme dicho ya mis desventuras\
\
Que eres viento, no más, cuando te quejas,\
Eres viento si ruges ó murmuras, .\
Viento si llegas, viento si te alejas.\
\
Prisión de Santiago Tlaltelolco.\
Julio de 1884.\
\
El amor del chinaco\
\
Encarnación Torreblanca,\
Valiente y afortunado,\
Espuma y flor de ginetes\
y espejo de los chinacos,\
Que planta dos banderillas\
En menos que canta un gallo,\
y es en Puruándiro antojo\
De las muchachas del barrio,\
y nadie con más destreza\
Despide y amarra un lazo\
y hace como rehilete\
Al más soberbio caballo,\
y se alza la lorenzana\
y grita 'que salga un guapo,'\
Sin haber quien le responda,\
Porque saben que es 'planchado,'\
Está triste y pensativo\
y ni se asoma al fandango\
A bailar como solía,\
Ni sale del pueblo un paso,\
Ni va a lucir su destreza\
Sobre su tordo rodado\
Que relincha tristemente\
Prisionero en el establo,\
Extrañando cariñoso\
De su dueño los halagos.\
¿Qué ha tenido Torreblanca?\
Que el amor le ha derrotado,·\
Y no alcanza en sus congojas\
A calmar tan fiero estrago.\
Causa su pena doliente\
Flor del vecino cercado,\
Más pura que una azucena\
y más fragante que un nardo.\
Con dos ojos como soles,\
Trigueña, cutis de raso,\
Tan garbosa, tan flexible,\
Que más que cuerpo es el tallo\
En que a la roja amapola\
Columpia céfiro blando;\
Más negro tiene el cabello\
Que tiene la noche el manto,\
y si en los hombros lo suelta\
El sol sale por besarlo;\
La camisa como nieve, \
y el zagalejo encarnado,\
y sobre el mórbido pecho\
El rebozo con tal garbo,\
Que si por la calle cruza\
Llueven flores a su paso,\
y dice hasta el más bendito:\
'¡Bien, haya lo bien logrado!\
Pena el mancebo por ella,\
y se murmura en el barrio\
Que ella al encontrarle dijo:\
'¡Adiós mi cielo estrellado!'\
Pero el padre de la chica,\
Ranchero, rico y anciano,\
No quiere que Torreblanca\
Aprisione en dulce lazo\
A la gallarda doncella,\
Hasta que tenga probado\
'Que ni precia de valiente,\
Ni es en amores un rayo,\
Ni le gustan los amigos\
Ni tiene horror al trabajo,\
y que hasta las esperanzas\
Perdió ya de ser chinaco.'\
y al saber las condiciones .\
Exclama el pobre muchacho:\
'Tan picuda me la ponen \
Que de seguro no alcanzo;\
Pues pide más imposibles\
Que una vieja en el rosario.'\
\
El sol y el átomo\
\
Entre el raudo torbellino\
Un átomo arrebatado \
Vuela ignoto y peregrino\
Por el incierto camino\
Del huracán desatado;\
\
y al sentir la inmensidad,\
Lo infinito, en su presencia,\
Exclama con humildad:\
-'¿Qué es ante la majestad\
'Del sol, mi pobre existencia?\
\
'Desconocido y errante\
'Me alzan en incierto giro\
'Así el huracán gigante\
'Como el aliento abrasante\
'De apasionado suspiro.\
\
'¿De qué procedo? ¿qué soy?\
'Cómo existo, y para qué?\
'¿De dónde vengo ¿dónde voy?\
'¿Mañana seré cual hoy,\
'O mañana no seré?\
\
'¡Sol cuya luz esplendente\
'Alumbra lejanos mundos, \
'Que giras eternamente\
'Como antorcha indeficiente\
'En los abismos profundos!\
\
'Si en tu rápida carrera\
'llegas a mirar aquí,\
'Sobre esta perdida esfera\
'Donde tu luz reverbera,\
'Dime, ¿qué soy junto a ti?'\
\
-'También un átomo soy,'\
Dijo el sol, 'vuelo perdido ·\
'Sin saber adónde voy;\
'No tengo mañana ni hoy,\
'Ni sé de dónde he venido.\
\
'Si eres nada junto a mí\
'y envidias mis resplandores,\
'Átomo, sube hasta aquí,\
'Do me ven como yo a ti,\
'Átomo, mundos mayores.\
\
'No preguntes tu destino,\
'Yo soy átomo también,\
'Que Ignorante y peregrino\
'Cruzando voy el camino\
'Donde mil soles se ven.\
\
'y si hasta allá a preguntar\
'Vas en tu constante anhelo,\
'Alcanzarás a mirar\
'Átomos, siempre al llegar,\
'Que átomos pueblan el cielo.\
\
'Y en la infinita carrera\
'Hallarás siempre lo mismo,\
'y de una esfera a otra esfera,\
'Siempre con la duda fiera\
'Irás de abismo en abismo.\
\
'No acates mi majestad,\
'Iguales somos los dos;\
'Que el ser en la inmensidad\
'Es siempre la realidad\
'Del pensamiento de Dios.\
\
Sueño y realidad\
\
Soñé que te miraba,\
Y después que entre nubes te perdía\
Y que tu alma conmigo se quedaba\
Y que contigo se iba el alma mía .\
\
Estando ya despierto, \
Me dijo mi razón enternecida\
Que era mi sueño cierto,\
Porque era tu alma el alma de mi vida.\
\
Mi ventura\
\
Con tan apacible calma\
Las horas van de mi vida,\
Que apenas se agita el alma\
Como la gigante palma\
Por blanda brisa mecida.\
\
Llega la luz de la aurora,\
y al despertar de mi sueño\
Tal mi vida se colora,\
Que en mi ilusión seductora\
Estar despierta es mi empeño.\
\
Ni una sombra que acongoje\
La dicha de mi conciencia, \
Ni zozobra que me enoje,\
Ni una lágrima que moje\
Las flores de mi existencia.\
\
Ni un recuerdo doloroso\
Luchando en el pensamiento,\
Ni un porvenir proceloso;\
Un lago puro y hermoso\
Que riza plácido el viento.\
\
y cuando allá en Occidente\
En flotantes cortinajes\
El sol esconde la frente\
y se tiñen dulcemente\
Con su arrebol los celajes,\
\
Aspirando de las flores\
Blandas esencias suaves,\
Me hablan de dicha y amores\
Los arroyos bullidores,\
La luz, el cielo y las aves.\
\
Tiende la noche su manto,\
y yo con plácido empeño\
Busco del sueño el encanto,\
No por olvidar quebranto\
Sino por gozar del sueño.\
\
¡Qué dulce soñar! dichosa\
Despliega todas sus galas\
El alma feliz, y ansiosa\
En la inmensidad hermosa\
Bate tranquila sus alas.\
\
¡Oh! tú que con tu ternura\
y con tu cariño ardiente \
Me has dado dicha tan pura,\
Que Dios' mande su 'ventura\
Sobre tu elevada frente\
\
A mi madre\
\
¡Oh! cuán lejos están aquellos días\
En que cantando alegre y placentera,\
Jugando con mi negra cabellera,\
En tu blando regazo me dormías.\
\
Con que grato embeleso recogías\
La balbuciente frase pasajera,\
Que por ser de mis labios la primera,\
Con maternal orgullo repetías.\
\
Hoy que de la vejez con el quebranto\
Mi barba se desata en blanco armiño,\
y contemplo la vida sin encanto,\
\
Al recordar tu celestial cariño,\
De mis cansados ojos brota el llanto,\
Porque pensando en ti me siento niño.\
\
Cantares\
\
Son esos ojos tan bellos\
y es tan tierna su mirada,\
Que a tener yo sus destellos\
Te guardaría con ellos\
Constante y apasionada.\
\
Cuando me llegue a morir\
y el mundo me eche en olvido,\
Aunque un siglo haya corrido,\
Mis huesos han de decir\
Lo mucho que te he querido.\
\
Cambiaremos corazones,\
Para que el tuyo me lleve'\
Crecerán sus ilusiones, '\
Pues yo le daré lecciones\
De adorarte como debe.\
\
Tu amor encierra mi historia,\
Por ti no tengo pasado;\
Que no es completa la gloria\
Si el alma guarda memoria\
De la vida en que ha penado.\
\
He conocido un perfume\
Que llaman de todas flores,\
y mi alma, que se consume,\
En sólo tu amor resume\
El amor de sus amores.\
\
Mi tumba en el campo santo\
Tendrá dos lirios abiertos;\
Córtalos tú sin espanto,\
Han de crecer con mi llanto,\
Que también lloran los muertos.\
\
Tú tienes el alma mía,\
Blanca luz, nítida estrella,\
y si te cansa algún día,\
No me la des, no sabría\
Yo mismo qué hacer con ella\
\
Las golondrinas\
\
¿Has visto cómo viene la parlera\
Banda de golondrinas festejosa,\
Cuando en el valle y la floresta umbrosa\
Tiende sus galas rica primavera? \
\
¿y no has visto después cómo ligera,\
En busca de otra tierra, presurosa\
Huye la banda tímida y medrosa\
Al sentir del invierno la carrera? \
\
Así también, la turba cortesana\
Llega, de su impudor haciendo alarde,\
De la fortuna a la primer mañana;\
\
Pero se alzan las sombras de la tarde,\
Ruge la tempestad, aunque lejana,\
y aquella tropa vil huye cobarde .\
\
El agua y la flor \
\
Unas blancas amapolas,\
En las orinas de un lago,\
Inclinaban sus corolas\
Contemplándose en las olas\
De la brisa al tierno halago.\
\
El agua, que recibía\
Esa imagen en su seno,\
De gozo se estremecía\
y con dulce vez decía\
Mirando al éter sereno:\
\
-'En vano querrá el destino\
De tan plácidos amores\
Cortar el dulce camino:\
Mi amor irá peregrino\
Tras el cáliz de esas flores.' \
\
El sol cubrió la pradera\
De luz ardiente; inclinada\
Gimió la flor hechicera,\
y como nube ligera\
Subió el agua evaporada.\
\
-'Para siempre te perdí,'\
Dijo llorando la flor.\
-'Nunca te olvides de mí,\
Que te adore mientras fui,'\
Dijo el agua con dolor.\
\
En la atmósfera flotando\
El agua en leves vapores, \
Iba á la tierra mirando,\
y en la tierra contemplando\
Iban al cielo las flores.\
\
Huyó la luz bienhechora ....\
Tornose el cielo sombrío;\
Pero luego encantadora\
Volvió a despuntar la aurora\
Vertiendo dulce rocío.\
\
Triste, abandonada, sola,\
y llorando sus amores,\
La desgraciada amapola\
Inclinaba su corola\
Al peso de sus dolores.\
\
Mas cuando allá en el Oriente,\
Blanca la mañana brota,\
Sintió llegar dulcemente\
Hasta su cáliz ardiente\
Una cristalina gota,\
\
Estremeciose la flor\
Sobre BU tallo agitada,\
y el rocío, con amor,\
Dijo: cese tu dolor,\
Soy el agua evaporada.\
\
Lejos me llevó la suerte,\
Quedaste tú sin abrigo; .\
Mas si se acerca tu muerte,\
Antes, mi bien, que perderte,\
Yo vengo a morir contigo.\
\
y entre la verde enramada\
El céfiro que se agita\
En la tarde sosegada,\
Vio la gota evaporada\
y la amapola marchita.\
\
Dulce amor de mis amores,\
Que me das vida en tu halago:\
Si soplan los sinsabores,\
Sé tú la flor de las flores,\
y yo la gota del lago.\
\
La moral\
\
El ser de la virtud la senda estrecha,\
y la del vicio cómoda y florida,\
Verdad, es, tan antigua y tan sabida,\
Que repetirlo, a nadie le aprovecha.\
\
¿Quién no sabe que el malo hace cosecha,\
y que el bueno se pasa triste vida;\
Que comenzando iguales la partida\
Éste se muere de hambre aquél pelecha?\
\
Si de tales premisas la experiencia\
Deduce como regla, que los bobos\
Son los llamados 'hombres de conciencia,'\
\
Si son triunfos escándalos y robos,\
A la moral defino como ciencia,\
De preparar ovejas a los lobos. \
\
Los dos espíritus\
\
'¡Adiós! adiós! al espirar decía\
Un amante infeliz; y ella en su duelo,\
-'¡Jamás te olvidaré, le repetía,\
Pronto nos uniremos en el cielo.\
\
Murió el amante, y luego cariñoso\
Su espíritu volvió... mas con tristura,\
Mirando roto el vínculo amoroso,\
Lanzó un suspiro y se tornó a la altura.\
\
Murió también la ingrata, y desolado\
Su espíritu buscaba el de su amante...\
No le encontró jamás y atormentado\
Su espíritu vagó solo y errante.\
\
¡Ay de aquella alma, que al amante muerto\
Sepulta en el olvido más profundo! '\
Más allá de la vida hay un desierto,\
Castigo del olvido en este mundo.\
\
En un álbum\
\
Lució brillante aurora del estío,\
Abrió sus hojas la modesta flor,\
Cayó en ellas la gota de rocío\
y trinó el ruiseñor.\
\
Perdiose el trino entre la selva ignota,\
y aun no llegaba el sol hasta el Zenit,\
y evaporada ya la limpia gota,\
Murió la flor en búcaro gentil.\
\
Una mirada de tus ojos bellos\
Brillante aurora de mi vida fue,\
y al comprender tu corazón en ellos\
Sentí el consuelo y de placer cauté.\
\
¿Como el trino y la gota de roclo,\
Mi oscuro nombre en tu alma morirá~\
¿Como la flor, hasta el recuerdo mío\
También perecerá?\
\
El joven y el viejo \
\
-La tribunal el periodismo!\
Faros de la humanidad.\
-Joven, tu temprana edad\
Te hace engañarte a ti mismo.\
-No es sueño — Pues qué? Verdad\
\
Verdad que enseña la historia,\
Que entusiasma al corazón:\
Hallar la fama y la gloria,\
y alcanzar una victoria\
Con la luz de la razón.\
\
Jugando con las pasiones,\
Hacer a un pueblo feliz, \
y entre ardientes ovaciones\
Arrancar de su raíz\
Añejas preocupaciones;\
\
y con entusiasmo santo,\
Poder, padre, a nuestro antojo,\
Mover en el pecho espanto,\
y alcanzar como despojo\
Sonrisa, aplausos ó llanto.\
\
¿Y pensáis que desvarío?\
-Puede ser, que tus pasiones\
Te hacen ver como razones\
Lo que es tan sólo, hijo mio,\
Una ilusión de ilusiones.\
\
-Pálido está tu semblante.\
-La desgracia me importuna.\
-¿y la prensa? ¿Y la tribuna?\
-En vano busqué anhelante\
El curso de la fortuna;\
\
Que encontré, por donde quiera\
Cuando dije la verdad,\
Aquí la audacia altanera,\
Más allá la envidia fiera;\
Por todas partes maldad.\
\
y en vano con bizarría\
Luché, padre, en mi abandono;\
Que el pueblo a quien defendía,\
Siempre contra mí volvía\
Sus armas con fiero encono.\
\
y llagado el corazón,\
Padre, me volví a mi hogar,\
Porque dieron en llamar\
A mi valor ambición,\
Locura a mi bien obrar.\
\
y solo y abandonado\
Nadie escuchó mis razones,\
y entre tristes decepciones\
Conocí que había soñado\
Sólo ilusión de ilusiones.\
\
Epístola\
\
No busques, Juan, con loca incertidumbre,\
Esa heroica virtud que te fascina,\
Entre la palaciega muchedumbre.\
\
La codicia su marcha determina,\
y siguen todos como rumbo cierto,\
Del viento la corriente que domina:\
\
La vista fija en anhelado puerto,\
Con huracán deshecho, ó con suave\
Brisa, llega más pronto el más experto.\
\
Allí solo zozobra el que no sabe,\
O que saber no quiere, el fácil modo\
De aligerar mejor la frágil nave.\
\
Quien, por salvar el cargamento todo,\
Alegre lanza a la onda, procelosa,\
O a negro cenagal de oprobio y lodo,\
\
El limpio honor de la modesta esposa,\
O de. amor fraternal haciendo alarde,\
Sacrifica a la virgen pudorosa.\
\
Quien, a la baja adulación, cobarde,\
Prestados pide los batientes remos,\
Temeroso quizá de llegar tarde,\
\
y sin rubor agota los supremos\
Medios de la lisonja, y degradado\
Toca de la abyección a los extremos.\
\
y a veces con ardid más reprobado\
Acude a la calumnia y la mentira\
En la denuncia vil del hombre honrado.\
\
Por alcanzar el premio a que se aspira,\
El honor no detiene, ni amedrenta,\
Ni nada digno ni cruel se mira;\
\
Que del favor la llama se alimenta.\
Lo mismo con ajeno sacrificio\
Que con el cieno de la propia afrenta.\
\
Ni de infame se nota el ejercicio\
De llevar diligente al poderoso\
Codiciados objetos de su vicio.\
\
Nombre allí la virtud tiene oprobioso\
Que el labio calla y el pudor ignora,\
y son uno el prudente y el medroso .\
\
Allí de lealtad nadie atesora\
El noble don; cual gallos vigilantes\
Esperan el fulgor de nueva aurora.\
\
Todos quieren llegar, todos ser antes,\
Si un astro nuevo con sus rayos hiere,\
Huyendo al que se eclipsa tumultantes.\
\
y el coro indigno sin rubor profiere\
Cantos de triunfo para el sol que nace,\
Gritos de guerra para el sol que muere .\
\
Ni hay amparo tampoco que reemplace\
Allí de la amistad, al dulce abrigo\
Que á humano pecho tanto satisface .\
\
y si fiera ocasión lleva consigo\
Exigir una víctima, de puente\
Sirve bien el cadáver del amigo \
\
Siempre el triunfo será del diligente\
Que ni escrúpulo sufre, ni repara\
Si al malvado inmoló ó al inocente\
\
Nadie allí se conoce ni se ampara\
Si un interés cualquiera se subleva.\
Planta es la caridad allí tan rara,\
\
Que si acaso a. nombrarla hay quien se atreva,\
Tan brusca carcajada le responde,\
Que de su necio error castigo lleva.\
\
Con cuidadoso empeño, allí se esconde\
Lo que el vulgo ruin llama conciencia,\
y a los villanos sólo corresponde.\
\
En la patria pensar fuera demencia,\
Que está su nombre allí tan ignorado,\
Que apenas se sospecha su existencia.\
\
Todos miran el puesto a que han llegado,\
Como medio, no más, de hacer fortuna;\
Busca pingües ganancias el privado, \
\
No excusa el que pretende, mengua alguna\
Por alcanzar ruin, mezquina gracia,\
Cualquiera humillación es oportuna.\
\
Quien más consigue, quien mayor audacia\
Muestra, y mayor cinismo, más aprecio\
Gana en la palaciega aristocracia.\
\
Huye Juan, de tal gente, aunque de necio\
Te tachen y te burlen, y con fiera\
Soberbia, te contemplen con desprecio.\
\
No pretendas pisar tan alta esfera,\
Reprueba tanto crimen sin embozo,\
Que la honradez nos hace placentera\
La triste soledad del calabozo.\
\
Prisión de Santiago Tlaltelolco,\
Setiembre de 1884\
\
La huérfana\
\
¡Madre! ¡mi madre!\
Las horas pasan,\
y yo estoy triste\
Porque me faltas.\
\
¿Por qué te has muerto\
Madre adorada? .\
¿Por qué me dejas\
Cuando te llama\
Llena de angustia\
Mi pobre alma?\
¿Ya no me quieres?\
¡Cuánto me amabas!\
¡Estoy tan sola!\
¡Sola en mi casa,\
Por donde quiera\
Pienso que me hablas!\
Lloro en la noche\
Y en la mañana.\
Ya mire el prado,\
Ya la montaña,\
Nada me alegra,\
Todo me cansa,\
Una tras otra\
Las horas pasan\
Y yo estoy triste\
Porque me faltas.\
\
Si miro al ave\
Que en la enramada\
A sus hijuelos\
Alegre llama;\
Si. entre las peñas\
La oveja blanca\
A sus corderos\
Feliz halaga,\
Cuánto su dicha,\
Cuánto me encanta\
y entonces vierten\
Mis ojos lágrimas,\
Porque estoy sola\
Y abandonada.\
No tengo a nadie,\
La mía, santa\
Madre querida,\
Madre del alma;\
Dejó la tierra.\
Sin esperanzas\
De verla nunca\
Las horas pasan,\
y yo estoy triste.\
Porque me faltas.\
\
¿Me oyes, mi madre?\
De esa morada \
En donde habitas,\
¿Ves lo que pasa \
Sobre este mundo\
De penas y ansias?\
¿Piensas en la hija\
De tus entrañas,\
Que tanto llora,\
Que tanto te ama?\
¿Ya no te acuerdas?\
En las mañanas\
¡Cómo a mi lecho\
Te aproximabas!\
Tu faz risueña\
Iluminada,\
¡Qué dulce beso!\
¡Era tu alma!\
\
Pero ¡ay, Dios mío!\
Todo se acaba,\
Madre, mi madre,\
Las horas' pasan\
y yo estoy triste\
Porque me faltas.\
\
Las oraciones\
Que me enseñabas,\
No las olvido.\
¿Oyes? se alzan\
Cuando los ecos\
Del mundo callan\
y de la noche\
Llega la calma;\
Pues por ti sola\
Es la plegaria\
Que de mi pecho\
Triste se exhala.\
Siento tu sombra\
Junto a mi cama,\
tu dulce acento\
Mi frente baña,\
Sueño contigo,\
Te miro rauda\
Cruzar el cielo,\
Despierto y... nada.\
Madre, mi madre,\
Las horas pasan\
y yo estoy triste\
Porque me faltas.\
\
Gloria\
\
No me hablen de Colón y Galileo,\
Ni de Miguel Cervantes ni de Ovidio,\
Que después del destierro ó el presidio\
Llegaron de la gloria al apogeo.\
\
Fueron grandes sus penas, bien lo creo,\
Es inmortal su fama, y yo la envidio,\
Pero lleva conato de suicidio;\
Consolarse con eso es devaneo.\
\
Yo recuerdo muy bien toda la historia\
De esos ilustres hombres (no me alabo,\
Pues talento del tonto es la memoria,)\
\
Pero hay que convenir al fin y al cabo\
Que es fórmula constante de la gloria\
'Que al asno muerto, la cebada al rabo.'\
\
Querellas y consuelos\
\
Herido está mi corazón, herido;\
Le hirió la ingratitud,\
Eclipsaron las nubes del olvido\
De su primer amor la blanca luz.\
\
Herido está mi corazón, herido;\
Le hirió la ingratitud,\
¡Ay, pobre corazón que vas perdido\
En la tierra buscando la virtud!\
\
Herido está mi corazón, herido;\
Le hirió la ingratitud,\
¡Ay, pobre corazón, noble y sufrido,\
Pronto tendrás la dicha y la salud!\
\
El alma a su sagrario\
Llevó una blanca y perfumada rosa;\
Pero la flor, abriendo su nectario,\
Destiló en el santuario\
Una gota de esencia venenosa.\
\
No llores tu quebranto,\
Alma, ni de la rosa falsía,\
Que una traición no vale un llanto;\
Perdió la flor su encanto;\
¿Dónde una alma hallará como la mía?\
\
La noche en el escorial \
\
La noche envuelve con su sombra fría\
El claustro, los salones, la portada,\
y vacila la lámpara agitada,\
De la iglesia en la bóveda sombría.\
\
Como triste presagio de agonía\
Gime el viento en la lúgubre morada,\
y ondulando la yerba desecada\
Vago rumor entre la noche envía.\
\
De Felipe segundo, misterioso\
Se alza el espectro del marmóreo suelo\
y vaga en el convento silencioso,\
\
y se le escucha en infernal desvelo\
Crujiendo por el claustro pavoroso\
La seda de su negro ferreruelo.\
\
La muerte y la mariposa\
\
Junto al tronco derribado\
Del árbol de un cementerio,\
En apartado misterio\
Crece un rosal delicado.\
\
El aroma de la rosa\
Que lleva el aire en su giro\
Atrae a su retiro \
A una errante mariposa.\
\
Allí, en torno de la flor,\
Revolando alegre, advierte\
Que es el jardín de la muerte\
Que es la mansión del dolor.\
\
Quiere huir, más de repente\
Vaga sombra misteriosa,\
Alzándose de una fosa\
La llama con voz doliente,\
\
la dice: 'Ten el vuelo\
'Mensajera del amor,\
'En la mansión del dolor,\
'Del llanto y del desconsuelo.\
\
'Deja de vagar ufana,\
'Descuidada de tu suerte,\
'Que soy la implacable muerte\
'Que debe herirte mañana.'\
\
Parando entonces el vuelo\
Sobre el cáliz de una rosa,\
Contestó la mariposa\
Alzando la vista al cielo:\
\
-'¿La muerte? ¡nunca me aterra\
'Esa palabra temida,\
'Que hallé en la muerte la vida,\
'Gusano vil de la tierra!\
\
'Yo viví lánguida y triste,\
'Pobre larva, masa inerte;\
'Morí, mas me dio la muerte\
'El ser que mi ser reviste.\
\
'Sentí acabarse mi vida\
'En un sepulcro encerrada;\
'Mas renací de la nada '\
'De ricas galas vestida.\
\
'y conocí que en el mundo\
'No hay muerte, trasformación,\
'Que guarda de redención\
El misterio más profundo.\
\
'y el que hoy se oculta en la fosa\
'y deja la forma humana,\
'Se alzará vivo mañana\
'Árbol, ave ó mariposa.\
\
'Y en esa eterna cadena\
'El ser jamas se consume;\
'Quizá mañana perfume\
'Seré de blanca azucena.\
\
'y no tiembla mi humildad\
'y al amago de la suerte,\
'Que vuelvo a entrar con la muerte\
'De vida en la eternidad.\
\
La mariposa calló,\
Alzándose con la brisa,\
y una apacible sonrisa\
El espectro dibujó.\
\
La hamaca\
\
Preso en su misma cadena\
Quedó al fin el amor niño, \
y arde en su pecho de armiño\
El amor de una Sirena.\
\
En vano con loco anhelo\
Rechaza el tirano yugo;\
Que es víctima sin consuelo\
Quien sin piedad fue verdugo.\
\
y por la playa arenosa\
Va llorando sus pesares,\
Al ver la Sirena hermosa\
Cruzar los azules mares.\
\
y va la playa siguiendo\
Sin librarse de su pena,\
y entre los tumbos oyendo\
El cantar de su Sirena.\
\
Ella en las ondas se mece,\
Él tiende el arco pujante,\
y ella... ríe y desparece\
Entre la espuma flotante.\
\
Venus, por calmar su pena\
y su pasión desgraciada,\
Teje una red encantada\
Para pescar la Sirena.\
\
Lanza las redes Cupido,\
y al ver que logra su intento,\
Dando sus alas al viento\
Deja la red en olvido.\
\
Un ignoto pescador\
Entre las ondas la saca,\
y se convierte en hamaca\
Las que eran redes de amor.\
\
La catedral de Toledo\
\
Indiferente, el mar crucé y los ríos,\
Las fértiles campiñas cultivadas\
y las selvas desiertas y azotadas\
Por huracanes roncos y bravíos. \
\
Vi las montañas con sus picos fríos,\
Por las eternas nieves coronadas,\
Reí en las ciudades levantadas\
Por Señores y príncipes impíos.\
\
Pero en tu inmensa catedral ¡Toledo!\
Hay no sé qué misterio que me asombra;\
Mi espíritu vacila, tengo miedo,\
\
Que se adivina a Dios entre tu sombra,\
y aunque quisiera resistir, no puedo;\
Tiembla mi labio y con pavor le nombra.\
\
El canto del explorador \
\
'Es bello por la mañana,\
Cuando apenas nace el so],\
Por la desierta montaña\
Marchar como marcho yo,\
Con mi mosquete en la mano\
y sobre mi buen trotón,\
Buscando el camino oculto\
Por donde va el invasor\
Procurando dar albazo\
A mi brava división,\
Sin pensar que entre las peñas,\
Sin descuido y sin temor,\
Sus más leves movimientos\
Siguiendo constante voy,\
y entre el polvo que levanta\
Su infantería veloz,\
Cruzo atrevido el camino\
Que hace un momento cruzó.\
\
Es hermoso al medio día,\
Cuando de ardiente calor\
y de fatiga rendido\
El enemigo paró,\
Ver cómo reparte el rancho,\
Cómo descansa el traidor,\
Mientras que casi a su vista\
También descansando estoy.\
\
y cuando cierra la noche\
y el enemigo acampó\
y se encienden las hogueras\
y luego cesa el rumor,\
Después de rondar su campo\
y mirar cómo quedó,\
Embozado en mi sarape\
y dando gracias a Dios,\
Qué grato es el campamento,\
Volverme sin dilación\
y dar le parte de todo\
Al vigilante mayor\
Diciéndole: No son cuentos,\
Que todo-lo he visto yo,'\
y luego muy orgulloso\
Ir adonde está mi amor\
A reposar la fatiga\
Mientras no hay otra facción.'\
Así cantaba un chinaco\
Que caminaba veloz\
Entre huestes enemigas\
Sirviendo de explorador.\
\
Celos\
\
Entre angustias y desvelos\
Paso la noche agitada:\
¡Ay de la alma enamorada\
Adonde anidan los celos!\
\
y mi razón se extravía\
Entre el temor y el recuerdo,\
Que en esos amores pierdo\
El alma del alma mía.\
\
Tengo celos de la fuente\
Que retrata su sonrisa,\
Celos de la blanda brisa\
Que llega á besar su frente.\
\
y agita el celo su saña\
Cuando su voz seductora\
Va repitiendo sonora\
Con sus ecos la montaña.\
\
y crece mi desventura\
Si de su lado me alejo,\
y pienso cuando le dejo\
Que va a olvidar mi ternura.\
\
y si está ausente le llamo,\
y tanto el celo me agita,\
Que si mi  pasión se irrita\
Llego a soñar que no amo.\
\
y entre angustias y desvelos\
Exclamo desesperada: \
¡ Ay del alma enamorada\
Adonde anidan los celos! \
\
y mi alma la muerte pide ·\
En lucha tan congojosa;\
¿Por qué no soy muy hermosa\
Para que nunca me olvide?\
\
y corre mi ardiente lloro,\
Que si mi fe no merece,\
Mientras más mi celo crece\
Con mayor fuego le adoro.\
\
Pobre amor, pobre amor mío,\
Te agosta el sol con su rayo,\
y no ali vía tu desmayo\
Ni una gota de rocío.\
\
Mas si con olvido fiero\
De pasión su pecho muda,\
Otra le amará sin duda,\
Mas no como yo le quiero .\
\
y entre angustias y desvelos\
Moriré desesperada:\
¡Ay de la alma enamorada\
Adonde anidan los celos!\
\
Pero mi alma se extasía...\
Si vivo... si vivo amante,\
N o me ha olvidado un instante,\
Si no, ya no existiría.\
\
La vejez\
\
Mienten los que nos dicen que la vida\
Es la copa dorada y engañosa,\
Que si de dulce néctar se rebosa,\
Ponzoña de dolor guarda escondida.\
\
Que es, en la juventud senda florida,\
Y, en la vejez, pendiente, que escabrosa\
Va recorriendo el alma, congojosa,\
Sin fe, sin esperanza y desvalida.\
\
¡Mienten! Si a la virtud sus homenajes\
El corazón rindió con sus querellas\
No contesta del tiempo á los ultrajes;\
\
Que tiene la vejez horas tan bellas\
Como tiene la tarde sus celajes,\
Como tiene la noche sus estrellas.\
\
La Rosa y la Espina\
\
¿Por qué con dardo punzante,\
Dijo a la espina la rosa,\
Te opones siempre arrogante .\
A que me toque anhelante\
una mano cariñosa?\
\
Miro la blanca azucena \
Que con su dulce perfume\
Allá en la pradera amena\
Con su beldad enajena\
y el tedio no la consume.\
\
y yo triste, abandonada,\
Nadie se acerca a mirarme\
Que siempre espina acerada\
Amenaza despiadada\
Al que se atreve a tocarme.\
\
y así, sola, sin consuelo,\
Moriré, pidiendo en vano,\
Presa de terrible anhelo,\
Que llegue a librarme el cielo\
De mi destino tirano.-\
\
Calló la sensible rosa,\
Callando siguió la espina,\
y pintada mariposa\
Vino alegre y vagarosa\
Con el aura matutina.\
\
Entonces gracioso niño\
Llega a la rosa, la mira,\
y con infantil cariño\
Tiende su mano de armiño,\
Pero al punto la retira.\
\
Hiere la espina su mano,\
Burla la espina su intento,\
y viendo su empeño vano\
Toma la azucena ufano\
y rota la entrega al viento.\
\
Ay de la tierna doncella\
A quien punzantes abrojos\
No circundan; que si es bella\
Verá eclipsarse su estrella\
Con el llanto de sus ojos!\
\
La fiesta de Chepetlán\
\
Alegre viste sus galas\
El pueblo de Chepetlan,\
Que está celebrando el día\
De la fiesta titular.\
¡Cuál repican las campanas\
De la iglesia parroquial!\
¡Cómo suena el teponaxtle\
Con monótono compás!\
y cámaras y cohetes\
Estallan aquí y allá,\
y se escucha en todas partes\
Una algazara infernal.\
Por donde quiera enramadas,\
En las que vendiendo están\
Aguas frescas y sandías,\
\
y al son de una arpa tenaz\
Nativos y forasteros\
Bailan con dulce igualdad; \
Se oye la voz estentórea\
Del que tiene el carcamán,\
y de otro, que lotería \
Llama á todos a jugar.\
Entre los arcos de fuego\
Pasa la . fugaz,\
Templando apenas el fuego\
De ardiente sol tropical.\
En grupos la muchedumbre\
Se agita, en constante afán, ·\
A vida de divertirse\
Anhelando por gozar.\
Los hombres, ancho sombrero\
y negro, en lo general,\
Camisa y calzón muy anchos,\
Muy blancos, y nada mas;\
Las mujeres con enaguas\
De extraña diversidad\
y todos ríen y cantan .\
y llegan, vienen y van,\
Tomando de cuando en cuando\
Algún trago de mezcal.\
\
Entre tanto forastero\
Que ha llegado a Cltepetlán\
Buscando en aquellas fiestas\
Tener un grato solaz,\
Se notan muchos soldados\
Que, con licencia quizá,\
De las tropas virreinales\
Se apartaron, sin pensar\
En guerras ni en insurgentes,\
Porque muy lejos están\
Guerrero y todos los suyos,\
y no· hay que temerles ya,\
Al menos mientras que dure\
La fiesta de Chepetlán.\
\
Cuando la tarde se acerca\
y el sol declinando está,\
Se escucha rumor extraño,\
Inusitado y marcial,\
y la gente se alborota .\
Ya, sin poder explicar\
Lo que causa aquella alarma\
y produce lance tal;\
De repente por las calles,\
Sobre un erguido alazán\
Que tasca el freno impaciente\
y echa fuego al respirar,\
Altivo pero sereno, \
Llega un hombre en cuya faz\
Se pinta el alma de un bravo\
\
Tan noble como leal:\
Es Guerrero, el indomable\
Hijo de la libertad;\
Le sigue valiente tropa\
Que al pueblo llegando va,\
y se ocultan los que temen\
y otros salen a mirar.\
Entra Guerrero a la plaza,\
y del soberbio animal\
Tiembla la rienda y detiene\
Del seco trote el compás.\
Trascurren pocos instantes\
y comienzan a llegar\
Unos y otros, prisioneros\
Los del bando virreinal.\
Todos ellos cabizbajos\
y silenciosos están;\
Guerrero les mira un rato\
y luego con dulce faz\
Les pregunta: '¿a qué han venido?'\
y nadie osa contestar.\
Vuelve a preguntar Guerrero,\
y entonces, saliendo audaz\
Un sargento, con despejo\
Contesta: «Mi general,\
«Hemos venido a la fiesta\
«A gustar de Chepetlán;\
(y venimos con licencia.»\
\
-(¿Y nada más?» «Nada más.»\
Vuelve a reinar el silencio,\
Afable Guerrero está,\
y dice con voz pausada:\
«Pues vinisteis a gustar,\
«Seguid alegres gustando,\
«Que yo os doy la libertad;\
«Pero mañana, os lo advierto,\
«Que no os halle por acá\
'La luz de la madrugada;'\
'¡Que viva mi general'\
Grita entusiasta el sargento:\
-'¡Viva!' gritan los demás,\
y alegre sigue la fiesta\
Que nada vuelve a turbar;\
y chaquetas e insurgentes\
Siguen con grato solaz,\
Que es una noche le gusto\
Esa noche era Chepetlán.\
\
Yo y tú\
\
Entre la blanca nieve aprisionada\
y de la noche en el temido horror,\
Sola, sin esperanza, abandonada,\
Lloró la pobre flor .\
\
Rajo el negro crespón de la tormenta\
Con que se entolda, el cielo de zafir\
y en la noche terrible que amedrenta, \
Creyó el ave morir.\
\
Perdido y solo entre la selva umbría,\
Sin una estrella que su luz le dé,\
Triste viajero que perdió la guía,\
Piensa morir también.\
\
Pero se alza radioso en el Oriente,\
Puro, brillante, esplendoroso el sol,\
\
y aye, y viajero, y flor, ven dulcemente\
Las tintas de arrebol.\
\
Yo soy la flor apasionada y muerta,\
Yo soy el ave que perdió la luz,\
Yo soy viajero en la región desierta,\
Puro sol eres tú.\
\
Ruego\
\
Unas tras otras, fieras y espantosas,\
Alzáronse las nubes hasta el cielo,\
y entre su oscuro y proceloso velo\
Van del rayo las luces pavorosas .\
\
El trueno en las montañas fragorosas\
Repite el eco, reina el desconsuelo,\
Mas brilla el sol y con amante anhelo\
Cantan las aves tiernas y dichosas.\
\
Si negra tempestad de nuestra vida\
Llegó a manchar el cielo, si tu lloro\
Vino a turbar nuestra ilusión querida,\
\
Tú mi única pasión, tú mi tesoro,\
Vuelve a mi pecho la quietud perdida,\
Vuélveme a dar tu fe, porque te adoro .\
\
Romance\
\
Está muriendo la tarde\
y las nubes se coloran\
Con los rayos postrimeros\
De la luz, que presurosa\
Va huyendo de estas regiones\
Que se envuelven en las sombras.\
El ave duerme en su nido\
y sus cantares no entona;\
Los lirios de la montaña\
Abrieron ya sus corolas,\
y exhalan las maravillas\
Llenas de encanto su aroma. \
¡Cómo es dulce la tristeza\
Que derraman estas horas\
En que al bullicio del día\
Sucede paz deliciosa!\
El misterioso silencio\
\
De la noche encantadora\
Al pecho amante le ofrece\
Cuanto la mente ambiciona.\
Ven a gozar, dueño mío,\
Del cariño que atesora\
Para ti tan sólo, el alma\
Que en ti concentra su gloria.\
No se escuchará el arrullo\
De tórtola gemidora,\
y al pié de la ruda peña,\
En donde la fuente brota,\
Te hablaré de mis amores,\
Te cantaré mis congojas,\
y pronunciando tu nombre\
Sentiré dulce mi boca.\
y celos tendré del aire\
Que el dulce nombre me roba\
Llevándolo entre sus alas,\
Hasta la selva remota.\
Ven, amor de mis amores,\
Que la nube presurosa\
Tiende su negro ropaje\
Para velar nuestra gloria .\
\
La muerte del tirano\
\
Herido está de muerte, vacilante\
y con el paso torpe y mal seguro,\
Apoyo busca en el cercano muro,\
Pero antes se desploma palpitante.\
\
El que en rico palacio, deslumbrante, \
Manchó el ambiente con su aliento impuro,\
De ajeno hogar en el recinto oscuro,\
La negra eternidad mira delante. ,\
\
Se extiende sin calor la corrompida\
y negra sangre, que en el seno vierte\
De sus cárdenos labios la ancha herida,\
\
y el mundo dice al contemplarle inerte:\
Escarnio a la virtud era su vida;\
Vindicta del derecho fue su muerte.'\
\
Quejas\
\
¿Qué te hice? ¡Tal rigor! \
Mi pobre alma se consume.\
¿Por qué he perdido tu amor?\
¡Ay! que se agosta la flor\
Cuando pierde su perfume.\
\
¿Por qué de tu amor el día\
Me dio vida con su luz,\
Si arrebatarme debía\
Noche espantosa y sombría\
En su lúgubre capuz?\
\
Si eran mucho para mí\
Tanto amor tanta ventura\
¿Por qué me engañaste así?\
¿Por qué entonces no morí\
Feliz con tanta ternura?\
\
Humilde fiel retrataba\
Tu imagen mi alma gozosa, .\
Tu alma, en mi alma reflejaba:\
Si estaba triste, lloraba,\
y si alegre; era dichosa.\
\
y con ese amor ardiente\
Miré las flores más bellas,\
Más espumoso el torrente,\
Más apacible la fuente,\
Más brillantes las estrellas.\
\
y no halló mi abnegación,\
Sin ti, la dicha un momento,\
Ni un latido el corazón,\
Ni el alma una inspiración,\
Ni el cerebro un pensamiento.\
\
y tanto amor, ¿qué merece?\
¿Por qué llegó tu desvío?\
¡Ay! que mi alma desfallece...\
Celaje que desvanece\
Soplo de huracán bravío.\
\
Entre el hielo aprisionada\
Pobre flor que mira luego,\
Mísera y desamparada,\
La luz del sol adorada\
Sin poder sentir su fuego.\
\
A veces quiero morir, \
Pero es perder tu recuerdo,\
Mas, si olvido he de sufrir,\
Entre la muerte ó vivir\
No sé cómo más te pierdo.\
\
En mi dolor te bendigo,\
y corre amargo mi llanto,\
Que ni una esperanza abrigo:\
¿Por qué fuiste así conmigo\
Cuando yo te amaba tanto?\
\
¡Adiós! mi triste querella\
No turbará tu memoria;\
Alumbre pura tu estrella\
y no dejen ni una huella\
Mis lágrimas en tu historia.\
\
La siesta\
\
Aquí, bajo la copa\
Flotante del palmero,\
Que altiva se dibuja\
Sobre el espacio azul,\
A orillas de las aguas\
Tranquilas del estero\
y cerca de las ondas\
Del mar que ruge fiero,\
Aguardo en nuestra hamaca,\
Hasta que llegues tú.\
\
Te espero, ven, señora;\
Pasó de la mañana\
La brisa fugitiva,\
y el sol abrasador\
Marchita la azucena\
Que se columpia ufana,\
y del gigante cedro\
\
La cariñosa liana\
Afloja desmayada.\
Los nudos del amor.\
\
Se ocultan en el bosque\
Los tímidos faisanes,\
y en las fangosas grutas\
Del tétrico manglar,\
Entre los verdes tules\
Se aduermen los caimanes,\
Los tristes alcatraces\
Sin miedo de huracanes\
Escuchan en las rocas\
Los tumbos de la mar.\
\
No se oye de las aves\
La cántiga sencilla,\
No cruza la gaviota\
El cielo de zafir;\
Ninguna nave surca\
Las aguas con su quilla,\
Y llegan presurosas\
Hasta tocar la orilla\
Las olas que en espuma\
Se tornan al morir.\
\
Silencio majestuoso\
Que guarda los amores,\
\
Señora, ven, te espero,\
Acércate, mi bien;\
Te envolverán los gratos\
Perfumes de las flores,\
y miraré en tus ojos\
Brillantes, seductores,\
Espléndida irradiando\
La llama del placer.\
\
De mirtos y azucenas\
Tejiendo una guirnalda,\
Tu negra cabellera\
Con ella ceñiré;\
\
Sus flores desprendidas\
Sobre tu fresca espalda\
Dejando irán sus besos,\
Hasta tocar la falda\
Donde el encanto asoma\
De tu desnudo pié.\
\
Podré, como otras veces,\
En tu agitado seno\
Tranquilo mi cabeza\
Ardiente reposar,\
Sintiendo cuál se mueve\
Con tu alentar sereno;\
y de placer y amores\
\
y de ternura lleno\
Sobre tus blandas manos\
Mis labios estampar.\
\
¿Llegaste, mi adorada?...\
Coloca, sí, coloca\
Tu seno junto al mío.\
¿Suspiras de placer?\
Tus labios seductores\
Sellando están mi boca,\
Me oprimes en tus brazos,\
Tu aliento me sofoca;\
Estréchame, ángel mío,\
Confúndete en mi ser .\
\
Hastío\
\
Entrecerrados ya tus ojos bellos\
Perdieron su mirar resplandeciente,\
y yo también te miro indiferente\
Sin buscar el amor en sus destellos.\
\
Triste y pálida estás; de tus cabellos\
Negros rizos se pegan a tu frente,\
Te reclinas en mí, mas ya no ardiente\
Pongo mis labios con pasión en ellos.\
\
Todo pasó, de la ilusión las flores\
Marchitáronse al fuego del estío;\
Perdiste tus encantos seductores;\
\
Apurando el placer llegó el hastío,\
Huyeron espantados los amores\
y siente el alma aterrador vacío.\
\
Los tres suspiros\
\
Te vi pasar gallarda y altanera,\
¡Ni una sola mirada para mí!\
Mi pecho suspiró por vez primera,\
¡y suspiró por ti!\
\
En mi hombro reclinabas tu cabeza:\
De tanto amarte, me llegaste á amar;\
El dueño me sentí de tu belleza;\
¡Y volví a suspirar...\
\
Entre los dos, la noche de la ausencia\
Tendió sus alas y enlutó mi edén,\
¡Te llevaste la luz de mi existencia\
y suspiré también!\
\
Suspira el corazón con la esperanza;\
Suspira con la dicha que perdió;\
Suspira con el bien, cuando le alcanza;\
¿Por qué suspiro yo?\
\
La campana\
\
Anunciando la fiesta de la aldea\
Matutino repique se desata,\
Que lanza como rauda catarata\
La campana que alegre clamorea.\
\
Mas triste y melancólica golpea\
y fúnebre el tañido se dilata,\
Cuando la muerte pálida arrebata\
Algún ser cuya fosa el viento orea.\
\
Por eso con profunda simpatía\
Escucha el pueblo, y con cariño santo,\
Ese tañer que grato le extasía;\
\
Porque a ese bronce, en misterioso encanto\
Siempre le oye reír en su alegría,\
Siempre le oye llorar en su quebranto .\
\
Idilio\
\
Una casita\
Sobre una alfombra\
De blancas flores y verde grama,\
Donde recuestan su fresca sombra\
Los arrayanes y la retama.\
\
Entre las juncias\
y carrizales\
Un arroyito que corre puro,\
Acariciando con sus cristales\
La madreselva que escala el muro.\
\
Blancas ovejas\
Sobre las lomas,\
Tordos parleros por los sembrados,\
y en dulce arrullo blancas palomas\
En los aleros de los tejados. \
\
Cabe las puertas\
y en las ventanas,\
De roja hiedra fresca cortina.\
y por los patios cruzando ufana\
En raudo vuelo la golondrina.\
\
Entre los fresnos\
A ves cantando,\
Junto al estanque lirios y rosas,\
y por las flores, ledas buscando\
El dulce néctar las mariposas.\
\
y tú a la sombra,\
Cerca del río,\
El verde musgo por blando lecho,\
La trova oyendo que el pecho mío\
Manda a que more dentro tu pecho;\
\
y allí pintando\
Mi amor ardiente,\
y contemplando tus bellos ojos,\
Húmedos besos sobre mi frente\
Pondrán temblando tus labios rojos.\
\
Dos miradas\
\
Anoche me veías\
Con el alma en los ojos concentrada,\
y yo te comprendí que me decías\
(Bésame con la luz de tu mirada.»\
\
Entonces, más ardiente\
Otra mirada de tus ojos bellos,\
Vino á contarme pura y refulgente,\
Que mi alma toda recibías en ellos.\
\
Cuando el alma atesora.\
Tan infinito amor que va de hinojos\
Culto rindiendo al ser á quien adora,\
La palabra se siente abrumadora\
y el idioma del alma está en los ojos.\
\
A D. Pedro Calderón de la Barca .\
\
Con un golpe certero y poderoso -\
El cautivo de Argel, manco en Lepanto,\
Hiere de lo ideal el tierno encanto,\
Pedestal de la dama del Toboso.\
\
En campo abierto y sin buscar reposo\
Con sardónica risa paga el llanto,\
y burla lo más noble y lo más santo\
Que se alberga en el pecho generoso.\
\
Mas llegas tú, con soberano empeño\
Al idealismo tu poder redime\
y torna de la España a hacerle dueño,\
\
Y al mundo dices, que entre penas gime:\
'Levanta el corazón, la vida es sueño\
'y debes tú soñar con lo sublime.'\
\
Composición\
\
¿Lloras, Patria, mi Patria? tu gemido\
Llega hasta mí tristísimo y doliente;\
¿Y sufres otra vez, y otra vez lloras,\
y otra vez inclemente\
El rayo de la guerra\
Con su dardo de fuego hirió tu frente?\
\
¡Yo te miré triunfante, vindicada,\
y sobre un alto pedestal de gloria,\
Tu frente circundada\
Por el iris brillante de la Historia;\
Flotando tu bandera\
Del viento de la paz al grato impulso,\
Vuelto hacia el porvenir tu noble rostro,\
\
Sacudiendo tu negra cabellera,\
Mirando en lontananza '\
En la bóveda inmensa de los cielos\
Aparecer el sol de la esperanza!\
\
¡Hermosa era su luz! bajo sus rayos\
Que cruzaban la atmósfera serena,\
La fe del sentimiento,\
Rica de inspiración y de ternura,\
Un fantástico cuadro de ventura\
A la región llevó del pensamiento!\
\
Yo te soñaba así! Me parecía\
Que la escarbada arena del combate\
En fratricida lucha \
Nuestra sangre jamás empaparía;\
y sólo del cansado\
y tenaz labrador el corvo arado\
Sobre aquellos recuerdos surcaría,\
Borrando sus dolores,\
Como cubren las flores\
La removida tierra de una tumba;\
Como a la aurora cuando el sol aclara\
y el estrago pasó de la tormenta\
Virgen la selva su hermosura ostenta!\
\
¡Yo te soñaba así! Mi humilde acero\
Colgando en el hogar, tomé la lira,\
Soldado errante y vate peregrino,\
y besando la arena de la playa,\
De otras regiones emprendí el camino.\
\
Desde el bajel y lleno de tristeza,\
Con la mano en el pecho dolorido,\
Descubrí con respeto mi cabeza;\
Fijé ea las rocas la tenaz mirada,\
Sentí crujir la nave \
A impulsos del vapor arrebatada,\
y con la ronca voz de los pesares\
Te dí un adiós y me perdí en los mares!\
\
¿Dónde no va la Patria con nosotros,\
Recuerdo vivo, palpitante y tierno?\
¡Si es inmortal el alma\
Que ese recuerdo lleva,\
También ese recuerdo será eterno!\
\
Al través de la calma y la tormenta\
Crucé la soledad del mar hirviente,\
Cual átomo perdido\
Al soplo de huracán embravecido,\
De corriente en corriente,\
De región en región arrebatado,\
De tormenta en tormenta sacudido.\
\
Aún no tocaba con su hendiente quilla\
El rápido bajel a la ribera,\
\
Cuando allá en la tendida superficie\
Miré como la bruma\
y flotando del mar sobre la espuma,\
El humo en densa nube\
Que arrebatado entre los aires sube.\
\
Era el terrible aliento\
Con que soplaba el monstruo de la guerra\
En su rugir profundo,\
Al recorrer violento \
La turbada región de aquella tierra,\
A cuyos ecos se estremece el mundo.\
\
Pisé la playa y el hervor siniestro\
Del rugiente volcán sentí á mi planta:\
Era un pueblo luchando en la agonía,\
Un pueblo valeroso \
Que entre marciales cantos se levanta,\
y al eclipsarse de su gloria el día\
Sus mismas armas con furor quebranta.\
\
Atravesé su campos desolados,\
Los pueblos de terror abandonados,\
Las ciudades desiertas,\
Y con el alma triste,\
De la imperial París llegué a las puertas.\
\
No era el París que el mundo proclamaba\
Latiente corazón de los placeres,\
Del siglo maravilla,\
De gloria monumento;\
Que el encendido soplo del combate\
Echó por tierra su soberbio asiento!\
\
¡Ante ese cuadro de terror y estrago,\
De horribles desvaríos,\
Lúgubre cifra de la gloria humana,\
Me acordé de mi patria y de los míos!\
y con la faz turbada\
y al través de mi llanto\
La contempló mi orgullo a tanta altura,\
Que lleno de emoción y de ternura\
¡A ti, mi Patria, levanté mi canto!\
\
Los ecos de mi lira se apagaban\
En la emoción del seno,\
y mi espíritu audaz resplandecía,\
y de entusiasmo lleno\
Desde el fondo de mi alma te decía:\
'Ni tiene triunfos que envidiar tu historia,\
Ni tiene glorias que envidiar tu gloria!'\
\
Cuánto anhelé volver. Mi sola idea\
Fue estar, entre los nuestros la cansada\
Narración de mi viaje repitiendo\
La verdad revelando , '\
El velo del engaño descorriendo\
\
Y en nombre de la Patria\
Lanzar como sentencia de mi labio:\
'Devolvamos desprecio por calumnia:\
Devolvamos grandeza por agravio.' \
\
Dejando al fin las playas de la Europa\
Vuelvo a cruzar los encrespados mares:\
Inmensa parecía\
Su agitada extensión que entre sus sombras\
Devoraba la luz de cada día.\
Yo en tanto en la cubierta\
Viendo el sol apagarse en Occidente,\
Entre los vientos de la mar buscaba\
La brisa tropical sobre mi frente\
\
¡Tierra! clama una voz, se abre la bruma,\
Alumbra el sol y la mirada inquieta\
Busca el confín de la agitada espuma,\
y blanca faja pinta el horizonte,\
y el ojo del marino\
Mira del Orizaba el alto monte\
Cual término feliz de su camino.\
y brota de mi labio balbuciente,\
Trémulo de quebranto, .\
Un grito de saludo al continente,\
y á las playas natales\
En homenaje de cariño un canto!\
\
Salté a la playa con febril anhelo,\
y con faz angustiada\
Contemplé con asombro\
La linfa pura de tu paz turbada,\
Mas reí con desdén tú eres un pueblo\
Que de la guerra entre el fragor gigante\
Te conservas ileso\
y marchas adelante\
En los tendidos rieles del progreso.\
\
¡Gloria a tu nombre!¡honor a tu constancia!\
De agitación tu vida se alimenta,\
En tu ser el relámpago encendido\
Que engendra la tormenta,\
Es el hinchado mar embravecido\
Cuya sublime majestad se ostenta\
Al sentirse del viento sacudido!\
Es tu frente altanera\
Que no se inclina ante el acerbo duel\
Ejemplo soberano\
De ese volcán del suelo americano\
Que con sus rocas amenaza al cielo.\
\
¡Aquí siento el latir de tu existencia,\
Palpitación ardiente\
De esa generación que se levanta,\
Se alza de los escombros de la tierra\
Soberbia se adelanta '\
Entre el revuelto polvo de la guerra,\
\
y el eslabón gastado\
Rompe de las cadenas del pasado!\
\
¡Aquí está el porvenir! luz de la ciencia\
Cuyos laureles vuestra frente ciñe!\
Tiernos hijos del pueblo,\
De la Patria esperanza,\
Acaba el porvenir para nosotros,\
Mas nuestra vista alcanza,\
Llevada por la fe de nuestro anhelo,\
Una esplendente luz en lontananza\
Que será el pabellón ele vuestro cielo!\
\
Generación que nace en tus hogares,\
Como memoria santa,\
Como ofrenda sagrada en tus altares,\
Coloca esas coronas .\
Como un recuerdo vivo\
De la heroica virtud de tus matronas.\
\
¡Tuyo es el porvenir, niñez querida!\
El ángel de la fe sus alas bate: \
y ésta que se derrumba\
Generación de duelo y de combate,\
Puede orgullosa contemplar su tumba\
Que compró con su sangre la victoria\
y planta aquí las palmas de tu gloria .",
                    path=u"/c", tags=u"RBT")


writer.commit()

searcher = ix.searcher()

from whoosh.qparser import QueryParser
parser = QueryParser("content", ix.schema)
#myquery = parser.parse("This is")

qp = QueryParser("content", schema=ix.schema)
q = qp.parse(u"Acapulco")

with ix.searcher() as s:
    results = s.search(q)

#results = searcher.search(myquery)
#print(len(results))

#print(results[0])
#{"title": "Second try", "path": "/b", "icon": "/icons/sheep.png"}