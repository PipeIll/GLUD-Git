# GLUD-Git

## Descripción

Plataforma web para coaches personales que permite:

* Registrar clientes
* Crear rutinas
* Asignar rutinas a clientes
* Registrar progreso (texto simple)
* Consultar el progreso de un cliente

La información se almacena en archivos JSON para mantener el proyecto simple y enfocado en lógica y colaboración.

---

## Tecnologías

* **Backend:** FastAPI
* **Servidor:** Uvicorn
* **Frontend:** HTML + CSS
* **Persistencia:** Archivos JSON (sin base de datos)

---

## Integrantes

* Juan Sebastian Garzon Beltran
* Adrian Felipe Aparicio Chaparro

---

## Estructura del Proyecto

```
GLUD-Git/
├── app/
│   ├── main.py
│   ├── utils.py
│   ├── data/
│   │   ├── clients.json
│   │   ├── routines.json
│   │   └── progress.json
│   └── routes/
│       ├── clients.py
│       ├── routines.py
│       └── progress.py
├── frontend/
│   ├── index.html
│   ├── clients.html
│   ├── routines.html
│   └── styles.css
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Requisitos

* Python 3.10 o superior
* pip
* Sistema operativo Linux/Mac/Windows

---

## Ejecución del Proyecto

```bash
# Clonar repositorio
git clone <URL_DEL_REPO>
cd GLUD-Git

# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
uvicorn app.main:app --reload
```

---

## Acceso a la API

Una vez ejecutado el servidor:

* API base:
  http://127.0.0.1:8000/

* Documentación interactiva (Swagger):
  http://127.0.0.1:8000/docs

---

## Endpoints

### Clientes

* `GET /clients` → Obtener lista de clientes
* `POST /clients` → Crear cliente

### Rutinas

* `GET /routines` → Obtener rutinas
* `POST /routines` → Crear rutina

### Progreso

* `POST /progress` → Registrar progreso
* `GET /progress/{client_id}` → Ver progreso de un cliente

---

## Almacenamiento

Los datos se almacenan en archivos JSON dentro de:

```
app/data/
```

* `clients.json`
* `routines.json`
* `progress.json`

---

## Flujo de Trabajo (Git)

Se utiliza:

* **Feature Branch Workflow**
* **Conventional Commits**

### Reglas:

* No hacer push directo a `main`
* Usar ramas tipo:

  * `feat/...`
  * `fix/...`
  * `chore/...`
* Todo cambio pasa por Pull Request (PR)

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.
