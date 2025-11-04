# Canvas API Configuration
import os
from canvasapi import Canvas
from Key import USERS

# URL base de tu instancia de Canvas
CANVAS_URL = "https://canvas.unab.cl/"

# Variables globales
canvas = None
current_user_name = None
current_course_id = None

# Diccionario simple de unidades y semanas (retrocompatibilidad)
unidades = {
    "UNIDAD I: ELEMENTOS BÁSICOS": [1, 2],
    "UNIDAD II: PROGRAMACIÓN EN PYTHON": [3, 4, 5],
    "UNIDAD III: CONTROLADORES Y ARREGLOS": [6, 7, 8],
    "UNIDAD IV: EL CICLO FOR, GRÁFICAS": [9, 10],
    "UNIDAD V: CLASES & ANALISIS DE DATOS": [11, 12],
    "UNIDAD VI: ALGORITMOS, & PERFORMANCE": [13, 14, 15]
}

# Diccionario base con estructura completa y posiciones
def _generar_estructura_base():
    """
    Genera la estructura base completa del módulo con posiciones
    Retorna un diccionario con la jerarquía completa
    """
    estructura = {}
    posicion = 1
    
    for unidad_titulo, semanas_nums in unidades.items():
        estructura[unidad_titulo] = {
            'position': posicion,
            'indent': 0,
            'semanas': {}
        }
        posicion += 1
        
        for num_semana in semanas_nums:
            semana_str = f"{num_semana:02d}"
            semana_titulo = f"Semana {semana_str}"
            
            estructura[unidad_titulo]['semanas'][num_semana] = {
                'titulo': semana_titulo,
                'position': posicion,
                'indent': 1,
                'archivos': {}
            }
            posicion += 1
            
            # Agregar archivos P1 y P2
            for parte in ['P1', 'P2']:
                archivo_nombre = f"Semana{semana_str}-{parte}.pdf"
                estructura[unidad_titulo]['semanas'][num_semana]['archivos'][archivo_nombre] = {
                    'position': posicion,
                    'indent': 2
                }
                posicion += 1
    
    return estructura

def ver_estructura_base():
    """
    Muestra la estructura base completa con posiciones
    Útil para debugging y verificación
    """
    estructura = _generar_estructura_base()
    
    print("=" * 80)
    print("📚 ESTRUCTURA BASE DEL MÓDULO")
    print("=" * 80)
    
    for unidad_titulo, unidad_data in estructura.items():
        print(f"\n[{unidad_data['position']}] {unidad_titulo} (indent={unidad_data['indent']})")
        
        for num_semana, semana_data in unidad_data['semanas'].items():
            print(f"  [{semana_data['position']}] {semana_data['titulo']} (indent={semana_data['indent']})")
            
            for archivo_nombre, archivo_data in semana_data['archivos'].items():
                print(f"    [{archivo_data['position']}] {archivo_nombre} (indent={archivo_data['indent']})")
    
    print("\n" + "=" * 80)
    print(f"Total de items en estructura base: {sum(1 + len(u['semanas']) + sum(len(s['archivos']) for s in u['semanas'].values()) for u in estructura.values())}")
    print("=" * 80)

def select_user(nombre_usuario):
    """
    Selecciona y conecta con un usuario de Canvas
    
    Args:
        nombre_usuario: Nombre del usuario ("David", "Fabrizzio") o un token personalizado
    
    Returns:
        True si la conexión fue exitosa, False en caso contrario
    """
    global canvas, current_user_name, current_course_id
    
    # Verificar si es un usuario registrado o un token personalizado
    if nombre_usuario in USERS:
        token = USERS[nombre_usuario]
        # Obtener el ID del curso asociado al usuario
        course_id_key = f"{nombre_usuario}_id"
        current_course_id = USERS.get(course_id_key, None)
        print(f"✓ Usuario seleccionado: {nombre_usuario}")
        if current_course_id:
            print(f"✓ ID del curso asignado: {current_course_id}")
    else:
        # Asumir que es un token personalizado
        token = nombre_usuario
        nombre_usuario = "Usuario personalizado"
        current_course_id = None
        print("✓ Usando token personalizado")
        print("⚠ Deberás especificar el course_id al subir contenido")
    
    # Inicializar la conexión a Canvas
    try:
        canvas = Canvas(CANVAS_URL, token)
        user = canvas.get_current_user()
        current_user_name = user.name
        print(f"✓ Conectado como: {current_user_name}")
        return True
    except Exception as e:
        print(f"❌ Error al conectar con Canvas: {e}")
        canvas = None
        current_user_name = None
        current_course_id = None
        return False

def ver_cursos(filtro_codigo="2326"):
    """
    Muestra todos los cursos disponibles para el usuario conectado
    
    Args:
        filtro_codigo: Código para filtrar cursos (por defecto "2326")
                      Si es None o "", muestra todos los cursos
    
    Returns:
        Lista de cursos
    """
    if canvas is None:
        print("❌ Error: No hay conexión activa con Canvas")
        print("💡 Primero ejecuta: Canvas_Key.select_user('TuNombre')")
        return None
    
    print("=" * 70)
    print(f"📚 CURSOS DISPONIBLES PARA: {current_user_name}")
    if filtro_codigo:
        print(f"🔍 Filtro aplicado: '{filtro_codigo}'")
    print("=" * 70)
    
    try:
        courses = canvas.get_courses()
        curso_lista = []
        
        for course in courses:
            try:
                # Obtener información del curso
                course_name = course.name if hasattr(course, 'name') else 'Sin nombre'
                course_id = course.id if hasattr(course, 'id') else 'N/A'
                course_code = course.course_code if hasattr(course, 'course_code') else 'N/A'
                
                # Aplicar filtro si está especificado
                if filtro_codigo:
                    # Buscar el código en el nombre o en el course_code
                    if filtro_codigo not in course_name and filtro_codigo not in course_code:
                        continue
                
                print(f"\n📖 {course_name}")
                print(f"   ID: {course_id}")
                print(f"   Código: {course_code}")
                
                curso_lista.append({
                    'id': course_id,
                    'name': course_name,
                    'code': course_code,
                    'object': course
                })
            except Exception as e:
                print(f"   ⚠ Error al obtener detalles del curso: {e}")
                continue
        
        print("\n" + "=" * 70)
        print(f"Total de cursos encontrados: {len(curso_lista)}")
        print("=" * 70)
        
        return curso_lista
        
    except Exception as e:
        print(f"❌ Error al obtener cursos: {e}")
        return None

def ordenar_modulo(course_id=None, test_mode=False):
    """
    Ordena manualmente todas las unidades del módulo según el orden correcto
    
    Args:
        course_id: ID del curso en Canvas (si es None, usa el ID del usuario seleccionado)
        test_mode: Si True, ordena el módulo TEST en lugar del módulo principal
    
    Returns:
        True si se realizaron cambios, False si no
    """
    if canvas is None:
        print("❌ Error: No hay conexión activa con Canvas")
        print("💡 Primero ejecuta: Canvas_Key.select_user('TuNombre')")
        return None
    
    # Usar el course_id del usuario si no se especifica uno
    if course_id is None:
        if current_course_id is None:
            print("❌ Error: No hay un course_id asignado al usuario")
            print("💡 Especifica el course_id: Canvas_Key.ordenar_modulo(course_id=123456)")
            return None
        course_id = current_course_id
        print(f"📌 Usando course_id del usuario: {course_id}")

    
    # Nombre del módulo
    module_name = 'Material del curso'
    if test_mode:
        module_name += ' TEST'
    
    # Obtener el curso
    course = canvas.get_course(course_id)
    
    print("=" * 60)
    print(f"🔧 ORDENAMIENTO MANUAL DE MÓDULO")
    print(f"Curso ID: {course_id}")
    print(f"Módulo: {module_name}")
    print("=" * 60)
    
    # Buscar el módulo
    print("\n1. Buscando módulo...")
    main_module = None
    modules = course.get_modules()
    
    for module in modules:
        if module.name == module_name:
            print(f"  ✓ Módulo '{module.name}' encontrado (ID: {module.id})")
            main_module = module
            break
    
    if not main_module:
        print(f"  ❌ Módulo '{module_name}' no encontrado")
        return False
    
    # Llamar a la función de reordenamiento
    resultado = _reordenar_unidades(main_module, unidades)
    
    print("\n" + "=" * 60)
    if resultado:
        print("✅ Módulo ordenado correctamente")
    else:
        print("ℹ️ No se requirieron cambios")
    print("=" * 60)
    
    return resultado

def _reordenar_unidades(main_module, unidades_dict):
    """
    Reordena todas las unidades, semanas y archivos según la estructura base
    Usa las posiciones predefinidas del diccionario base
    
    Args:
        main_module: El módulo de Canvas a organizar
        unidades_dict: Diccionario simple de unidades (para compatibilidad)
    
    Returns:
        True si se realizaron cambios, False si no
    """
    print("\n🔄 Verificando y ordenando estructura completa...")
    
    # Generar estructura base con posiciones
    estructura_base = _generar_estructura_base()
    
    # Obtener todos los items del módulo
    items = list(main_module.get_module_items())
    
    if not items:
        print("  ℹ No hay items en el módulo")
        return False
    
    # Crear mapa de items actuales
    items_mapa = {}
    
    for item in items:
        if item.type == 'SubHeader':
            # Es una unidad o semana
            if item.indent == 0:
                # Es una unidad
                items_mapa[('unidad', item.title)] = item
            elif item.indent == 1:
                # Es una semana
                items_mapa[('semana', item.title)] = item
        elif item.indent == 2:
            # Es un archivo
            items_mapa[('archivo', item.title)] = item
    
    if not items_mapa:
        print("  ℹ No hay items para reordenar")
        return False
    
    # Verificar si hay cambios necesarios
    cambios_necesarios = False
    items_a_reposicionar = []
    
    print("  📋 Comparando estructura actual con estructura base...")
    
    # Recorrer estructura base y comparar posiciones
    for unidad_titulo, unidad_data in estructura_base.items():
        # Verificar unidad
        key_unidad = ('unidad', unidad_titulo)
        if key_unidad in items_mapa:
            item_actual = items_mapa[key_unidad]
            posicion_esperada = unidad_data['position']
            
            if item_actual.position != posicion_esperada:
                cambios_necesarios = True
                items_a_reposicionar.append((item_actual, posicion_esperada, f"Unidad: {unidad_titulo}"))
            
            # Verificar semanas de esta unidad
            for num_semana, semana_data in unidad_data['semanas'].items():
                key_semana = ('semana', semana_data['titulo'])
                if key_semana in items_mapa:
                    item_semana = items_mapa[key_semana]
                    posicion_esperada_semana = semana_data['position']
                    
                    if item_semana.position != posicion_esperada_semana:
                        cambios_necesarios = True
                        items_a_reposicionar.append((item_semana, posicion_esperada_semana, f"  Semana: {semana_data['titulo']}"))
                    
                    # Verificar archivos de esta semana
                    for archivo_nombre, archivo_data in semana_data['archivos'].items():
                        key_archivo = ('archivo', archivo_nombre)
                        if key_archivo in items_mapa:
                            item_archivo = items_mapa[key_archivo]
                            posicion_esperada_archivo = archivo_data['position']
                            
                            if item_archivo.position != posicion_esperada_archivo:
                                cambios_necesarios = True
                                items_a_reposicionar.append((item_archivo, posicion_esperada_archivo, f"    Archivo: {archivo_nombre}"))
    
    if not cambios_necesarios:
        print("  ✓ Todo está en el orden correcto según estructura base")
        return False
    
    # Aplicar reposicionamiento
    print(f"  🔧 Reposicionando {len(items_a_reposicionar)} items...")
    
    for item, nueva_posicion, descripcion in items_a_reposicionar:
        try:
            item.edit(module_item={'position': nueva_posicion})
            print(f"    ✓ {descripcion} → posición {nueva_posicion}")
        except Exception as e:
            print(f"    ✗ Error en {descripcion}: {e}")
    
    print("  ✓ Estructura completamente ordenada según base")
    return True

def subir_contenido(numero_semana, course_id=None, test_mode=False):
    """
    Sube contenido de una semana al curso de Canvas organizándolo por unidades
    Mantiene el orden correcto: Unidades → Semanas → Archivos
    
    Args:
        numero_semana: Número de la semana (1-15)
        course_id: ID del curso en Canvas (si es None, usa el ID del usuario seleccionado)
        test_mode: Si es False, publica el módulo automáticamente
    
    Returns:
        El módulo creado o actualizado
    """
    if canvas is None:
        print("❌ Error: No hay conexión activa con Canvas")
        print("💡 Primero ejecuta: Canvas_Key.select_user('TuNombre')")
        return None
    
    # Usar el course_id del usuario si no se especifica uno
    if course_id is None:
        if current_course_id is None:
            print("❌ Error: No hay un course_id asignado al usuario")
            print("💡 Especifica el course_id: Canvas_Key.subir_contenido(1, course_id=123456)")
            return None
        course_id = current_course_id
        print(f"📌 Usando course_id del usuario: {course_id}")
        
    # Encontrar a qué unidad pertenece la semana
    nombre_unidad = None
    for unidad, semanas in unidades.items():
        if numero_semana in semanas:
            nombre_unidad = unidad
            break
    
    if not nombre_unidad:
        print(f"❌ Error: La semana {numero_semana} no está asignada a ninguna unidad")
        return None
    
    # Formatear número de semana con ceros a la izquierda
    semana_str = f"{numero_semana:02d}"
    
    # Nombre del módulo principal
    module_name = 'Material del curso'
    if test_mode:
        module_name += ' TEST'
    
    # Obtener el curso
    course = canvas.get_course(course_id)
    
    print("=" * 60)
    print(f"Procesando: Semana {semana_str}")
    print(f"Unidad: {nombre_unidad}")
    print("=" * 60)
    
    # Buscar si existe el módulo "Material del curso"
    print("\n1. Verificando módulo principal...")
    main_module = None
    modules = course.get_modules()
    
    for module in modules:
        if module.name == module_name:
            print(f"  ✓ Módulo '{module.name}' encontrado (ID: {module.id})")
            main_module = module
            break
    
    # Si no existe, crear el módulo
    if not main_module:
        print(f"  ⚠ Módulo '{module_name}' no existe. Creando...")
        main_module = course.create_module(
            module={
                'name': module_name,
                'position': 1,
                'published': not test_mode
            }
        )
        print(f"  ✓ Módulo creado: {main_module.name} (ID: {main_module.id})")
    
    # Reordenar unidades si es necesario
    _reordenar_unidades(main_module, unidades)
    
    # Obtener todos los items actuales del módulo
    print("\n2. Analizando estructura actual del módulo...")
    items = list(main_module.get_module_items())
    
    # Encontrar o crear la posición de la unidad
    unidad_item = None
    unidad_position = None
    
    for idx, item in enumerate(items):
        if item.type == 'SubHeader' and item.title == nombre_unidad:
            unidad_item = item
            unidad_position = idx
            print(f"  ✓ Unidad '{nombre_unidad}' encontrada en posición {unidad_position}")
            break
    
    # Si la unidad no existe, encontrar dónde debe insertarse
    if not unidad_item:
        print(f"  ⚠ Unidad '{nombre_unidad}' no existe. Determinando posición...")
        
        # Encontrar la posición correcta basada en el orden de unidades
        unidades_list = list(unidades.keys())
        unidad_index = unidades_list.index(nombre_unidad)
        
        # Buscar la última unidad anterior que ya existe
        insert_position = 0
        for prev_unidad in unidades_list[:unidad_index]:
            for idx, item in enumerate(items):
                if item.type == 'SubHeader' and item.title == prev_unidad:
                    # Encontrar el final de esta unidad (siguiente unidad o final)
                    next_unidad_pos = len(items)
                    for j in range(idx + 1, len(items)):
                        if items[j].type == 'SubHeader' and items[j].indent == 0:
                            next_unidad_pos = j
                            break
                    insert_position = next_unidad_pos
        
        # Crear la unidad en la posición correcta
        unidad_item = main_module.create_module_item(
            module_item={
                'type': 'SubHeader',
                'title': nombre_unidad,
                'position': insert_position + 1,
                'published': not test_mode
            }
        )
        print(f"  ✓ Unidad agregada en posición {insert_position + 1}")
        
        # Actualizar la lista de items
        items = list(main_module.get_module_items())
        unidad_position = insert_position
    
    # Procesar la semana
    print(f"\n3. Procesando Semana {semana_str}...")
    semana_titulo = f'Semana {semana_str}'
    
    # Verificar si la semana ya existe y eliminarla junto con sus archivos
    items = list(main_module.get_module_items())
    items_to_delete = []
    
    for idx, item in enumerate(items):
        if item.type == 'SubHeader' and item.title == semana_titulo and item.indent == 1:
            print(f"  ⚠ Semana '{semana_titulo}' ya existe. Eliminando versión anterior...")
            items_to_delete.append(item)
            
            # Eliminar archivos asociados (los que tienen indent=2 después de esta semana)
            for j in range(idx + 1, len(items)):
                if items[j].indent == 2:
                    items_to_delete.append(items[j])
                elif items[j].type == 'SubHeader':
                    break
    
    # Eliminar items marcados
    for item in items_to_delete:
        item.delete()
        print(f"    ✓ Eliminado: {item.title}")
    
    # Actualizar lista de items después de eliminaciones
    items = list(main_module.get_module_items())
    
    # Encontrar la posición correcta para insertar la semana
    # Debe estar después de la unidad y antes de la siguiente unidad o semana mayor
    insert_position = len(items)  # Por defecto al final
    
    for idx, item in enumerate(items):
        if item.type == 'SubHeader' and item.title == nombre_unidad:
            # Buscar después de esta unidad
            for j in range(idx + 1, len(items)):
                current_item = items[j]
                
                # Si encontramos otra unidad (indent=0), insertar antes
                if current_item.type == 'SubHeader' and current_item.indent == 0:
                    insert_position = j
                    break
                
                # Si encontramos una semana posterior, insertar antes
                if current_item.type == 'SubHeader' and current_item.indent == 1:
                    # Verificar que sea un título de semana (comienza con "Semana")
                    if current_item.title.startswith('Semana'):
                        try:
                            current_semana_num = int(current_item.title.split()[-1])
                            if current_semana_num > numero_semana:
                                insert_position = j
                                break
                        except ValueError:
                            # Si no se puede convertir a número, ignorar
                            continue
            else:
                # No se encontró siguiente unidad ni semana mayor, insertar al final de esta unidad
                insert_position = len(items)
            break
    
    # Agregar título de la semana en la posición correcta
    main_module.create_module_item(
        module_item={
            'type': 'SubHeader',
            'title': semana_titulo,
            'indent': 1,
            'position': insert_position + 1,
            'published': not test_mode
        }
    )
    print(f"  ✓ Semana agregada en posición {insert_position + 1}")
    
    # Archivos a subir
    base_path = r"d:\5) Clases Programacion 1\Clase PCFI 161\pcfi161\lectures"
    files_to_upload = [
        os.path.join(base_path, f"Semana{semana_str}", f"Semana{semana_str}-P1.pdf"),
        os.path.join(base_path, f"Semana{semana_str}", f"Semana{semana_str}-P2.pdf")
    ]
    
    # Subir y agregar archivos
    print("\n4. Subiendo archivos...")
    uploaded_count = 0
    
    for file_path in files_to_upload:
        if os.path.exists(file_path):
            file_name = os.path.basename(file_path)
            print(f"  📄 Subiendo: {file_name}...")
            
            # Verificar si el archivo ya existe y eliminarlo
            existing_files = course.get_files()
            for existing_file in existing_files:
                if existing_file.display_name == file_name:
                    print(f"    ⚠ Archivo '{file_name}' ya existe. Eliminando...")
                    existing_file.delete()
            
            # Subir el archivo al curso
            uploaded_file = course.upload(file_path)
            print(f"    ✓ Archivo subido (ID: {uploaded_file[1]['id']})")
            
            # Agregar el archivo como item del módulo con indentación 2
            # Insertar después del título de la semana
            module_item = main_module.create_module_item(
                module_item={
                    'type': 'File',
                    'content_id': uploaded_file[1]['id'],
                    'title': file_name,
                    'indent': 2,
                    'position': insert_position + 2 + uploaded_count,
                    'published': not test_mode
                }
            )
            print(f"    ✓ Agregado al módulo: {module_item.title}")
            uploaded_count += 1
        else:
            print(f"  ✗ Archivo no encontrado: {file_path}")
    
    # Publicar el módulo si no es modo test
    if not test_mode:
        print("\n5. Publicando módulo...")
        main_module.edit(module={'published': True})
        print("  ✓ Módulo publicado")
    
    print("\n" + "=" * 60)
    print(f"✅ Proceso completado para Semana {semana_str}")
    print(f"   Unidad: {nombre_unidad}")
    print(f"   Archivos subidos: {uploaded_count}/{len(files_to_upload)}")
    print(f"   Estado: {'PUBLICADO' if not test_mode else 'NO PUBLICADO (TEST)'}")
    print("=" * 60)
    
    return main_module

def crear_modulo_solemne(numero_solemne, html_path=None, course_id=None, 
                         fecha_inicio=None, fecha_hasta=None, test_mode=False):
    """
    Crea o actualiza un solemne como Examen (Assignment) dentro del módulo "Solemnes"
    Organización: Solemnes -> Solemne 1, Solemne 2, Solemne 3... (exámenes)
    Los exámenes se crean en el grupo de calificaciones "Nota de presentación"
    
    Args:
        numero_solemne: Número del solemne (1, 2, 3, etc.)
        html_path: Ruta al archivo HTML (si es None, busca en Solemnes/Solemne {numero}.html)
        course_id: ID del curso en Canvas (si es None, usa el ID del usuario seleccionado)
        fecha_inicio: Fecha de disponibilidad en formato "DD-MM-YYYY HH:MM" (ej: "30-10-2025 14:00")
        fecha_hasta: Fecha de entrega en formato "DD-MM-YYYY HH:MM" (ej: "30-10-2025 15:40")
        test_mode: Si es True, no publica el módulo ni el examen
    
    Returns:
        El módulo principal "Solemnes"
    """
    if canvas is None:
        print("❌ Error: No hay conexión activa con Canvas")
        print("💡 Primero ejecuta: Canvas_Key.select_user('TuNombre')")
        return None
    
    # Usar el course_id del usuario si no se especifica uno
    if course_id is None:
        if current_course_id is None:
            print("❌ Error: No hay un course_id asignado al usuario")
            print("💡 Especifica el course_id: Canvas_Key.crear_modulo_solemne(1, course_id=123456)")
            return None
        course_id = current_course_id
        print(f"📌 Usando course_id del usuario: {course_id}")
    
    # Ruta por defecto del archivo HTML
    if html_path is None:
        base_path = r"d:\5) Clases Programacion 1\Clase PCFI 161\pcfi161\Solemnes"
        html_path = os.path.join(base_path, f"Solemne {numero_solemne}.html")
    
    # Verificar que el archivo HTML existe
    if not os.path.exists(html_path):
        print(f"❌ Error: Archivo HTML no encontrado: {html_path}")
        return None
    
    # Leer el contenido HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Obtener el curso
    course = canvas.get_course(course_id)
    
    print("=" * 60)
    print(f"📋 Creando/Actualizando Solemne {numero_solemne}")
    print(f"Curso ID: {course_id}")
    if fecha_inicio:
        print(f"📅 Disponible desde: {fecha_inicio}")
    if fecha_hasta:
        print(f"📅 Disponible hasta: {fecha_hasta}")
    print("=" * 60)
    
    # Buscar o crear el módulo principal "Solemnes"
    print("\n1. Verificando módulo principal 'Solemnes'...")
    solemnes_module = None
    modules = course.get_modules()
    
    for module in modules:
        if module.name == "Solemnes":
            print(f"  ✓ Módulo 'Solemnes' encontrado (ID: {module.id})")
            solemnes_module = module
            break
    
    # Parámetros básicos del módulo (sin fechas)
    module_params = {
        'name': 'Solemnes',
        'published': not test_mode
    }
    
    # Si no existe el módulo "Solemnes", crearlo
    if not solemnes_module:
        print("  ⚠ Módulo 'Solemnes' no existe. Creando...")
        solemnes_module = course.create_module(module=module_params)
        print(f"  ✓ Módulo 'Solemnes' creado (ID: {solemnes_module.id})")
    
    # Buscar o crear el grupo de calificaciones "Nota de presentación"
    print("\n2. Verificando grupo de calificaciones 'Nota de presentación'...")
    assignment_group = None
    assignment_groups = course.get_assignment_groups()
    
    for group in assignment_groups:
        if group.name == "Nota de presentación":
            print(f"  ✓ Grupo de calificaciones encontrado (ID: {group.id})")
            assignment_group = group
            break
    
    # Si no existe el grupo, crearlo
    if not assignment_group:
        print("  ⚠ Grupo 'Nota de presentación' no existe. Creando...")
        assignment_group = course.create_assignment_group(
            name="Nota de presentación",
            group_weight=0  # Peso del grupo (puedes ajustarlo)
        )
        print(f"  ✓ Grupo de calificaciones creado (ID: {assignment_group.id})")
    
    # Crear el examen (Assignment)
    print(f"\n3. Creando examen 'Solemne {numero_solemne}'...")
    assignment_title = f"Solemne {numero_solemne}"
    
    # Preparar parámetros del examen
    from datetime import datetime
    assignment_params = {
        'name': assignment_title,
        'description': html_content,
        'assignment_group_id': assignment_group.id,
        'submission_types': ['online_upload', 'online_text_entry'],  # Tipos de entrega
        'points_possible': 100,  # Puntos (ajústalo según necesites)
        'grading_type': 'points',
        'published': not test_mode
    }
    
    # Agregar fechas si se especificaron
    if fecha_inicio:
        try:
            unlock_at = datetime.strptime(fecha_inicio, "%d-%m-%Y %H:%M")
            assignment_params['unlock_at'] = unlock_at.isoformat()
            print(f"  📅 Fecha de disponibilidad: {fecha_inicio}")
        except ValueError:
            print("  ⚠ Formato de fecha_inicio incorrecto. Use: DD-MM-YYYY HH:MM")
    
    if fecha_hasta:
        try:
            due_at = datetime.strptime(fecha_hasta, "%d-%m-%Y %H:%M")
            assignment_params['due_at'] = due_at.isoformat()
            print(f"  📅 Fecha de entrega: {fecha_hasta}")
        except ValueError:
            print("  ⚠ Formato de fecha_hasta incorrecto. Use: DD-MM-YYYY HH:MM")
    
    # Verificar si el examen ya existe y eliminarlo
    try:
        existing_assignments = course.get_assignments()
        for assignment in existing_assignments:
            if assignment.name == assignment_title:
                print(f"  ⚠ Examen '{assignment_title}' ya existe. Eliminando...")
                assignment.delete()
                print("    ✓ Examen eliminado")
                break
    except Exception as e:
        print(f"  ℹ No se pudo verificar exámenes existentes: {e}")
    
    # Crear el nuevo examen
    try:
        assignment = course.create_assignment(assignment=assignment_params)
        print(f"  ✓ Examen creado: {assignment.name} (ID: {assignment.id})")
    except Exception as e:
        print(f"  ❌ Error al crear el examen: {e}")
        return None
    
    # Buscar y subir el archivo PDF del solemne si existe
    print(f"\n4. Buscando archivo PDF del Solemne {numero_solemne}...")
    pdf_path = os.path.join(base_path, f"Solemne {numero_solemne}.pdf")
    
    if os.path.exists(pdf_path):
        print(f"  ✓ Archivo PDF encontrado: {os.path.basename(pdf_path)}")
        
        # Verificar si el archivo ya existe en Canvas y eliminarlo
        try:
            existing_files = course.get_files()
            pdf_filename = f"Solemne {numero_solemne}.pdf"
            for existing_file in existing_files:
                if existing_file.display_name == pdf_filename:
                    print(f"  ⚠ Archivo '{pdf_filename}' ya existe en Canvas. Eliminando...")
                    existing_file.delete()
                    print(f"    ✓ Archivo eliminado")
                    break
        except Exception as e:
            print(f"  ℹ No se pudo verificar archivos existentes: {e}")
        
        # Subir el archivo PDF a Canvas
        try:
            print(f"  📤 Subiendo PDF a Canvas...")
            uploaded_file = course.upload(pdf_path)
            file_id = uploaded_file[1]['id']
            print(f"  ✓ PDF subido exitosamente (ID: {file_id})")
            
            # Aplicar restricciones al archivo PDF
            # ESTRATEGIA: Usar la API de Canvas para actualizar propiedades del archivo
            # El archivo se ocultará y se aplicarán las fechas de disponibilidad
            try:
                # Construir parámetros para actualizar el archivo
                file_update_params = {
                    'hidden': True,              # Ocultar el archivo
                    'locked': True,              # Bloquear el archivo
                }
                
                # Agregar fechas si fueron especificadas
                if fecha_inicio:
                    file_update_params['unlock_at'] = assignment_params.get('unlock_at')
                    print(f"  📅 Aplicando fecha de disponibilidad al PDF: {fecha_inicio}")
                
                if fecha_hasta:
                    file_update_params['lock_at'] = assignment_params.get('due_at')
                    print(f"  📅 Aplicando fecha de bloqueo al PDF: {fecha_hasta}")
                
                # Actualizar el archivo usando la API directamente
                # Canvas API: PUT /api/v1/files/:id
                import requests
                headers = {
                    'Authorization': f'Bearer {canvas._Canvas__requester.access_token}'
                }
                file_url = f"{CANVAS_URL}api/v1/files/{file_id}"
                
                response = requests.put(file_url, headers=headers, json=file_update_params)
                
                if response.status_code == 200:
                    print(f"  ✓ Archivo PDF configurado como oculto con fechas de disponibilidad")
                    
                    # Verificar configuración
                    file_data = response.json()
                    print(f"  ℹ Verificación - Hidden: {file_data.get('hidden')}, Locked: {file_data.get('locked')}")
                    if file_data.get('unlock_at'):
                        print(f"  ℹ Disponible desde: {file_data.get('unlock_at')}")
                    if file_data.get('lock_at'):
                        print(f"  ℹ Se bloquea el: {file_data.get('lock_at')}")
                else:
                    print(f"  ⚠ Error al actualizar archivo (código {response.status_code}): {response.text}")
                
            except Exception as e:
                print(f"  ⚠ Error al aplicar restricciones al PDF: {e}")
                import traceback
                print(f"  Detalles: {traceback.format_exc()}")
            
            # Adjuntar el PDF al examen usando la API
            # Actualizar el HTML para incluir un enlace al PDF
            file_url = f"/courses/{course_id}/files/{file_id}/download"
            html_with_pdf = html_content + f"""
<hr style="margin:2rem 0;">
<div style="background:#f5f5f5;padding:1rem;border-radius:4px;text-align:center;">
    <p style="margin-bottom:0.5rem;font-weight:600;">📄 Documento del Solemne</p>
    <a href="{file_url}" class="Button Button--primary" download>
        <i class="icon-download"></i> Descargar PDF del Solemne {numero_solemne}
    </a>
</div>
"""
            
            # Actualizar la descripción del examen con el enlace al PDF
            try:
                assignment.edit(assignment={'description': html_with_pdf})
                print(f"  ✓ Enlace al PDF agregado a la descripción del examen")
            except Exception as e:
                print(f"  ⚠ No se pudo actualizar la descripción: {e}")
            
        except Exception as e:
            print(f"  ❌ Error al subir el PDF: {e}")
    else:
        print(f"  ⚠ Archivo PDF no encontrado: {pdf_path}")
        print(f"  ℹ El examen se creará sin el archivo PDF adjunto")
    
    # Buscar si el examen ya existe como item del módulo y eliminarla
    print("\n5. Verificando items existentes del módulo...")
    items = list(solemnes_module.get_module_items())
    
    for item in items:
        if item.type == 'Assignment' and item.title == assignment_title:
            print(f"  ⚠ Item '{assignment_title}' ya existe en el módulo. Eliminando...")
            item.delete()
            print("    ✓ Item eliminado")
            break
    
    # Actualizar lista después de eliminaciones
    items = list(solemnes_module.get_module_items())
    
    # Determinar la posición correcta (ordenar por número de solemne)
    insert_position = len(items)  # Por defecto al final
    
    for idx, item in enumerate(items):
        if item.type == 'Assignment' and item.title.startswith('Solemne '):
            try:
                current_solemne_num = int(item.title.split()[-1])
                if current_solemne_num > numero_solemne:
                    insert_position = idx
                    break
            except ValueError:
                continue
    
    # Determinar indentación: Solemnes sin indent (0)
    indent_value = 0 
    
    # Preparar parámetros del item
    module_item_params = {
        'type': 'Assignment',
        'content_id': assignment.id,
        'title': assignment_title,
        'indent': indent_value,
        'position': insert_position + 1,
        'published': not test_mode
    }
    
    # Agregar el examen al módulo
    print(f"\n6. Agregando examen al módulo en posición {insert_position + 1} (indent={indent_value})...")
    try:
        module_item = solemnes_module.create_module_item(module_item=module_item_params)
        print(f"  ✓ Examen agregado al módulo: {module_item.title}")
            
    except Exception as e:
        print(f"  ❌ Error al agregar examen al módulo: {e}")
        return None
    
    # Publicar el módulo si no es modo test
    if not test_mode:
        print("\n7. Publicando módulo...")
        solemnes_module.edit(module={'published': True})
        print("  ✓ Módulo publicado")
    
    print("\n" + "=" * 60)
    print(f"✅ Solemne {numero_solemne} creado/actualizado exitosamente")
    print(f"   Tipo: Examen (Assignment)")
    print(f"   Grupo de calificaciones: Nota de presentación")
    print(f"   Puntos posibles: 100")
    print(f"   Estado: {'PUBLICADO' if not test_mode else 'NO PUBLICADO (TEST)'}")
    if fecha_inicio:
        print(f"   Disponible desde: {fecha_inicio}")
    if fecha_hasta:
        print(f"   Fecha de entrega: {fecha_hasta}")
    print("=" * 60)
    
    return solemnes_module

def actualizar_fechas_solemne(numero_solemne, course_id=None, 
                               fecha_inicio=None, fecha_hasta=None):
    """
    Actualiza las fechas de disponibilidad de un solemne específico
    NOTA: En Canvas, para controlar la disponibilidad individual de páginas dentro de un módulo,
    necesitamos usar las fechas del módulo. Esta función recrea el solemne con las nuevas fechas.
    
    Args:
        numero_solemne: Número del solemne (1, 2, 3, etc.)
        course_id: ID del curso en Canvas (si es None, usa el ID del usuario seleccionado)
        fecha_inicio: Fecha de inicio en formato "DD-MM-YYYY HH:MM"
        fecha_hasta: Fecha de término en formato "DD-MM-YYYY HH:MM"
    
    Returns:
        True si se actualizó correctamente, False en caso contrario
    """
    if canvas is None:
        print("❌ Error: No hay conexión activa con Canvas")
        return False
    
    if course_id is None:
        if current_course_id is None:
            print("❌ Error: No hay un course_id asignado al usuario")
            return False
        course_id = current_course_id
    
    print(f"🔄 Actualizando fechas de 'Solemne {numero_solemne}'...")
    print("💡 NOTA: Las fechas se aplican recreando el solemne con las nuevas fechas")
    
    # Buscar el archivo HTML del solemne
    base_path = r"d:\5) Clases Programacion 1\Clase PCFI 161\pcfi161\Solemnes"
    html_path = os.path.join(base_path, f"Solemne {numero_solemne}.html")
    
    if not os.path.exists(html_path):
        print(f"❌ Archivo HTML no encontrado: {html_path}")
        return False
    
    # Recrear el solemne con las nuevas fechas usando la función principal
    try:
        resultado = crear_modulo_solemne(
            numero_solemne=numero_solemne,
            html_path=html_path,
            course_id=course_id,
            fecha_inicio=fecha_inicio,
            fecha_hasta=fecha_hasta,
            test_mode=False
        )
        
        if resultado:
            print(f"✅ Fechas de Solemne {numero_solemne} actualizadas correctamente")
            return True
        else:
            print(f"❌ Error al actualizar fechas de Solemne {numero_solemne}")
            return False
            
    except Exception as e:
        print(f"❌ Error al actualizar fechas: {e}")
        return False

def estado_solemnes(course_id=None):
    """
    Muestra el estado completo del módulo "Solemnes" y todos sus items
    Incluye información de publicación, fechas de disponibilidad y entrega
    
    Args:
        course_id: ID del curso en Canvas (si es None, usa el ID del usuario seleccionado)
    
    Returns:
        Diccionario con información del módulo y sus items
    
    Ejemplo:
        Canvas_Key.estado_solemnes()
    """
    if canvas is None:
        print("❌ Error: No hay conexión activa con Canvas")
        print("💡 Primero ejecuta: Canvas_Key.select_user('TuNombre')")
        return None
    
    # Usar el course_id del usuario si no se especifica uno
    if course_id is None:
        if current_course_id is None:
            print("❌ Error: No hay un course_id asignado al usuario")
            print("💡 Especifica el course_id: Canvas_Key.estado_solemnes(course_id=123456)")
            return None
        course_id = current_course_id
        print(f"📌 Usando course_id del usuario: {course_id}")
    
    # Obtener el curso
    course = canvas.get_course(course_id)
    
    print("=" * 80)
    print("📊 ESTADO DEL MÓDULO SOLEMNES")
    print("=" * 80)
    
    # Buscar el módulo "Solemnes"
    print("\n1. Buscando módulo 'Solemnes'...")
    solemnes_module = None
    modules = course.get_modules()
    
    for module in modules:
        if module.name == "Solemnes":
            solemnes_module = module
            break
    
    if not solemnes_module:
        print("  ❌ Módulo 'Solemnes' no encontrado")
        print("\n💡 Crea el módulo usando:")
        print("   Canvas_Key.crear_modulo_solemne(numero_solemne=1)")
        return None
    
    # Información del módulo
    print(f"  ✓ Módulo encontrado (ID: {solemnes_module.id})")
    print(f"\n📦 INFORMACIÓN DEL MÓDULO:")
    print(f"   Nombre: {solemnes_module.name}")
    print(f"   ID: {solemnes_module.id}")
    print(f"   Posición: {solemnes_module.position}")
    
    # Estado de publicación
    published_icon = "✅" if solemnes_module.published else "❌"
    print(f"   Publicado: {published_icon} {solemnes_module.published}")
    
    # Fechas del módulo
    unlock_at = getattr(solemnes_module, 'unlock_at', None)
    lock_at = getattr(solemnes_module, 'lock_at', None)
    
    if unlock_at:
        from datetime import datetime
        try:
            unlock_date = datetime.fromisoformat(unlock_at.replace('Z', '+00:00'))
            print(f"   📅 Fecha de desbloqueo: {unlock_date.strftime('%d-%m-%Y %H:%M')}")
        except:
            print(f"   📅 Fecha de desbloqueo: {unlock_at}")
    else:
        print(f"   📅 Fecha de desbloqueo: Sin restricción")
    
    if lock_at:
        from datetime import datetime
        try:
            lock_date = datetime.fromisoformat(lock_at.replace('Z', '+00:00'))
            print(f"   📅 Fecha de bloqueo: {lock_date.strftime('%d-%m-%Y %H:%M')}")
        except:
            print(f"   📅 Fecha de bloqueo: {lock_at}")
    else:
        print(f"   📅 Fecha de bloqueo: Sin restricción")
    
    # Obtener items del módulo
    print(f"\n2. Analizando items del módulo...")
    try:
        items = list(solemnes_module.get_module_items())
        
        if not items:
            print("  ⚠ El módulo no tiene items")
            return {
                'module': {
                    'id': solemnes_module.id,
                    'name': solemnes_module.name,
                    'published': solemnes_module.published,
                    'position': solemnes_module.position,
                    'unlock_at': unlock_at,
                    'lock_at': lock_at
                },
                'items': []
            }
        
        print(f"\n📋 ITEMS DEL MÓDULO ({len(items)} total):")
        print("=" * 80)
        
        items_info = []
        
        for idx, item in enumerate(items, 1):
            print(f"\n[{idx}] {item.title}")
            print(f"    ID: {item.id}")
            print(f"    Tipo: {item.type}")
            
            # Estado de publicación del item
            item_published = getattr(item, 'published', None)
            if item_published is not None:
                pub_icon = "✅" if item_published else "❌"
                print(f"    Publicado: {pub_icon} {item_published}")
            else:
                print(f"    Publicado: N/A")
            
            print(f"    Posición: {item.position}")
            print(f"    Indent: {item.indent}")
            
            # Si es un Assignment (examen), obtener más detalles
            if item.type == 'Assignment':
                content_id = getattr(item, 'content_id', None)
                if content_id:
                    try:
                        assignment = course.get_assignment(content_id)
                        
                        # Información adicional del examen
                        print(f"\n    📝 DETALLES DEL EXAMEN:")
                        print(f"       Puntos: {getattr(assignment, 'points_possible', 'N/A')}")
                        
                        # Grupo de calificaciones
                        assignment_group_id = getattr(assignment, 'assignment_group_id', None)
                        if assignment_group_id:
                            try:
                                group = course.get_assignment_group(assignment_group_id)
                                print(f"       Grupo: {group.name}")
                            except:
                                print(f"       Grupo ID: {assignment_group_id}")
                        
                        # Fechas del examen
                        unlock_at_assign = getattr(assignment, 'unlock_at', None)
                        due_at = getattr(assignment, 'due_at', None)
                        lock_at_assign = getattr(assignment, 'lock_at', None)
                        
                        from datetime import datetime
                        
                        if unlock_at_assign:
                            try:
                                unlock_date = datetime.fromisoformat(unlock_at_assign.replace('Z', '+00:00'))
                                print(f"       📅 Disponible desde: {unlock_date.strftime('%d-%m-%Y %H:%M')}")
                            except:
                                print(f"       📅 Disponible desde: {unlock_at_assign}")
                        else:
                            print(f"       📅 Disponible desde: Sin restricción")
                        
                        if due_at:
                            try:
                                due_date = datetime.fromisoformat(due_at.replace('Z', '+00:00'))
                                print(f"       📅 Fecha de entrega: {due_date.strftime('%d-%m-%Y %H:%M')}")
                            except:
                                print(f"       📅 Fecha de entrega: {due_at}")
                        else:
                            print(f"       📅 Fecha de entrega: Sin fecha límite")
                        
                        if lock_at_assign:
                            try:
                                lock_date = datetime.fromisoformat(lock_at_assign.replace('Z', '+00:00'))
                                print(f"       📅 Se cierra el: {lock_date.strftime('%d-%m-%Y %H:%M')}")
                            except:
                                print(f"       📅 Se cierra el: {lock_at_assign}")
                        
                        # Tipos de entrega
                        submission_types = getattr(assignment, 'submission_types', [])
                        if submission_types:
                            print(f"       Tipos de entrega: {', '.join(submission_types)}")
                        
                        items_info.append({
                            'id': item.id,
                            'title': item.title,
                            'type': item.type,
                            'published': item_published,
                            'position': item.position,
                            'assignment_id': content_id,
                            'points_possible': getattr(assignment, 'points_possible', None),
                            'unlock_at': unlock_at_assign,
                            'due_at': due_at,
                            'lock_at': lock_at_assign
                        })
                        
                    except Exception as e:
                        print(f"       ⚠ No se pudieron obtener detalles del examen: {e}")
                        items_info.append({
                            'id': item.id,
                            'title': item.title,
                            'type': item.type,
                            'published': item_published,
                            'position': item.position
                        })
            else:
                # Para otros tipos de items
                items_info.append({
                    'id': item.id,
                    'title': item.title,
                    'type': item.type,
                    'published': item_published,
                    'position': item.position
                })
        
        print("\n" + "=" * 80)
        print(f"✅ Análisis completado - {len(items)} items encontrados")
        print("=" * 80)
        
        return {
            'module': {
                'id': solemnes_module.id,
                'name': solemnes_module.name,
                'published': solemnes_module.published,
                'position': solemnes_module.position,
                'unlock_at': unlock_at,
                'lock_at': lock_at
            },
            'items': items_info
        }
        
    except Exception as e:
        print(f"  ❌ Error al obtener items del módulo: {e}")
        return None

def mover_modulo(module_id, nueva_posicion=None, nuevo_nombre=None, publicado=None, course_id=None):
    """
    Modifica un módulo: cambia su posición, nombre y/o estado de publicación
    
    Args:
        module_id: ID del módulo a modificar (obtenido con ver_modulos())
        nueva_posicion: Nueva posición del módulo (1, 2, 3, etc.) - Opcional
        nuevo_nombre: Nuevo nombre del módulo - Opcional
        publicado: Estado de publicación (True/False) - Opcional
        course_id: ID del curso en Canvas (si es None, usa el ID del usuario seleccionado)
    
    Returns:
        True si se modificó correctamente, False en caso contrario
    
    Ejemplos:
        # Solo mover posición
        Canvas_Key.mover_modulo(module_id=1454673, nueva_posicion=10)
        
        # Cambiar nombre
        Canvas_Key.mover_modulo(module_id=1454673, nuevo_nombre="Evaluaciones")
        
        # Cambiar estado de publicación
        Canvas_Key.mover_modulo(module_id=1454673, publicado=True)
        
        # Cambiar múltiples propiedades
        Canvas_Key.mover_modulo(module_id=1454673, nueva_posicion=5, nuevo_nombre="Solemnes 2025", publicado=True)
    """
    if canvas is None:
        print("❌ Error: No hay conexión activa con Canvas")
        print("💡 Primero ejecuta: Canvas_Key.select_user('TuNombre')")
        return False
    
    # Validar que al menos un parámetro de cambio esté presente
    if nueva_posicion is None and nuevo_nombre is None and publicado is None:
        print("❌ Error: Debes especificar al menos un cambio (nueva_posicion, nuevo_nombre o publicado)")
        print("💡 Ejemplo: Canvas_Key.mover_modulo(module_id=123, nueva_posicion=5)")
        return False
    
    # Usar el course_id del usuario si no se especifica uno
    if course_id is None:
        if current_course_id is None:
            print("❌ Error: No hay un course_id asignado al usuario")
            print("💡 Especifica el course_id: Canvas_Key.mover_modulo(module_id=123, nueva_posicion=1, course_id=123456)")
            return False
        course_id = current_course_id
        print(f"📌 Usando course_id del usuario: {course_id}")
    
    # Obtener el curso
    course = canvas.get_course(course_id)
    
    print("=" * 60)
    print(f"� MODIFICANDO MÓDULO")
    print(f"Curso ID: {course_id}")
    print(f"Módulo ID: {module_id}")
    print("=" * 60)
    
    # Buscar el módulo
    print("\n1. Buscando módulo...")
    try:
        target_module = course.get_module(module_id)
        print(f"  ✓ Módulo encontrado: '{target_module.name}'")
        print(f"    Posición actual: {target_module.position}")
        print(f"    Publicado actual: {target_module.published}")
    except Exception as e:
        print(f"  ❌ Error: No se pudo encontrar el módulo con ID {module_id}")
        print(f"     Detalles: {e}")
        print("\n💡 Usa Canvas_Key.ver_modulos() para ver todos los módulos disponibles")
        return False
    
    # Preparar los cambios
    print("\n2. Preparando cambios...")
    cambios = {}
    
    if nueva_posicion is not None:
        cambios['position'] = nueva_posicion
        print(f"  • Posición: {target_module.position} → {nueva_posicion}")
    
    if nuevo_nombre is not None:
        cambios['name'] = nuevo_nombre
        print(f"  • Nombre: '{target_module.name}' → '{nuevo_nombre}'")
    
    if publicado is not None:
        cambios['published'] = publicado
        pub_actual = "Publicado" if target_module.published else "No publicado"
        pub_nuevo = "Publicado" if publicado else "No publicado"
        print(f"  • Estado: {pub_actual} → {pub_nuevo}")
    
    # Aplicar los cambios
    print("\n3. Aplicando cambios...")
    try:
        target_module.edit(module=cambios)
        print(f"  ✓ Cambios aplicados exitosamente")
        
        # Verificar los cambios
        updated_module = course.get_module(module_id)
        print("\n4. Verificando cambios...")
        print(f"  ✓ Nombre actual: {updated_module.name}")
        print(f"  ✓ Posición actual: {updated_module.position}")
        print(f"  ✓ Publicado actual: {updated_module.published}")
        
    except Exception as e:
        print(f"  ❌ Error al modificar el módulo: {e}")
        return False
    
    print("\n" + "=" * 60)
    print(f"✅ Módulo modificado exitosamente")
    print("=" * 60)
    
    return True

def ver_contenido_modulo(module_id, course_id=None):
    """
    Muestra el contenido detallado de un módulo específico
    
    Args:
        module_id: ID del módulo a inspeccionar
        course_id: ID del curso en Canvas (si es None, usa el ID del usuario seleccionado)
    
    Returns:
        Lista de diccionarios con información de los items del módulo
    
    Ejemplo:
        Canvas_Key.ver_contenido_modulo(module_id=1454673)
    """
    if canvas is None:
        print("❌ Error: No hay conexión activa con Canvas")
        print("💡 Primero ejecuta: Canvas_Key.select_user('TuNombre')")
        return None
    
    # Usar el course_id del usuario si no se especifica uno
    if course_id is None:
        if current_course_id is None:
            print("❌ Error: No hay un course_id asignado al usuario")
            print("💡 Especifica el course_id: Canvas_Key.ver_contenido_modulo(module_id=123, course_id=123456)")
            return None
        course_id = current_course_id
        print(f"📌 Usando course_id del usuario: {course_id}")
    
    # Obtener el curso
    course = canvas.get_course(course_id)
    
    # Buscar el módulo
    try:
        module = course.get_module(module_id)
    except Exception as e:
        print(f"❌ Error: No se pudo encontrar el módulo con ID {module_id}")
        print(f"   Detalles: {e}")
        print("\n💡 Usa Canvas_Key.ver_modulos() para ver todos los módulos disponibles")
        return None
    
    print("=" * 100)
    print(f"📦 CONTENIDO DEL MÓDULO: {module.name}")
    print(f"ID: {module.id} | Posición: {module.position} | Publicado: {'✅' if module.published else '❌'}")
    print("=" * 100)
    
    items_lista = []
    
    try:
        items = list(module.get_module_items())
        
        if not items:
            print("\n  (Sin contenido)")
            return []
        
        print(f"\nTotal de items: {len(items)}\n")
        
        for item in items:
            # Crear indentación visual según el nivel de sangría
            indent_visual = "  " + ("  " * item.indent) + "↳ "
            
            # Tipo de item con emoji
            type_emoji = {
                'File': '📄',
                'Page': '📝',
                'Assignment': '📋',
                'SubHeader': '📌',
                'ExternalUrl': '🔗',
                'ExternalTool': '🔧'
            }.get(item.type, '📦')
            
            # Estado de publicación
            item_published = getattr(item, 'published', None)
            if item_published is not None:
                item_pub_icon = "✅" if item_published else "❌"
            else:
                item_pub_icon = "❓"
            
            # Imprimir línea del item 
            print(f"{item.indent} {indent_visual}[{item.position}] {item_pub_icon} | {type_emoji} | ID: {item.id} | {item.title}")
            #| Tipo: {item.type}


            items_lista.append({
                'id': item.id,
                'title': item.title,
                'type': item.type,
                'position': item.position,
                'indent': item.indent,
                'published': item_published
            })
        
        print("\n" + "=" * 100)
        print("💡 Para modificar items, usa:")
        print("   Canvas_Key.mover_item_modulo(module_id=..., item_id=..., nueva_posicion=...)")
        print("   Canvas_Key.modificar_item_modulo(module_id=..., item_id=..., nuevo_titulo='...', publicado=True/False, indent=...)")
        print("=" * 100)
        
        return None
        
    except Exception as e:
        print(f"❌ Error al obtener items del módulo: {e}")
        return None

def mover_item_modulo(module_id, item_id, nueva_posicion, course_id=None):
    """
    Mueve un item a una nueva posición dentro de un módulo
    
    Args:
        module_id: ID del módulo que contiene el item
        item_id: ID del item a mover
        nueva_posicion: Nueva posición del item dentro del módulo
        course_id: ID del curso en Canvas (si es None, usa el ID del usuario seleccionado)
    
    Returns:
        True si se movió correctamente, False en caso contrario
    
    Ejemplo:
        Canvas_Key.mover_item_modulo(module_id=1454673, item_id=12345, nueva_posicion=3)
    """
    if canvas is None:
        print("❌ Error: No hay conexión activa con Canvas")
        print("💡 Primero ejecuta: Canvas_Key.select_user('TuNombre')")
        return False
    
    # Usar el course_id del usuario si no se especifica uno
    if course_id is None:
        if current_course_id is None:
            print("❌ Error: No hay un course_id asignado al usuario")
            return False
        course_id = current_course_id
    
    # Obtener el curso y módulo
    course = canvas.get_course(course_id)
    
    try:
        module = course.get_module(module_id)
    except Exception as e:
        print(f"❌ Error: No se pudo encontrar el módulo con ID {module_id}")
        return False
    
    print("=" * 60)
    print(f"🔄 MOVIENDO ITEM DENTRO DEL MÓDULO: {module.name}")
    print("=" * 60)
    
    # Buscar el item
    try:
        items = list(module.get_module_items())
        target_item = None
        
        for item in items:
            if item.id == item_id:
                target_item = item
                break
        
        if not target_item:
            print(f"❌ Error: No se encontró el item con ID {item_id}")
            return False
        
        print(f"\nItem encontrado: {target_item.title}")
        print(f"Posición actual: {target_item.position} → Nueva posición: {nueva_posicion}")
        
        # Mover el item
        target_item.edit(module_item={'position': nueva_posicion})
        print(f"✅ Item movido exitosamente")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al mover el item: {e}")
        return False

def modificar_item_modulo(module_id, item_id, nuevo_titulo=None, publicado=None, indent=None, course_id=None):
    """
    Modifica las propiedades de un item dentro de un módulo
    
    Args:
        module_id: ID del módulo que contiene el item
        item_id: ID del item a modificar
        nuevo_titulo: Nuevo título del item - Opcional
        publicado: Estado de publicación (True/False) - Opcional
        indent: Nivel de sangría (0-3) - Opcional
        course_id: ID del curso en Canvas (si es None, usa el ID del usuario seleccionado)
    
    Returns:
        True si se modificó correctamente, False en caso contrario
    
    Ejemplos:
        # Cambiar título
        Canvas_Key.modificar_item_modulo(module_id=1454673, item_id=12345, nuevo_titulo="Nuevo nombre")
        
        # Cambiar nivel de sangría
        Canvas_Key.modificar_item_modulo(module_id=1454673, item_id=12345, indent=2)
        
        # Cambiar múltiples propiedades
        Canvas_Key.modificar_item_modulo(module_id=1454673, item_id=12345, nuevo_titulo="Archivo", publicado=True, indent=1)
    """
    if canvas is None:
        print("❌ Error: No hay conexión activa con Canvas")
        print("💡 Primero ejecuta: Canvas_Key.select_user('TuNombre')")
        return False
    
    # Validar que al menos un parámetro de cambio esté presente
    if nuevo_titulo is None and publicado is None and indent is None:
        print("❌ Error: Debes especificar al menos un cambio (nuevo_titulo, publicado o indent)")
        return False
    
    # Validar nivel de sangría
    if indent is not None and (indent < 0 or indent > 3):
        print("❌ Error: El nivel de sangría (indent) debe estar entre 0 y 3")
        return False
    
    # Usar el course_id del usuario si no se especifica uno
    if course_id is None:
        if current_course_id is None:
            print("❌ Error: No hay un course_id asignado al usuario")
            return False
        course_id = current_course_id
    
    # Obtener el curso y módulo
    course = canvas.get_course(course_id)
    
    try:
        module = course.get_module(module_id)
    except Exception as e:
        print(f"❌ Error: No se pudo encontrar el módulo con ID {module_id}")
        return False
    
    print("=" * 60)
    print(f"🔧 MODIFICANDO ITEM DEL MÓDULO: {module.name}")
    print("=" * 60)
    
    # Buscar el item
    try:
        items = list(module.get_module_items())
        target_item = None
        
        for item in items:
            if item.id == item_id:
                target_item = item
                break
        
        if not target_item:
            print(f"❌ Error: No se encontró el item con ID {item_id}")
            return False
        
        print(f"\nItem encontrado: {target_item.title}")
        
        # Preparar los cambios
        cambios = {}
        
        if nuevo_titulo is not None:
            cambios['title'] = nuevo_titulo
            print(f"• Título: '{target_item.title}' → '{nuevo_titulo}'")
        
        if publicado is not None:
            cambios['published'] = publicado
            pub_actual = getattr(target_item, 'published', None)
            if pub_actual is not None:
                pub_texto_actual = "Publicado" if pub_actual else "No publicado"
            else:
                pub_texto_actual = "Desconocido"
            pub_texto_nuevo = "Publicado" if publicado else "No publicado"
            print(f"• Estado: {pub_texto_actual} → {pub_texto_nuevo}")
        
        if indent is not None:
            cambios['indent'] = indent
            print(f"• Sangría: {target_item.indent} → {indent}")
        
        # Aplicar los cambios
        target_item.edit(module_item=cambios)
        print(f"\n✅ Item modificado exitosamente")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al modificar el item: {e}")
        return False

def ver_modulos(course_id=None, mostrar_items=True):
    """
    Lista todos los módulos del curso con sus IDs, posiciones y contenidos internos
    Útil para identificar el module_id antes de mover o modificar un módulo
    
    Args:
        course_id: ID del curso en Canvas (si es None, usa el ID del usuario seleccionado)
        mostrar_items: Si es True, muestra los items dentro de cada módulo (por defecto True)
    
    Returns:
        Lista de diccionarios con información de los módulos
    
    Ejemplo:
        Canvas_Key.ver_modulos()
        Canvas_Key.ver_modulos(mostrar_items=False)  # Solo módulos, sin items
    """
    if canvas is None:
        print("❌ Error: No hay conexión activa con Canvas")
        print("💡 Primero ejecuta: Canvas_Key.select_user('TuNombre')")
        return None
    
    # Usar el course_id del usuario si no se especifica uno
    if course_id is None:
        if current_course_id is None:
            print("❌ Error: No hay un course_id asignado al usuario")
            print("💡 Especifica el course_id: Canvas_Key.ver_modulos(course_id=123456)")
            return None
        course_id = current_course_id
        print(f"📌 Usando course_id del usuario: {course_id}")
    
    # Obtener el curso
    course = canvas.get_course(course_id)
    
    print("=" * 100)
    print(f"📚 MÓDULOS DEL CURSO (ID: {course_id})")
    print("=" * 100)
    
    modulos_lista = []
    
    try:
        modules = course.get_modules()
        
        for mod in modules:
            # Estado de publicación con emoji
            pub_icon = "✅" if mod.published else "❌"
            
            # Línea principal del módulo
            print(f"\n[{mod.position}] {pub_icon} | ID: {mod.id} | {mod.name}")
            
            modulo_info = {
                'id': mod.id,
                'name': mod.name,
                'position': mod.position,
                'published': mod.published,
                'items': []
            }
            
            # Mostrar items si está habilitado
            if mostrar_items:
                try:
                    items = list(mod.get_module_items())
                    
                    if items:
                        for item in items:
                            # Crear indentación visual según el nivel de sangría
                            indent_visual = "  " + ("  " * item.indent) + "↳ "
                            
                            # Tipo de item con emoji
                            type_emoji = {
                                'File': '📄',
                                'Page': '📝',
                                'Assignment': '📋',
                                'SubHeader': '📌',
                                'ExternalUrl': '🔗',
                                'ExternalTool': '🔧'
                            }.get(item.type, '📦')
                            
                            # Estado de publicación
                            item_published = getattr(item, 'published', None)
                            if item_published is not None:
                                item_pub_icon = "✅" if item_published else "❌"
                            else:
                                item_pub_icon = "❓"
                            
                            # Imprimir línea del item
                            print(f"{indent_visual}[Pos={item.position}] {type_emoji} {item.title} | ID: {item.id} | Publicado: {item_pub_icon} | Indent: {item.indent}")
                            
                            modulo_info['items'].append({
                                'id': item.id,
                                'title': item.title,
                                'type': item.type,
                                'position': item.position,
                                'indent': item.indent,
                                'published': item_published
                            })
                    else:
                        print("    (Sin contenido)")
                        
                except Exception as e:
                    print(f"    ⚠ Error al obtener items: {e}")
            
            modulos_lista.append(modulo_info)
        
        print("\n" + "=" * 100)
        print(f"Total de módulos: {len(modulos_lista)}")
        if mostrar_items:
            total_items = sum(len(m['items']) for m in modulos_lista)
            print(f"Total de items: {total_items}")
        print("=" * 100)
        print("\n💡 Para gestionar módulos, usa:")
        print("   Canvas_Key.mover_modulo(module_id=ID, nueva_posicion=X, nuevo_nombre='...', publicado=True/False)")
        
        return None
        
    except Exception as e:
        print(f"❌ Error al obtener módulos: {e}")
        return None










