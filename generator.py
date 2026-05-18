def generate_description(product_name, audience, tone):
    hook = f"Discover the power of {product_name} designed for {audience}."

    benefits = [
        "Built to solve everyday problems with ease",
        "Designed for high performance and reliability",
        "Helps you save time while improving results"
    ]

    if tone == "luxury":
        hook = f"Experience premium quality with {product_name}, crafted for {audience}."

        benefits = [
            "Elegant design that stands out instantly",
            "Premium materials built for long term use",
            "Engineered for those who expect the best"
        ]

    elif tone == "casual":
        hook = f"Meet {product_name}, made simple for {audience}."

        benefits = [
            "Easy to use with zero stress",
            "Perfect for daily needs",
            "Affordable and practical"
        ]

    description = hook + "\n\nKey Benefits:\n"

    for item in benefits:
        description += "• " + item + "\n"

    description += "\nGet yours today and upgrade your experience."

    return description
