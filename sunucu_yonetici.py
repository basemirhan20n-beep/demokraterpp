# Complete Server and Subchannel Management System

class Channel:
    def __init__(self, name):
        self.name = name
        self.permissions = {}  # Store permissions for different roles

class Role:
    def __init__(self, name):
        self.name = name

class Server:
    def __init__(self, name):
        self.name = name
        self.channels = []  # List of channels in the server
        self.roles = []  # List of roles in the server

    def create_channel(self, channel_name):
        new_channel = Channel(channel_name)
        self.channels.append(new_channel)

    def create_role(self, role_name):
        new_role = Role(role_name)
        self.roles.append(new_role)

    def set_permissions(self, channel_name, role_name, permissions):
        for channel in self.channels:
            if channel.name == channel_name:
                channel.permissions[role_name] = permissions
                break

    def get_channel_permissions(self, channel_name, role_name):
        for channel in self.channels:
            if channel.name == channel_name:
                return channel.permissions.get(role_name, 'No permissions set')
        return 'Channel not found'

# Example Usage
server = Server('My Server')
server.create_channel('general')
server.create_role('admin')
server.set_permissions('general', 'admin', ['manage_channels', 'send_messages'])
print(server.get_channel_permissions('general', 'admin'))  # Outputs: ['manage_channels', 'send_messages']