# Discord/Telegram-Style Server and Subchannel Management System for Session

class Server:
    def __init__(self, name):
        self.name = name
        self.channels = []

    def create_channel(self, channel_name):
        channel = Channel(channel_name)
        self.channels.append(channel)
        return channel

class Channel:
    def __init__(self, name):
        self.name = name
        self.subchannels = []

    def create_subchannel(self, subchannel_name):
        subchannel = Subchannel(subchannel_name)
        self.subchannels.append(subchannel)
        return subchannel

class Subchannel:
    def __init__(self, name):
        self.name = name

# Example usage
server = Server("My Server")
channel1 = server.create_channel("General")
subchannel1 = channel1.create_subchannel("Introductions")
subchannel2 = channel1.create_subchannel("Chat")

print(f"Server: {server.name}")
for channel in server.channels:
    print(f" Channel: {channel.name}")
    for subchannel in channel.subchannels:
        print(f"  Subchannel: {subchannel.name}")
