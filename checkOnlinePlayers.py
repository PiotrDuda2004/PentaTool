from mcstatus import MinecraftServer
server = MinecraftServer.lookup("212.159.79.57:25565")
status = server.status()
print(status.players.online)