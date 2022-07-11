import json
import logging

from channels.generic.websocket import AsyncWebsocketConsumer


logger = logging.Logger(__name__)


class CoinsListConsumer(AsyncWebsocketConsumer):    
    async def connect(self):
        logger.info('Websocket was connected.')
        await self.channel_layer.group_add('coins_list_group', self.channel_name)
        self.groups.append('coins_list_group')
        await self.accept()

    async def disconnect(self, code):
        logger.warning('Websocket was disconnected.')
        pass

    async def send_message(self, event) -> None:
        """Sending messages"""
        if event['message']:
            logger.info('Some coins has been updated.')
            await self.send(json.dumps(event['message']))