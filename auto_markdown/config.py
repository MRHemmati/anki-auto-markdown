from aqt import mw

def getConfig():
    # Use the parent package name for config lookup
    # __name__ here is "auto_markdown.config", but we need "auto_markdown"
    addon_package = __name__.split(".")[0]
    return mw.addonManager.getConfig(addon_package)

def shouldShowCodeLineNums():
    return getConfig()['code']['lineNums']

def getCodeColorScheme():
    return getConfig()['code']['colorScheme']

def isAutoMarkdownEnabled():
    return getConfig()['auto']['enabled']

def shouldShowEditFieldCheckbox():
    return getConfig()['auto']['uiEditFieldCheckbox']

def getManualMarkdownShortcut():
    return getConfig()['manual']['shortcut']

def shouldShowFieldMarkdownButton():
    return getConfig()['manual']['uiToggleFieldMarkdownButton']