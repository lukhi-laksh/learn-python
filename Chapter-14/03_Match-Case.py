def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not Found"
        case 500:
            return "Laksh lukhi"
        case _:
            return "Unknown Status"

print(http_status(404))
        