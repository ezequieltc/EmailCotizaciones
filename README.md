# EmailCotizaciones
Programa para enviar cotizaciones a proveedores.

Programa diseñado para enviar cotizaciones a proveedores.

Problema: Se descubrió que se perdía aproximadamente entre 15 y 20 minutos por pedido de cotizaciones enviando emails de manera manual a los proveedores adjuntando archivos y especificaciones

Se decidió crear este programa para enviar automaticamente los pedidos a los proveedores del mismo tipo y pais. Por ejemplo: Si deseo enviar un email a todos los proveedores de motores en Argentina, el programa consulta en la base de datos quienes son los contactos que corresponden con proveedores de motores y que sean de Argentina.
De esta forma, el programa envia automaticamente el email de cotización a todos aquellos que cumplan con las configuraciones elegidas, adjuntando también los archivos necesarios en cada email.

El programa posee una interface gráfica muy sencilla realizada con PyQt5.

![image](https://user-images.githubusercontent.com/94491753/167318443-a9429f0c-bb2c-49db-8822-87722ade018b.png)

En la misma que puede ingresar el RFQ (número de pedido), el servicio donde va a estar operando el equipo, a que pais y que destinatarios (motores, sellos, acoples) deseo enviar el email. En el cuerpo del email se ingresa el texto que se desea enviar en el email.

Activando la casilla de "Adjuntar Archivos" se activa la opción "Elegir Archivos" que despliega un cuadro de dialogos para navegar a la ubicacion del o los archivos que se desean adjuntar

![image](https://user-images.githubusercontent.com/94491753/167318608-6ef18f1c-6e92-4d8b-b36a-aea01c99dd4f.png)

Una vez finalizada la configuración, se apreta en "Enviar" y el programa envia los email por medio del servidor SMPT configurado.
