# Guia per a la Integració d'una Raspberry Pi en un Dron

> ⚠️Aquesta guia **no està completa**, però proporciona una **bona base des d’on començar** i anar afegint funcionalitats a mesura que es desenvolupa el projecte.

Aquesta guia ofereix una base sòlida per començar a treballar amb una **Raspberry Pi integrada** en un dron, juntament amb un **mòdul de càmera**. El punt de partida és un dron ja muntat i funcional, com el que es mostra a la seguent imatge, capaç de volar tant de manera manual (amb emissora de ràdio) com automàtica mitjançant el programari **Mission Planner**.

<img src="https://github.com/user-attachments/assets/fe6e4731-297a-45f7-8bf2-ad365cc31fc6" alt="Dron muntat i operatiu (fase inicial)" width="500"/>

> ⚠️ **Aquesta guia no inclou el muntatge inicial del dron.** Es parteix d’una plataforma ja operativa. El focus està en la integració de nous components per ampliar-ne les funcionalitats. Guia de muntatge del dron: https://github.com/dronsEETAC/GuiaHexsoonEDU450.git

## Què es vol aconseguir

Amb aquesta integració, es busca aconseguir que el dron sigui capaç de:

- Capturar **imatges o vídeo** durant el vol.
- Executar **codi personalitzat** des de la Raspberry Pi sense dependre d’un ordinador extern.
- Fer un **mapatge bàsic del terreny** que sobrevola, combinant la imatge capturada amb la posició GPS del dron.
- Establir les bases per a aplicacions futures com la **detecció d’objectes**, el seguiment, o la presa de decisions autònoma en temps real.

## Material utilitzat

A continuació es mostra el material **extra** que s’ha afegit al dron per fer possible la integració de la Raspberry Pi i les funcionalitats de visió:

##### -Raspberry Pi 4 (amb caixa) 
<img src="https://github.com/user-attachments/assets/df4619ca-0362-4a6b-a28b-0b0860bf646e" alt="Raspberry Pi 4 amb caixa" width="200"/>

##### -Mòdul de càmera Raspberry Pi v3

<img src="https://github.com/user-attachments/assets/5f219733-a2a6-4440-935b-03d073141c90" alt="Mòdul càmera Raspberry Pi v3" width="200"/>

##### -Pack de cables jumpers (femella-femella): Cables de connexió de la telemetria i alimentació de la Raspberry Pi a la caixa

<img src="https://github.com/user-attachments/assets/80249896-b468-4a8c-9fd2-f39dd5329622" alt="Jumpers multicolors" width="200"/>

##### -Cables de telemetria i corrent: Conectats de la caixa a el dron

<img src="https://github.com/user-attachments/assets/aa4d092c-e369-4873-82a9-f9cadcd2a1bc" alt="Cables de telemetria i corrent" width="200"/>
<img src="https://github.com/user-attachments/assets/c31ecad2-7ae4-4c17-a9e9-915a39595853" alt="Cables de telemetria i corrent" width="200"/>

##### -Base de metacrilat: Plataforma física per subjectar la Raspberry Pi i els seus components al dron de manera segura.

<img src="https://github.com/user-attachments/assets/e4f0bc29-baaa-4b64-bd16-692582b4fb51" alt="Base de metacrilat" width="200"/>

##### -Adaptador Wifi - USB: Necessaria para poder pasar archivos de el dron a nuestro ordenador.

<img src="https://github.com/user-attachments/assets/1572776b-de14-447d-a7ce-1bceaf22b843" alt="Adaptador Wifi USB" width="200"/>

##### -Cable micro-HDMI a HDMI:  Utilitzat mentre es configuraba la Raspberry Pi.

<img src="https://github.com/user-attachments/assets/8d1c718a-55af-4f0c-a93a-bd02de2b3f0d" alt="Adaptador Wifi USB" width="200"/>

##### -Font alimentacio per a la Raspberry Pi 4: Utilitzat mentre es configuraba la Raspberry Pi.

<img src="https://github.com/user-attachments/assets/c642dde2-360f-4e9f-80ad-4cb124fff369d" alt="Adaptador Wifi USB" width="200"/>
