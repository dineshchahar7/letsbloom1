def individual_serial(val) -> dict:
    return {
        "id" : str(val["_id"]),
        "bookId": val["bookId"],
        "bookName" : val["bookName"],
        "authorName": val["authorName"],
        "quantity" : val["quantity"]
    }

def list_serial(vals) -> list:
    return[individual_serial(val) for val in vals]