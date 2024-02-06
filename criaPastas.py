import os

for i in range(8):

    nomePasta= f"TPC{i+1}"
    os.makedirs(nomePasta)

    open(f"{nomePasta}/.gitkeep", "w")

nomeProj = "Projeto"
os.mkdir(nomeProj)
open(f"{nomeProj}/.gitkeep", "w")

nomeTeste = "Teste"
os.mkdir(nomeTeste)
open(f"{nomeTeste}/.gitkeep", "w")
