from generator import generate_description

print("Ecommerce Product Description Generator")

product_name = input("Product name: ")
audience = input("Target audience: ")
tone = input("Tone (luxury, casual, default): ")

result = generate_description(product_name, audience, tone)

print("\nGenerated Description:\n")
print(result)
