from .__init__ import *

import importlib
from pathlib import Path
import xml.etree.ElementTree as ET

from scripts.scene.Scene import Scene
from scripts.window.layers.Layer import Layer
from scripts.scene.IGameObject import IGameObject
from scripts.window.layers.BackgroundLayer import BackgroundLayer


from .LayersTags import LayersTags
from .ScenesTags import ScenesTags
from .GameObjectTagsTypes import GameObjectTagsTypes


class SceneLoader:
    __modulesList: list = list()

    @staticmethod
    def cleanModulesList():
        SceneLoader.__modulesList.clear()

    @staticmethod
    def loadFromXml(scenePath: Path):
        tree = ET.parse(scenePath)
        main = tree.getroot()
        
        scene = Scene()
        
        for element in main:
            match element.tag:
                case ScenesTags.IMPORT.value:
                    SceneLoader.__modulesList.append(importlib.import_module(element.get("module")))
                case ScenesTags.BACKGROUND.value:
                    scene.setBackgroundLayer(BackgroundLayer([int(x) for x in element.text.split()]))
                case ScenesTags.LAYER.value:
                    SceneLoader.__loadLayer(scene, element)
                case ScenesTags.GAME_OBJECT.value:
                    scene.addGameObject(SceneLoader.__instantiateGameObject(element))

        return scene
    
    #TODO: Maybe swap the .xml scene GameObjetc inside layer to sprite
    @staticmethod
    def __loadLayer(scene: Scene, element: ET.Element) -> None:
        layer = Layer()

        for layerElement in element:
            match layerElement.tag:
                case LayersTags.GAME_OBJECT.value:
                    gameObject = SceneLoader.__instantiateGameObject(layerElement)
                    layer.add(gameObject)
                    scene.addGameObject(gameObject)

        scene.addLayer(layer)

    @staticmethod
    def __instantiateGameObject(element: ET.Element) -> IGameObject:
        attributeList = list()
        attr: ET.Element

        for attr in element:
            match attr.get("type"):
                case GameObjectTagsTypes.INT.value:
                    attributeList.append(int(attr.text))
                case GameObjectTagsTypes.LIST_INT.value:
                    attributeList.append([int(x) for x in attr.text.split()])

        for module in SceneLoader.__modulesList:
            try:
                obj = getattr(module, element.get("type"))
            except AttributeError:
                continue
            except Exception as e:
                raise e
            
            return obj(*attributeList)
        
        raise NameError("The class {} not exist or had not been imported.".format(element.get("type")))
