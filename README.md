TimeLapseMachine
================

Raspberry pi Timelapse Machine

*  Raspberry pi - model - B - 8gb SD Card -  Running Raspbian 
*  Raspi-Camera http://www.raspberrypi.org/product/camera-module/ 
*  1 Nano USB flash drive - 8gb
*  1 Sony 5000mah portable charger - podria se cualquier bateria que te de 5v a mas de 1amp
*  1 tapper - like sandwich box 
*  1 modulo wifi like this http://www.adafruit.com/products/814 (en mi caso use un linksys y lo compile)


El sistema esta montado así:

* Instalar RaspBian

En raspbian active un servicio ssh

* sudo apt-get install ssh
* sudo /etc/init.d/ssh start 
* sudo update-rc.d ssh defaults

adicionalmente instale un servidor Samba (opcional) 
* http://theurbanpenguin.com/wp/?p=2415

Configure el montaje automatico de la USB flash drive.
Configure el modulo wifi.

---------------------------------------------------

Una vez tenes todo esto listo y funcionado puedes acceder a la rasberry pi desde cualquier equipo conectado en la misma red local.

y aquí esta la novedad porque lo que hice fue usar las capacidades de los nuevos telefonos moviles para generar una red wifi.

* http://es.wikihow.com/utilizar-tu-tel%C3%A9fono-Android-como-zona-de-Wifi-port%C3%A1til-(Tethering)

posteriormente desde el raspberry acceder a esta red, de esta manera tienes conexión directa al raspberry desde tu celular. (guardas la IP o la pones estática).

y asi desde cualquier aplicación SSH para android (en mi caso use  

* https://play.google.com/store/apps/details?id=com.sonelli.juicessh

puedes conectarte a la raspberry y ejecutar script en python.


En mi caso programe un sistema de timelapse para que tomara fotos cada X cantidad de segundos
* https://github.com/mrzork/TimeLapseMachine/ 

es libre y puede mejorarse si te interesa.

Con este codigo pude lograr tomar las imagenes para este video:
* https://www.youtube.com/watch?v=GhMNeVCyBZA

pero podría ser cualquier script desde SSH.

el servidor Samba (opcional) te sera útil desde para ver el avance o las fotos tomadas por el script, desde un explorador de archivos de android cualquiera e inclusive desde otros computadores.

y la USB Flash Drive te sirve para guardar todas las tomas que realice el script, así solo debes apagar el raspberry pi y conectar la Flash Drive a tu PC para acceder a todas las Fotos.

