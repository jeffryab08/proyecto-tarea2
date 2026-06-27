from processor import process_images_and_report

def main():
    print(f"====================================================")
    print(f" Inciando Proceso de Escaneo y Catalogo de Imagenes ")
    print(f"====================================================\n")

    # Ejecucion de proceso de imagenes y reporte de excel
    process_images_and_report()

    print(f"\n==================================================")
    print(f"                Proceso Finalizado                ")
    print(f"==================================================")

if __name__ == "__main__":
    main()