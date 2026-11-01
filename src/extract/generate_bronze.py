import os
import pandas as pd
from datetime import datetime, timedelta
import random

def generate_mock_ecommerce_data(num_records=1000):
    print("A gerar dados simulados de E-Commerce (Camada Bronze)...")
    
    # 1. Simular Clientes
    customers = [
        {
            "customer_id": f"CUST_{i:04d}",
            "signup_date": (datetime.now() - timedelta(days=random.randint(10, 365))).strftime("%Y-%m-%d"),
            "state": random.choice(["SP", "RJ", "MG", "RS", "PR", "BA"])
        }
        for i in range(1, 101)
    ]
    df_customers = pd.DataFrame(customers)

    # 2. Simular Produtos
    categories = ["Eletrónicos", "Roupas", "Casa", "Livros", "Desporto"]
    products = [
        {
            "product_id": f"PROD_{i:03d}",
            "product_name": f"Produto {i}",
            "category": random.choice(categories),
            "unit_price": round(random.uniform(20.0, 1500.0), 2)
        }
        for i in range(1, 31)
    ]
    df_products = pd.DataFrame(products)

    # 3. Simular Vendas (Transações)
    sales = []
    for i in range(1, num_records + 1):
        cust = random.choice(customers)
        prod = random.choice(products)
        qty = random.randint(1, 5)
        
        sales.append({
            "order_id": f"ORD_{i:06d}",
            "customer_id": cust["customer_id"],
            "product_id": prod["product_id"],
            "quantity": qty,
            "total_amount": round(prod["unit_price"] * qty, 2),
            "order_timestamp": (datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))).isoformat()
        })
    df_sales = pd.DataFrame(sales)

    # Caminho de destino na Camada Bronze local
    output_dir = "data/bronze"
    os.makedirs(output_dir, exist_ok=True)

    # Guardar como Parquet (Padrão Lakehouse)
    df_customers.to_parquet(f"{output_dir}/customers.parquet", index=False)
    df_products.to_parquet(f"{output_dir}/products.parquet", index=False)
    df_sales.to_parquet(f"{output_dir}/sales.parquet", index=False)

    print(f"Sucesso! Dados brutos guardados em formato Parquet na pasta '{output_dir}/'.")

if __name__ == "__main__":
    generate_mock_ecommerce_data()