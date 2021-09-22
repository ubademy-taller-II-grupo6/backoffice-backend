Backoffice Backend - Ubademy

Ejecución de la app

    1 - Instalar Docker: https://docs.docker.com/engine/install/
    2 - Instalar Docker-Compose: https://docs.docker.com/compose/install/
    3 - Clonar el reporsitorio de git: https://github.com/ubademy-taller-II-grupo6/backoffice-backend.git
    4 - Chequear que se este ejecutando docker-compose. Para eso ejecutar el comando: docker-compose -v   
    5 - Posicionarse en la carpeta backoffice-backend y ejecutar el comando: docker-compose up

    En esta instancia el web server esta corriendo. Para verificarlo, ingresar al navegador web con la siguiente URL: http://localhost:8000/ 
    Se visualizara el mensaje de "Web Server UP"

    Ademas se encuentra corriendo el motor de base de datos postgres dockerizado. Al estar recien creado, hay que crear la base de datos y la tabla necesaria para poder pegarle a los endpoints (la aplicación tiene la configuración de la base de datos hardcodeada).

    6 - En una nueva terminal, ejecutar el comando: docker exec -tiu postgres psql-container psql

    7 - Una vez adentro del postgres (vas a tener el promt "posgrest=#") ejecutar el comando: CREATE DATABASE ubademy; (Esto creará tu base de datos "ubademy". Para verificarlo ejecutar el comando: "\l").

    8 - Una vez creada la base de datos, posicionarse dentro de ella. Para ello ejecutar el comando: \c ubademy 
    Una vez dentro de la base de datos "ubademy", ejecutar el comando: CREATE TABLE IF NOT EXISTS usuariobackoffice (idusuario VARCHAR (50) NOT NULL, contraseña VARCHAR (50) NOT NULL, nombre VARCHAR (50) NOT NULL, apellido VARCHAR (50) NOT NULL, email VARCHAR (50) NOT NULL, PRIMARY KEY (idusuario)); 
    Este comando crea la tabla "usuariobackoffice".

    9 - Abrir la aplicacion POSTMAN y ejecutar el metodo POST con el siguiente JSON en la URL: http://localhost:8000/usuario

    {
        "idusuario": "admin",
        "nombre": "Nelson",
        "apellido": "Ramos",
        "contraseña": "admin",
        "email": "nramos@fi.uba.ar"
    }

    10 - El metodo anterior graba el registro en la base de datos. (Se puede seguir agregando registros ejecutando el metodo POST, siempre y cuando se cambie el idusuario)

    11 - Para consultar los registro de la tabla, ejecutar el metodo GET con la siguiente URL: http://localhost:8000/usuario/{ACA VA EL ID USUARIO A CONSULTAR} 