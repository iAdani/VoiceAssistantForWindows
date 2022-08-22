import Configurations
import yaml

#
# def run_exe(program, path):
#     program += ".exe"
#     for root, dir, files in os.walk(path):
#         if program in files:
#             subprocess.call([os.path.join(root, program)])
#             return True
#     return False



# from tkinter import Tk, font

if __name__ == '__main__':
    a = Configurations.get_theme_config("dark")
    print(a['bg'])
    # recognize()
    # root = Tk()
    # print(font.families())
    # apps = os.popen("powershell -ExecutionPolicy Bypass -Command get-StartApps").read().split()
    # apps = list(filter(None, apps))
    # lst = []
    # e = ''
    # for app in apps:
    #     if len(app) < 15:

    #     else:
    #         lst.append(e[:-1])
    #         e = ''
    # apps = lst
    # for string in apps:
    #     print(string)
    # with open('config.yaml') as f:
    #     data = yaml.load(f, Loader=yaml.FullLoader)
    #     print(data)
    # print (Configurations.config)
    # Configurations.change_voice(0)
    # print (Configurations.config)


