# Miyamoto Evolution Patch
# Custom Miyamoto sprites.py Module
# By Rimea and friends

from PyQt5 import QtCore, QtGui
Qt = QtCore.Qt

import spritelib as SLib

ImageCache = SLib.ImageCache


class SpriteImage_TouchPlatform(SLib.SpriteImage_StaticMultiple):  # 367
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ToPlatNL'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ToPlatNL', 'touch_platform_left.png')
        SLib.loadIfNotInImageCache('ToPlatNM', 'touch_platform_middle.png')
        SLib.loadIfNotInImageCache('ToPlatNR', 'touch_platform_right.png')
        SLib.loadIfNotInImageCache('MoveArrowUp','touch_arrow_up.png')
        SLib.loadIfNotInImageCache('MoveArrowDown','touch_arrow_down.png')
        SLib.loadIfNotInImageCache('MoveArrowLeft','touch_arrow_left.png')
        SLib.loadIfNotInImageCache('MoveArrowRight','touch_arrow_right.png')
        SLib.loadIfNotInImageCache('MoveArrowNone','touch_arrow_none.png')

    def dataChanged(self):
        super().dataChanged()

        self.width = self.parent.spritedata[8] & 0xF
        self.direction = self.parent.spritedata[3] >> 4 & 0xF
        self.xOffset = 0


        self.width *= 16

    def paint(self, painter):
        super().paint(painter)

        if self.width > 16:
            painter.drawPixmap(0, 0, ImageCache['ToPlatNL'])
            painter.drawPixmap((self.width - 16) * 3.75, 0, ImageCache['ToPlatNR'])

            if self.width > 32:
                painter.drawTiledPixmap(60, 0, (self.width - 32) * 3.75, 60, ImageCache['ToPlatNM'])
                if self.direction == 0:
                   painter.drawPixmap((self.width - 16) * 1.875, 0, ImageCache['MoveArrowRight'])
                if self.direction == 1:
                   painter.drawPixmap((self.width - 16) * 1.875, 0, ImageCache['MoveArrowLeft'])
                if self.direction == 2:
                   painter.drawPixmap((self.width - 16) * 1.875, 0, ImageCache['MoveArrowUp'])
                if self.direction == 3:
                   painter.drawPixmap((self.width - 16) * 1.875, 0, ImageCache['MoveArrowDown'])
                if self.direction == 4:
                   painter.drawPixmap((self.width - 16) * 1.875, 0, ImageCache['MoveArrowNone'])

        else:
            painter.drawPixmap(0, 0, ImageCache['ToPlatNL'])
            painter.drawPixmap(30, 0, ImageCache['ToPlatNR'])
			
			
class SpriteImage_Goomba(SLib.SpriteImage_Static):  # 0
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Goomba'],
			(0, -2),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Goomba', 'goomba.png')
		
		
class SpriteImage_Paragoomba(SLib.SpriteImage_Static):  # 1
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Paragoomba'],
            (-8, -10),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Paragoomba', 'paragoomba.png')
		
		
class SpriteImage_BanzaiBillLauncher(SLib.SpriteImage_Static):  # 173
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BanzaiBillLauncher'],
            (-32, -64),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BanzaiBillLauncher', 'banzai_bill_cannon.png')
		
		
class SpriteImage_UpDownBanzaiBillLauncher(SLib.SpriteImage_Static):  # 174
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['UpDownBanzaiBillLauncher'],
            (-32, 16),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('UpDownBanzaiBillLauncher', 'up_down_banzai_bill_cannon.png')
		
		
class SpriteImage_BulletBill(SLib.SpriteImage_StaticMultiple):  # 125
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

        self.yOffset = 4
        self.xOffset = -5

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BullRight', 'bullet_bill_r.png') 
        SLib.loadIfNotInImageCache('BullLeft', 'bullet_bill_l.png')
        SLib.loadIfNotInImageCache('BullDown', 'bullet_bill_d.png')
        SLib.loadIfNotInImageCache('BullUp', 'bullet_bill_u.png')
        SLib.loadIfNotInImageCache('BullLeftUp', 'bullet_bill_lu.png')
        SLib.loadIfNotInImageCache('BullRightUp', 'bullet_bill_ru.png')
        SLib.loadIfNotInImageCache('BullLeftDown', 'bullet_bill_ld.png')
        SLib.loadIfNotInImageCache('BullRightDown', 'bullet_bill_rd.png')
        SLib.loadIfNotInImageCache('BullFront', 'bullet_bill.png')

    def dataChanged(self):

        spawntype = self.parent.spritedata[5]

        if spawntype == 0:
            self.image = ImageCache['BullRight']
        elif spawntype == 1:
            self.image = ImageCache['BullLeft']


        super().dataChanged()
		
		
class SpriteImage_BanzaiBill(SLib.SpriteImage_StaticMultiple):  # 126
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

        self.yOffset = -32
        self.xOffset = -40

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BanRight', 'banzai_bill_r.png') 
        SLib.loadIfNotInImageCache('BanLeft', 'banzai_bill_l.png')
        SLib.loadIfNotInImageCache('BanDown', 'banzai_bill_d.png')
        SLib.loadIfNotInImageCache('BanUp', 'banzai_bill_u.png')
        SLib.loadIfNotInImageCache('BanLeftUp', 'banzai_bill_lu.png')
        SLib.loadIfNotInImageCache('BanRightUp', 'banzai_bill_ru.png')
        SLib.loadIfNotInImageCache('BanLeftDown', 'banzai_bill_ld.png')
        SLib.loadIfNotInImageCache('BanRightDown', 'banzai_bill_rd.png')
        SLib.loadIfNotInImageCache('BanFront', 'banzai_bill.png')

    def dataChanged(self):

        spawntype = self.parent.spritedata[5]

        if spawntype == 0:
            self.image = ImageCache['BanRight']
        elif spawntype == 1:
            self.image = ImageCache['BanLeft']


        super().dataChanged()
		
		
class SpriteImage_BullsEyeBill(SLib.SpriteImage_Static):  # 127
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BullsEyeBill'],
            (-2, 3),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BullsEyeBill', 'bulls-eye bill.png')
		
		
class SpriteImage_BullsEyeBanzaiBill(SLib.SpriteImage_Static):  # 128
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BullsEyeBanzaiBill'],
            (-32, -32),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BullsEyeBanzaiBill', 'bulls-eye banzai bill.png')
		
		
class SpriteImage_BullsEyeBanzaiBillLauncher(SLib.SpriteImage_Static):  # 582
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BullsEyeBanzaiBillLauncher'],
            (-32, -64),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BullsEyeBanzaiBillLauncher', 'banzai_bill_cannon.png')
		
		
class SpriteImage_UpDownBullsEyeBanzaiBillLauncher(SLib.SpriteImage_Static):  # 583
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['UpDownBullsEyeBanzaiBillLauncher'],
            (-32, 16),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('UpDownBullsEyeBanzaiBillLauncher', 'up_down_banzai_bill_cannon.png')
		
		
class SpriteImage_BullsEyeBillCannon(SLib.SpriteImage_Static):  # 581
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BullsEyeBillCannon', 'bullet_bill_cannon.png')
        SLib.loadIfNotInImageCache('BullsEyeBillCannonPiece', 'bullet_bill_cannon_piece.png')

        if 'BullsEyeBillCannonInverted' not in ImageCache:
            ImageCache['BullsEyeBillCannonInverted'] = QtGui.QPixmap.fromImage(
                SLib.GetImg('bullet_bill_cannon.png', True).mirrored(False, True))

    def dataChanged(self):
        super().dataChanged()

        self.inverted = ((self.parent.spritedata[2] & 0xF0) >> 4) & 1
        self.cannonHeight = (self.parent.spritedata[5] & 0xF0) >> 4
        self.height = (self.cannonHeight + 2) * 16

        if self.inverted == 1:
            self.yOffset = 0

        else:
            self.yOffset = -(self.cannonHeight + 1) * 16

    def paint(self, painter):
        if self.inverted == 1:
            painter.drawTiledPixmap(0, 0, 60, 60 * self.cannonHeight, ImageCache['BullsEyeBillCannonPiece'])
            painter.drawPixmap(0, 60 * self.cannonHeight, 60, 120, ImageCache['BullsEyeBillCannonInverted'])

        else:
            painter.drawPixmap(0, 0, 60, 120, ImageCache['BullsEyeBillCannon'])
            painter.drawTiledPixmap(0, 120, 60, 60 * self.cannonHeight, ImageCache['BullsEyeBillCannonPiece'])
        
        super().paint(painter)

		
class SpriteImage_LavaBlock(SLib.SpriteImage_StaticMultiple):  # 359
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

 

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('LavaBlock0', 'lava_block_0.png') 
        SLib.loadIfNotInImageCache('LavaBlock1', 'lava_block_1.png')
        SLib.loadIfNotInImageCache('LavaBlock2', 'lava_block_2.png')
        SLib.loadIfNotInImageCache('LavaBlock3', 'lava_block_3.png')
        SLib.loadIfNotInImageCache('LavaBlock4', 'lava_block_4.png')
        SLib.loadIfNotInImageCache('LavaBlock5', 'lava_block_5.png')
        SLib.loadIfNotInImageCache('LavaBlock6', 'lava_block_6.png')
        SLib.loadIfNotInImageCache('LavaBlock7', 'lava_block_7.png')
        SLib.loadIfNotInImageCache('LavaBlock8', 'lava_block_8.png')
        SLib.loadIfNotInImageCache('LavaBlock9', 'lava_block_9.png')
        SLib.loadIfNotInImageCache('LavaBlock10', 'lava_block_10.png')

    def dataChanged(self):

        spawntype = self.parent.spritedata[4]

        if spawntype == 0:
            self.image = ImageCache['LavaBlock0']
        elif spawntype == 1:
            self.image = ImageCache['LavaBlock1']
        elif spawntype == 2:
            self.image = ImageCache['LavaBlock2']
        elif spawntype == 3:
            self.image = ImageCache['LavaBlock3'] 
        elif spawntype == 4:
            self.image = ImageCache['LavaBlock4']
        elif spawntype == 5:
            self.image = ImageCache['LavaBlock5']
        elif spawntype == 6:
            self.image = ImageCache['LavaBlock6'] 
        elif spawntype == 7:
            self.image = ImageCache['LavaBlock7']
        elif spawntype == 8:
            self.image = ImageCache['LavaBlock8'] 
        elif spawntype == 9:
            self.image = ImageCache['LavaBlock9']
        elif spawntype == 10:
            self.image = ImageCache['LavaBlock10']


        super().dataChanged()
		
		
class SpriteImage_GiantPiranhaPlant(SLib.SpriteImage_StaticMultiple):  # 550
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

 

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GiantPiranhaUp', 'giant_piranha_plant_up.png') 
        SLib.loadIfNotInImageCache('GiantPiranhaDown', 'giant_piranha_plant_down.png')
        SLib.loadIfNotInImageCache('GiantPiranhaRight', 'giant_piranha_plant_left.png')
        SLib.loadIfNotInImageCache('GiantPiranhaLeft', 'giant_piranha_plant_right.png')
    def dataChanged(self):

        spawntype = ((self.parent.spritedata[2] & 0xF0) >> 4)

        if spawntype == 0:
            self.image = ImageCache['GiantPiranhaUp']
            self.yOffset = -128
            self.xOffset = -32
        elif spawntype == 1:
            self.image = ImageCache['GiantPiranhaDown']
            self.yOffset = 64 
            self.xOffset = -32
        elif spawntype == 2:
            self.image = ImageCache['GiantPiranhaLeft']
            self.yOffset = -32 
            self.xOffset = 64
        elif spawntype == 3:
            self.image = ImageCache['GiantPiranhaRight']
            self.yOffset = -32 
            self.xOffset = -128			
        super().dataChanged()
		
		
class SpriteImage_TowerCog(SLib.SpriteImage_StaticMultiple):  # 269
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

 

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GearSmall', 'gear_small.png') 
        SLib.loadIfNotInImageCache('GearMedium', 'gear_medium.png')
        SLib.loadIfNotInImageCache('GearBig', 'gear_big.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[4] & 0xF

        if spawntype == 0:
            self.image = ImageCache['GearMedium']
            self.yOffset = -96
            self.xOffset = -104
        elif spawntype == 1:
            self.image = ImageCache['GearBig']
            self.yOffset = -152 
            self.xOffset = -152
        elif spawntype == 2:
            self.image = ImageCache['GearSmall']
            self.yOffset = -96
            self.xOffset = -104		
        super().dataChanged()
		
		
class SpriteImage_BowserAmp(SLib.SpriteImage_Static):  # 500
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BowserAmp'],
            (-32, -32),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BowserAmp', 'bowser_amp.png')
		
		
class SpriteImage_ParachuteCoin(SLib.SpriteImage_StaticMultiple):  # 353
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

        self.yOffset = -8
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ParachuteCoin1', 'parachute_coin_1.png') 
        SLib.loadIfNotInImageCache('ParachuteCoin2', 'parachute_coin_2.png')
        SLib.loadIfNotInImageCache('ParachuteCoin3', 'parachute_coin_3.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[8] & 0xF

        if spawntype == 0:
            self.image = ImageCache['ParachuteCoin1']
        elif spawntype == 1:
            self.image = ImageCache['ParachuteCoin2']
        elif spawntype == 2:
            self.image = ImageCache['ParachuteCoin3']
			
        super().dataChanged()
		
		
class SpriteImage_PoltergesitBlock(SLib.SpriteImage_Static):  # 305
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['PoltergeistBlock'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('PoltergeistBlock', 'poltergeist_block.png')
		
		
class SpriteImage_ChainChomp(SLib.SpriteImage_Static):  # 409
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ChainChomp'],
        )
        self.yOffset = -48
        self.xOffset = -48
    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ChainChomp', 'chain_chomp.png')
		
		
class SpriteImage_StationaryIcicle(SLib.SpriteImage_StaticMultiple):  # 185
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('StationaryIcicle1x1', 'icicle_small.png')
        SLib.loadIfNotInImageCache('StationaryIcicle1x2', 'icicle_big.png')

    def dataChanged(self):

        size = self.parent.spritedata[5]

        if size == 0:
            self.image = ImageCache['StationaryIcicle1x1']
        elif size == 1:
            self.image = ImageCache['StationaryIcicle1x2']
        else:
            self.image = ImageCache['StationaryIcicle1x1']

        super().dataChanged()
		
		
class SpriteImage_MediumIcicle(SLib.SpriteImage_Static):  # 533
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['MediumIcicle'],
        )
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('MediumIcicle', 'icicle_medium.png')
		
		
class SpriteImage_BowserJrW5(SLib.SpriteImage_Static):  # 392, 399
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BowserJrW5'],
        )
        self.yOffset = -24
        self.xOffset = -32

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BowserJrW5', 'bowser_jr_w5.png')
		
		
class SpriteImage_BowserJrW7(SLib.SpriteImage_Static):  # 433
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BowserJrW7'],
        )
        self.yOffset = -24
        self.xOffset = -24

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BowserJrW7', 'bowser_jr_w7.png')
		
		
class SpriteImage_BoomBoom(SLib.SpriteImage_Static):  # 206, 223, 225, 246, 302, 317
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BoomBoom'],
        )
        self.yOffset = -32
        self.xOffset = -18

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BoomBoom', 'boomboom.png')
		
		
class SpriteImage_BoltMushroom(SLib.SpriteImage_Static):  # 241
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BoltShroom'],
        )
        self.yOffset = -16
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BoltShroom', 'bolt_mushroom.png')
		
class SpriteImage_BoltMushroomNo(SLib.SpriteImage_Static):  # 242
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BoltShroomNo'],
        )
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BoltShroomNo', 'bolt_mushroom_no.png')
		
		
class SpriteImage_EnemyRaft(SLib.SpriteImage_StaticMultiple):  # 330
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('RaftLava', 'raft_lava.png') 
        SLib.loadIfNotInImageCache('RaftWood', 'raft_wood.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[5]

        if spawntype == 0:
            self.image = ImageCache['RaftLava']
        elif spawntype == 1:
            self.image = ImageCache['RaftWood']
			
        super().dataChanged()
		
		
class SpriteImage_WobbleRock(SLib.SpriteImage_Static):  # 304
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['WobbleRock'],
        )
        self.xOffset = -8
        self.yOffset = -16

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('WobbleRock', 'wobble_rock.png')
		
		
class SpriteImage_RisingTiltPlatform(SLib.SpriteImage_Static):  # 300
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['RisingTiltPlatform'],
        )
        self.xOffset = -32
        self.yOffset = -16

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('RisingTiltPlatform', 'rising_tilt_platform.png')
		
		
class SpriteImage_SwayingPlatform(SLib.SpriteImage_StaticMultiple):  # 275
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

 

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('SwayingPlatformSmall', 'swaying_platform_small.png') 
        SLib.loadIfNotInImageCache('SwayingPlatformMedium', 'swaying_platform_medium.png')
        SLib.loadIfNotInImageCache('SwayingPlatformBig', 'swaying_platform_big.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[4] & 0xF

        if spawntype == 0:
            self.image = ImageCache['SwayingPlatformSmall']
            self.yOffset = -16
            self.xOffset = -32
        elif spawntype == 1:
            self.image = ImageCache['SwayingPlatformMedium']
            self.yOffset = -16
            self.xOffset = -48
        elif spawntype == 2:
            self.image = ImageCache['SwayingPlatformBig']
            self.yOffset = -16
            self.xOffset = -64	
        super().dataChanged()
		
		
class SpriteImage_WheelPlatform(SLib.SpriteImage_Static):  # 287
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['WheelPlatform'],
        )
        self.xOffset = -64
        self.yOffset = -48

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('WheelPlatform', 'wheel_platform.png')
		
		
class SpriteImage_BonePlatform(SLib.SpriteImage_StaticMultiple):  # 491, 492
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BonePlatNL'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BonePlatNL', 'bone_platform_left.png')
        SLib.loadIfNotInImageCache('BonePlatNM', 'bone_platform_middle.png')
        SLib.loadIfNotInImageCache('BonePlatNR', 'bone_platform_right.png')

    def dataChanged(self):
        super().dataChanged()

        self.width = self.parent.spritedata[8] & 0xF
        self.width *= 16
        self.width  =self.width+16

    def paint(self, painter):
        super().paint(painter)

        if self.width > 16:
            painter.drawPixmap(0, 0, ImageCache['BonePlatNL'])
            painter.drawPixmap((self.width - 16) * 3.75, 0, ImageCache['BonePlatNR'])

            if self.width > 32:
                painter.drawTiledPixmap(60, 0, (self.width - 32) * 3.75, 80, ImageCache['BonePlatNM'])

        else:
            painter.drawPixmap(0, 0, ImageCache['BonePlatNL'])
            painter.drawPixmap(30, 0, ImageCache['BonePlatNR'])
			
			
class SpriteImage_SeesawShroom(SLib.SpriteImage_StaticMultiple):  # 278
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['SeesawL'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('SeesawL', 'seesaw_shroom_l.png')
        SLib.loadIfNotInImageCache('SeesawM', 'seesaw_shroom_m.png')
        SLib.loadIfNotInImageCache('SeesawR', 'seesaw_shroom_r.png')
        SLib.loadIfNotInImageCache('SeesawC', 'seesaw_shroom_centre.png')
        SLib.loadIfNotInImageCache('SeesawStemT', 'seesaw_stem_top.png')
        SLib.loadIfNotInImageCache('SeesawStemB', 'seesaw_stem.png')

    def dataChanged(self):
        super().dataChanged()
        self.width = self.parent.spritedata[8] & 0xF
        self.height = (self.parent.spritedata[9] & 0xF) + 1.5
        if not self.width:
            self.width = 8
        self.width *= 32
        self.height *= 32  
        self.xOffset =-112+(240-self.width/2)
        self.yOffset = -8

    def paint(self, painter):
        super().paint(painter)
        painter.drawPixmap((self.width - 16) * 1.875, 60, ImageCache['SeesawStemT'])
        painter.drawTiledPixmap((self.width - 16) * 1.875, 120, 60,(self.height - 32) * 3.75, ImageCache['SeesawStemB'])
        if self.width > 16:
            painter.drawPixmap(0, 0, ImageCache['SeesawL'])
            painter.drawPixmap((self.width - 16) * 3.75, 0, ImageCache['SeesawR'])
            if self.width > 32:
                painter.drawTiledPixmap(60, 0, (self.width - 32) * 3.75, 60, ImageCache['SeesawM'])
            painter.drawPixmap((self.width - 16) * 1.875, 0, ImageCache['SeesawC'])
			
			
class SpriteImage_RectanglePlatforms(SLib.SpriteImage_StaticMultiple):  # 132
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

 

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Blue', 'rectangle_blue.png') 
        SLib.loadIfNotInImageCache('Green', 'rectangle_green.png')
        SLib.loadIfNotInImageCache('Red', 'rectangle_red.png')
        SLib.loadIfNotInImageCache('Orange', 'rectangle_orange.png')
        SLib.loadIfNotInImageCache('Pink', 'rectangle_pink.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[5] & 0xF

        if spawntype == 0:
            self.image = ImageCache['Blue']
            self.yOffset = -48
            self.xOffset = -112
        elif spawntype == 1:
            self.image = ImageCache['Green']
            self.yOffset = -112
            self.xOffset = -48
        elif spawntype == 2:
            self.image = ImageCache['Red']
            self.yOffset = -32 
            self.xOffset = -144
        elif spawntype == 3:
            self.image = ImageCache['Orange']
            self.yOffset = -48 
            self.xOffset = -80
        elif spawntype == 4:
            self.image = ImageCache['Pink']
            self.yOffset = -48 
            self.xOffset = -80				
        super().dataChanged()
		
		
class SpriteImage_AirshipLemmy(SLib.SpriteImage_Static):  # 414
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ALemmy'],
        )
        self.xOffset = -88
        self.yOffset = -88

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ALemmy', 'Airship_Lemmy.png')
		
		
class SpriteImage_AirshipMorton(SLib.SpriteImage_Static):  # 415
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['AMorton'],
        )
        self.xOffset = -88
        self.yOffset = -88

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('AMorton', 'Airship_Morton.png')
		
		
class SpriteImage_AirshipLarry(SLib.SpriteImage_Static):  # 417
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ALarry'],
        )
        self.xOffset = -88
        self.yOffset = -88

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ALarry', 'Airship_Larry.png')
		
		
class SpriteImage_AirshipWendy(SLib.SpriteImage_Static):  # 418
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['AWendy'],
        )
        self.xOffset = -88
        self.yOffset = -88

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('AWendy', 'Airship_Wendy.png')
		
		
class SpriteImage_AirshipIggy(SLib.SpriteImage_Static):  # 419
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['AIggy'],
        )
        self.xOffset = -88
        self.yOffset = -88

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('AIggy', 'Airship_Iggy.png')
		
		
class SpriteImage_AirshipRoy(SLib.SpriteImage_Static):  # 420
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ARoy'],
        )
        self.xOffset = -88
        self.yOffset = -88

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ARoy', 'Airship_Roy.png')
		
		
		
class SpriteImage_AirshipLudwig(SLib.SpriteImage_Static):  # 421
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ALudwig'],
        )
        self.xOffset = -88
        self.yOffset = -88

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ALudwig', 'Airship_Ludwig.png')
		

	 
class SpriteImage_NutPlatform(SLib.SpriteImage_StaticMultiple):  # 341
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['NutPlatform'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('NutPlatform', 'nut_platform.png')

    def dataChanged(self):
        super().dataChanged()
        self.single   = self.parent.spritedata[5]
        self.multiple = self.parent.spritedata[5] & 0xF
        self.yOffset  = -8+self.single/2-self.multiple/2
        self.xOffset  = -16+self.multiple*8
		
		
class SpriteImage_MetalBar(SLib.SpriteImage_StaticMultiple):  # 429
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

 

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('MetalBar0', 'metal_bar_0.png') 
        SLib.loadIfNotInImageCache('MetalBar1', 'metal_bar_1.png')
        SLib.loadIfNotInImageCache('MetalBar2', 'metal_bar_2.png')
        SLib.loadIfNotInImageCache('MetalBar3', 'metal_bar_3.png')
        SLib.loadIfNotInImageCache('MetalBar4', 'metal_bar_4.png')
        SLib.loadIfNotInImageCache('MetalBar5', 'metal_bar_5.png')
        SLib.loadIfNotInImageCache('MetalBar6', 'metal_bar_6.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[5]  & 0xF       

        if   spawntype == 0:
            self.image = ImageCache['MetalBar0']
        elif spawntype == 1:
            self.image = ImageCache['MetalBar1']
        elif spawntype == 2:
            self.image = ImageCache['MetalBar2']
        elif spawntype == 3:
            self.image = ImageCache['MetalBar3'] 
        elif spawntype == 4:
            self.image = ImageCache['MetalBar4']
        elif spawntype == 5:
            self.image = ImageCache['MetalBar5']
        elif spawntype == 6:
            self.image = ImageCache['MetalBar6'] 
        super().dataChanged() 
		
		
class SpriteImage_MetalGearBox(SLib.SpriteImage_StaticMultiple):  # 485
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

 

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('MetalGearBox0', 'metal_gearbox_0.png') 
        SLib.loadIfNotInImageCache('MetalGearBox1', 'metal_gearbox_1.png')
        SLib.loadIfNotInImageCache('MetalGearBox2', 'metal_gearbox_2.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[5]  & 0xF       

        if   spawntype == 0:
            self.image = ImageCache['MetalGearBox0']
            self.yOffset = 0
        elif spawntype == 1:
            self.image = ImageCache['MetalGearBox1']
            self.yOffset = 0
        elif spawntype == 2:
            self.image = ImageCache['MetalGearBox2']
            self.yOffset = -64
		
        super().dataChanged()



class SpriteImage_TargetingTedBox(SLib.SpriteImage_Static):  # 596
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['TargetingTedBox'],
        )
        self.xOffset = -32
        self.yOffset = -16

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('TargetingTedBox', 'targeting_ted_launcher.png')	


class SpriteImage_IggyRoom(SLib.SpriteImage_Static):  # 609
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['IggyRoom'],
        )
        self.xOffset = -288
        self.yOffset = -256

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('IggyRoom', 'iggy_room.png')


class SpriteImage_MeltableIceChunk(SLib.SpriteImage_Static):  # 386
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['MeltableIceChunk'],
        )
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('MeltableIceChunk', 'meltable_ice_chunk.png')


class SpriteImage_Magmaw(SLib.SpriteImage_Static):  # 565
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Magmaw'],
        )
        self.xOffset = -24
        self.yOffset = -16

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Magmaw', 'magmaw.png')	
		
		
class SpriteImage_IronBlock(SLib.SpriteImage):  # 80
    def __init__(self, parent):
        super().__init__(parent, 3.75)

        self.spritebox.shown = False

    @staticmethod
    def loadImages():
        ImageCache['IronBTopL'] = SLib.GetImg('iron_block_top_l.png')
        ImageCache['IronBTopM'] = SLib.GetImg('iron_block_top_m.png')
        ImageCache['IronBTopR'] = SLib.GetImg('iron_block_top_r.png')
        ImageCache['IronBMiddleL'] = SLib.GetImg('iron_block_mid_l.png')
        ImageCache['IronBMiddleM'] = SLib.GetImg('iron_block_mid_m.png')
        ImageCache['IronBMiddleR'] = SLib.GetImg('iron_block_mid_r.png')
        ImageCache['IronBBottomL'] = SLib.GetImg('iron_block_bottom_l.png')
        ImageCache['IronBBottomM'] = SLib.GetImg('iron_block_bottom_m.png')
        ImageCache['IronBBottomR'] = SLib.GetImg('iron_block_bottom_r.png')

    def dataChanged(self):
        super().dataChanged()

        self.width = ((self.parent.spritedata[8] & 0xF) * 16)+16
        self.height = ((self.parent.spritedata[9] & 0xF) * 16)+16
        if self.width / 16 == 0: self.width = 1
        if self.height / 16 == 0: self.height = 1

    def paint(self, painter):
        super().paint(painter)

        # Top of sprite.
        if self.width / 16 == 0:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['IronBTopM'])
        elif self.width / 16 == 1:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['IronBTopM'])
        elif self.width / 16 == 2:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['IronBTopL'])
            painter.drawPixmap(60, 0, 60, 60, ImageCache['IronBTopR'])
        elif self.width / 16 == 3:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['IronBTopL'
            ])
            painter.drawPixmap(60, 0, 60, 60, ImageCache['IronBTopM'])
            painter.drawPixmap(120, 0, 60, 60, ImageCache['IronBTopR'])
        else:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['IronBTopL'
            ])
            painter.drawTiledPixmap(60, 0, (self.width / 16 - 2) * 60, 60, ImageCache['IronBTopM'])
            painter.drawPixmap(60 + ((self.width / 16 - 2) * 60), 0, 60, 60, ImageCache['IronBTopR'])

        # Bottom
        if self.height / 16 > 1:
            if self.width / 16 == 0:
                painter.drawPixmap(0, 0, 60, 60, ImageCache['IronBBottomM'])
            elif self.width / 16 == 1:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['IronBBottomM'])
            elif self.width / 16 == 2:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['IronBBottomL'])
                painter.drawPixmap(60, (self.height / 16) * 60 - 60, 60, 60, ImageCache['IronBBottomR'])
            elif self.width / 16 == 3:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['IronBBottomL'
                ])
                painter.drawPixmap(60, (self.height / 16) * 60 - 60, 60, 60, ImageCache['IronBBottomM'])
                painter.drawPixmap(120, (self.height / 16) * 60 - 60, 60, 60, ImageCache['IronBBottomR'])
            else:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['IronBBottomL'
                ])
                painter.drawTiledPixmap(60, (self.height / 16) * 60 - 60, (self.width / 16 - 2) * 60, 60,
                                        ImageCache['IronBBottomM'])
                painter.drawPixmap(60 + ((self.width / 16 - 2) * 60), (self.height / 16) * 60 - 60, 60, 60,
                                   ImageCache['IronBBottomR'])

        # Left
        if self.height / 16 == 3:
            painter.drawPixmap(0, 60, 60, 60, ImageCache['IronBMiddleL'])
        elif self.height / 16 > 3:
            painter.drawPixmap(0, 60, 60, 60, ImageCache['IronBMiddleL'])
            painter.drawTiledPixmap(0, 120, 60, (self.height / 16 - 3) * 60, ImageCache['IronBMiddleL'])

        # Right
        if self.height / 16 == 3:
            painter.drawPixmap((self.width / 16 * 60) - 60, 60, 60, 60, ImageCache['IronBMiddleR'])
        elif self.height / 16 > 3:
            painter.drawPixmap((self.width / 16 * 60) - 60, 60, 60, 60, ImageCache['IronBMiddleR'])
            painter.drawTiledPixmap((self.width / 16 * 60) - 60, 120, 60, (self.height / 16 - 3) * 60,
                                    ImageCache['IronBMiddleR'])

        # Middle
        if self.width / 16 > 2:
            if self.height / 16 > 2:
                painter.drawTiledPixmap(60, 60, ((self.width / 16) - 2) * 60, ((self.height / 16) - 2) * 60,
                                        ImageCache['IronBMiddleM'])

        # 1 Glitch
        if self.width / 16 < 2:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['IronBTopM'])
            painter.drawTiledPixmap(0, 60, 60, ((self.height / 16) - 2) * 60, ImageCache['IronBMiddleM'])
            if self.height > 1:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['IronBBottomM'])
            painter.drawPixmap(0, 0, 60, 60, ImageCache['IronBTopM'])
			
			
class SpriteImage_MovingAcornBlock(SLib.SpriteImage):  # 81
    def __init__(self, parent):
        super().__init__(parent, 3.75)

        self.spritebox.shown = False

    @staticmethod
    def loadImages():
        ImageCache['MovATopL'] = SLib.GetImg('mov_land_top_l.png')
        ImageCache['MovATopM'] = SLib.GetImg('mov_land_top_m.png')
        ImageCache['MovATopR'] = SLib.GetImg('mov_land_top_r.png')
        ImageCache['MovAMiddleL'] = SLib.GetImg('mov_land_middle_l.png')
        ImageCache['MovAMiddleM'] = SLib.GetImg('mov_land_middle_m.png')
        ImageCache['MovAMiddleR'] = SLib.GetImg('mov_land_middle_r.png')
        ImageCache['MovABottomL'] = SLib.GetImg('mov_land_bottom_l.png')
        ImageCache['MovABottomM'] = SLib.GetImg('mov_land_bottom_m.png')
        ImageCache['MovABottomR'] = SLib.GetImg('mov_land_bottom_r.png')

    def dataChanged(self):
        super().dataChanged()

        self.width = ((self.parent.spritedata[8] & 0xF) * 16)+16
        self.height = ((self.parent.spritedata[9] & 0xF) * 16)+16
        if self.width / 16 == 0: self.width = 1
        if self.height / 16 == 0: self.height = 1

    def paint(self, painter):
        super().paint(painter)

        # Top of sprite.
        if self.width / 16 == 0:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['MovATopM'])
        elif self.width / 16 == 1:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['MovATopM'])
        elif self.width / 16 == 2:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['MovATopL'])
            painter.drawPixmap(60, 0, 60, 60, ImageCache['MovATopR'])
        elif self.width / 16 == 3:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['MovATopL'
            ])
            painter.drawPixmap(60, 0, 60, 60, ImageCache['MovATopM'])
            painter.drawPixmap(120, 0, 60, 60, ImageCache['MovATopR'])
        else:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['MovATopL'
            ])
            painter.drawTiledPixmap(60, 0, (self.width / 16 - 2) * 60, 60, ImageCache['MovATopM'])
            painter.drawPixmap(60 + ((self.width / 16 - 2) * 60), 0, 60, 60, ImageCache['MovATopR'])

        # Bottom
        if self.height / 16 > 1:
            if self.width / 16 == 0:
                painter.drawPixmap(0, 0, 60, 60, ImageCache['MovABottomM'])
            elif self.width / 16 == 1:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['MovABottomM'])
            elif self.width / 16 == 2:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['MovABottomL'])
                painter.drawPixmap(60, (self.height / 16) * 60 - 60, 60, 60, ImageCache['MovABottomR'])
            elif self.width / 16 == 3:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['MovABottomL'
                ])
                painter.drawPixmap(60, (self.height / 16) * 60 - 60, 60, 60, ImageCache['MovABottomM'])
                painter.drawPixmap(120, (self.height / 16) * 60 - 60, 60, 60, ImageCache['MovABottomR'])
            else:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['MovABottomL'
                ])
                painter.drawTiledPixmap(60, (self.height / 16) * 60 - 60, (self.width / 16 - 2) * 60, 60,
                                        ImageCache['MovABottomM'])
                painter.drawPixmap(60 + ((self.width / 16 - 2) * 60), (self.height / 16) * 60 - 60, 60, 60,
                                   ImageCache['MovABottomR'])

        # Left
        if self.height / 16 == 3:
            painter.drawPixmap(0, 60, 60, 60, ImageCache['MovAMiddleL'])
        elif self.height / 16 > 3:
            painter.drawPixmap(0, 60, 60, 60, ImageCache['MovAMiddleL'])
            painter.drawTiledPixmap(0, 120, 60, (self.height / 16 - 3) * 60, ImageCache['MovAMiddleL'])

        # Right
        if self.height / 16 == 3:
            painter.drawPixmap((self.width / 16 * 60) - 60, 60, 60, 60, ImageCache['MovAMiddleR'])
        elif self.height / 16 > 3:
            painter.drawPixmap((self.width / 16 * 60) - 60, 60, 60, 60, ImageCache['MovAMiddleR'])
            painter.drawTiledPixmap((self.width / 16 * 60) - 60, 120, 60, (self.height / 16 - 3) * 60,
                                    ImageCache['MovAMiddleR'])

        # Middle
        if self.width / 16 > 2:
            if self.height / 16 > 2:
                painter.drawTiledPixmap(60, 60, ((self.width / 16) - 2) * 60, ((self.height / 16) - 2) * 60,
                                        ImageCache['MovAMiddleM'])

        # 1 Glitch
        if self.width / 16 < 2:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['MovATopM'])
            painter.drawTiledPixmap(0, 60, 60, ((self.height / 16) - 2) * 60, ImageCache['MovAMiddleM'])
            if self.height > 1:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['MovABottomM'])
            painter.drawPixmap(0, 0, 60, 60, ImageCache['MovATopM'])
			
			
class SpriteImage_KamekFloor(SLib.SpriteImage_StaticMultiple):  # 465
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

 

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('KamekFloor0', 'kamek_floor_0.png') 
        SLib.loadIfNotInImageCache('KamekFloor1', 'kamek_floor_1.png')
        SLib.loadIfNotInImageCache('KamekFloor2', 'kamek_floor_2.png')
        SLib.loadIfNotInImageCache('KamekFloor3', 'kamek_floor_3.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[5]  & 0xF       

        if   spawntype == 0:
            self.image = ImageCache['KamekFloor0']
        elif spawntype == 1:
            self.image = ImageCache['KamekFloor1']
        elif spawntype == 2:
            self.image = ImageCache['KamekFloor2']
        elif spawntype == 3:
            self.image = ImageCache['KamekFloor3']
		
        super().dataChanged()
		

class SpriteImage_KamekBlock(SLib.SpriteImage_Static):  # 450
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['KamekBlock'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('KamekBlock', 'kamek_block.png')


class SpriteImage_IceBlock(SLib.SpriteImage_StaticMultiple):  # 268
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

 

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('IceBlock0', 'ice_0.png') 
        SLib.loadIfNotInImageCache('IceBlock1', 'ice_1.png')
        SLib.loadIfNotInImageCache('IceBlock2', 'ice_2.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[5]  & 0xF       

        if   spawntype == 0:
            self.image = ImageCache['IceBlock0']
            self.yOffset = -16
            self.xOffset = -8
        elif spawntype == 1:
            self.image = ImageCache['IceBlock1']
            self.yOffset = -16
            self.xOffset = -16
        elif spawntype == 2:
            self.image = ImageCache['IceBlock2']
            self.yOffset = -16
            self.xOffset = -8
		
        super().dataChanged()


class SpriteImage_LongBurner(SLib.SpriteImage_StaticMultiple):  # 290
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

 

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('LongBurnerR', 'fire_bar_long_r.png') 
        SLib.loadIfNotInImageCache('LongBurnerD', 'fire_bar_long_d.png')
        SLib.loadIfNotInImageCache('LongBurnerL', 'fire_bar_long_l.png')
        SLib.loadIfNotInImageCache('LongBurnerU', 'fire_bar_long_u.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[5]  & 3      

        if   spawntype == 0:
            self.image = ImageCache['LongBurnerR']
            self.yOffset = 0
            self.xOffset = 0
        elif spawntype == 1:
            self.image = ImageCache['LongBurnerL']
            self.yOffset = 0
            self.xOffset = -96
        elif spawntype == 2:
            self.image = ImageCache['LongBurnerU']
            self.yOffset = -96
            self.xOffset = 0
        elif spawntype == 3:
            self.image = ImageCache['LongBurnerD']
            self.yOffset = 0
            self.xOffset = 0
		
        super().dataChanged()
		
class SpriteImage_BoltMushroom(SLib.SpriteImage_StaticMultiple):  # 241
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )
        self.xOffset = -8
        self.yOffset = -16


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BoltMushShort', 'bolt_mushroom.png') 
        SLib.loadIfNotInImageCache('BoltMushLong', 'bolt_mushroom_long.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[8] & 0xf

        if spawntype == 0:
            self.image = ImageCache['BoltMushShort']
        elif spawntype == 1:
            self.image = ImageCache['BoltMushLong']
			
        super().dataChanged()
	
	
class SpriteImage_BoltMushroomNo(SLib.SpriteImage_StaticMultiple):  # 242
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )
        self.xOffset = -8


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BoltMushNoShort', 'bolt_mushroom_no.png') 
        SLib.loadIfNotInImageCache('BoltMushNoLong', 'bolt_mushroom_no_long.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[8] & 0xf

        if spawntype == 0:
            self.image = ImageCache['BoltMushNoShort']
        elif spawntype == 1:
            self.image = ImageCache['BoltMushNoLong']
			
        super().dataChanged()
		
		
class SpriteImage_Dragoneel(SLib.SpriteImage_StaticMultiple):  # 382
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )
        self.xOffset = -16


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('DragoneelSmall', 'dragoneel_small.png') 
        SLib.loadIfNotInImageCache('DragoneelBig', 'dragoneel_big.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[5] & 0xf

        if spawntype == 0:
            self.image = ImageCache['DragoneelSmall']
        elif spawntype == 1:
            self.image = ImageCache['DragoneelBig']
			
        super().dataChanged()
		
		
class SpriteImage_FloatingQBlock(SLib.SpriteImage):  # 205
    def __init__(self, parent):
        super().__init__(parent, 3.75)
        self.spritebox.shown = False
        self.dimensions = (0, 16, 24, 24)

    def dataChanged(self):
        super().dataChanged()

        self.contents = self.parent.spritedata[9] & 0xF
        self.acorn = (self.parent.spritedata[6] >> 4) & 1

        items = {0: 0x800 + 160, 1: 49, 2: 32, 3: 32, 4: 37, 5: 38, 6: 36, 7: 33, 8: 34, 9: 41, 12: 35, 13: 42, 15: 39}

        self.dopaint = True
        self.image = None
        self.yOffset = -4
        self.xOffset = -4

        if self.acorn:
            self.tilenum = 40
        elif self.contents in items:
            self.tilenum = items[self.contents]
        else:
            self.dopaint = False
            if self.contents == 10:
                self.imagecache = ImageCache['Q10']
            elif self.contents == 11:
                self.imagecache = ImageCache['QKinokoUP']
            elif self.contents == 14:
                self.imagecache = ImageCache['QKinoko']
            else:
                self.dopaint = True
                self.tilenum = 49

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Q10', 'block_q_10.png')
        SLib.loadIfNotInImageCache('QKinokoUP', 'block_q_kinoko_up.png')
        SLib.loadIfNotInImageCache('QKinoko', 'block_q_kinoko_coin.png')

    def paint(self, painter):
        super().paint(painter)

        if self.dopaint:
            painter.drawPixmap(0, 0, 90, 90, SLib.Tiles[self.tilenum].main)
        else:
            painter.drawPixmap(0, 0, 90, 90, self.imagecache)
			
			
class SpriteImage_Wrench(SLib.SpriteImage_Static):  # 537
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Wrench'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Wrench', 'wrench.png')


class SpriteImage_Peach(SLib.SpriteImage_Static):  # 571
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Peach'],
        )
        self.xOffset = -16
        self.yOffset = -48

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Peach', 'peach.png')
	
		
class SpriteImage_ScaffoldPlatform(SLib.SpriteImage_StaticMultiple):  # 228
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ScaffoldPlatformSmall', 'scaffold_platform.png')
        SLib.loadIfNotInImageCache('ScaffoldPlatformBig', 'scaffold_platform_big.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[8]

        if spawntype == 0:
            self.image = ImageCache['ScaffoldPlatformSmall']
            self.xOffset = -72
        elif spawntype == 16:
            self.image = ImageCache['ScaffoldPlatformBig']
            self.xOffset = -112
			
        super().dataChanged()
		
		
		
class SpriteImage_TiltGirder(SLib.SpriteImage_Static):  # 349
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['TiltGirder'],
        )
        self.yOffset = -8
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('TiltGirder', 'tilt_girder.png')
		
		
class SpriteImage_AirshipSegment(SLib.SpriteImage_StaticMultiple):  # 489
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['AirshipSegment1'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('AirshipSegment1', 'Airship_Segment_1.png')
        SLib.loadIfNotInImageCache('AirshipSegment2', 'Airship_Segment_2.png')
        SLib.loadIfNotInImageCache('AirshipSegment3', 'Airship_Segment_3.png')

    def dataChanged(self):
        super().dataChanged()

        self.width = (self.parent.spritedata[8])+17
        self.xOffset = -112
        self.yOffset = -304


        self.width *= 16

    def paint(self, painter):
        super().paint(painter)

        if self.parent.spritedata[8] > 0:
            painter.drawTiledPixmap(960, 0,self.parent.spritedata[8]*60 , 1200, ImageCache['AirshipSegment2'])
            painter.drawPixmap(0, 0, ImageCache['AirshipSegment1'])
            painter.drawPixmap((self.width - 35) * 3.75, 0, ImageCache['AirshipSegment3'])
			
			
class SpriteImage_AirshipCollar(SLib.SpriteImage_Static):  # 490
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['AirshipCollar'],
        )
        self.yOffset = -128
        self.xOffset = -10

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('AirshipCollar','Airship_Segment_3.png')
		
		
class SpriteImage_Fence(SLib.SpriteImage):  # 307
    def __init__(self, parent):
        super().__init__(parent, 3.75)

        self.spritebox.shown = False

    @staticmethod
    def loadImages():
        ImageCache['FenceTopL'] = SLib.GetImg('fence_top_l.png')
        ImageCache['FenceTopM'] = SLib.GetImg('fence_top_m.png')
        ImageCache['FenceTopR'] = SLib.GetImg('fence_top_r.png')
        ImageCache['FenceMiddleL'] = SLib.GetImg('fence_mid_l.png')
        ImageCache['FenceMiddleM'] = SLib.GetImg('fence_mid_m.png')
        ImageCache['FenceMiddleR'] = SLib.GetImg('fence_mid_r.png')
        ImageCache['FenceBottomL'] = SLib.GetImg('fence_bottom_l.png')
        ImageCache['FenceBottomM'] = SLib.GetImg('fence_bottom_m.png')
        ImageCache['FenceBottomR'] = SLib.GetImg('fence_bottom_r.png')

    def dataChanged(self):
        super().dataChanged()

        self.width = ((self.parent.spritedata[8] & 0xF) * 32)+64
        self.height = ((self.parent.spritedata[9] & 0xF) * 32)+64
        self.xOffset = -64-(self.width/2-64)
        self.yOffset = -64-(self.height/2-64)

    def paint(self, painter):
        super().paint(painter)

        # Top of sprite.
        if self.width / 16 == 0:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['FenceTopM'])
        elif self.width / 16 == 1:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['FenceTopM'])
        elif self.width / 16 == 2:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['FenceTopL'])
            painter.drawPixmap(60, 0, 60, 60, ImageCache['FenceTopR'])
        elif self.width / 16 == 3:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['FenceTopL'
            ])
            painter.drawPixmap(60, 0, 60, 60, ImageCache['FenceTopM'])
            painter.drawPixmap(120, 0, 60, 60, ImageCache['FenceTopR'])
        else:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['FenceTopL'
            ])
            painter.drawTiledPixmap(60, 0, (self.width / 16 - 2) * 60, 60, ImageCache['FenceTopM'])
            painter.drawPixmap(60 + ((self.width / 16 - 2) * 60), 0, 60, 60, ImageCache['FenceTopR'])

        # Bottom
        if self.height / 16 > 1:
            if self.width / 16 == 0:
                painter.drawPixmap(0, 0, 60, 60, ImageCache['FenceBottomM'])
            elif self.width / 16 == 1:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['FenceBottomM'])
            elif self.width / 16 == 2:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['FenceBottomL'])
                painter.drawPixmap(60, (self.height / 16) * 60 - 60, 60, 60, ImageCache['FenceBottomR'])
            elif self.width / 16 == 3:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['FenceBottomL'
                ])
                painter.drawPixmap(60, (self.height / 16) * 60 - 60, 60, 60, ImageCache['FenceBottomM'])
                painter.drawPixmap(120, (self.height / 16) * 60 - 60, 60, 60, ImageCache['FenceBottomR'])
            else:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['FenceBottomL'
                ])
                painter.drawTiledPixmap(60, (self.height / 16) * 60 - 60, (self.width / 16 - 2) * 60, 60,
                                        ImageCache['FenceBottomM'])
                painter.drawPixmap(60 + ((self.width / 16 - 2) * 60), (self.height / 16) * 60 - 60, 60, 60,
                                   ImageCache['FenceBottomR'])

        # Left
        if self.height / 16 == 3:
            painter.drawPixmap(0, 60, 60, 60, ImageCache['FenceMiddleL'])
        elif self.height / 16 > 3:
            painter.drawPixmap(0, 60, 60, 60, ImageCache['FenceMiddleL'])
            painter.drawTiledPixmap(0, 120, 60, (self.height / 16 - 3) * 60, ImageCache['FenceMiddleL'])

        # Right
        if self.height / 16 == 3:
            painter.drawPixmap((self.width / 16 * 60) - 60, 60, 60, 60, ImageCache['FenceMiddleR'])
        elif self.height / 16 > 3:
            painter.drawPixmap((self.width / 16 * 60) - 60, 60, 60, 60, ImageCache['FenceMiddleR'])
            painter.drawTiledPixmap((self.width / 16 * 60) - 60, 120, 60, (self.height / 16 - 3) * 60,
                                    ImageCache['FenceMiddleR'])

        # Middle
        if self.width / 16 > 2:
            if self.height / 16 > 2:
                painter.drawTiledPixmap(60, 60, ((self.width / 16) - 2) * 60, ((self.height / 16) - 2) * 60,
                                        ImageCache['FenceMiddleM'])

        # 1 Glitch
        if self.width / 16 < 2:
            painter.drawPixmap(0, 0, 60, 60, ImageCache['FenceTopM'])
            painter.drawTiledPixmap(0, 60, 60, ((self.height / 16) - 2) * 60, ImageCache['FenceMiddleM'])
            if self.height > 1:
                painter.drawPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['FenceBottomM'])
            painter.drawPixmap(0, 0, 60, 60, ImageCache['FenceTopM'])		


class SpriteImage_RedRing(SLib.SpriteImage_Static):  # 44
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['RedRing'],
        )

        self.yOffset = -7
        self.xOffset = -9

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('RedRing', 'red_ring.png')


class SpriteImage_GreenRing(SLib.SpriteImage_Static):  # 402
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['GreenRing'],
        )

        self.yOffset = -7
        self.xOffset = -9

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GreenRing', 'green_ring.png')	


class SpriteImage_BlueRing(SLib.SpriteImage_Static):  # 662
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BlueRing'],
        )

        self.yOffset = -7
        self.xOffset = -9

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BlueRing', 'blue_ring.png')


class SpriteImage_GhostHouseBlock(SLib.SpriteImage):  # 512
    def __init__(self, parent):
        super().__init__(parent, 3.75)

        self.spritebox.shown = False

    @staticmethod
    def loadImages():
        ImageCache['GHBlockTopL'] = SLib.GetImg('ghost_house_top_l.png')
        ImageCache['GHBlockTopM'] = SLib.GetImg('ghost_house_top_m.png')
        ImageCache['GHBlockTopR'] = SLib.GetImg('ghost_house_top_r.png')
        ImageCache['GHBlockMiddleL'] = SLib.GetImg('ghost_house_mid_l.png')
        ImageCache['GHBlockMiddleM'] = SLib.GetImg('ghost_house_mid_m.png')
        ImageCache['GHBlockMiddleR'] = SLib.GetImg('ghost_house_mid_r.png')
        ImageCache['GHBlockBottomL'] = SLib.GetImg('ghost_house_bottom_l.png')
        ImageCache['GHBlockBottomM'] = SLib.GetImg('ghost_house_bottom_m.png')
        ImageCache['GHBlockBottomR'] = SLib.GetImg('ghost_house_bottom_r.png')

    def dataChanged(self):
        super().dataChanged()

        self.width = ((self.parent.spritedata[8] & 0xF) * 16)+48
        self.height = ((self.parent.spritedata[9] & 0xF) * 16)+48
        if self.width / 16 == 0: self.width = 1
        if self.height / 16 == 0: self.height = 1

    def paint(self, painter):
        super().paint(painter)

        # Top of sprite.
        if self.width / 16 == 0:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHBlockTopM'])
        elif self.width / 16 == 1:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHBlockTopM'])
        elif self.width / 16 == 2:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHBlockTopL'])
            painter.drawTiledPixmap(60, 0, 60, 60, ImageCache['GHBlockTopR'])
        elif self.width / 16 == 3:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHBlockTopL'
            ])
            painter.drawTiledPixmap(60, 0, 60, 60, ImageCache['GHBlockTopM'])
            painter.drawTiledPixmap(120, 0, 60, 60, ImageCache['GHBlockTopR'])
        else:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHBlockTopL'
            ])
            painter.drawTiledPixmap(60, 0, (self.width / 16 - 2) * 60, 60, ImageCache['GHBlockTopM'])
            painter.drawTiledPixmap(60 + ((self.width / 16 - 2) * 60), 0, 60, 60, ImageCache['GHBlockTopR'])

        # Bottom
        if self.height / 16 > 1:
            if self.width / 16 == 0:
                painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHBlockBottomM'])
            elif self.width / 16 == 1:
                painter.drawTiledPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHBlockBottomM'])
            elif self.width / 16 == 2:
                painter.drawTiledPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHBlockBottomL'])
                painter.drawTiledPixmap(60, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHBlockBottomR'])
            elif self.width / 16 == 3:
                painter.drawTiledPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHBlockBottomL'
                ])
                painter.drawTiledPixmap(60, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHBlockBottomM'])
                painter.drawTiledPixmap(120, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHBlockBottomR'])
            else:
                painter.drawTiledPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHBlockBottomL'
                ])
                painter.drawTiledPixmap(60, (self.height / 16) * 60 - 60, (self.width / 16 - 2) * 60, 60,
                                        ImageCache['GHBlockBottomM'])
                painter.drawTiledPixmap(60 + ((self.width / 16 - 2) * 60), (self.height / 16) * 60 - 60, 60, 60,
                                   ImageCache['GHBlockBottomR'])

        # Left
        if self.height / 16 == 3:
            painter.drawTiledPixmap(0, 60, 60, 60, ImageCache['GHBlockMiddleL'])
        elif self.height / 16 > 3:
            painter.drawTiledPixmap(0, 60, 60, 60, ImageCache['GHBlockMiddleL'])
            painter.drawTiledPixmap(0, 120, 60, (self.height / 16 - 3) * 60, ImageCache['GHBlockMiddleL'])

        # Right
        if self.height / 16 == 3:
            painter.drawTiledPixmap((self.width / 16 * 60) - 60, 60, 60, 60, ImageCache['GHBlockMiddleR'])
        elif self.height / 16 > 3:
            painter.drawTiledPixmap((self.width / 16 * 60) - 60, 60, 60, 60, ImageCache['GHBlockMiddleR'])
            painter.drawTiledPixmap((self.width / 16 * 60) - 60, 120, 60, (self.height / 16 - 3) * 60,
                                    ImageCache['GHBlockMiddleR'])

        # Middle
        if self.width / 16 > 2:
            if self.height / 16 > 2:
                painter.drawTiledPixmap(60, 60, ((self.width / 16) - 2) * 60, ((self.height / 16) - 2) * 60,
                                        ImageCache['GHBlockMiddleM'])

        # 1 Glitch
        if self.width / 16 < 2:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHBlockTopM'])
            painter.drawTiledPixmap(0, 60, 60, ((self.height / 16) - 2) * 60, ImageCache['GHBlockMiddleM'])
            if self.height > 1:
                painter.drawTiledPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHBlockBottomM'])
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHBlockTopM'])


class SpriteImage_GhostTouchBlock(SLib.SpriteImage):  # 324
    def __init__(self, parent):
        super().__init__(parent, 3.75)

        self.spritebox.shown = False

    @staticmethod
    def loadImages():
        ImageCache['GHTouchTopL'] = SLib.GetImg('ghost_touch_top_l.png')
        ImageCache['GHTouchTopM'] = SLib.GetImg('ghost_touch_top_m.png')
        ImageCache['GHTouchTopR'] = SLib.GetImg('ghost_touch_top_r.png')
        ImageCache['GHTouchMiddleL'] = SLib.GetImg('ghost_touch_mid_l.png')
        ImageCache['GHTouchMiddleM'] = SLib.GetImg('ghost_touch_mid_m.png')
        ImageCache['GHTouchMiddleR'] = SLib.GetImg('ghost_touch_mid_r.png')
        ImageCache['GHTouchBottomL'] = SLib.GetImg('ghost_touch_bottom_l.png')
        ImageCache['GHTouchBottomM'] = SLib.GetImg('ghost_touch_bottom_m.png')
        ImageCache['GHTouchBottomR'] = SLib.GetImg('ghost_touch_bottom_r.png')

    def dataChanged(self):
        super().dataChanged()

        self.width = ((self.parent.spritedata[8] & 0xF) * 16)+32
        self.height = (self.parent.spritedata[4])+32
        if self.width / 16 == 0: self.width = 1
        if self.height / 16 == 0: self.height = 1

    def paint(self, painter):
        super().paint(painter)

        # Top of sprite.
        if self.width / 16 == 0:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHTouchTopM'])
        elif self.width / 16 == 1:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHTouchTopM'])
        elif self.width / 16 == 2:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHTouchTopL'])
            painter.drawTiledPixmap(60, 0, 60, 60, ImageCache['GHTouchTopR'])
        elif self.width / 16 == 3:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHTouchTopL'
            ])
            painter.drawTiledPixmap(60, 0, 60, 60, ImageCache['GHTouchTopM'])
            painter.drawTiledPixmap(120, 0, 60, 60, ImageCache['GHTouchTopR'])
        else:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHTouchTopL'
            ])
            painter.drawTiledPixmap(60, 0, (self.width / 16 - 2) * 60, 60, ImageCache['GHTouchTopM'])
            painter.drawTiledPixmap(60 + ((self.width / 16 - 2) * 60), 0, 60, 60, ImageCache['GHTouchTopR'])

        # Bottom
        if self.height / 16 > 1:
            if self.width / 16 == 0:
                painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHTouchBottomM'])
            elif self.width / 16 == 1:
                painter.drawTiledPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHTouchBottomM'])
            elif self.width / 16 == 2:
                painter.drawTiledPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHTouchBottomL'])
                painter.drawTiledPixmap(60, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHTouchBottomR'])
            elif self.width / 16 == 3:
                painter.drawTiledPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHTouchBottomL'
                ])
                painter.drawTiledPixmap(60, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHTouchBottomM'])
                painter.drawTiledPixmap(120, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHTouchBottomR'])
            else:
                painter.drawTiledPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHTouchBottomL'
                ])
                painter.drawTiledPixmap(60, (self.height / 16) * 60 - 60, (self.width / 16 - 2) * 60, 60,
                                        ImageCache['GHTouchBottomM'])
                painter.drawTiledPixmap(60 + ((self.width / 16 - 2) * 60), (self.height / 16) * 60 - 60, 60, 60,
                                   ImageCache['GHTouchBottomR'])

        # Left
        if self.height / 16 == 3:
            painter.drawTiledPixmap(0, 60, 60, 60, ImageCache['GHTouchMiddleL'])
        elif self.height / 16 > 3:
            painter.drawTiledPixmap(0, 60, 60, 60, ImageCache['GHTouchMiddleL'])
            painter.drawTiledPixmap(0, 120, 60, (self.height / 16 - 3) * 60, ImageCache['GHTouchMiddleL'])

        # Right
        if self.height / 16 == 3:
            painter.drawTiledPixmap((self.width / 16 * 60) - 60, 60, 60, 60, ImageCache['GHTouchMiddleR'])
        elif self.height / 16 > 3:
            painter.drawTiledPixmap((self.width / 16 * 60) - 60, 60, 60, 60, ImageCache['GHTouchMiddleR'])
            painter.drawTiledPixmap((self.width / 16 * 60) - 60, 120, 60, (self.height / 16 - 3) * 60,
                                    ImageCache['GHTouchMiddleR'])

        # Middle
        if self.width / 16 > 2:
            if self.height / 16 > 2:
                painter.drawTiledPixmap(60, 60, ((self.width / 16) - 2) * 60, ((self.height / 16) - 2) * 60,
                                        ImageCache['GHTouchMiddleM'])

        # 1 Glitch
        if self.width / 16 < 2:
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHTouchTopM'])
            painter.drawTiledPixmap(0, 60, 60, ((self.height / 16) - 2) * 60, ImageCache['GHTouchMiddleM'])
            if self.height > 1:
                painter.drawTiledPixmap(0, (self.height / 16) * 60 - 60, 60, 60, ImageCache['GHTouchBottomM'])
            painter.drawTiledPixmap(0, 0, 60, 60, ImageCache['GHTouchTopM'])
	

			
			
class SpriteImage_SledgeBro(SLib.SpriteImage_Static):  # 77
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['SledgeBro'],
        )

        self.yOffset = -32
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('SledgeBro', 'sledge_bro.png')

		
class SpriteImage_UpDownSpiny(SLib.SpriteImage_Static):  # 24
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['UpDownSpiny'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('UpDownSpiny', 'up_down_spiny.png')
		
		
class SpriteImage_MovingDesertBlock(SLib.SpriteImage_Static):  # 549
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['MovingDesertBlock'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('MovingDesertBlock', 'desert_block.png')
		
		
class SpriteImage_Tendril(SLib.SpriteImage_StaticMultiple):  # 425
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('TendrilLeftShort', 'tendril_left_short.png')
        SLib.loadIfNotInImageCache('TendrilLeftLong', 'tendril_left_long.png')
        SLib.loadIfNotInImageCache('TendrilRightShort', 'tendril_right_short.png')
        SLib.loadIfNotInImageCache('TendrilRightLong', 'tendril_right_long.png')
    def dataChanged(self):

        spawntype = self.parent.spritedata[4]

        if spawntype == 0:
            self.image = ImageCache['TendrilRightLong']
            self.xOffset = -8
            self.yOffset = -40
        elif spawntype == 1:
            self.image = ImageCache['TendrilRightShort']
            self.xOffset = -8
            self.yOffset = -40
        elif spawntype == 16:
            self.image = ImageCache['TendrilLeftLong']
            self.xOffset = -180
            self.yOffset = -40
        elif spawntype == 17:
            self.image = ImageCache['TendrilLeftShort']
            self.xOffset = -116
            self.yOffset = -40
			
        super().dataChanged()
		


class SpriteImage_BeanStalkLeaf(SLib.SpriteImage_StaticMultiple):  # 396
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BLeaf_L_Small', 'bleaf_l_small.png')
        SLib.loadIfNotInImageCache('BLeaf_L_Medium', 'bleaf_l_medium.png')
        SLib.loadIfNotInImageCache('BLeaf_L_Big', 'bleaf_l_big.png')
        SLib.loadIfNotInImageCache('BLeaf_R_Small', 'bleaf_r_small.png')
        SLib.loadIfNotInImageCache('BLeaf_R_Medium', 'bleaf_r_medium.png')
        SLib.loadIfNotInImageCache('BLeaf_R_Big', 'bleaf_r_big.png')
    def dataChanged(self):

        spawntype = (self.parent.spritedata[8] & 0xf)+(self.parent.spritedata[5] & 0xf)*16
         
        if spawntype == 0:
            self.image = ImageCache['BLeaf_L_Small']
            self.xOffset = -48
            self.yOffset = -16
        elif spawntype == 1:
            self.image = ImageCache['BLeaf_L_Medium']
            self.xOffset = -96
            self.yOffset = -16
        elif spawntype == 2:
            self.image = ImageCache['BLeaf_L_Big']
            self.xOffset = -144
            self.yOffset = -16
        elif spawntype == 16:
            self.image = ImageCache['BLeaf_R_Small']
            self.xOffset = 0
            self.yOffset = -16
        elif spawntype == 17:
            self.image = ImageCache['BLeaf_R_Medium']
            self.xOffset = 0
            self.yOffset = -16
        elif spawntype == 18:
            self.image = ImageCache['BLeaf_R_Big']
            self.xOffset = 0
            self.yOffset = -16
			
        super().dataChanged()


class SpriteImage_JellyBeam(SLib.SpriteImage_Static):  # 276
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['JellyBeam'],
        )

        self.yOffset = -8
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('JellyBeam', 'jelly_beam.png')


class SpriteImage_Bulber(SLib.SpriteImage_Static):  # 321
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Bulber'],
        )

        self.yOffset = -16
        self.xOffset = -16

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Bulber', 'bulber.png')	


class SpriteImage_EnviromentalSFX(SLib.SpriteImage_Static):  # 384
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['EnviromentalSFX'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('EnviromentalSFX', 'sfx.png')


class SpriteImage_ZoneTrigger(SLib.SpriteImage_Static):  # 36
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ZoneTrigger'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ZoneTrigger', 'zone_trigger.png')


class SpriteImage_And(SLib.SpriteImage_Static):  # 37
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['And'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('And', 'and.png')


class SpriteImage_Or(SLib.SpriteImage_Static):  # 38
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Or'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Or', 'or.png')


class SpriteImage_Random(SLib.SpriteImage_Static):  # 39
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Random'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Random', 'ra.png')	


class SpriteImage_Chain(SLib.SpriteImage_Static):  # 40
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Chain'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Chain', 'chain.png')


class SpriteImage_Multi(SLib.SpriteImage_Static):  # 42
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Multi'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Multi', 'multi.png')	


class SpriteImage_Timed(SLib.SpriteImage_Static):  # 43
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Timed'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Timed', 'timed.png')


class SpriteImage_Path(SLib.SpriteImage_Static):  # 100
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Path'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Path', 'path.png')


class SpriteImage_CannonBall(SLib.SpriteImage_StaticMultiple):  # 179
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('CannonBallSmall', 'cannonball_small.png')
        SLib.loadIfNotInImageCache('CannonBallBig', 'cannonball_big.png')
    def dataChanged(self):

        size = self.parent.spritedata[5] & 0xf

        if size == 0:
            self.image = ImageCache['CannonBallSmall']
            self.xOffset = 0
            self.yOffset = 0
        elif size == 1:
            self.image = ImageCache['CannonBallBig']
            self.xOffset = -16
            self.yOffset = -16
			
        super().dataChanged()


class SpriteImage_Line(SLib.SpriteImage_Static):  # 196
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Line'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Line', 'line.png')


class SpriteImage_WendyBattleFloor(SLib.SpriteImage_Static):  # 560
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['WendyBattleFloor'],
        )

        self.yOffset = -224
        self.xOffset = -208

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('WendyBattleFloor', 'wendy_floor.png')


class SpriteImage_SandPillar(SLib.SpriteImage_StaticMultiple):  # 123
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('SandPillar0', 'sandpillar_0.png')
        SLib.loadIfNotInImageCache('SandPillar1', 'sandpillar_1.png')
        SLib.loadIfNotInImageCache('SandPillar2', 'sandpillar_2.png')
        SLib.loadIfNotInImageCache('SandPillar3', 'sandpillar_3.png')
    def dataChanged(self):

        size = (self.parent.spritedata[5] >> 4)

        if size == 0:
            self.image = ImageCache['SandPillar0']
            self.xOffset = -24
            self.yOffset = -160
        elif size == 1:
            self.image = ImageCache['SandPillar1']
            self.xOffset = -24
            self.yOffset = -256
        elif size == 2:
            self.image = ImageCache['SandPillar2']
            self.xOffset = -24
            self.yOffset = -64
        elif size == 3:
            self.image = ImageCache['SandPillar3']
            self.xOffset = -24
            self.yOffset = -208
			
        super().dataChanged()


class SpriteImage_LightningBolt(SLib.SpriteImage_Static):  # 594
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['LightningBolt'],
        )

        self.yOffset = -16

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('LightningBolt', 'lightning_bolt.png')


class SpriteImage_MediumEepCheep(SLib.SpriteImage_Static):  # 591
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['MediumEepCheep'],
        )

        self.yOffset = -6

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('MediumEepCheep', 'medium_eep_cheep.png')


class SpriteImage_EepCheep(SLib.SpriteImage_Static):  # 590
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['EepCheep'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('EepCheep', 'eep_cheep.png')



class SpriteImage_GrassFlowerSetter(SLib.SpriteImage_StaticMultiple):  # 564
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('FlowerForest', 'flower_forest.png')
        SLib.loadIfNotInImageCache('FlowerUnderground', 'flower_underground.png')
        SLib.loadIfNotInImageCache('FlowerSky', 'flower_sky.png')
        SLib.loadIfNotInImageCache('FlowerOverworld', 'flower_overworld.png')
    def dataChanged(self):

        size = self.parent.spritedata[5]

        if size == 0:
            self.image = ImageCache['FlowerForest']
        elif size == 2:
            self.image = ImageCache['FlowerUnderground']
        elif size == 4:
            self.image = ImageCache['FlowerSky']
        elif size == 5:
            self.image = ImageCache['FlowerOverworld']

			
        super().dataChanged()


class SpriteImage_SnowBoxes(SLib.SpriteImage_StaticMultiple):  # 444
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('SnowBoxes1', 'snowbox_1.png')
        SLib.loadIfNotInImageCache('SnowBoxes2', 'snowbox_2.png')
        SLib.loadIfNotInImageCache('SnowBoxes3', 'snowbox_3.png')
    def dataChanged(self):

        size = self.parent.spritedata[5]

        if size == 0:
            self.image = ImageCache['SnowBoxes1']
            self.xOffset = -8
            self.yOffset = 24
        elif size == 2:
            self.image = ImageCache['SnowBoxes2']
            self.xOffset = -8
            self.yOffset = -24
        elif size == 3:
            self.image = ImageCache['SnowBoxes3']
            self.xOffset = -8
            self.yOffset = -72

			
        super().dataChanged()


class SpriteImage_Toad(SLib.SpriteImage_Static):  # 408
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Toad'],
        )

        self.yOffset = -32
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Toad', 'toad.png')	


class SpriteImage_LavaGeyser(SLib.SpriteImage_StaticMultiple):  # 207
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('LavaGeyser0', 'lava_geyser_11.png')
        SLib.loadIfNotInImageCache('LavaGeyser1', 'lava_geyser_10.png')
        SLib.loadIfNotInImageCache('LavaGeyser2', 'lava_geyser_9.png')
        SLib.loadIfNotInImageCache('LavaGeyser3', 'lava_geyser_8.png')
        SLib.loadIfNotInImageCache('LavaGeyser4', 'lava_geyser_7.png')
        SLib.loadIfNotInImageCache('LavaGeyser5', 'lava_geyser_6.png')
        SLib.loadIfNotInImageCache('LavaGeyser6', 'lava_geyser_2.png')
    def dataChanged(self):

        size = round(self.parent.spritedata[4]/16)

        if size == 0:
            self.image = ImageCache['LavaGeyser0']
            self.xOffset = -16
            self.yOffset = -168
        elif size == 1:
            self.image = ImageCache['LavaGeyser1']
            self.xOffset = -16
            self.yOffset = -152
        elif size == 2:
            self.image = ImageCache['LavaGeyser2']
            self.xOffset = -16
            self.yOffset = -136
        elif size == 3:
            self.image = ImageCache['LavaGeyser3']
            self.xOffset = -16
            self.yOffset = -120
        elif size == 4:
            self.image = ImageCache['LavaGeyser4']
            self.xOffset = -16
            self.yOffset = -104
        elif size == 5:
            self.image = ImageCache['LavaGeyser5']
            self.xOffset = -16
            self.yOffset = -88
        elif size == 6:
            self.image = ImageCache['LavaGeyser6']
            self.xOffset = -16
            self.yOffset = -24

			
        super().dataChanged()


class SpriteImage_IceBro(SLib.SpriteImage_Static):  # 75
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['IceBro'],
        )

        self.yOffset = -24
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('IceBro', 'ice_bro.png')	


class SpriteImage_HammerBro(SLib.SpriteImage_Static):  # 76
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['HammerBro'],
        )

        self.yOffset = -24
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('HammerBro', 'hammer_bro.png')	


class SpriteImage_FireBro(SLib.SpriteImage_Static):  # 79
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['FireBro'],
        )

        self.yOffset = -24
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('FireBro', 'fire_bro.png')	


class SpriteImage_BoomerangBro(SLib.SpriteImage_Static):  # 78
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BoomerangBro'],
        )

        self.yOffset = -24
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BoomerangBro', 'boomerang_bro.png')
		
		
class SpriteImage_RollingIce(SLib.SpriteImage_StaticMultiple):  # 539
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('RollingIce', '15x15 iceblock.png')

    def dataChanged(self):
        super().dataChanged()

        self.height = (self.parent.spritedata[8] & 0xF) * 16
        self.width = (self.parent.spritedata[9] & 0xF) * 16
        if self.height == 0 : self.height = 16
        if self.width == 0 : self.width = 16
        self.image = ImageCache['RollingIce'].scaled(self.width*3.75, self.height*3.75)
        self.yOffset = (self.height)*-1
		
		
class SpriteImage_RockyWrench(SLib.SpriteImage_Static):  # 536
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['RockyWrench'],
            (-3, -40),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('RockyWrench', 'rocky_wrench.png')
		
		
class SpriteImage_LudwigPlatform2(SLib.SpriteImage_StaticMultiple):  # 428
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['LudwigPlatform2L'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('LudwigPlatform2L', 'ludwig_platform_2_l.png')
        SLib.loadIfNotInImageCache('LudwigPlatform2M', 'ludwig_platform_2_m.png')
        SLib.loadIfNotInImageCache('LudwigPlatform2R', 'ludwig_platform_2_r.png')

    def dataChanged(self):
        super().dataChanged()

        self.width = (self.parent.spritedata[8])
        self.xOffset = 0
        self.yOffset = 0


        self.width = self.width*16+48

    def paint(self, painter):
        super().paint(painter)

        if self.parent.spritedata[8] > -1:
            painter.drawTiledPixmap(60, 0,self.width*3.75 , 120, ImageCache['LudwigPlatform2M'])
            painter.drawPixmap(0, 0, ImageCache['LudwigPlatform2L'])
            painter.drawPixmap((self.width - 16) * 3.75, 0, ImageCache['LudwigPlatform2R'])
			
			
class SpriteImage_LudwigPlatform(SLib.SpriteImage_StaticMultiple):  # 410
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,				
        )

 

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('LudwigPlatform11', 'ludwig_platform_1_1.png') 
        SLib.loadIfNotInImageCache('LudwigPlatform12', 'ludwig_platform_1_2.png')
        SLib.loadIfNotInImageCache('LudwigPlatform13', 'ludwig_platform_1_3.png')

    def dataChanged(self):

        spawntype = self.parent.spritedata[4]

        if spawntype == 0:
            self.image = ImageCache['LudwigPlatform11']
        elif spawntype == 1:
            self.image = ImageCache['LudwigPlatform12']
        elif spawntype == 2:
            self.image = ImageCache['LudwigPlatform13']


        super().dataChanged()

class SpriteImage_Spotlight(SLib.SpriteImage_Static):  # 153
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Spotlight'],
        )

        self.yOffset = -64

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Spotlight', 'spotlight.png')
		
		
class SpriteImage_ClimablePole(SLib.SpriteImage_StaticMultiple):  # 294
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ClimablePoleU'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('ClimablePoleU', 'climable_pole_up.png')
        SLib.loadIfNotInImageCache('ClimablePoleM', 'climable_pole_mid.png')
        SLib.loadIfNotInImageCache('ClimablePoleD', 'climable_pole_down.png')

    def dataChanged(self):
        super().dataChanged()

        self.height = self.parent.spritedata[5]
        self.yOffset = -8
        self.height = self.height*16 + 64

    def paint(self, painter):
        super().paint(painter)
        painter.drawPixmap(0, 0, ImageCache['ClimablePoleU'])
        painter.drawPixmap(0,(self.height - 16) * 3.75, ImageCache['ClimablePoleD'])
        painter.drawTiledPixmap(0, 60, 60,(self.height - 32) * 3.75, ImageCache['ClimablePoleM'])
		
		
class SpriteImage_WaterGeyser(SLib.SpriteImage_StaticMultiple):  # 156
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('WaterGeyserTop', 'water_geyser_top.png')
        SLib.loadIfNotInImageCache('WaterGeyserBottom', 'water_geyser_bottom.png')

    def dataChanged(self):
        super().dataChanged()

        self.height = (self.parent.spritedata[5] >> 4) + (self.parent.spritedata[4]*16)
        if self.height > 255 :
             self.height = self.height - 256
        self.bleh = round(self.parent.spritedata[3]/16)
        self.bleh2 = self.parent.spritedata[8]
        self.yOffset = -72-self.height*8
        self.height = self.height*16 + 16
        self.actualwidth = 10
        if self.bleh == 0:
            self.actualwidth = 6
        if self.bleh == 1:
            self.actualwidth = 3
        if self.bleh == 2:
            self.actualwidth = 4.5
        if self.bleh == 3:
            self.actualwidth = 6
        if self.bleh == 4:
            self.actualwidth = 8
        if self.bleh == 5:
            self.actualwidth = 9.5
        if self.bleh == 6:
            self.actualwidth = 11.5
        if self.bleh == 7:
            self.actualwidth = 13
        if self.bleh == 8:
            self.actualwidth = 15
        if self.bleh == 9:
            self.actualwidth = 16
        if self.bleh == 10:
            self.actualwidth = 17.5
        if self.bleh == 11:
            self.actualwidth = 19
        if self.bleh == 12:
            self.actualwidth = 20.5
        if self.bleh == 13:
            self.actualwidth = 22
        if self.bleh == 14:
            self.actualwidth = 24
        if self.bleh == 15:
            self.actualwidth = 26
        if self.bleh2 == 1:
            self.actualwidth = 2.5
        self.xOffset = -self.actualwidth*8 +8
        self.width = self.actualwidth*16

    def paint(self, painter):
        super().paint(painter)
        painter.drawPixmap(self.actualwidth*10, 60, self.actualwidth*40,(self.height - 32) * 3.75, ImageCache['WaterGeyserBottom'])
        painter.drawPixmap(0, 0, self.actualwidth*60, 180, ImageCache['WaterGeyserTop'])
		
		
class SpriteImage_WaterGeyserLocation(SLib.SpriteImage_StaticMultiple):  # 163
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('WaterGeyserTop', 'water_geyser_top.png')
        SLib.loadIfNotInImageCache('WaterGeyserBottom', 'water_geyser_bottom.png')

    def dataChanged(self):
        super().dataChanged()

        self.height = (self.parent.spritedata[5] >> 4)
        if self.height > 255 :
             self.height = self.height - 256
        self.bleh = round(self.parent.spritedata[3]/16)
        self.bleh2 = self.parent.spritedata[8]
        self.yOffset = -72-self.height*8
        self.height = self.height*16 + 16
        self.actualwidth = 10
        if self.bleh == 0:
            self.actualwidth = 6
        if self.bleh == 1:
            self.actualwidth = 3
        if self.bleh == 2:
            self.actualwidth = 4.5
        if self.bleh == 3:
            self.actualwidth = 6
        if self.bleh == 4:
            self.actualwidth = 8
        if self.bleh == 5:
            self.actualwidth = 9.5
        if self.bleh == 6:
            self.actualwidth = 11.5
        if self.bleh == 7:
            self.actualwidth = 13
        if self.bleh == 8:
            self.actualwidth = 15
        if self.bleh == 9:
            self.actualwidth = 16
        if self.bleh == 10:
            self.actualwidth = 17.5
        if self.bleh == 11:
            self.actualwidth = 19
        if self.bleh == 12:
            self.actualwidth = 20.5
        if self.bleh == 13:
            self.actualwidth = 22
        if self.bleh == 14:
            self.actualwidth = 24
        if self.bleh == 15:
            self.actualwidth = 26
        if self.bleh2 == 1:
            self.actualwidth = 2.5
        self.xOffset = -self.actualwidth*8 +8
        self.width = self.actualwidth*16

    def paint(self, painter):
        super().paint(painter)
        painter.drawPixmap(self.actualwidth*10, 60, self.actualwidth*40,(self.height - 32) * 3.75, ImageCache['WaterGeyserBottom'])
        painter.drawPixmap(0, 0, self.actualwidth*60, 180, ImageCache['WaterGeyserTop'])
		
		
		
class SpriteImage_Sledge_Block(SLib.SpriteImage_Static):  # 327
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Sledge'],
        )

        self.yOffset = -8
        self.xOffset = -32

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Sledge', 'sledge.png')
		
		
class SpriteImage_PipePiranhaUpFire(SLib.SpriteImage_Static):  # 6
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['PipePiranhaUpFire'],
            (0, -32),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('PipePiranhaUpFire', 'firetrap_pipe_up.png')


class SpriteImage_PipePiranhaDownFire(SLib.SpriteImage_Static):  # 7
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['PipePiranhaDownFire'],
            (0, 32),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('PipePiranhaDownFire', 'firetrap_pipe_down.png')


class SpriteImage_PipePiranhaLeftFire(SLib.SpriteImage_Static):  # 8
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['PipePiranhaLeftFire'],
            (-32, 0),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('PipePiranhaLeftFire', 'firetrap_pipe_left.png')


class SpriteImage_PipePiranhaRightFire(SLib.SpriteImage_Static):  # 9
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['PipePiranhaRightFire'],
            (32, 0),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('PipePiranhaRightFire', 'firetrap_pipe_right.png')
		
		
class SpriteImage_Foo(SLib.SpriteImage_Static):  # 229
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Foo'],
        )

        self.yOffset = -16
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Foo', 'foo.png')
		
		
class SpriteImage_CheepCheep(SLib.SpriteImage_Static):  # 101
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['CheepCheep'],
            (-1, -2),
        )
        self.aux.append(SLib.AuxiliaryRectOutline(parent, 0, 0))

    def dataChanged(self):
        super().dataChanged()

        nybbleWidth = self.parent.spritedata[3] & 0xF

        width = nybbleWidth * 120 + 120

        offsetX = -(nybbleWidth * 60 + 26.25)

        self.aux[0].setSize(width, 60, offsetX, 7.5)

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('CheepCheep', 'cheep_cheep.png')
		
		
class SpriteImage_MontyMole(SLib.SpriteImage_Static):  # 51
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['MontyMole'],
        )

        self.xOffset = -8
        self.yOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('MontyMole', 'monty_mole.png')
		
		
class SpriteImage_GreenCoin(SLib.SpriteImage_Static):  # 50
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['GreenCoin'],
        )

        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GreenCoin', 'green_coins.png')
		
		
		
class SpriteImage_ScalePlatform(SLib.SpriteImage_StaticMultiple):  # 309
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('HMovPlatNL', 'wood_platform_left.png')
        SLib.loadIfNotInImageCache('HMovPlatNM', 'wood_platform_middle.png')
        SLib.loadIfNotInImageCache('HMovPlatNR', 'wood_platform_right.png')
        SLib.loadIfNotInImageCache('HMovPlatSL', 'wood_platform_snow_left.png')
        SLib.loadIfNotInImageCache('HMovPlatSM', 'wood_platform_snow_middle.png')
        SLib.loadIfNotInImageCache('HMovPlatSR', 'wood_platform_snow_right.png')
        SLib.loadIfNotInImageCache('ScalePulley', 'scale_pulley.png')
        SLib.loadIfNotInImageCache('ScaleRopeVert', 'scale_rope_vert.png')
        SLib.loadIfNotInImageCache('ScaleRopeHor', 'scale_rope_horz.png')

    def dataChanged(self):
## https://en.wikipedia.org/wiki/Spaghetti_code
        super().dataChanged()
        self.RopeLengthLeft = (self.parent.spritedata[4] & 0xF) + 0.5
        self.ropeWidth = (self.parent.spritedata[5] & 0xF) + 0.5
        self.RopeLengthRight = self.parent.spritedata[5] + 8
        self.PlatformWidthLeft = (self.parent.spritedata[8] & 0xf) + 3
        self.PlatformWidthRight = (self.parent.spritedata[9]) + 48
        self.additionalwidth = 0
        self.RopeLengthLeft *= 16
        self.PlatformWidthLeft *= 16
        self.RopeLengthRight = self.RopeLengthRight - self.ropeWidth + 0.5
        self.ropeWidth =self.ropeWidth * 16
        self.height = self.RopeLengthRight + 12
        if self.RopeLengthRight > self.RopeLengthLeft : 
         self.height = self.RopeLengthRight + 12	
        elif self.RopeLengthLeft > self.RopeLengthRight : 
         self.height = self.RopeLengthLeft + 12
        self.customOffset = self.PlatformWidthLeft / 2    		
        self.yOffset = -12
        self.xOffset = -4 - self.customOffset
        if  (self.PlatformWidthLeft / 2) > self.ropeWidth :
             self.additionalwidth = self.ropeWidth-self.PlatformWidthLeft / 2 - 4		
        self.width = self.ropeWidth  + self.customOffset - self.additionalwidth + self.PlatformWidthRight / 2
    def paint(self, painter):
        super().paint(painter)
        painter.drawTiledPixmap(-15 + self.customOffset*3.75, 30, 60,(self.RopeLengthLeft) * 3.75 -45, ImageCache['ScaleRopeVert'])
        painter.drawTiledPixmap(self.ropeWidth * 3.75 -45 + + self.customOffset*3.75, 30, 60,(self.RopeLengthRight) * 3.75 -45, ImageCache['ScaleRopeVert'])
        painter.drawTiledPixmap(30 + self.customOffset*3.75, -15, (self.ropeWidth) * 3.75 -60, 60 , ImageCache['ScaleRopeHor'])
        painter.drawPixmap(self.customOffset*3.75, 0, ImageCache['ScalePulley'])
        painter.drawPixmap(self.ropeWidth * 3.75 -45 + + self.customOffset*3.75, 0, ImageCache['ScalePulley'])

        painter.drawPixmap(15, self.RopeLengthLeft * 3.75 - 15, ImageCache['HMovPlatNL'])
        painter.drawPixmap((self.PlatformWidthLeft - 16) * 3.75 + 15, self.RopeLengthLeft * 3.75 - 15, ImageCache['HMovPlatNR'])
        painter.drawTiledPixmap(75, self.RopeLengthLeft * 3.75 - 15, (self.PlatformWidthLeft - 32) * 3.75, 60, ImageCache['HMovPlatNM'])
		
        painter.drawPixmap(-15 +self.ropeWidth * 3.75 + self.customOffset*3.75 - self.PlatformWidthRight * 1.875, self.RopeLengthRight * 3.75 - 15, ImageCache['HMovPlatNL'])
        painter.drawPixmap(-15 +(self.PlatformWidthRight - 16) * 3.75 +  self.ropeWidth * 3.75 + self.customOffset*3.75 - self.PlatformWidthRight * 1.875, self.RopeLengthRight * 3.75 - 15, ImageCache['HMovPlatNR'])
        painter.drawTiledPixmap(45 + self.ropeWidth * 3.75 + self.customOffset*3.75 - self.PlatformWidthRight * 1.875, self.RopeLengthRight * 3.75 - 15 , (self.PlatformWidthRight - 32) * 3.75, 60, ImageCache['HMovPlatNM'])
			
		
		
		
class SpriteImage_HorizontalMovingPlatform(SLib.SpriteImage_StaticMultiple):  # 186
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('HMovPlatNL', 'wood_platform_left.png')
        SLib.loadIfNotInImageCache('HMovPlatNM', 'wood_platform_middle.png')
        SLib.loadIfNotInImageCache('HMovPlatNR', 'wood_platform_right.png')
        SLib.loadIfNotInImageCache('HMovPlatSL', 'wood_platform_snow_left.png')
        SLib.loadIfNotInImageCache('HMovPlatSM', 'wood_platform_snow_middle.png')
        SLib.loadIfNotInImageCache('HMovPlatSR', 'wood_platform_snow_right.png')
        SLib.loadIfNotInImageCache('HMovPlatRL', 'metal_platform_left.png')
        SLib.loadIfNotInImageCache('HMovPlatRM', 'metal_platform_middle.png')
        SLib.loadIfNotInImageCache('HMovPlatRR', 'metal_platform_right.png')

    def dataChanged(self):
        super().dataChanged()

        type_ = (self.parent.spritedata[3] >> 4) & 0x3
        self.platformwidth = (self.parent.spritedata[8] & 0xF) + 1
        self.distance = round((self.parent.spritedata[7] / 16) -0.4)
        self.thing = (self.parent.spritedata[3] & 0xF) * 0.5

        if self.platformwidth == 1:
            self.platformwidth = 2

        self.platformwidth *= 16

        self.distance = self.distance * 60
        self.width = self.platformwidth + (self.distance) / 3.75
        self.xOffset = self.distance / 3.75 * self.thing * -2        
        self.imgType = 'N'

        if type_ == 1:
            self.imgType = 'R'

        elif type_ == 3:
            self.imgType = 'S'

    def paint(self, painter):
        super().paint(painter)
        painter.setOpacity(1 - self.thing)
        painter.drawPixmap(0, 0, ImageCache['HMovPlat%sL' % self.imgType])
        painter.drawPixmap((self.platformwidth - 16) * 3.75, 0, ImageCache['HMovPlat%sR' % self.imgType])

        if self.width > 32:
            painter.drawTiledPixmap(60, 0, (self.platformwidth - 32) * 3.75, 60, ImageCache['HMovPlat%sM' % self.imgType])
			
        painter.setOpacity(0.5 + self.thing)

        painter.drawPixmap(self.distance, 0, ImageCache['HMovPlat%sL' % self.imgType])
        painter.drawPixmap((self.platformwidth - 16) * 3.75 + self.distance, 0, ImageCache['HMovPlat%sR' % self.imgType])

        if self.width > 32:
            painter.drawTiledPixmap(60 + self.distance, 0, (self.platformwidth - 32) * 3.75, 60, ImageCache['HMovPlat%sM' % self.imgType])
			
			
class SpriteImage_VerticalMovingPlatform(SLib.SpriteImage_StaticMultiple):  # 182
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('VMovPlatNL', 'wood_platform_left.png')
        SLib.loadIfNotInImageCache('VMovPlatNM', 'wood_platform_middle.png')
        SLib.loadIfNotInImageCache('VMovPlatNR', 'wood_platform_right.png')
        SLib.loadIfNotInImageCache('VMovPlatSL', 'wood_platform_snow_left.png')
        SLib.loadIfNotInImageCache('VMovPlatSM', 'wood_platform_snow_middle.png')
        SLib.loadIfNotInImageCache('VMovPlatSR', 'wood_platform_snow_right.png')
        SLib.loadIfNotInImageCache('VMovPlatRL', 'metal_platform_left.png')
        SLib.loadIfNotInImageCache('VMovPlatRM', 'metal_platform_middle.png')
        SLib.loadIfNotInImageCache('VMovPlatRR', 'metal_platform_right.png')

    def dataChanged(self):
        super().dataChanged()

        type_ = (self.parent.spritedata[3] >> 4) & 0x3
        self.platformwidth = (self.parent.spritedata[8] & 0xF) + 1
        self.distance = round((self.parent.spritedata[7] / 16) -0.4)
        self.thing = 0.5 + (self.parent.spritedata[3] & 0xF) * -0.5

        if self.platformwidth == 1:
            self.platformwidth = 2

        self.platformwidth *= 16
        self.width = self.platformwidth
        self.distance = self.distance * 60
        self.height = 16 + (self.distance) / 3.75
        self.yOffset = self.distance / 3.75 * self.thing * -2        
        self.imgType = 'N'

        if type_ == 1:
            self.imgType = 'R'

        elif type_ == 3:
            self.imgType = 'S'

    def paint(self, painter):
        super().paint(painter)
        painter.setOpacity(1 - self.thing)
        painter.drawPixmap(0, 0, ImageCache['VMovPlat%sL' % self.imgType])
        painter.drawPixmap((self.platformwidth - 16) * 3.75, 0, ImageCache['VMovPlat%sR' % self.imgType])

        if self.width > 32:
            painter.drawTiledPixmap(60, 0, (self.platformwidth - 32) * 3.75, 60, ImageCache['VMovPlat%sM' % self.imgType])
			
        painter.setOpacity(0.5 + self.thing)

        painter.drawPixmap(0, self.distance, ImageCache['VMovPlat%sL' % self.imgType])
        painter.drawPixmap((self.platformwidth - 16) * 3.75, self.distance, ImageCache['VMovPlat%sR' % self.imgType])

        if self.width > 32:
            painter.drawTiledPixmap(60, self.distance, (self.platformwidth - 32) * 3.75, 60, ImageCache['VMovPlat%sM' % self.imgType])

class SpriteImage_PricklyGoomba(SLib.SpriteImage_Static):  # 247
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['PricklyGoomba'],
        )

        self.yOffset = -13
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('PricklyGoomba', 'prickly_goomba.png')


class SpriteImage_Fliprus(SLib.SpriteImage_StaticMultiple):  # 441
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.yOffset = -96
        self.xOffset = -8

    @staticmethod
    def loadImages():
        if "FliprusL" not in ImageCache:
            fliprus = SLib.GetImg('fliprus.png', True)
            ImageCache['FliprusL'] = QtGui.QPixmap.fromImage(fliprus)
            ImageCache['FliprusR'] = QtGui.QPixmap.fromImage(fliprus.mirrored(True, False))

    def dataChanged(self):
        direction = self.parent.spritedata[4]

        if direction == 0:
            self.image = ImageCache['FliprusL']
        elif direction == 1:
            self.image = ImageCache['FliprusR']
        elif direction == 2:
            self.image = ImageCache['FliprusL']
        else:
            self.image = ImageCache['FliprusL']

        super().dataChanged()	


class SpriteImage_StalkingPiranha(SLib.SpriteImage_Static):  # 63
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['StalkingPiranha'],
        )

        self.yOffset = -56
        self.xOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('StalkingPiranha', 'stalking_piranha.png')
		
		
class SpriteImage_Spike(SLib.SpriteImage_Static):  # 180
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Spike'],
            (-9, -32),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Spike', 'spike.png')
		
		
class SpriteImage_SteerablePlatform(SLib.SpriteImage_Static):  # 553
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['SteerablePlatform'],
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('SteerablePlatform', 'steerable_platform.png')
		
		
class SpriteImage_NabbitPlacement(SLib.SpriteImage_Static):  # 451
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['NabbitP'],
            (-16, -24),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('NabbitP', 'nabbit_placement.png')
		
		
class SpriteImage_NabbitPrize(SLib.SpriteImage_Static):  # 569
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['NabbitPrize'],
            (40, -16),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('NabbitPrize', 'nabbit_prize.png')

		
class SpriteImage_Bramball(SLib.SpriteImage_Static):  # 336
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Bramball'],
        )

        self.xOffset = -30
        self.yOffset = -48

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Bramball', 'bramball.png')
		
		
class SpriteImage_GiantThwomp(SLib.SpriteImage_Static):  # 136
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['GiantThwomp'],
        )

        self.xOffset = -8
        self.yOffset = -8

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GiantThwomp', 'thwomp_giant.png')
		

		
ImageClasses = {
    0  : SpriteImage_Goomba,
    1  : SpriteImage_Paragoomba,
    6  : SpriteImage_PipePiranhaUpFire,
    7  : SpriteImage_PipePiranhaDownFire,
    8  : SpriteImage_PipePiranhaLeftFire,
    9  : SpriteImage_PipePiranhaRightFire,
    10 : SpriteImage_PipePiranhaUpFire,
    11 : SpriteImage_PipePiranhaDownFire,
    12 : SpriteImage_PipePiranhaLeftFire,
    13 : SpriteImage_PipePiranhaRightFire,
    24 : SpriteImage_UpDownSpiny,
    36 : SpriteImage_ZoneTrigger,
    37 : SpriteImage_And,
    38 : SpriteImage_Or,
    39 : SpriteImage_Random,
    40 : SpriteImage_Chain,
    42 : SpriteImage_Multi,
    43 : SpriteImage_Timed,
    44 : SpriteImage_RedRing,
    50 : SpriteImage_GreenCoin,
    51 : SpriteImage_MontyMole,
    63 : SpriteImage_StalkingPiranha,
    75 : SpriteImage_IceBro,
    76 : SpriteImage_HammerBro,
    77 : SpriteImage_SledgeBro,
    78 : SpriteImage_BoomerangBro,
    79 : SpriteImage_FireBro,
    80 : SpriteImage_IronBlock,
    81 : SpriteImage_MovingAcornBlock,
    100: SpriteImage_Path,
    101: SpriteImage_CheepCheep,
    123: SpriteImage_SandPillar,
    125: SpriteImage_BulletBill,
    126: SpriteImage_BanzaiBill,
    127: SpriteImage_BullsEyeBill,
    128: SpriteImage_BullsEyeBanzaiBill,
    132: SpriteImage_RectanglePlatforms,
    136: SpriteImage_GiantThwomp,
    153: SpriteImage_Spotlight,
    156: SpriteImage_WaterGeyser,
    163: SpriteImage_WaterGeyserLocation,
    173: SpriteImage_BanzaiBillLauncher,
    174: SpriteImage_UpDownBanzaiBillLauncher,
    179: SpriteImage_CannonBall,
    180: SpriteImage_Spike,
    182: SpriteImage_VerticalMovingPlatform,
    185: SpriteImage_StationaryIcicle,
    186: SpriteImage_HorizontalMovingPlatform,
    196: SpriteImage_Line,
    205: SpriteImage_FloatingQBlock,
    206: SpriteImage_BoomBoom,
    207: SpriteImage_LavaGeyser,
    223: SpriteImage_BoomBoom,
    225: SpriteImage_BoomBoom,
    228: SpriteImage_ScaffoldPlatform,
    229: SpriteImage_Foo,
    241: SpriteImage_BoltMushroom,
    242: SpriteImage_BoltMushroomNo,
    246: SpriteImage_BoomBoom,
    247: SpriteImage_PricklyGoomba,
    268: SpriteImage_IceBlock,
    269: SpriteImage_TowerCog,
    275: SpriteImage_SwayingPlatform,
    276: SpriteImage_JellyBeam,
    278: SpriteImage_SeesawShroom,
    287: SpriteImage_WheelPlatform,
    290: SpriteImage_LongBurner,
    294: SpriteImage_ClimablePole,
    300: SpriteImage_RisingTiltPlatform,
    302: SpriteImage_BoomBoom,
    304: SpriteImage_WobbleRock,
    305: SpriteImage_PoltergesitBlock,
    307: SpriteImage_Fence,
    309: SpriteImage_ScalePlatform,
    317: SpriteImage_BoomBoom,
    321: SpriteImage_Bulber,
    324: SpriteImage_GhostTouchBlock,
    327: SpriteImage_Sledge_Block,
    330: SpriteImage_EnemyRaft, 
    336: SpriteImage_Bramball,
    341: SpriteImage_NutPlatform,
    349: SpriteImage_TiltGirder,
    353: SpriteImage_ParachuteCoin,
    359: SpriteImage_LavaBlock,
    367: SpriteImage_TouchPlatform,
    382: SpriteImage_Dragoneel,
    384: SpriteImage_EnviromentalSFX,
    386: SpriteImage_MeltableIceChunk,
    392: SpriteImage_BowserJrW5,
    396: SpriteImage_BeanStalkLeaf,
    399: SpriteImage_BowserJrW5,
    402: SpriteImage_GreenRing,
    408: SpriteImage_Toad,
    409: SpriteImage_ChainChomp,
    410: SpriteImage_LudwigPlatform,
    414: SpriteImage_AirshipLemmy,
    415: SpriteImage_AirshipMorton,
    417: SpriteImage_AirshipLarry,
    418: SpriteImage_AirshipWendy,
    419: SpriteImage_AirshipIggy,
    420: SpriteImage_AirshipRoy,
    421: SpriteImage_AirshipLudwig,
    425: SpriteImage_Tendril,
    428: SpriteImage_LudwigPlatform2,
    429: SpriteImage_MetalBar,
    433: SpriteImage_BowserJrW7,
    441: SpriteImage_Fliprus,
    444: SpriteImage_SnowBoxes,
    450: SpriteImage_KamekBlock,
    451: SpriteImage_NabbitPlacement,
    465: SpriteImage_KamekFloor,
    485: SpriteImage_MetalGearBox,
    489: SpriteImage_AirshipSegment,
    490: SpriteImage_AirshipCollar,
    491: SpriteImage_BonePlatform,
    492: SpriteImage_BonePlatform,
    500: SpriteImage_BowserAmp,
    512: SpriteImage_GhostHouseBlock,
    537: SpriteImage_Wrench,
    550: SpriteImage_GiantPiranhaPlant,
    533: SpriteImage_MediumIcicle,
    536: SpriteImage_RockyWrench,
    539: SpriteImage_RollingIce,
    549: SpriteImage_MovingDesertBlock,
    553: SpriteImage_SteerablePlatform,
    560: SpriteImage_WendyBattleFloor,
    564: SpriteImage_GrassFlowerSetter,
    565: SpriteImage_Magmaw,
    569: SpriteImage_NabbitPrize,
    571: SpriteImage_Peach,
    581: SpriteImage_BullsEyeBillCannon,
    582: SpriteImage_BullsEyeBanzaiBillLauncher,
    583: SpriteImage_UpDownBullsEyeBanzaiBillLauncher,
    590: SpriteImage_EepCheep,
    591: SpriteImage_MediumEepCheep,
    594: SpriteImage_LightningBolt,
    596: SpriteImage_TargetingTedBox,
    609: SpriteImage_IggyRoom,
    662: SpriteImage_BlueRing,
    674: SpriteImage_LavaBlock,
}
