## PROGRAMACIÓN III - Proyecto Integrador (Python)
**Leyenda de Estados**:  
- ✅ **Completo**: Tarea finalizada y validada.  
- 🔍 **En pruebas**: En fase de testing/QA.  
- 🚧 **En progreso**: Desarrollo activo.  
- ⌛ **Pendiente**: Esperando recursos/aprobación.  
- 🗑️ **Eliminada**: Descarta (sin impacto en el sistema). 

### Estructura de Paquetes y Responsabilidad
**📌 Raiz: Contiene la clase principal Main, que es el punto de entrada del programa.** <br>
**📌 data: _DatabaseConnection_ → Maneja la conexión con la base de datos.** <br>
**📌 daos: Implementa el acceso a datos para distintas entidades del sistema (_ButacaDAO_, _CandyDAO_, _ClienteDAO_, etc.), facilitando consultas y persistencia.** <br>
**📌 domain/entities: Define las clases principales del dominio, como _Butaca_, _Cliente_, _Reserva_, _Sala_, etc., representando objetos de negocio.** <br>
**📌 domain/entities/types: Agrupa tipos específicos dentro del dominio, como _Ubicación_, _FormatoPelicula_, _TipoCandy_ y _TipoButaca_, proporcionando categorizaciones dentro del modelo.** <br>
**📌 services: Contiene clases como _Cine_services_ y _ServicioValidacion_, que encapsulan la lógica de negocio y validaciones dentro del sistema.** <br>


##  *Creación de Clases* 
| Clase                   | Paquete/Subpaquete    | Lenguaje/Herramientas | Asignado a        | Estado                                    |
|-------------------------|-----------------------|-----------------------|-------------------|-------------------------------------------|
| *Main*                  | Raiz                  | Python                | Lanatta, Wanda    | 🚀  **Pruebas completadas correctamente** |
| *DatabaseConnection*    | data                  | Python                | Quiroz, Ezequiel  | 🚀  **Pruebas completadas correctamente** |
| *ButacaDAO*             | daos                  | Python                | Aguilera, Mariana | 🚀  **Pruebas completadas correctamente** |
| *CandyDAO*              | daos                  | Python                | Mercado, Nicolas  | 🚀  **Pruebas completadas correctamente** |
| *ClienteDAO*            | daos                  | Python                | Aguilar, Melina   | 🚀  **Pruebas completadas correctamente** |
| *PeliculaDAO*           | daos                  | Python                | Atim, Mercedes    | 🚀  **Pruebas completadas correctamente** |
| *ReservaDAO*            | daos                  | Python                | Ríos Garín, Ana   | 🚀  **Pruebas completadas correctamente** |
| *SalaDAO*               | daos                  | Python                | Quiroz, Ezequiel  | 🚀  **Pruebas completadas correctamente** |
| *DetalleCandyDAO*       | daos                  | Python                | Lanatta, Wanda    | 🚀  **Pruebas completadas correctamente** |
| *DetalleReservaDAO*     | daos                  | Python                | Quiroz, Ezequiel  | 🚀  **Pruebas completadas correctamente** |
| *Butaca*                | domain/entities       | Python                | Ríos Garín, Ana   | 🚀  **Pruebas completadas correctamente** |
| *Candy*                 | domain/entities       | Python                | Aguilera, Mariana | 🚀  **Pruebas completadas correctamente** |
| *Cliente*               | domain/entities       | Python                | Aguilar, Melina   | 🚀  **Pruebas completadas correctamente** |
| *Pelicula*              | domain/entities       | Python                | Mercado, Nicolas  | 🚀  **Pruebas completadas correctamente** |
| *Reserva*               | domain/entities       | Python                | Ríos Garín, Ana   | 🚀  **Pruebas completadas correctamente** |
| *Sala*                  | domain/entities       | Python                | Quiroz, Ezequiel  | 🚀  **Pruebas completadas correctamente** |
| *Ubicación*             | domain/entities/types | Python                | Aguilar, Melina   | 🚀  **Pruebas completadas correctamente** |
| *FormatoPelicula*       | domain/entities/types | Python                | Ríos Garín, Ana   | 🚀  **Pruebas completadas correctamente** |
| *TipoCandy*             | domain/entities/types | Python                | Lanatta, Wanda    | 🚀  **Pruebas completadas correctamente** |
| *TipoButaca*            | domain/entities/types | Python                | Aguilera, Mariana | 🚀  **Pruebas completadas correctamente** |
| *Cine_services*         | services              | Python                | Atim, Mercedes    | 🚀  **Pruebas completadas correctamente** |
| *ServicioValidacion*    | services              | Python                | Atim, Mercedes    | 🚀  **Pruebas completadas correctamente** |


##  *Bases de Datos* 
| Clase                   | Lenguaje/Herramientas | Gestor             | Asignado a        | Estado             |
|-------------------------|-----------------------|--------------------|-------------------|--------------------|
| *butaca*                | SQL                   | PostgreSQL         | Aguilera, Mariana | ✅ **Operativo**  |
| *candy*                 | SQL                   | PostgreSQL         | Mercado, Nicolás  | ✅ **Operativo**  |
| *cliente*               | SQL                   | PostgreSQL         | Aguilar, Melina   | ✅ **Operativo**  |
| *pelicula*              | SQL                   | PostgreSQL         | Mercado, Nicolás  | ✅ **Operativo**  |
| *reserva*               | SQL                   | PostgreSQL         | Ríos Garín, Ana   | ✅ **Operativo**  |
| *sala*                  | SQL                   | PostgreSQL         | Quiroz, Ezequiel  | ✅ **Operativo**  |
| *detalle_candy*         | SQL                   | PostgreSQL         | Lanatta, Wanda    | ✅ **Operativo**  |
| *detalle_reserva*       | SQL                   | PostgreSQL         | Quiroz, Ezequiel  | ✅ **Operativo**  |

## Diagrama de entidad-relacion:

![image](https://github.com/user-attachments/assets/8a0e441d-82d3-4afc-b59b-cb651025f17d)
