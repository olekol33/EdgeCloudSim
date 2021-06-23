from plotGenericResult import *
def plotAvgNetworkDelay():
    print("Running " + plotAvgNetworkDelay.__name__)
    plotGenericResult(TotalTasks, networkDelay, 'Average Network Delay per Object Read (sec)', 'ALL_APPS', '','totalDelay')
    # plotGenericResult(TotalTasks, networkDelay, 'Average Network Delay for Augmented Reality App (sec)', 'AUGMENTED_REALITY', '')
    # plotGenericResult(TotalTasks, networkDelay, 'Average Network Delay for Health App (sec)', 'HEALTH_APP', '')
    # plotGenericResult(TotalTasks, networkDelay, 'Average Network Delay for Infotainment App (sec)', 'INFOTAINMENT_APP', '')
    # plotGenericResult(TotalTasks, networkDelay, 'Average Network Delay for Heavy Comp. App (sec)', 'HEAVY_COMP_APP', '')

    plotGenericResult(NetworkData, lanDelay, 'Average WLAN Delay  per Object Read (sec)', 'ALL_APPS', '','lanDelay')
    # plotGenericResult(NetworkData, lanDelay, 'Average WLAN Delay for Augmented Reality App (sec)', 'AUGMENTED_REALITY', '')
    # plotGenericResult(NetworkData, lanDelay, 'Average WLAN Delay for Health App (sec)', 'HEALTH_APP', '')
    # plotGenericResult(NetworkData, lanDelay, 'Average WLAN Delay for Infotainment App (sec)', 'INFOTAINMENT_APP', '')
    # plotGenericResult(NetworkData, lanDelay, 'Average WLAN Delay for Heavy Comp. App %(sec)', 'HEAVY_COMP_APP', '')
    
    plotGenericResult(NetworkData, manDelay, 'Average MAN Delay  per Object Read (sec)', 'ALL_APPS', '','manDelay')
    # plotGenericResult(NetworkData, manDelay, 'Average MAN Delay for Augmented Reality App (sec)', 'AUGMENTED_REALITY', '')
    # plotGenericResult(NetworkData, manDelay, 'Average MAN Delay for Health App (sec)', 'HEALTH_APP', '')
    # plotGenericResult(NetworkData, manDelay, 'Average MAN Delay for Infotainment App (sec)', 'INFOTAINMENT_APP', '')
    # plotGenericResult(NetworkData, manDelay, 'Average MAN Delay for Heavy Comp. App %(sec)', 'HEAVY_COMP_APP', '')

    plotGenericResult(NetworkData, wanDelay, 'Average WAN Delay  per Object Read (sec)', 'ALL_APPS', '','wanDelay')
    # plotGenericResult(NetworkData, wanDelay, 'Average WAN Delay for Augmented Reality App (sec)', 'AUGMENTED_REALITY', '')
    # plotGenericResult(NetworkData, wanDelay, 'Average WAN Delay for Health App (sec)', 'HEALTH_APP', '')
    # plotGenericResult(NetworkData, wanDelay, 'Average WAN Delay for Infotainment App (sec)', 'INFOTAINMENT_APP', '')
    # plotGenericResult(NetworkData, wanDelay, 'Average WAN Delay for Heavy Comp. App (sec)', 'HEAVY_COMP_APP', '')
    
# plotAvgNetworkDelay()