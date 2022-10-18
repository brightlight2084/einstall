# -*- coding: utf-8 -*-
from .base import BaseTool
from .base import PrintUtils,CmdTask,FileUtils,AptUtils,ChooseTask
from .base import osversion
from .base import run_tool_file

class Tool(BaseTool):
    def __init__(self):
        self.type = BaseTool.TYPE_CONFIG
        self.name = "模板工程"
        self.autor = '小鱼'

    def install_rosdepc(self):
        CmdTask("sudo apt update", 0).run()
        CmdTask("sudo apt-get install ntpdate", 0).run()
        CmdTask("sudo ntpdate time.windows.com", 0).run()
        CmdTask("sudo hwclock --localtime --systohc", 0).run()
        PrintUtils.print_info('config timezone success!')


    def run(self):
        #正式的运行
        self.install_rosdepc()
