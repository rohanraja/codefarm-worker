import docker
import os
from filetransfers import *


def py_run(op):

    client = docker.from_env()
    cont = client.containers.run(
            op["image"],
            command=op["cmd"],
            publish_all_ports=op["publishPorts"],
            volumes={
                op["fromPath"]: {'bind': op["toPath"], 'mode': 'rw'}
            },
            detach=True
    )
    return cont

def dockerRun(runOptions):
    return py_run(runOptions)

def imageExists(imageName):
    client = docker.from_env()
    try:
        client.images.get(imageName)
        return True
    except:
        return False

    return False

def downloadImage(r):
    fpath = requestImageFromServer(r["imageUrl"], r["image"])
    loadImageFromFile(fpath)
    assert imageExists(r["image"]) == True

def saveImageToFile(imageName, filePath):
    assert imageExists(imageName) == True
    client = docker.from_env()
    i = client.images.get(imageName)
    resp = i.save()
    f = open(filePath, 'w')
    for chunk in resp.stream():
        f.write(chunk)
    f.close()

def loadImageFromFile(filePath):
    f = open(filePath, 'r')
    data = f.read()
    f.close()
    client = docker.from_env()
    img = client.images.load(data)
    return img


