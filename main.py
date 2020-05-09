from resources import miner

roteiro = "C:\\Users\\Snades\\Desktop\\roteiros\\roteiro1.pdf"

obj = miner.ScriptMiner(roteiro)

print(obj.scenesList()[0])
