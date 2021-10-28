Source: https://www.youtube.com/watch?v=z_p8WxFGV5A, https://www.youtube.com/watch?v=HU0rq917P58

# Configuración inicial
Instalar el módulo gettext a partir del binario precompilado en https://mlocati.github.io/articles/gettext-iconv-windows.html

## Settings.py
En `/BCDSaliva/settings.py` a la lista de MIDDLEWARE añadir `"django.middleware.locale.LocaleMiddleware",` entre sessions y common, de modo que se vea así:
```python
...
"django.contrib.sessions.middleware.SessionMiddleware",
"django.middleware.locale.LocaleMiddleware",
"django.middleware.common.CommonMiddleware",
...
```

Añadir una lista con los idiomas que va a soportar la aplicación.
```python
from django.utils.translation import gettext_lazy as _
...
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)
```

Indicar dónde está el folder de locale
```python
import os
...
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
```

## Creación de archivos
Crea las carpetas para cada idioma `/locale/en ; /locale/es`

## Views.py
Añadir `from django.utils.translation import gettext as _` y `from django.utils.translation import get_language, activate`.

# Seleccionar cadenas que traducir

Se tiene que definir un nuevo alias para la función gettext(). La convención es que el alias sea "_" por facilidad de escritura. Así, en cada lugar que quieras marcar un texto que se debe traducir se debe incluir `from django.utils.translation import gettext as _`. Ejemplo: `messages.info(request, _("Username or password is incorrect"))`.

# Generar archivos de traducción

Ya que seleccionaste algunas cadenas que se deben traducir, hay que crear el archivo donde se realizan las traducciones. En la terminal ejecuta el siguiente comando:
`py manage.py makemessages --all`. En mi caso se tardó un rato corriendo así que no desesperes. El proceso va a generar unos archivos con extensión ".po" en las carpetas de idioma `/locale/en/LC_MESSAGES` y `/locale/es/LC_MESSAGES`. A partir de ahora ya podrías empezar a traducir todas las cadenas. Se recomienda traducir una o dos para que veas que sí vaya funcionando, pero instalaremos más adelante un paquete para hacer más facil o gráfico el proceso de la traducción.

## Compilar la traducción

En la terminal correr `py manage.py compilemessages`

# Traducir en templates

Primero se debe añadir el módulo de internacionalización al template donde quieres añadir un texto traducido: `{% load i18n %}`. Tras esto, puedes usar `{% translate "TEXTO" %}` para indicar el texto a traducir. Por ejemplo: `{% block title %} {% trans "About Us" %} {% endblock title %}`. Nota: se recomienda usar "translate", pero por compatibilidad usar "trans" también funciona, y es lo que se usará a lo largo de ésta guía.

# Cambiar de idioma dentro de la aplicación

Ahora necesitamos una forma de permitir a los usuarios cambiar el idioma de la página. En mi caso lo haré en mi barra de navegación pero se puede adaptar a la forma deseada.

```
<div class="dropdown-navbar">
            <li class="dropli-language">{% trans "Language" %}</li>
            
            <div class="dropdown-content">
                {% get_current_language as LANGUAGE_CODE %}
                {% get_available_languages as LANGUAGES %}
                {% get_language_info_list for LANGUAGES as languages %}

                {% for lang in languages %}
                    <a href="/{{ lang.code }}/BCDSaliva/">{{ lang.name_local|title }}</a>
                {% endfor %}

            </div>
            
    </div>
```

# Añadir idioma a la url

En el archivo `/BCDSaliva/urls.py` añadimos:

```python
from django.conf.urls.i18n import i18n_patterns
...
urlpatterns += i18n_patterns(
    path("", include("webpage.urls", namespace="webpage")),
)
```

Ahora en `/webpage/urls.py` se añade la linea `app_name = 'webpage'`

Si se te rompe todo y dice algo que el reverse falló, a todos tus urls vas a tener que cambiarlas por `{% url 'webpage:show-profile'`, nota que "webpage" es el namespace que asignamos anteriormente.