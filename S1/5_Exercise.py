# Código con defecto oculto
class SistemaDescuentos:
    """
    Sistema de descuentos de una tienda online
    ¿Puedes encontrar el ERROR, DEFECTO y predecir la FALLA?
    """
    
    def __init__(self):
        self.descuento_maximo = 50  # 50% máximo
    
    def calcular_descuento(self, precio_original, porcentaje_descuento):
        """
        Calcula el precio con descuento aplicado
        
        Requisito: El descuento no debe exceder el 50%
        """
        # 🐛 ¿Encuentras el defecto?
        if porcentaje_descuento > self.descuento_maximo:
            porcentaje_descuento = self.descuento_maximo
        
        descuento = precio_original * porcentaje_descuento / 100
        return precio_original - descuento

# Casos de prueba
sistema = SistemaDescuentos()

print("🧪 PROBANDO SISTEMA DE DESCUENTOS\n")

# Caso 1: Normal
resultado1 = sistema.calcular_descuento(100, 20)
print(f"Producto $100 con 20% descuento: ${resultado1}")

# Caso 2: Límite
resultado2 = sistema.calcular_descuento(100, 50)
print(f"Producto $100 con 50% descuento: ${resultado2}")

# Caso 3: Excede límite
resultado3 = sistema.calcular_descuento(100, 80)
print(f"Producto $100 con 80% descuento: ${resultado3}")

# Caso 4: ¿Y si alguien intenta descuento negativo?
resultado4 = sistema.calcular_descuento(100, -20)
print(f"Producto $100 con -20% descuento: ${resultado4}")
print("💥 ¡FALLA! El precio aumentó en lugar de aplicar descuento")

print("\n" + "="*70)
print("❓ ANÁLISIS:")
print("  • ERROR: El desarrollador no consideró descuentos negativos")
print("  • DEFECTO: Falta validación 'if porcentaje_descuento < 0'")
print("  • FALLA: Cliente puede 'comprar' con precios inflados")
print("  • DEPURACIÓN: Agregar validación al inicio de la función")
print("="*70)