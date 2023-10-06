# https://fastapi.tiangolo.com/
# Installation via: pip install fastapi (oder pip3)
import sys
from  fastapi import FastAPI


# Globals
app = FastAPI()


# Entrypoint
def main():
    print("Python Version:",sys.version)
    print("FastAPI Demo:", app.version)

if __name__ == "__main__":
    main()