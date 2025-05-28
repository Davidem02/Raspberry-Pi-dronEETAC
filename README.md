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

##### -Cables de telemetría y alimentación: Conectados de la caja al dron

<img src="https://github.com/user-attachments/assets/aa4d092c-e369-4873-82a9-f9cadcd2a1bc" alt="Cables de telemetría y alimentación" width="200"/>
<img src="https://github.com/user-attachments/assets/c31ecad2-7ae4-4c17-a9e9-915a39595853" alt="Cables de telemetría y alimentación" width="200"/>

##### -Base de metacrilato: Plataforma física para sujetar la Raspberry Pi y sus componentes al dron de forma segura.

<img src="https://github.com/user-attachments/assets/e4f0bc29-baaa-4b64-bd16-692582b4fb51" alt="Base de metacrilato" width="200"/>

##### -Adaptador Wifi - USB: Necesario para poder transferir archivos del dron a nuestro ordenador.

<img src="https://github.com/user-attachments/assets/1572776b-de14-447d-a7ce-1bceaf22b843" alt="Adaptador Wifi USB" width="200"/>

##### -Cable micro-HDMI a HDMI: Utilizado durante la configuración de la Raspberry Pi.

<img src="https://github.com/user-attachments/assets/8d1c718a-55af-4f0c-a93a-bd02de2b3f0d" alt="Cable HDMI" width="200"/>

##### -Fuente de alimentación para Raspberry Pi 4: Utilizada durante la configuración de la Raspberry Pi.

<img src="https://github.com/user-attachments/assets/c642dde2-360f-4e9f-80ad-4cb124fff369d" alt="Fuente de alimentación" width="200"/>
