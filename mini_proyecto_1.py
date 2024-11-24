import pandas as pd
import random

# Define operations and their corresponding lambda functions
operations = {
    'SUM': lambda x, y: x + y,
    'SUB': lambda x, y: x - y,
    'MUL': lambda x, y: x * y,
    'DIV': lambda x, y: x / y if y != 0 else None,  # Handle division by zero
    'POW': lambda x, y: x ** y if y < 10 else None  # Limit exponent to avoid very large numbers
}

# Generate data
data = []
for _ in range(1000):
    operation = random.choice(list(operations.keys()))
    operand_1 = random.randint(1, 1000)
    operand_2 = random.randint(1, 1000)
    if operation == 'POW' and operand_2 < 10: operand_2 = random.randint(1, 15)
    data.append([operation, operand_1, operand_2])

# Create DataFrame
df = pd.DataFrame(data, columns=['operation', 'operand_1', 'operand_2'])

# Save to CSV
csv_path = './data/math_operations.csv'
df.to_csv(csv_path, index=False)

# cargar datos del csv
df_loaded = pd.read_csv(csv_path)

# especificar operaciones
def perform_operation(row):
    operation = row['operation']
    operand_1 = row['operand_1']
    operand_2 = row['operand_2']
    func = operations.get(operation)
    return func(operand_1, operand_2) if func else None

# se agrega la nueva columna para los resultados
df_loaded['calculated_result'] = df_loaded.apply(perform_operation, axis=1)

# guardar los nuevos datos
updated_csv_path = './data/math_operations_updated.csv'
df_loaded.to_csv(updated_csv_path, index=False)

# imprimir que todo fue exito
print(f"Se actualizó el CSV y se guardó en: {updated_csv_path}")