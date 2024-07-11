import nexo
from nexo import start_nexo_server
from nexo import routes

if __name__ == '__main__':
    try:
        start_nexo_server()

    except KeyboardInterrupt:
        print("Exiting...")
