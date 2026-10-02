import requests as req

def main():
    while True:
        url = input("Insert a website's URL: ")

        try:
            response = req.get(url)
        except req.exceptions.RequestException:
            print("ERROR: The website you have searched for does not exist")
            continue

        if response.status_code == 200: # OK
            print("OK: Website is active")
            break
        elif response.status_code == 401: # ACCESS DENIED
            print("UNAUTHORIZATION: Website requires authorization")
            break
        elif response.status_code == 403: # FORBIDDEN
            print("FORBIDDEN: Authentication successful, but denied permission")
            break
        elif response.status_code == 404: # NOT FOUND
            print("ERROR: The website you have searched for does not exist")
            continue
        elif response.status_code == 500: # SERVER FAILURE
            print("INTERNAL FAILURE: Server failure")
            break

main()