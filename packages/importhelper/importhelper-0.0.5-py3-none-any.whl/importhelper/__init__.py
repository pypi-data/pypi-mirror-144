import os 
import subprocess
import traceback
import threading
import sys
import gc

__python_cmd_prefix_versions = ["python3 -m pip3","python3 -m pip","python -m pip3"]
if sys.version_info[0] == 2:
    for i in __python_cmd_prefix_versions:
        __python_cmd_prefix_versions[i] = __python_cmd_prefix_versions[i].replace("3","2")
__python_cmd_prefix_versions.append("python -m pip")

PIP_CMD_PREFIX_VERSIONED = ""

__verCount = 0
while __verCount < len(__python_cmd_prefix_versions) + 1:
    try:
        sp = subprocess.Popen(PIP_CMD_PREFIX_VERSIONED + " --version",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        ou = sp.stdout.read()
        err = sp.stderr.read()
        if(err):
            raise Exception()
    except Exception as e:
        try:
            PIP_CMD_PREFIX_VERSIONED = __python_cmd_prefix_versions[__verCount]
        except:
            print("[importhelper] Could not find pip or could not find python. Please manually install both if they are not already installed.")
            exit(1)
    __verCount = __verCount + 1

del __python_cmd_prefix_versions
del __verCount
gc.collect()

class ModVersion(str):
    def __init__(self,versionStr):
        self.versions = [int(i) for i in versionStr.split(".")]
    def __str__(self):
        st = ""
        for i in self.versions:
            st = "%s.%s" % (st,i)
        return st.strip(".")
    def __gt__(self, other):
        for i,j in self.versions,other.versions:
            if (i > j):
                return True
            elif (i < j):
                return False
        return False
    def __eq__(self, other):
        for i,j in self.versions,other.versions:
            if(i != j):
                return False
        return True
class Mod:
    PIP_FREEZE = {}
    SILENCE_IMPORT_START = False
    SILENCE_IMPORT_ERRORS = False
    SILENCE_IMPORT_SUCCESS = False
    SILENCE_INSTALL_START = False
    SILENCE_INSTALL_OUTPUT = False
    SILENCE_INSTALL_SUCCESS = False
    SILENCE_INSTALL_ERRORS = False
    SILENCE_UNINSTALL_START = False
    SILENCE_UNINSTALL_OUTPUT = False
    SILENCE_UNINSTALL_SUCCESS = False
    SILENCE_UNINSTALL_ERRORS = False
    IMPORT_ERROR_MESSAGE = "> Failed to import %s"
    IMPORT_START_MESSAGE = "> Importing %s..."
    IMPORT_SUCCESS_MESSAGE = "> Successfully imported %s"
    INSTALL_ERROR_MESSAGE = "> Failed to install %s==%s"
    INSTALL_START_MESSAGE = "> Installing %s==%s..."
    INSTALL_SUCCESS_MESSAGE = "> Successfully installed %s==%s"
    UNINSTALL_ERROR_MESSAGE = "> Failed to uninstall %s==%s"
    UNINSTALL_START_MESSAGE = "> Uninstalling %s==%s..."
    UNINSTALL_SUCCESS_MESSAGE = "> Successfully uninstalled %s==%s"
    def __init__(self, modules=None,src=None,pip=None,onInstallFail=None,onImportFail=None):
        self.modules = modules
        if(self.modules is None):
           if(pip is None):
               raise RuntimeError("Mod constructor requires EITHER modules as string/list/dict OR pip as string.")
        self.src = src
        self.package = pip
        self.packageVersion = None
        if(self.package is None):
            self.package = self.src
        if(type(self.package) is str and self.package.count("==") > 0):
            self.package,self.packageVersion = self.package.split("==")
        if(self.packageVersion is not None):
            self.packageVersion = ModVersion(self.packageVersion)
        if(self.package is None and type(self.modules) is str):
            self.package = self.modules
        self.__installOP = None
        self.__uninstallOP = None
        self.onInstallFail = onInstallFail
        if(self.onInstallFail is not None and "function" not in str(type(self.onInstallFail))):
            raise RuntimeError("onInstallFail argument MUST be a function")
        self.onImportFail = onImportFail
        if(self.onImportFail is not None and "function" not in str(type(self.onImportFail))):
            raise RuntimeError("onImportFail argument MUST be a function")
    def isInstalled(self):
        """Is the package atleast installed?
        Returns(boolean):
            True if atleast the package is installed
        """
        return self.package in Mod.PIP_FREEZE
    def isMinimumVersionInstalled(self):
        """Is the minimum required version installed? (1.3 installed vs 1.0 required returns True)
        Returns(boolean):
            True if atleast the minimum required version is installed
        """
        return self.isInstalled and Mod.PIP_FREEZE[self.package] >= self.packageVersion
    def isRequiredVersionInstalled(self):
        """Is ONLY the required version installed? (1.0 installed vs 1.0 required returns True)
        Returns(boolean):
            True if ONLY the required version is installed
        """
        return self.isInstalled and Mod.PIP_FREEZE[self.package] == self.packageVersion
    def getImportScript(self):
        """Get the python script used to import all modules
        Returns:
            The python script to import modules.
        """
        if(self.modules is None):
            return None
        toExec = "import "
        if self.src is not None:
            toExec = "from %s " % self.src + toExec
        if(type(self.modules) is dict):
            for modl in self.modules:
                toExec = toExec + "%s as %s," % (modl,self.modules[modl])
        elif(type(self.modules) is list):
            for modl in self.modules:
                toExec = toExec + "%s," % modl
        else:
            toExec = toExec + self.modules
        if(toExec.endswith(",")):
            toExec = toExec[:-1]
        return toExec
    def getPackageVersion(self):
        """Get the package version of the package TO BE installed
        Returns:
            "Latest" if version not specified, else returns the version as a ModVersion object.
        """
        return self.packageVersion if self.packageVersion else "Latest"
    def getInstalledPackageVersion(self):
        """Get the package version of the package that IS installed
        Returns:
            "UNKWN" if package is not installed, else returns the version as a ModVersion object.
        """
        return Mod.PIP_FREEZE[self.package] if self.package in Mod.PIP_FREEZE else "UNKWN"
    def __str__(self):
        return st
    def __install(self,*args):
        try:
            if(not Mod.SILENCE_INSTALL_START):
                if(Mod.INSTALL_START_MESSAGE.count("%s") == 2):
                    print(Mod.INSTALL_START_MESSAGE % (self.package,self.getPackageVersion()))
                else:
                    print(Mod.INSTALL_START_MESSAGE + " " + self.package + "==" + self.getPackageVersion())
            with subprocess.Popen(self.pipInstallCmd,shell=True,stdout=subprocess.PIPE) as sp:
                self.__installOP = ""
                while True:
                    line = sp.stdout.readline().decode()
                    if not line:
                        break
                    line = line.rstrip()
                    if(not Mod.SILENCE_INSTALL_OUTPUT):
                        print(line)
                    self.__installOP = self.__installOP + "%s\n" % line
            Mod.refreshPipFreezeInfo()
            if(not Mod.SILENCE_INSTALL_SUCCESS):
                if(Mod.INSTALL_SUCCESS_MESSAGE.count("%s") == 2):
                    print(Mod.INSTALL_SUCCESS_MESSAGE % (self.package,self.getInstalledPackageVersion()))
                else:
                    print(Mod.INSTALL_SUCCESS_MESSAGE + " " + self.package + "==" + str(self.getInstalledPackageVersion()))
        except Exception as e:
            if(not Mod.SILENCE_INSTALL_ERRORS):
                if(Mod.INSTALL_ERROR_MESSAGE.count("%s") == 2):
                    print(Mod.INSTALL_ERROR_MESSAGE % (self.package,self.getPackageVersion()))
                else:
                    print(Mod.INSTALL_ERROR_MESSAGE + " " + self.package + "==" + str(self.getPackageVersion()))
            if(self.onInstallFail is not None):
                if(not Mod.SILENCE_INSTALL_ERRORS):
                    print("Executing onInstallFail()")
                return self.onInstallFail()
            return False
    def __uninstall(self,*args):
        try:
            if(not Mod.SILENCE_UNINSTALL_START):
                if(Mod.UNINSTALL_START_MESSAGE.count("%s") == 2):
                    print(Mod.UNINSTALL_START_MESSAGE % (self.package,self.getInstalledPackageVersion()))
                else:
                    print(Mod.UNINSTALL_START_MESSAGE + " " + self.package + "==" + self.getInstalledPackageVersion())
            with subprocess.Popen(self.pipUninstallCmd,shell=True,stdout=subprocess.PIPE) as sp:
                self.__uninstallOP = ""
                while True:
                    line = sp.stdout.readline().decode()
                    if not line:
                        break
                    line = line.rstrip()
                    if(not Mod.SILENCE_UNINSTALL_OUTPUT):
                        print(line)
                    self.__uninstallOP = self.__uninstallOP + "%s\n" % line
            Mod.refreshPipFreezeInfo()
            if(not Mod.SILENCE_UNINSTALL_SUCCESS):
                if(Mod.UNINSTALL_SUCCESS_MESSAGE.count("%s") == 2):
                    print(Mod.UNINSTALL_SUCCESS_MESSAGE % (self.package,self.getInstalledPackageVersion()))
                else:
                    print(Mod.UNINSTALL_SUCCESS_MESSAGE + " " + self.package + "==" + str(self.getInstalledPackageVersion()))
        except Exception as e:
            if(not Mod.SILENCE_UNINSTALL_ERRORS):
                if(Mod.UNINSTALL_ERROR_MESSAGE.count("%s") == 2):
                    print(Mod.UNINSTALL_ERROR_MESSAGE % (self.package,self.getPackageVersion()))
                else:
                    print(Mod.UNINSTALL_ERROR_MESSAGE + " " + self.package + "==" + str(self.getPackageVersion()))
            return False
    def install(self,upgrade=True,blockThread=True):
        """Installs the package
        Parameters:
            upgrade(boolean): Should the argument --upgrade be given to pip/Should package be upgraded?
            blockThread(boolean): Should you block the calling thread?
        Returns(string):
            Output from the installation subprocess
        """
        if(self.package is None):
            return False
        self.pipInstallCmd = PIP_CMD_PREFIX_VERSIONED + " install "
        if(upgrade):
            self.pipInstallCmd = self.pipInstallCmd + "--upgrade "
        self.pipInstallCmd = self.pipInstallCmd + self.package
        if(self.packageVersion is not None):
            self.pipInstallCmd = self.pipInstallCmd + "==%s" % self.packageVersion
        th = threading.Thread(target=self.__install,args=(self,),daemon=True)
        th.start()
        if(blockThread):
            th.join()
        if(self.__installOP):
            return self.__installOP
    def uninstall(self,blockThread=True):
        """Uninstalls the package
        Parameters:
            blockThread(boolean): Should you block the calling thread?
        Returns(string):
            Output from the uninstallation subprocess
        """
        self.pipUninstallCmd = PIP_CMD_PREFIX_VERSIONED + (" uninstall -y %s" % self.package)
        th = threading.Thread(target=self.__uninstall,args=(self,),daemon=True)
        th.start()
        if(blockThread):
            th.join()
        if(self.__uninstallOP):
            return self.__uninstallOP
    def attemptImport(self,scope,installIfNotInstalled=False,*args):
        """Uninstalls the package
        Parameters:
            installIfNotInstalled(boolean): Pretty obvious, but it will install the package before importing (If package is not installed)
            *args: Passed down to Mod.install()
        Returns(Boolean):
            True if successful in importing the modules
        """
        if(scope is None):
            scope = globals()
        if(installIfNotInstalled and not self.isInstalled()):
            self.install(args)
        toExec = self.getImportScript()
        if(toExec is None):
            return False
        if(not Mod.SILENCE_IMPORT_START):
            if(Mod.IMPORT_START_MESSAGE.count("%s") == 1):
                print(Mod.IMPORT_START_MESSAGE % (toExec))
            else:
                print(Mod.IMPORT_START_MESSAGE + " " + toExec)
        try:
            exec(toExec,scope)
            if(not Mod.SILENCE_IMPORT_SUCCESS):
                if(Mod.IMPORT_SUCCESS_MESSAGE.count("%s") == 1):
                    print(Mod.IMPORT_SUCCESS_MESSAGE % (toExec))
                else:
                    print(Mod.IMPORT_SUCCESS_MESSAGE + " " + toExec)
            return True
        except ImportError as e:
            if(not Mod.SILENCE_IMPORT_ERRORS):
                if(Mod.IMPORT_ERROR_MESSAGE.count("%s") == 1):
                    print(Mod.IMPORT_ERROR_MESSAGE % (toExec))
                else:
                    print(Mod.IMPORT_ERROR_MESSAGE + " " + toExec)
                traceback.print_exc()
            if(self.onImportFail is not None):
                if(not Mod.SILENCE_IMPORT_ERRORS):
                    print("Executing onImportFail()")
                return self.onImportFail()
            return False
    @classmethod
    def getPipFreeze(cls):
        """Gets the output from doing "pip freeze -all"
        Returns(dict):
            Dictionay with keys being the installed packages and values being ModVersion objects
        """
        with (subprocess.Popen("pip freeze --all",shell=True,stdout=subprocess.PIPE)) as sp:
            red = (sp.stdout.read().decode().replace("\r\n","\n")).split("\n")
            toReturn = dict(tuple(i.split("==")) for i in red if i.count("==") > 0)
            for i in toReturn:
                toReturn[i] = ModVersion(toReturn[i])
            return toReturn
    @classmethod
    def refreshPipFreezeInfo(cls):
        """Refreshes Mod.PIP_FREEZE's values
        Returns(None):
            Nothing.... What would u expect??
        """
        Mod.PIP_FREEZE = Mod.getPipFreeze()
Mod.refreshPipFreezeInfo()
