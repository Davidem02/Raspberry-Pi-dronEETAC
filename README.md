# Guía para la Integración de una Raspberry Pi en un Dron

> ⚠️Esta guía **no está completa**, pero proporciona una **buena base desde la que empezar** y seguir añadiendo funcionalidades a medida que se desarrolla el proyecto.

Esta guía ofrece una base sólida para comenzar a trabajar con una **Raspberry Pi integrada** en un dron, junto con un **módulo de cámara**. El punto de partida es un dron ya montado y funcional, como el que se muestra en la siguiente imagen, capaz de volar tanto de forma manual (con emisora de radio) como automática mediante el software **Mission Planner**.

<img src="https://github.com/user-attachments/assets/fe6e4731-297a-45f7-8bf2-ad365cc31fc6" alt="Dron montado y operativo (fase inicial)" width="500"/>

> ⚠️ **Esta guía no incluye el montaje inicial del dron.** Se parte de una plataforma ya operativa. El enfoque está en la integración de nuevos componentes para ampliar sus funcionalidades. Guía de montaje del dron: https://github.com/dronsEETAC/GuiaHexsoonEDU450.git

## Qué se quiere conseguir

Con esta integración, se busca que el dron sea capaz de:

- Capturar **imágenes o vídeo** durante el vuelo.
- Ejecutar **código personalizado** desde la Raspberry Pi sin depender de un ordenador externo.
- Realizar un **mapeo básico del terreno** que sobrevuela, combinando la imagen capturada con la posición GPS del dron.
- Establecer las bases para futuras aplicaciones como la **detección de objetos**, el seguimiento, o la toma de decisiones autónoma en tiempo real.

## Material utilizado

A continuación se muestra el material **extra** que se ha añadido al dron para hacer posible la integración de la Raspberry Pi y las funcionalidades de visión:

##### -Raspberry Pi 4 (con caja) 
<img src="https://github.com/user-attachments/assets/df4619ca-0362-4a6b-a28b-0b0860bf646e" alt="Raspberry Pi 4 con caja" width="200"/>

##### -Módulo de cámara Raspberry Pi v3

<img src="https://github.com/user-attachments/assets/5f219733-a2a6-4440-935b-03d073141c90" alt="Módulo cámara Raspberry Pi v3" width="200"/>

##### -Pack de cables jumpers (hembra-hembra): Cables de conexión de la telemetría y alimentación de la Raspberry Pi a la caja

<img src="https://github.com/user-attachments/assets/80249896-b468-4a8c-9fd2-f39dd5329622" alt="Jumpers multicolores" width="200"/>

##### -Cables de telemetría y alimentación: Telemetria de la caja al dron y corriente de la placa distribuidora a la caja

<img src="https://github.com/user-attachments/assets/aa4d092c-e369-4873-82a9-f9cadcd2a1bc" alt="Cables de telemetría" width="200"/>
<img src="https://github.com/user-attachments/assets/c31ecad2-7ae4-4c17-a9e9-915a39595853" alt="Cables de alimentación" width="200"/>

##### -Base de metacrilato: Plataforma física para sujetar la Raspberry Pi y sus componentes al dron de forma segura.

<img src="https://github.com/user-attachments/assets/e4f0bc29-baaa-4b64-bd16-692582b4fb51" alt="Base de metacrilato" width="200"/>

##### -Adaptador Wifi - USB: Necesario para poder transferir archivos del dron a nuestro ordenador.

<img src="https://github.com/user-attachments/assets/1572776b-de14-447d-a7ce-1bceaf22b843" alt="Adaptador Wifi USB" width="200"/>

##### -Cable micro-HDMI a HDMI: Utilizado durante la configuración de la Raspberry Pi.

<img src="https://github.com/user-attachments/assets/8d1c718a-55af-4f0c-a93a-bd02de2b3f0d" alt="Cable HDMI" width="200"/>

##### -Fuente de alimentación para Raspberry Pi 4: Utilizada durante la configuración de la Raspberry Pi.

<img src="https://github.com/user-attachments/assets/c642dde2-360f-4e9f-80ad-4cb124fff369d" alt="Fuente de alimentación" width="200"/>

## Versión final del dron con los componente añadidos

<img src="https://github.com/user-attachments/assets/fbf150c5-6253-432d-8082-509fbf09e381" alt="Dron montado y operativo (fase final)" width="400"/>
<img src="https://github.com/user-attachments/assets/ae78d7fb-7f92-4261-8bc8-204cb59eda9e" alt="Dron montado y operativo (fase final)" width="400"/>

## Configuración de la Raspberry Pi

Para poder utilizar la Raspberry Pi a bordo del dron, primero debemos configurarla correctamente con el sistema operativo, acceso remoto y los paquetes necesarios para poder trabajar con la cámara, la telemetría y otros módulos.

A continuación, se detallan los pasos necesarios:

### 1. Instalación del sistema operativo (Raspberry Pi OS)

El sistema operativo se instala en una tarjeta microSD, que luego insertaremos en la Raspberry Pi. Para ello, es necesario conectar la microSD al ordenador mediante un adaptador o lector de tarjetas. A continuación, se debe acceder a la página oficial de Raspberry Pi (https://www.raspberrypi.com/software/) y descargar la herramienta Raspberry Pi Imager, que facilita el proceso de instalación.

<img src="https://github.com/user-attachments/assets/fcf1a1b8-dc7a-446b-9558-396f94dd6b82" alt="Lector tarjetas" width="400"/>
<img src="https://github.com/user-attachments/assets/cefea9ee-5cfb-47dd-a62c-c1a3cc6e338e" alt="Raspberry Pi Imager" width="400"/>

Una vez abierta la aplicación, se selecciona el modelo de Raspberry Pi (en este caso, la Raspberry Pi 4), el sistema operativo Raspberry Pi OS (64 bits), y finalmente la unidad correspondiente a la microSD conectada. Al continuar, la aplicación preguntará si se desea realizar alguna configuración previa, pero en este momento seleccionamos “No”, ya que todos los ajustes necesarios los haremos manualmente más adelante.

<img src="https://github.com/user-attachments/assets/a0273919-176d-4916-b571-3eeaaa23c6c7" alt="Tipo Rasp" width="400"/>
<img src="https://github.com/user-attachments/assets/4be6af39-739c-4ff0-a5f8-54961269862e" alt="Tipo Sis" width="400"/>

Una vez todo esté listo, se pulsa el botón "Escribir" y comienza el proceso de instalación del sistema operativo en la tarjeta. Cuando finalice, se retira la microSD con seguridad. A continuación, ya podemos proceder a insertar la tarjeta en la Raspberry Pi y realizar la primera configuración.

<img src="https://github.com/user-attachments/assets/d6f6f40c-b32c-4b59-96ce-71f3300c2778" alt="Poner SD" width="400"/>

### 2. Consfiguración de "RasPi OS"

Para poder continuar con la configuración inicial, es necesario conectar la Raspberry Pi a un monitor mediante un cable micro-HDMI a HDMI, un teclado USB, un ratón USB, y por supuesto, a una fuente de alimentación.

Al encender la Raspberry Pi por primera vez, se iniciará un asistente de configuración. En él, seleccionaremos el país, idioma y zona horaria, y crearemos un usuario y contraseña. Es importante anotar estos datos, ya que los necesitaremos más adelante para acceder al sistema o conectarnos remotamente.

Cuando se ofrezca la opción de conectarse a una red Wi-Fi, la saltaremos seleccionando “Skip”, ya que la conexión se configurará más adelante. También se nos pedirá elegir un navegador predeterminado.

Finalmente, la Raspberry Pi intentará actualizarse, pero al no tener internet, fallará. No pasa nada: tras completar estos pasos, el sistema se reiniciará y mostrará la pantalla de inicio.

<img src="https://github.com/user-attachments/assets/38d066fe-6830-4908-be79-8648584714b5" alt="Escritorio" width="400"/>

### 3. Configuración de las conexiones a Internet

La Raspberry Pi puede conectarse a Internet por cable Ethernet, pero en este proyecto **no utilizaremos esa opción**. En su lugar, configuraremos **dos conexiones Wi-Fi** distintas:

1. **Conexión Wi-Fi interna (cliente):** Esta es la tarjeta Wi-Fi integrada de la Raspberry Pi. Se usará para conectarse a una red Wi-Fi existente (en nuestro caso, `dronsEETAC`), lo que permitirá a la Raspberry Pi **tener acceso a Internet**, algo que no es necesario pero ayuda durante la configuración.

2. **Conexión Wi-Fi externa (hotspot):** Para esta función, conectaremos un **adaptador Wi-Fi USB** a uno de los puertos disponibles. Este adaptador se configurará como un **punto de acceso (hotspot)**, de forma que otros dispositivos (como un portátil) puedan conectarse directamente a la Raspberry Pi a través de esta red. Esto será útil, por ejemplo, para **acceder por SSH** a la Raspberry Pi sin necesidad de conexión a internet externa mediante aplicaciones como PuTTY.

#### Configuración de la conexión Wi-Fi interna

Para comenzar, abrimos la configuración de redes desde el icono Wi-Fi. Veremos que hay **dos interfaces disponibles**:

- `Broadcom BCM43438` → Es la Wi-Fi interna. La usaremos para conectarnos a una red ya existente como `dronsEETAC`.

- `Ralink RT5370` → Es el adaptador USB. Funciona directamente al conectarlo, ya que el driver está incluido en el sistema operativo. Si se usara otro modelo, puede que se necesite instalar controladores adicionales.

<img src="https://github.com/user-attachments/assets/25cf25dd-06e5-4624-8832-7f78f25fcdc9" alt="Redes" width="500"/>

#### Configuración del hotspot (punto de acceso)

En la interfaz del adaptador USB, creamos una red nueva que funcionará como **punto de acceso Wi-Fi**. Esta red será el canal de comunicación directa entre nuestro portátil y la Raspberry Pi. Le pondremos un nombre que queramos, en este caso `MiHotSpot`.

<img src="https://github.com/user-attachments/assets/49b3b151-e889-4512-930f-ebc07456d504" alt="HotSpot" width="500"/>
<img src="https://github.com/user-attachments/assets/c1ed9758-0d0a-43cd-a342-ae61e5b5f226" alt="HotSpot" width="500"/>
<img src="https://github.com/user-attachments/assets/8b404162-7c4e-40e2-9443-a531ae97390d" alt="HotSpot" width="500"/>

#### Activar el hotspot al inicio

Para que el punto de acceso se active automáticamente al encender la Raspberry Pi:

1. Haz clic en el icono de Wi-Fi y selecciona **Advanced Options**.
2. Abre **Editar conexiones**.
3. Doble clic en la red `MiHotSpot`.
4. En la pestaña **General**, activa la opción de conexión automática al arrancar.

<img src="https://github.com/user-attachments/assets/96c4bb51-72df-446a-adf4-cded8ad2a66d" alt="HotSpot" width="500"/>
<img src="https://github.com/user-attachments/assets/51df7874-a557-4e3d-8a46-8a72c2adf88d" alt="HotSpot" width="500"/>

#### Comprobación de IPs

Una vez configurado todo, comprueba que ambas conexiones están activas y tienen IP asignada.

- Especialmente importante es la IP del hotspot (por defecto suele ser `10.42.0.1`), ya que será la IP a la que te conectarás desde tu portátil para usar **SSH**.
  
<img src="https://github.com/user-attachments/assets/089653c9-0f98-414c-af13-c616725064de" alt="HotSpot" width="500"/>

### 4. Conexión con la Raspberry Pi via SSH con el HotSpot

Para poder acceder a la Raspberry Pi desde un ordenador u otro dispositivo, primero es necesario activar el servicio SSH en la propia RPi.

#### Activar SSH en la Raspberry Pi

1. Abre una terminal en la Raspberry Pi.
2. Ejecuta el siguiente comando:

   ```bash
   sudo raspi-config

3. En el menú que aparece, navega por las siguientes opciones: Interfacing Options → SSH → Enable

<img src="https://github.com/user-attachments/assets/8bf7ef17-91ae-4e44-b012-b85a2e1a42cb" alt="SSH" width="500"/>
<img src="https://github.com/user-attachments/assets/48a39e25-44fc-4762-86c7-d321646a5063" alt="SSH" width="500"/>

4. Confirma y sal del menú. A partir de ahora la Raspberry Pi aceptará conexiones remotas vía SSH.

#### Conexión desde otro dispositivo

Ahora debemos conectarnos a la red Wi-Fi generada por la Raspberry Pi (MiHotSpot). Una vez conectados, podemos acceder por SSH desde nuestro ordenador.

Para hacer esto utilizaremos PuTTY. Si no tienes PuTTY instalado, puedes descargarlo desde: https://putty.org/

1. Abre PuTTY.
2. En el campo Host Name (or IP address), escribe la dirección IP del hotspot de la Raspberry Pi (10.42.0.1). Asegúrate de que el puerto esté en 22 y que el protocolo seleccionado sea SSH. Haz clic en Open.

<img src="https://github.com/user-attachments/assets/360a6f6f-ffe1-4a3e-ae1c-e2dd871232bd" alt="SSH" width="350"/>

   En caso de no funcionar abre una terminal y escribe el comando `ipconfig`. Este te dira a que IP estas conectado

3. Introduce el nombre de usuario y contraseña que creaste durante la configuración inicial.

<img src="https://github.com/user-attachments/assets/5451b694-b124-4735-8d48-b7d2d9770106" alt="SSH" width="350"/>

Una vez conectado mediante SSH a la Raspberry Pi, puedes ejecutar comandos directamente en ella desde tu ordenador, **sin necesidad de usar un monitor, teclado o ratón conectados físicamente** a la Raspberry

#### Compartir archivos mediante SSH

Otra herramienta útil es **WinSCP**, que permite **transferir archivos** entre tu ordenador y la Raspberry Pi utilizando el mismo acceso SSH. Es especialmente útil para **descargar las fotos o vídeos capturados durante el vuelo** o subir scripts directamente a la RPi. Puedes descargarlo desde: https://winscp.net/eng/download.php

Para conectarte, simplemente introduce los mismos datos que en el PuTTY. Una vez conectado, verás una interfaz de doble panel para arrastrar y soltar archivos entre ambos dispositivos.

<img src="https://github.com/user-attachments/assets/0faacd05-78e8-4f1c-814c-dbfd5828e06d" alt="SSH" width="350"/>

### 5. Conexión UART entre la Raspberry Pi y el Autopiloto

Para que la Raspberry Pi pueda comunicarse con el autopiloto (Cube Orange), es necesario conectarla físicamente a uno de sus puertos serie, y así permitir la comunicación mediante el protocolo UART. Esta conexión permitirá que la RPi envíe comandos y reciba datos del autopiloto durante el vuelo. Este protocolo es relativamente simple, solo se necesitan dos 3 cables, dos para la conexión de transmision y recepcion y un tercero para el ground.

<img src="https://github.com/user-attachments/assets/79e232a9-3cf4-445f-bac9-b16a34d50768" alt="Uart" width="500"/>

El autopiloto dispone de varios puertos de comunicación en la Carrier Board. Utilizaremos el puerto TELEM2, que funciona bajo el protocolo UART y está pensado para la conexión de periféricos como la RPi.

<img src="https://github.com/user-attachments/assets/780ef244-0fc9-497f-b980-863efb7efda1" alt="Uart" width="150"/>
<img src="https://github.com/user-attachments/assets/95138fe3-2e0e-4f06-8205-1f1b501900b3" alt="Uart" width="500"/>

Los pines que se han utilizado han sido el 2 (Tx), el 3 (Rx) y el 6 (Gnd) sabiendo que el pin 1 es el primero empezando desde la izquierda.

#### Coonexión entre Raspberry Pi y caja

Para establecer la comunicación entre la Raspberry Pi y el autopiloto (a través del puerto TELEM2), se utiliza un conector de 6 pines, aunque solo emplearemos 3 de ellos: TX, RX y GND. Este tipo de conector es el que se utiliza comúnmente para cables de telemetría.

Para realizar la conexión física, se utilizan cables jumper hembra-hembra, que permiten enlazar directamente los pines del conector de 6 pines con los pines GPIO de la Raspberry Pi.

<img src="https://github.com/user-attachments/assets/e33d0019-db07-4a11-ae5d-9d0631305fe4" alt="Uart" width="400"/>
<img src="https://github.com/user-attachments/assets/752a532e-6f50-4e38-a8f4-039382777573" alt="Uart" width="500"/>

 ##### Pines Raspberry Pi:
- Pin 6 → GND
- Pin 8 → TX (GPIO14)
- Pin 10 → RX (GPIO15)

##### Pines conector: Dado que el conector tiene 6 pines y solo necesitamos 3, usamos un multímetro para identificar cuáles corresponden a:
- Pin 2 del TELEM2 → TX
- Pin 3 del TELEM2 → RX
- Pin 6 del TELEM2 → GND

<img src="https://github.com/user-attachments/assets/065aa86b-a6c9-4158-818c-000ea5ef17a2" alt="Uart" width="500"/>

Una vez identificados, se conectan a los pines correspondientes de la Raspberry Pi utilizando los jumpers hembra-hembra, asegurando el cruce correcto de TX y RX:

- TX (autopiloto) → RX (RPi / Pin 10)
- RX (autopiloto) → TX (RPi / Pin 8)
- GND → GND (RPi / Pin 6)

#### Activar UART en la Raspberry Pi

Una vez establecida la conexión física entre el autopiloto y la Raspberry Pi mediante los pines UART (TX, RX y GND), es necesario activar la interfaz UART por software. De forma predeterminada, el puerto serie de la Raspberry Pi no está habilitado para comunicación con otros dispositivos, ya que puede estar reservado para la consola del sistema.

Activar el UART permitirá que la Raspberry Pi envíe y reciba datos al autopiloto a través del puerto `/dev/serial0`, lo cual es esencial para la telemetría y la comunicación bidireccional.

1. Abre la configuración de la Raspberry Pi con:

   ```bash
   sudo raspi-config

2. Navega a: Interface Options → Serial Port
3. A las preguntas que aparecen, responde lo siguiente:
   - ¿Quieres que la consola use el puerto serie? → No
   - ¿Quieres habilitar la interfaz serie? → Sí
4. Finalmente, reinicia la Raspberry Pi para aplicar los cambios:

   ```bash
   sudo reboot

<img src="https://github.com/user-attachments/assets/bb30533a-2d86-432b-a80e-b132c35ba86c" alt="UART" width="300"/>
<img src="https://github.com/user-attachments/assets/50a2b7f7-d6b5-4b71-b983-78bddae9b92f" alt="UART" width="300"/>
<img src="https://github.com/user-attachments/assets/b045f50e-5c70-46dd-96cc-188fa3946920" alt="UART" width="300"/>

Una vez reiniciada, la Raspberry Pi debería tener habilitada la comunicación UART a través del puerto `/dev/serial0`, lo que permitiría el intercambio de datos con el autopiloto.

Sin embargo, en nuestro caso experimentamos problemas persistentes de permisos en este puerto. A pesar de múltiples intentos de solución (modificando permisos, añadiendo el usuario al grupo `dialout`, verificando servicios activos, etc.), ninguna de las acciones parecía resolver el problema. Esto nos hizo perder bastante tiempo durante el desarrollo.

Curiosamente, tras varios intentos y reinicios, el error dejó de aparecer de forma aparentemente espontánea, y la conexión entre la Raspberry Pi y el dron comenzó a funcionar correctamente. No se pudo identificar con certeza cuál fue la solución definitiva, por lo que se recomienda paciencia y revisar cuidadosamente la configuración en caso de experimentar este mismo error.
