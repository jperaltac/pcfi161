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