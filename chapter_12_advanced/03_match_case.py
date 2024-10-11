def http_status(status):
    match status:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case _:
            return "Unknown status"
print(http_status(404))