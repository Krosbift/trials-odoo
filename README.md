# 🚀 trials-odoo: Repositorio para practicar Odoo

## ⚠️ **Antes de cualquier cosa, recuerda que debes estar en la carpeta raíz de Odoo**

## 🛠️ Comando para iniciar Odoo local con módulos personalizados

### 🔧 Parámetros del comando:
- **`-r`**: Usuario de la base de datos.
- **`-w`**: Contraseña del usuario.
- **`-d`**: Nombre de la base de datos.
- **`--addons-path`**: Directorios de addons separados por comas.  
    **Por defecto**: `./odoo/addons,./addons,./custom/trials-odoo/custom_addons`.
- **`-i`**: Módulo a instalar o reiniciar *(opcional)*.
- **`-u`**: Módulo a actualizar *(opcional, solo para módulos personalizados)*.

---

### 🐧 En Linux:
```bash
python3 odoo -r "<usuario>" -w "<contraseña>" -d "<base_de_datos>" --addons-path=<path> -i "<modulo>"
```

### 🪟 En Windows:
```shell
python odoo -r "<usuario>" -w "<contraseña>" -d "<base_de_datos>" --addons-path=<path> -i "<modulo>"
```

---

## 🧩 Comando para crear un nuevo módulo

### 📄 Descripción:
Este comando genera un nuevo módulo dentro de la estructura de Odoo.

---

### 🐧 En Linux:
```bash
python3 odoo-bin scaffold <nombre_del_modulo> <ruta_destino>
```

### 🪟 En Windows:
```shell
python .\odoo-bin scaffold <nombre_del_modulo> <ruta_destino>
```

---

### 📌 Parámetros:
- **`<nombre_del_modulo>`**: Nombre del módulo a crear.
- **`<ruta_destino>`**: Carpeta donde se generará el módulo.

---

### 🎯 Ejemplo:
#### Crear un módulo llamado `mi_modulo` en la carpeta `custom_addons`:
```bash
python3 odoo-bin scaffold mi_modulo custom/trials-odoo/custom_addons
```

---

✨ **Recuerda activar el modo desarrollador en Odoo. ¡Listo para empezar a programar!** ✨