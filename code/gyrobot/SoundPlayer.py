from pybricks.hubs import InventorHub
from pybricks.tools import wait

class SoundPlayer:
    def __init__(self, hub: InventorHub):
        self.hub = hub
        self.hub.speaker.volume(100)
        self.playing = False

    async def _OdeToJoy(self):
        if self.playing:
            await self.hub.speaker.play_notes(["E4/4", "E4/4", "F4/4", "G4/4", "G4/4", "F4/4", "E4/4", "D4/4", "C4/4", "C4/4", "D4/4", "E4/4", "E4/4.", "D4/8", "D4/2"])
        if self.playing:
            await self.hub.speaker.play_notes(["E4/4", "E4/4", "F4/4", "G4/4", "G4/4", "F4/4", "E4/4", "D4/4", "C4/4", "C4/4", "D4/4", "E4/4", "D4/4.", "C4/8", "C4/2"])
        if self.playing:
            await self.hub.speaker.play_notes(["D4/4", "D4/4", "E4/4", "C4/4", "D4/4", "E4/8", "F4/8", "E4/4", "C4/4", "D4/4", "E4/8", "F4/8", "E4/4", "D4/4", "C4/4", "D4/4", "G3/2"])
        if self.playing:
            await self.hub.speaker.play_notes(["E4/4", "E4/4", "F4/4", "G4/4", "G4/4", "F4/4", "E4/4", "D4/4", "C4/4", "C4/4", "D4/4", "E4/4", "D4/4.", "C4/8", "C4/2"])

    async def _WompWomp(self):
        if self.playing:
            await self.hub.speaker.play_notes(["E2/4", "C2/2."])

    def Play(self):
        self.song = self._OdeToJoy
        self.playing = True
    
    def WompWomp(self):
        self.song = self._WompWomp
        self.playing = True

    async def Stop(self):
        if (self.playing):
            self.playing = False
            await self.hub.speaker.beep(frequency=500, duration=1)

    async def run(self):
        while True:
            # if self.playing:
            #     await self.hub.speaker.play_notes(["E4/4", "E4/4", "F4/4", "G4/4", "G4/4", "F4/4", "E4/4", "D4/4", "C4/4", "C4/4", "D4/4", "E4/4", "E4/4.", "D4/8", "D4/2"])
            # if self.playing:
            #     await self.hub.speaker.play_notes(["E4/4", "E4/4", "F4/4", "G4/4", "G4/4", "F4/4", "E4/4", "D4/4", "C4/4", "C4/4", "D4/4", "E4/4", "D4/4.", "C4/8", "C4/2"])
            # if self.playing:
            #     await self.hub.speaker.play_notes(["D4/4", "D4/4", "E4/4", "C4/4", "D4/4", "E4/8", "F4/8", "E4/4", "C4/4", "D4/4", "E4/8", "F4/8", "E4/4", "D4/4", "C4/4", "D4/4", "G3/2"])
            # if self.playing:
            #     await self.hub.speaker.play_notes(["E4/4", "E4/4", "F4/4", "G4/4", "G4/4", "F4/4", "E4/4", "D4/4", "C4/4", "C4/4", "D4/4", "E4/4", "D4/4.", "C4/8", "C4/2"])
            # if self.playing:
            #     await self.hub.speaker.play_notes(["E2/4", "C2/2."])
            if self.playing:
                await self.song()
            self.playing = False
            await wait(1)