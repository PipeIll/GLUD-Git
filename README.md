# GLUD-Git

**DESCRIPCIÓN**
Proyecto de una plataforma web para coaches personales. 
Permite registrar clientes, crear rutinas y hacer seguimiento básico.

La información se guarda en archivos JSON, sin base de datos, para mantener el proyecto simple.

**INTEGRANTES**
- Juan Sebastian Garzon Beltran
- Adrian Felipe Aparicio Chaparro

**FUNCIONALIDADES**

- Crear clientes
- Ver lista de clientes
- Crear rutinas
- Asignar rutina a cliente
- Registrar progreso (texto simple)
- Ver progreso de un cliente

**ESTRUCTURA DEL PROYECTO**

project/
│
├── app/
│   ├── main.py
│   ├── utils.py
│   │
│   ├── data/
│   │   ├── clients.json
│   │   ├── routines.json
│   │   └── progress.json
│   │
│   └── routes/
│       ├── clients.py
│       ├── routines.py
│       └── progress.py
│
├── frontend/
│   ├── index.html
│   ├── clients.html
│   ├── routines.html
│   └── styles.css
│
├── requirements.txt
├── .gitignore
└── README.md

**ALMACENAMIENTO**

Los datos se guardan en archivos .json:

- clients.json
- routines.json
- progress.json


**ENDPOINTS**

- Clientes:
GET /clients
POST /clients

- Rutinas:
GET /routines
POST /routines

- Progreso:
POST /progress
GET /progress/{client_id}
