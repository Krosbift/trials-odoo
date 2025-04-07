# 🚀 trials-odoo: Repositorio para practicar Odoo y saber de que se basa el framework

<p align="center">
    <img src="https://www.globalteckz.com/wp-content/uploads/2019/03/ODOO-APPS-COMMUNITY-APPS-ODOO-PAID-APPS-ODOO-ENTERPRISE-MODULES-ODOO-MODULES.jpg" alt="Odoo ERP" width="800px">
</p>

## 🌟 ¿Qué es Odoo?

Odoo es un software de gestión empresarial de código abierto que integra una amplia gama de aplicaciones para cubrir las necesidades de cualquier negocio. Estas aplicaciones incluyen módulos para contabilidad, ventas, inventario, recursos humanos, marketing, fabricación, entre otros.

### 🧩 ¿Para qué sirve?

Odoo permite a las empresas automatizar y optimizar sus procesos internos, mejorando la eficiencia y reduciendo costos. Su arquitectura modular y personalizable lo hace ideal para adaptarse a negocios de cualquier tamaño y sector. Además, al ser de código abierto, ofrece flexibilidad para desarrollar soluciones específicas según las necesidades de cada organización.

---

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiD64WpD56v7YtVOwdH9pUjGKQUolNe3YTxg&s" alt="Odoo Framework" width="800px">
</p>

## ⚠️ Antes de cualquier cosa, recuerda que debes estar en la carpeta raíz de Odoo para poder desarrollar

## 🛠️ Comando para iniciar Odoo local con módulos personalizados

### 🔧 Parámetros del comando:

- **`-r`**: Usuario de la base de datos.
- **`-w`**: Contraseña del usuario que ingresaste.
- **`-d`**: Nombre de la base de datos.
- **`--addons-path`**: Directorios de addons separados por comas.  
   **Valor por defecto**: `addons,odoo/addons,custom/<nombre del repositorio>/custom_addons`.
- **`-i`**: Módulo a instalar o reiniciar _(opcional)_.
- **`-u`**: Módulo a actualizar _(opcional, solo cuando se estén usando módulos personalizados)_.

---

### 🐧 En Linux:

#### Preparación en Arch Linux:

Antes de ejecutar Odoo en Arch Linux, necesitas configurar el entorno:

1. Instala Python 3.11 y crea un entorno virtual:

```bash
python3.11 -m venv venv
```

2. Instala las dependencias necesarias:

```bash
sudo pacman -S openldap cyrus-sasl gcc make python-virtualenv python-devel
```

3. Activa el entorno virtual:

```bash
source venv/bin/activate
```

#### Ejecución:

```bash
python3 odoo-bin -r "<usuario>" -w "<contraseña>" -d "<base_de_datos>" --addons-path=<path> -i "<modulo>"
```

### 🪟 En Windows:

```shell
python odoo-bin -r "<usuario>" -w "<contraseña>" -d "<base_de_datos>" --addons-path=<path> -i "<modulo>"
```

<p align="center">
    <img src="https://startel.cl/wp-content/uploads/2022/12/desarrollar-un-modulo-en-Odoo.png" alt="Odoo Module" width="800px">
</p>

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

# 📦 Estructura de un Módulo de Odoo

Este repositorio contiene un módulo para Odoo, diseñado con una arquitectura clara y extensible. Aquí encontrarás una explicación detallada de cada carpeta y archivo, para que desarrolladores de todos los niveles puedan entender cómo funciona y cómo extenderlo.

---

## 📁 Estructura General

```
mi_modulo/
├── controllers/
│   ├── __init__.py
│   └── main.py
├── models/
│   ├── __init__.py
│   └── producto.py
├── views/
│   ├── producto_view.xml
│   └── menu_view.xml
├── data/
│   ├── secuencia_producto.xml
│   └── categorias.xml
├── security/
│   ├── ir.model.access.csv
│   └── reglas_acceso.xml
├── static/
│   ├── description/
│   │   └── icon.png
│   └── src/
│       ├── css/
│       │   └── estilos.css
│       ├── js/
│       │   └── funciones.js
│       └── img/
│           └── banner.jpg
├── report/
│   ├── producto_reporte.xml
│   └── plantilla_reporte_producto.xml
├── wizards/
│   ├── __init__.py
│   └── generar_informe_wizard.py
├── tests/
│   ├── __init__.py
│   └── test_producto.py
├── i18n/
│   └── es.po
├── demo/
│   └── demo_productos.xml
├── __init__.py
├── __manifest__.py
```

---

## 🧠 Archivos raíz

- **`__init__.py`**  
  Inicializa el módulo en Python. Aquí se importan los paquetes principales (`models`, `controllers`, etc.).

  📌 _Ejemplo:_

  ```python
  from . import models
  from . import controllers
  ```

- **`__manifest__.py`**  
  Define los metadatos del módulo: nombre, versión, categoría, dependencias, vistas, reglas de acceso, etc.

  📌 _Ejemplo:_

  ```python
  {
      'name': 'Gestión de Inventario Avanzada',
      'version': '1.0',
      'author': 'Tu Empresa',
      'depends': ['base', 'stock'],
      'data': [
          'views/inventario_view.xml',
          'security/ir.model.access.csv'
      ],
      'application': True,
      'installable': True,
  }
  ```

---

## 📂 controllers/

Contiene los controladores web del módulo. Se utilizan para exponer rutas HTTP (usualmente públicas o para el frontend).

📌 _Ejemplo:_

```python
from odoo import http

class MyController(http.Controller):
    @http.route('/mi_ruta', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('mi_modulo.template_id', {})
```

---

## 📂 models/

Aquí se definen los modelos de datos (clases que heredan de `models.Model`). Es el corazón del backend funcional de Odoo.

📌 _Ejemplo:_

```python
from odoo import models, fields

class ProductoPersonalizado(models.Model):
    _name = 'mi_modulo.producto'
    _description = 'Producto personalizado'

    name = fields.Char(string='Nombre')
    precio = fields.Float(string='Precio')
```

---

## 📂 views/

Define las vistas XML: formularios, listas (tree), kanban, calendarios, menús, acciones, etc.

📌 _Ejemplo:_

```xml
<record id="view_form_producto" model="ir.ui.view">
  <field name="name">producto.form</field>
  <field name="model">mi_modulo.producto</field>
  <field name="arch" type="xml">
    <form>
      <sheet>
        <group>
          <field name="name"/>
          <field name="precio"/>
        </group>
      </sheet>
    </form>
  </field>
</record>
```

---

## 📂 data/

Contiene datos de configuración o iniciales (por ejemplo, secuencias, categorías, reglas de negocio). Se cargan automáticamente con el módulo.

📌 _Ejemplo:_

```xml
<record id="grupo_ventas" model="res.groups">
  <field name="name">Grupo de Ventas</field>
</record>
```

---

## 📂 security/

Incluye la configuración de permisos de acceso.

- `ir.model.access.csv`: define quién puede leer/escribir modelos.
- Reglas (`ir.rule`): definen filtros de acceso dinámico por usuario.

📌 _Ejemplo (CSV):_

```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
acceso_producto,acceso_producto,model_mi_modulo_producto,,1,1,1,0
```

---

## 📂 static/

Contiene archivos estáticos que se usan en el sitio web o backend.

- `description/`: imágenes utilizadas en el `__manifest__.py`.
- `src/`: JS, CSS, fuentes, etc.

📌 _Ejemplo de uso:_

```xml
<template id="assets_backend" name="Assets Backend" inherit_id="web.assets_backend">
  <xpath expr="." position="inside">
    <link rel="stylesheet" href="/mi_modulo/static/src/css/estilos.css"/>
  </xpath>
</template>
```

---

## 📂 report/

Define informes personalizados (PDF, HTML) usando QWeb y plantillas.

📌 _Ejemplo:_

```xml
<report
  id="mi_reporte"
  model="mi_modulo.producto"
  string="Reporte Producto"
  report_type="qweb-pdf"
  name="mi_modulo.reporte_producto_template"
/>
```

---

## 📂 wizards/

Define wizards, es decir, asistentes con formularios paso a paso para flujos complejos o temporales.

📌 _Ejemplo:_

```python
class GenerarInformeWizard(models.TransientModel):
    _name = 'mi_modulo.generar_informe_wizard'

    fecha_inicio = fields.Date()
    fecha_fin = fields.Date()
```

---

## 📂 tests/

Contiene pruebas unitarias y funcionales. Odoo usa `unittest`.

📌 _Ejemplo:_

```python
from odoo.tests.common import TransactionCase

class TestProducto(TransactionCase):
    def test_creacion_producto(self):
        producto = self.env['mi_modulo.producto'].create({'name': 'Test', 'precio': 100})
        self.assertEqual(producto.precio, 100)
```

---

## 📂 i18n/

Contiene archivos `.po` para la traducción de textos a múltiples idiomas.

📌 _Ejemplo de línea en `.po`:_

```
msgid "Precio"
msgstr "Price"
```

---

## 📂 demo/

Carga datos de demostración cuando el entorno está en modo demo. Útil para pruebas y presentación del módulo.

---

## ✅ Buenas prácticas

- Usa nombres de archivos y carpetas en minúsculas y con guiones bajos (snake_case).
- Mantén el código modular: cada modelo o controlador en su propio archivo.
- Documenta tus modelos y controladores con docstrings.
- Usa `@api.model`, `@api.depends`, etc., correctamente para aprovechar el ORM de Odoo.

---

<p align="center">
    <img src="https://st3.depositphotos.com/7865540/13899/i/450/depositphotos_138995344-stock-photo-concept-on-laptop-screen.jpg" alt="Odoo Docs" width="800px">
</p>

# 📚 Documentación para Desarrolladores de Odoo

Para obtener más información sobre cómo desarrollar en Odoo, consulta la [Documentación para Desarrolladores de Odoo](https://www.odoo.com/documentation/18.0/developer.html).

---

