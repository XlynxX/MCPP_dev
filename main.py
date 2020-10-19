from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from MCPP import Ui_MCPP
from MCPP2 import Ui_MCPP2
from MCPP3 import Ui_MCPP3
import minecraft_rc
import tkinter as tk
from tkinter import filedialog
import sys, os, re, json, uuid
from zipfile import ZipFile
import shutil, configparser
from configobj import ConfigObj
from playsound import playsound
from PIL import Image
import time, webbrowser

app = QtWidgets.QApplication(sys.argv)
#main1.ui 
MCPP = QtWidgets.QMainWindow()
ui = Ui_MCPP()
ui.setupUi(MCPP)
#settings.ui
MCPP3 = QtWidgets.QMainWindow()
ui3 = Ui_MCPP3()
ui3.setupUi(MCPP3)
#settings.ui
#main2.ui
MCPP2 = QtWidgets.QDialog()
ui2 = Ui_MCPP2()
ui2.setupUi(MCPP2)
#tkinter
root = tk.Tk()
root.withdraw()
#main paths
app_path = os.path.join(os.path.join(os.environ['USERPROFILE']), r'Documents\MCPP')
config_path = r'%s\config.ini'%(app_path)
pack = str(None)
#creating config file and app path
if os.path.exists(app_path):
    pass
else:
    os.mkdir(app_path)
#MAIN FUNCTION
def Main():
    print('CONVERT button pressed ->')
    try:
        sound()
        print('***sound is OK...')
    except Exception as e:
        print(e)
        print('//Error with sound')
    try:
        check_pack()
        print('***pack is OK...')
    except Exception as e:
        print(e)
        return
    try:
        load_settings()
        print('***settings is OK...')
    except Exception as e:
        print(e)
        return
    try:
        load_paths()
        print('***paths is OK...')
    except Exception as e:
        print(e)
        print('//Error with loading paths')
        return
    try:
        create_packfolder()
        print('***pack folder is OK...')
    except Exception as e:
        print(e)
        print('//Error with creating app/pack folder')
        return
    try:
        manifest()
        print('***manifest is OK...')
    except Exception as e:
        print(e)
        print('//Error with creating manifest file')
    try:
        ffonts()
    except Exception as e:
        print(e)
        print('//Error with converting fonts')
    try:
        aarmor()
    except Exception as e:
        print(e)
        print('//Error with converting armor')
    try:
        texture()
    except Exception as e:
        print(e)
        print('//Error with converting textures')
    try:
        sky()
        print('***sky is OK...')
    except Exception as e:
        print(e)
        print('//Error with converting sky')
    try:
        packbuild()
        print('***pack building is OK...')
    except Exception as e:
        print(e)
        print('//Error with packaging converted files')
    print('Done!')
    if config_onclose == 'open':
        os.startfile('%s.mcpack'%(convertedPack))
        sys.exit()
    elif config_onclose == 'nothing':
        window('Успех', 'Ваш ресурспак был успешно портирован, вы можете его найти по следующему пути:\n%s.mcpack'%(convertedPack))
    elif config_onclose == 'close':
        sys.exit()
#SELECT FUNCTION
def Select():
    print('SELECT button pressed ->')
    try:
        sound()
        print('***sound is OK...')
    except Exception as e:
        print(e)
        print('//Error with sound function')
    global pack
    pack = filedialog.askopenfilename(filetypes =[('Zip archive', '*.zip'), ('Minecraft pack', '*.mcpack')])
#checking resource pack path and app path
def check_pack():
    if pack.strip() == '':
        window("Ошибка", "Вы не указали ресурспак для конвертирования")
        raise Exception('ERROR: There is no pack to convert')
    elif pack == 'None':
        window("Ошибка", "Вы не указали ресурспак для конвертирования")
        raise Exception('ERROR: There is no pack to convert')
    else:
        if os.path.exists(app_path):
            pass
        else:
            os.mkdir(app_path)
#playsound on button
def sound():
    playfile = os.path.abspath('click.wav')
    if os.path.exists(playfile):
        playfile = str(playfile).replace('\\','\\\\')
        playsound(playfile)
        #playsound('C:\\Users\\Lynx\\Desktop\\MCPP\\click.wav') #need to write full path to .wav with double backslash instead of 'playfile' to compile
#messagebox window function
def window(title, text):
    msg = QMessageBox(MCPP2)
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Information)
    msg.setStyleSheet("background-color: white;")
    msg.exec_()
#adding paths
def load_paths():
    global packName, pack_folder, assets, textures, skies, fonts, armor, convertedPack, blocks, cubemap, environment, entity, items, gui
    
    pack_zip = os.path.basename(pack)
    packName = os.path.splitext(pack_zip)[0]
    pack_folder = r'%s\%s'%(app_path, packName)
    #java skies path
    skies = 'assets\\minecraft\\mcpatcher\\sky\\world0'
    skies = r'%s\%s'%(pack_folder, skies)
    print('skies path: ' + skies)
    
    environment = 'textures\\environment'
    environment = r'%s\%s'%(pack_folder, environment)
    print('environment path: ' + environment)
    
    cubemap = '%s\\overworld_cubemap'%(environment)
    print('cubemap path: ' + cubemap)
    
    textures = 'assets\\minecraft\\textures'
    textures = r'%s\%s'%(pack_folder, textures)
    print('textures path: ' + textures)

    gui = '%s\\gui'%(textures)
    print('gui path: ' + gui)

    blocks = 'assets\\minecraft\\textures\\blocks'
    blocks = r'%s\%s'%(pack_folder, blocks)
    print('blocks textures path: ' + blocks)

    items = 'assets\\minecraft\\textures\\items'
    items = r'%s\%s'%(pack_folder, items)
    print('items path: ' + items)
    
    assets = 'assets'
    assets = r'%s\%s'%(pack_folder, assets)
    print('assets path: ' + assets)
    
    fonts = 'assets\\minecraft\\textures\\font'
    fonts = r'%s\%s'%(pack_folder, fonts)
    print('fonts path: ' + fonts)

    entity = 'assets\\minecraft\\textures\\entity'
    entity = r'%s\%s'%(pack_folder, entity)
    print('entity path: ' + entity)
    
    armor = 'assets\\minecraft\\textures\\models\\armor'
    armor = r'%s\%s'%(pack_folder, armor)
    print('armor path: ' + armor)
    
    convertedPack = '%s\\%s'%(app_path, packName)
    print('converted pack path: ' + armor)
#renaming function
def fixname(path, oldname, newname):
    for fileName in os.listdir(path):
        os.rename(os.path.join(path,fileName), os.path.join(path,fileName.replace(oldname, newname)))
    print('Filenames in %s have been renamed'%(path))
#sky converting function
def sky():
    print('Converting sky')
    if os.path.exists(skies):
        if os.path.exists(environment):
            if os.path.exists(cubemap):
                pass
            else:
                os.mkdir(cubemap)
        else:
            os.mkdir(environment)
            os.mkdir(cubemap)
        config1 = ConfigObj(r'%s\sky1.properties'%(skies))
        config2 = ConfigObj(r'%s\sky2.properties'%(skies))
        config3 = ConfigObj(r'%s\sky3.properties'%(skies))
        sky1 = config1.get('source')
        sky1 = sky1.lstrip('.')
        sky1 = sky1.replace(r"/", r'\\')
        sky1 = '%s%s'%(skies, sky1)
        sky2 = config2.get('source')
        sky2 = sky2.lstrip('.')
        sky2 = sky2.replace(r"/", r'\\')
        sky2 = '%s%s'%(skies, sky2)
        sky3 = config3.get('source')
        sky3 = sky3.lstrip('.')
        sky3 = sky3.replace(r"/", r'\\')
        sky3 = '%s%s'%(skies, sky3)
        if config_sky == 'day':
            infile = sky1
        elif config_sky == 'sunset':
            infile = sky2
        elif config_sky == 'night':
            infile = sky3
        file_extension = ".png"
        name_map = [ \
            ["cubemap_5", "cubemap_4", "cubemap_2"],
            ["cubemap_3", "cubemap_0", "cubemap_1"]]
        im = Image.open(infile)
        print(infile, im.format, "%dx%d" % im.size, im.mode)
        width, height = im.size
        cube_size = width / 3
        filelist = []
        for row in range(2):
            for col in range(3):
                if name_map[row][col] != "":
                    sx = cube_size * col
                    sy = cube_size * row
                    fn = name_map[row][col] + file_extension
                    fn = '%s\\%s'%(cubemap, fn)
                    print(fn)
                    filelist.append(fn)
                    im.crop((sx, sy, sx + cube_size, sy + cube_size)).save(fn)
#manifest file creating
def manifest():
    print('Creating manifest file...')
    os.rename(r'%s\pack.mcmeta'%(pack_folder), r'%s\pack.txt'%(pack_folder))
    config_manifest = r'%s\pack.txt'%(pack_folder)
    with open(config_manifest) as config:
        lines = config.readlines()
        lines = str(lines)
    mess, mess, mess = lines.partition('"description":')
    desc = mess.split('"')
    manifest_desc = desc[1]
    os.remove(config_manifest)
    config_manifest = r'%s\manifest.json'%(pack_folder)
    #getting random id using uuid4() 
    uuid1 = str(uuid.uuid4())
    uuid2 = str(uuid.uuid4())
    #manifest json data 
    manifest ={
        "format_version": 1,
        "header": {
            "description": manifest_desc,
            "name": packName,
            "uuid": uuid1,
            "version": [0, 0, 1],
            "min_engine_version": [0, 0, 1]
        },
        "modules": [
            {
                "description": manifest_desc,
                "type": "resources",
                "uuid": uuid2,
                "version": [0, 0, 1]
            }
        ]
    }
    with open(config_manifest, "w") as manifest_file:
        json.dump(manifest, manifest_file, indent = 4)
    print('Manifest data:\nPack name: %s\nPack description: %s\nUUID1: %s\nUUID2: %s'%(packName, manifest_desc, uuid1, uuid2))
#fonts converting
def ffonts():
    if config_font == 'yes':
        if os.path.exists(fonts):
            fixname(fonts, 'unicode_page', 'glyph')
            shutil.move(fonts, pack_folder)
            print('***fonts is OK...')
        else:
            print('No fonts in pack\n...Skipped')
    else:
        print('***fonts is OK...(Skipped)')
#armor converting
def aarmor():
    if os.path.exists(armor):
        fixname(armor, 'layer_', '')
        print('***armor is OK...')
    else:
        print('No armor in pack\n...Skipped')
#textures converting
def texture():
    if os.path.exists(textures):
        if config_textures_blocks == 'no':
            shutil.rmtree(blocks)
        if config_entity == 'no':
            shutil.rmtree(entity)
        try:
            fixname(blocks, 'layer_', '')
            shutil.copy(r'%s\fire_0.png'%(blocks), textures)
            os.rename(r'%s\fire_0.png'%(textures), r'%s\flame_atlas.png'%(textures))
            fixname(gui, 'widgets', 'gui')
        except Exception as e:
            print(e)
        try:
                im1 = Image.open(r'%s\grass_side_overlay.png'%(blocks))
                im2 = Image.open(r'%s\dirt.png'%(blocks))
                im2.putalpha(0)
                Image.alpha_composite(im2, im1).save(r"%s\grass_side.tga"%(blocks), "TGA")
                Image.alpha_composite(im2, im1).save(r"%s\grass_side_snowed.tga"%(blocks), "TGA")
                os.remove(r'%s\grass_side_overlay.png'%(blocks))
                os.remove(r'%s\grass_side.png'%(blocks))
                os.remove(r'%s\grass_side_snowed.png'%(blocks))
        except Exception as e:
                print(e)
                print('//Error with creating grass tga')
        try:
            fixname(items, 'layer_', '')
        except:
            pass
        #try:
            #for file in os.listdir(blocks):
                #if file.startswith("destroy_stage"):
                    #print(file)
                    #os.mkdir(environment)
                    #shutil.copy(os.path.join(blocks,file), 'C:\Users\Lynx\Documents\MCPP\§l§9Blue Default §r§716x\textures\environment')
                    #print('destroy gay')
        #except Exception as e:
            #print(e)
        shutil.move(textures, pack_folder)
    else:
        print('No textures in pack\n...Skipped')
#creating pack folder
def create_packfolder():
    if os.path.exists(pack_folder):
        shutil.rmtree(pack_folder)
        os.mkdir(pack_folder)
    else:
        os.mkdir(pack_folder)
    with ZipFile(pack,'r') as zip:
        zip.extractall(pack_folder)
    os.rename(r'%s\pack.png'%(pack_folder), r'%s\pack_icon.png'%(pack_folder))
#packing converted pack to .mcpack
def packbuild():
    shutil.rmtree(assets)
    shutil.make_archive(convertedPack, 'zip', pack_folder)
    os.rename(r'%s.zip'%(convertedPack), r'%s.mcpack'%(convertedPack))
    print('mcpack path: %s.mcpack'%(convertedPack))
def Settings():
    print('SETTINGS button pressed ->')
    try:
        sound()
        print('***sound is OK...')
    except Exception as e:
        print(e)
        print('//Error with sound')
    try:
        load_settings()
        print('***settings loaded')
    except Exception as e:
        print(e)
        print('//Error with loading settings')
    MCPP.hide()
    MCPP3.show()
def Settings_close():
    print('DONE button pressed ->')
    try:
        sound()
        print('***sound is OK...')
    except Exception as e:
        print(e)
        print('//Error with sound')
    MCPP3.hide()
    MCPP.show()
def skyButton():
    if config_sky == "day":
        newconf("Settings", "sky", "sunset")
    elif config_sky == "sunset":
        newconf("Settings", "sky", "night")
    elif config_sky == "night":
        newconf("Settings", "sky", "day")
    load_settings()
def fontButton():
    if config_font == "yes":
        newconf("Settings", "fonts", "no")
    elif config_font == "no":
        newconf("Settings", "fonts", "yes")
    load_settings()
def entityButton():
    if config_entity == "yes":
        newconf("Settings", "entity", "no")
    elif config_entity == "no":
        newconf("Settings", "entity", "yes")
    load_settings()
def blocksButton():
    if config_textures_blocks == "yes":
        newconf("Settings", "textures_blocks", "no")
    elif config_textures_blocks == "no":
        newconf("Settings", "textures_blocks", "yes")
    load_settings()
def oncloseButton():
    if config_onclose == "open":
        newconf("Settings", "on_close", "close")
    elif config_onclose == "close":
        newconf("Settings", "on_close", "nothing")
    elif config_onclose == "nothing":
        newconf("Settings", "on_close", "open")
    load_settings()
def newconf(datatype, data, data_new):
    config = configparser.ConfigParser()
    config.read(config_path)
    config.set(datatype, data, data_new)
    with open(config_path, "w") as config_file:
        config.write(config_file)
#settings and config
def load_settings():
    global config_sky, config_font, config_entity, config_textures_blocks, config_onclose
    if not os.path.exists(config_path):
        createConfig()
    config = configparser.ConfigParser()
    config.read(config_path)
    #reading config
    config_sky = config.get("Settings", "sky")
    config_font = config.get("Settings", "fonts")
    config_entity = config.get("Settings", "entity")
    config_textures_blocks = config.get("Settings", "textures_blocks")
    config_onclose = config.get("Settings", "on_close")
    #sky
    if config_sky == 'day':
        ui3.SkyB.setText('Небо: день')
    elif config_sky == 'sunset':
        ui3.SkyB.setText('Небо: закат')
    elif config_sky == 'night':
        ui3.SkyB.setText('Небо: ночь')
    #fonts
    if config_font == 'yes':
        ui3.FontB.setText('Шрифты: включить')
    elif config_font == 'no':
        ui3.FontB.setText('Шрифты: не включать')
    #entity
    if config_entity == 'yes':
        ui3.EntityB.setText('Энтити: включить')
    elif config_entity == 'no':
        ui3.EntityB.setText('Энтити: не включать')
    # block textures
    if config_textures_blocks == 'yes':
        ui3.TexturesB.setText('Блоки: включить')
    elif config_textures_blocks == 'no':
        ui3.TexturesB.setText('Блоки: не включать')
    # on end
    if config_onclose == 'open':
        ui3.OncloseB.setText('После: открыть пак')
    elif config_onclose == 'close':
        ui3.OncloseB.setText('После: закрыть')
    elif config_onclose == 'nothing':
        ui3.OncloseB.setText('После: ничего')
def createConfig():
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "sky", "day")
    config.set("Settings", "fonts", "yes")
    config.set("Settings", "entity", "yes")
    config.set("Settings", "textures_blocks", "yes")
    config.set("Settings", "on_close", "open")
    with open(config_path, "w") as config_file:
        config.write(config_file)
#support
def supportButton():
    webbrowser.open_new("https://www.donationalerts.com/r/xlynxx")
#connecting buttons
ui.SelectB.clicked.connect(Select)
ui.ConvertB.clicked.connect(Main)
ui.SettingsB.clicked.connect(Settings)
ui3.SkyB.clicked.connect(skyButton)
ui3.FontB.clicked.connect(fontButton)
ui3.EntityB.clicked.connect(entityButton)
ui3.TexturesB.clicked.connect(blocksButton)
ui3.OncloseB.clicked.connect(oncloseButton)
ui3.SupportB.clicked.connect(supportButton)
ui3.DoneB.clicked.connect(Settings_close)
#loading fonts from resource file
MCPP.addfont = QtGui.QFontDatabase()
MCPP.addfont.addApplicationFont(":/fonts/minecraft.ttf")
MCPP.setFont(QtGui.QFont("Minecraft Rus", 12))
#Show MAIN window
MCPP.show()
sys.exit(app.exec_())
