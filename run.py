import os
import socket
import sys

import uvicorn

root_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(root_dir, "HospitalManagement")

sys.path.insert(0, root_dir)
sys.path.insert(0, app_dir)


def get_available_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


if __name__ == "__main__":
    port = int(os.environ.get("PORT", get_available_port()))
    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=False)