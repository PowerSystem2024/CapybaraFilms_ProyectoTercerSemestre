carpinchos_programando/
│
├── requirements.txt            # Listado de dependencias del proyecto
├── README.md                   # Documentación del proyecto
├── main.py                     # Archivo principal para ejecutar el programa
│
├── database_config/
│   ├── connection.py           # Configuración de conexión a PostgreSQL
│
├── domain/                     # Lógica principal del sistema
│   ├── entities/               # Clases que representan las entidades del sistema
│   │   ├── cliente.py          # Clase Cliente
│   │   ├── pelicula.py         # Clase Película
│   │   ├── sala.py             # Clase Sala
│   │   ├── butaca.py           # Clase Butaca
│   │   ├── reserva.py          # Clase Reserva
│   │   ├── candy.py            # Clase Combo/Candy
│   │   ├── catalogo.py         # Clase Catálogo
│   ├── services/               # Servicios del sistema (procesos de negocio)
│   │   ├── servicio_validacion.py  # Servicio de validación de datos
│   │   ├── servicio_compra.py      # Servicio de compra de entradas
│
├── test/                       # Pruebas del sistema
│   ├── test_cliente.py         # Pruebas para la clase Cliente
│   ├── test_reserva.py         # Pruebas para la clase Reserva
│   ├── test_compra.py          # Pruebas para los servicios de Compra
│
└── utils/                      # Utilidades comunes
    ├── helpers.py              # Funciones auxiliares (validaciones, formato, etc.)