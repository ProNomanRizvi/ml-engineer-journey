"""
=========================================================
Project: Dataclass Practice
Concepts:
- @dataclass
- field()
- default_factory
- __post_init__()
- init=False
- frozen=True
- Auto-generated __repr__

Author: Noman Rizvi
=========================================================
"""

from dataclasses import FrozenInstanceError, dataclass, field


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1
    tags: list[str] = field(default_factory=list)
    total: float = field(init=False)

    def __post_init__(self) -> None:
        self.total = self.price * self.quantity


@dataclass(frozen=True)
class Invoice:
    invoice_id: str
    products: list[Product] = field(default_factory=list)


def main() -> None:
    product_1 = Product(
        name="Laptop",
        price=1200.00,
        quantity=2,
        tags=["electronics", "computer"],
    )

    product_2 = Product(
        name="Wireless Mouse",
        price=35.50,
        quantity=3,
        tags=["electronics", "accessory"],
    )

    invoice = Invoice(
        invoice_id="INV-1001",
        products=[product_1, product_2],
    )

    print("\nInvoice Details")
    print("-" * 40)
    print(f"Invoice ID: {invoice.invoice_id}")

    for index, product in enumerate(invoice.products, start=1):
        print(f"\nProduct {index}")
        print(f"  Name     : {product.name}")
        print(f"  Price    : ${product.price:.2f}")
        print(f"  Quantity : {product.quantity}")
        print(f"  Tags     : {', '.join(product.tags)}")
        print(f"  Total    : ${product.total:.2f}")

    print("\nTrying to modify invoice_id...")

    try:
        invoice.invoice_id = "changed"
    except FrozenInstanceError:
        print("Cannot modify invoice_id because Invoice is frozen.")


if __name__ == "__main__":
    main()