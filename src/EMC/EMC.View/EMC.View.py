import os
from DimensionsBlock import DimensionsBlock
from ClassHeader import Header
from ControlBlock import ControlBlock
from Geometry import GeometryBlock
from Frequency import Frequency
from FileOut import FileOut


sonnetFile = FileOut()

def MainMenu():    
    option = -1
    
    while option != 0:
        print("1. Параметры блока единиц измерения\n" + 
              "2. Параметры блока управления\n" + 
              "3. Параметры блока геометрии\n" + 
              "4. Изменить частоты моделирования\n" +
              "5. Запустить моделирование\n" + 
              "0. Выход\n")
        option = int(input("Выберите действие -> "))

        match option:
            case 0:
                print("\nВыход из программы ...")
            case 1:
                DimensionsBlockMenu()
            case 2:
                ControlBlockMenu()
            case 3:
                GeometryBlockMenu()
            case 4:
                sonnetFile.frequency.ShowFrequency()
                sonnetFile.frequency.ChangeSweepType()
            case 5:
                if sonnetFile.geometry.numberOfPorts == 0:
                    print("Невозможно запустить моделирование. " + 
                          "В проекте отсутствуют порты.")
                else:
                    sonnetFile.MakeFile()
            case _:
                print("\nДействие выбрано неверно.")
  

def DimensionsBlockMenu():
    option = -1
     
    while option != 0:
        print("1. Изменить единицу измерения емкости\n" + 
              "2. Изменить единицу измерения частоты\n" + 
              "3. Изменить единицу измерения индуктивности\n" + 
              "4. Изменить единицу измерения длины\n" + 
              "5. Изменить единицу измерения сопротивления\n" + 
              "6. Показать параметры блока\n" + 
              "0. Вернуться в главное меню\n")
        option = int(input("Выберите действие -> "))

        match option:
            case 0:
                print("\nВозвращение в главное меню ...")
            case 1:
                sonnetFile.dimensions.ChangeCapacitanceUnit()
            case 2:
                sonnetFile.dimensions.ChangeFrequencyUnit()
            case 3:
                sonnetFile.dimensions.ChangeInductivityUnit()
            case 4:
                sonnetFile.dimensions.ChangeLenghtUnit()
            case 5:
                sonnetFile.dimensions.ChangeResistanceUnit()
            case 6:
                sonnetFile.dimensions.ShowDimensionsBlock()
            case _:
                print("\nДействие выбрано неверно.")

def ControlBlockMenu():
    option = -1
     
    while option != 0:
        print("1. Изменить единицу измерения емкости\n" + 
              "2. Изменить единицу измерения частоты\n" + 
              "3. Изменить единицу измерения индуктивности\n" + 
              "4. Использование Q-фактора точности\n" + 
              "5. Показать параметры блока\n" + 
              "0. Вернуться в главное меню\n")
        option = int(input("Выберите действие -> "))

        match option:
            case 0:
                print("\nВозвращение в главное меню ...")
            case 1:
                sonnetFile.control.ChangeOptions()
            case 2:        
                sonnetFile.control.ChangeSpeed()
            case 3:        
                sonnetFile.control.ChangeCacheABS()
            case 4:        
                sonnetFile.control.ChangeQAcc()
            case 5:        
                sonnetFile.control.ShowControlBlock()
            case _:
                print("\nДействие выбрано неверно.")

def GeometryBlockMenu():
    option = -1
     
    while option != 0:
        print("1. Добавление диэлектрического слоя\n" + 
              "2. Добавление технологического слоя\n" + 
              "3. Добавление полигона\n" + 
              "4. Добавление порта\n" + 
              "5. Удаление диэлектрического слоя\n" +
              "6. Удаление технологического слоя\n" +
              "7. Удаление полигона\n" +
              "8. Удаление порта\n" +
              "9. Показать параметры блока\n" +
              "0. Вернуться в главное меню\n")
        option = int(input("Выберите действие -> "))

        match option:
            case 0:
                print("\nВозвращение в главное меню ...")
            case 1:
                sonnetFile.geometry.AddDielectricLayer()
            case 2:        
                sonnetFile.geometry.AddTechnologyLayer()
            case 3:        
                sonnetFile.geometry.AddPolygon()
            case 4:        
                sonnetFile.geometry.AddPort()
            case 5: 
                if sonnetFile.geometry.numberOfPorts == 0:
                    print("В проекте нет диэлектрических слоев.")
                else:
                    sonnetFile.geometry.RemoveDielectricLayer()
            case 6:
                if len(sonnetFile.geometry.TechnologyLayers) == 0:
                    print("В проекте нет технологических слоев.")
                else:
                    sonnetFile.geometry.RemoveTechnologyLayer()
            case 7:
                if sonnetFile.geometry.numberOfPolygons == 0:
                    print("В проекте нет полигонов.")
                else:
                    sonnetFile.geometry.RemovePolygon()
            case 8:
                if sonnetFile.geometry.numberOfPorts == 0:
                    print("В проекте нет портов.")
                else:
                    sonnetFile.geometry.RemovePort()
            case 9:
                sonnetFile.geometry.ShowGeometryBlock()
            case _:
                print("\nДействие выбрано неверно.")

MainMenu()