import json
from decimal import Decimal


def calculate_profit():
    with open("trades.json", "r") as f:
        trades = json.load(f)

    cash_flow = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"] or "0")
        sold = Decimal(trade["sold"] or "0")

        cash_flow += sold * price - bought * price
        matecoin_account += bought - sold

    result = {
        "earned_money": str(cash_flow),
        "matecoin_account": str(matecoin_account),
    }

    with open("summary.json", "w") as f:
        json.dump(result, f, indent=4)

    return result
