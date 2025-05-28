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

