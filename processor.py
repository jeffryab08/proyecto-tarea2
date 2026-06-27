import os
from PIL import Image
import xlsxwriter

# Creacion de variables
input_dir = "input_images"
output_dir = "output_images"
watermark_logo = "JAB_Watermark.png"
excel_report = "reporte_imagenes.xlsx"

def create_directories():
    """
    Comprueba la existencia de las carpetas detrabajo
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f"Se creo la carpeta '{input_dir}'. Por favor coloque las imagenes aqui.")

def process_images_and_report():
    """
    Procesa las imagenes y genera reporte de Excel
    """
    create_directories()

    # Confirmar si la marca de agua existe
    if not os.path.exists(watermark_logo):
        print(f"Error. No se encontro la marca de agua {watermark_logo}.")
        return
    
    # Validar imagenes en la carpeta de entrada (.jpg o .png)
    images = []

    # Lista todas las imagenes de la carpeta
    all_images = os.listdir(input_dir)
    
    # Filtrado de imagenes
    for i in all_images:
        lower_name = i.lower() # Convertir nombres a minusculas
        if lower_name.endswith((".png", ".jpg", ".jpeg")):
            images.append(i) # Si la imagen tiene cualquiera de las extensiones arriba mencionadas, se agrega a la lista

    if not images:
        print(F"No se encontraron imagenes en la carpeta {input_dir}")

    # Crear el reporte de Excel
    workbook = xlsxwriter.Workbook(excel_report)
    worksheet = workbook.add_worksheet("Inventario de Imagenes")
    
    # Styles para reporte de excel
    header_format = workbook.add_format({"bold": True, "bg_color": "#1f1f1f", "font_color": "#00ffff", "border": 1})
    cell_format = workbook.add_format({"border": 1})

    # Encabezados del reporte
    headers = ["Nombre de archivo original", "Formato de imagen", "Ancho original", "Alto original", "Estado"]
    for col, header in enumerate(headers):
        worksheet.write(0, col, header, header_format)

    row = 1

    for image in images:
        input_path = os.path.join(input_dir, image)
        output_path = os.path.join(output_dir, image)

        try:
            # Abrir imagen original y extraer informacion
            with Image.open(input_path) as img:
                nombre_original = image
                formato_original = img.format
                ancho_original, alto_original = img.size

                # Redimensionar imagen manteniendo relacion de aspecto
                #img.thumbnail((800, 800))
                max_permitido = 800

                # Verificar si la imagen es mas pequeña que el limite 800
                if ancho_original <= max_permitido and alto_original <= max_permitido:
                    nuevo_ancho = ancho_original
                    nuevo_alto = alto_original
                else:
                    # Relacion de Aspecto de la imagen
                    if ancho_original > alto_original:
                        nuevo_ancho = max_permitido # Si la imagen es mas ancha que alta
                        # Sacar la relacion de aspecto
                        nuevo_alto = int((alto_original / ancho_original) * max_permitido)
                    else:
                        nuevo_alto = max_permitido # Si la imagen es mas alta que ancha
                        nuevo_ancho = int((ancho_original / alto_original) * max_permitido)
                
                img_redimensionada = img.resize((nuevo_ancho, nuevo_alto))

                # Convertir imagen a escala de grises (Modo L)
                img_gris = img_redimensionada.convert("L")

                # Regresar formato imagen temporalmente a RGB para ageregar marca de agua con color
                img_final = img_gris.convert("RGB")

                # Procesar la marca de agua
                with Image.open(watermark_logo) as wm:
                    # Redimensionar marca de agua al 15%
                    wm_width = int(img_final.width * 0.10)
                    wm_height = int(wm.height * (wm_width / wm.width))
                    wm_resized = wm.resize((wm_width, wm_height))

                    # Calcular posicion esquina inferior derecha
                    margin = 10
                    pos_x = img_final.width - wm_resized.width - margin
                    pos_y = img_final.height - wm_resized.height - margin

                    # Caolocar la marce de agua
                    img_final.paste(wm_resized, (pos_x, pos_y))

                # Guardar resultado en la carpeta de salida
                img_final.save(output_path)

                # Guardar datos salvados en celdas de Excel
                worksheet.write(row, 0, nombre_original, cell_format)
                worksheet.write(row, 1, formato_original, cell_format)
                worksheet.write(row, 2, ancho_original, cell_format)
                worksheet.write(row, 3, alto_original, cell_format)
                worksheet.write(row, 4, "Procesada", cell_format)
                print(f"Procesada con exito: {nombre_original}")
                row += 1
        
        except Exception as e:
            print(f"Error al procesar {image}: {e}")

    # Ajustar anchode columnas de Exxcel
    worksheet.set_column(0, 0, 30)
    worksheet.set_column(1, 4, 18)

    # Cerrar archivo de Excel
    workbook.close()
    print(f"\nProceso completado. Archivo de excel generado: {excel_report}")