from mtgConstants import *
appNames = [ ('Registration',31),('Configuration',32), ('ChannelPing',34), ('GCL',35),
             ('TaskDeliveryApp',36), ('DataLogger',37), ('Reprogramming',38),  ('Diagnostics',40),
             ('CommServices',128), ('PowerManagement',129),('DebugLogs',131),('GSM',135), ('Iridium', 136), ('Ethernet', 137),
             ('DiagnosticsAppReporting', 139), ('TimeManager',142),
             ('DataloggerMonitor',143),('HourMeter', 148),  ('PlatformCANServiceApp', 150), ('QualcommLegacy',152),
             ('GSMNetworkSimulator', 154), ('BreadcrumbsApp', 172),   ('WiFiAdapter', 177), ('ConnectedDeviceProxyApp',203), 
             ('DebugInterface',205), ('CANWANControl', 217)]
                         
def sortByParamId ( objDictionary ):
   minValue = 10000
   lastValue = -1
   list = []
   lastItem = ''
   for x in objDictionary:
      for item in objDictionary: 
         paramId = objDictionary[item]['ParamID']     
         if (paramId < minValue) and (paramId > lastValue):
            minValue = paramId     
            lowest = objDictionary[item]
            lastItem = item
      lastValue = minValue
      minValue = 10000
      list.append ((lastItem,lowest))
   return list

   
f = open ( 'java.txt', 'w')
f.write ( "final String[] appIds = {" )
first = True
count = 0
for item in appNames:   
   id = item[1]
   if count == 10:
      f.write ( '\n' )
   if not first:
      f.write ( ',' )
   f.write ( '\"' + str(id) + '\"' )   
   count = count + 1
   first = False
f.write ( "};\n" );

f.write ( "\nfinal String[][] commandNames = { \n" )
first = True
for appInfo in appNames:    
   name = appInfo[0]
   if not first:
      f.write (",\n")
   f.write  ("  /* " + name + "*/\n")
   f.write ("{")
   values = sortByParamId (unsortedconfigDB [name])   
   count = 0
   for item in values:   
      # print str(item)
      if item != values[0]: # next command
         f.write (',')
         if count >= 3:
            count = 0
            f.write ( '\n' ) 
      f.write ( '\"' + str(item[1]['ParamID']) + ' ' + str(item[0]) + '\"') 
      first = False
      count = count + 1
      
   f.write ( "}\n")  
f.write ( "};\n" )

f.write ( '\nfinal String[][] commandDescriptions = {\n')
first = True
for appInfo in appNames:    
   name = appInfo[0]
   if not first:
      f.write (",\n")
   f.write  ("  /* " + name + "*/\n")
   f.write ("{")
   values = sortByParamId (unsortedconfigDB [name])   
   count = 0
   for item in values:   
      # print str(item)
      if item != values[0]: # next command
         f.write (',\n')
      info = str(item[1]['Info'])
      info = info.replace ('\"', '' )
      f.write ( '\"' + info + '\"') 
      first = False
      count = count + 1
      
   f.write ( "\n}")  
f.write ( "};\n" )

f.write ( '\nfinal String[][] paramIds = {\n' )
first = True
for appInfo in appNames:    
   name = appInfo[0]
   if not first:
      f.write (",\n")
   f.write  ("  /* " + name + "*/\n")
   f.write ("{")
   values = sortByParamId (unsortedconfigDB [name])   
   count = 0
   for item in values:   
      # print str(item)
      if item != values[0]: # next command
         f.write (',')
      f.write ('\"' + str(item[1]['ParamID']) + '\"') 
      first = False
      count = count + 1    
   f.write ( "}")  
f.write ( "};\n" )

f.write ( '\nfinal String[][] configTypes = {\n' )
first = True
for appInfo in appNames:    
   name = appInfo[0]
   if not first:
      f.write (",\n")
   f.write  ("  /* " + name + "*/\n")
   f.write ("{")
   values = sortByParamId (unsortedconfigDB [name])   
   count = 0
   for item in values:   
      # print str(item)
      if item != values[0]: # next command
         f.write (',')
      f.write ('\"' + item[1]['DataType'] + '\"') 
      first = False
      count = count + 1
      
   f.write ( "}")  
f.write ( "};\n" )

f.write ( '\nfinal String[] appNames = {\n' )
first = True
count = 0
for appInfo in appNames:    
   name = appInfo[0]
   if not first:
      f.write (",")
      if count == 10:
         count = 0
         f.write ( '\n' )
   f.write  ('\"' + name + '\"')
   first = False
   count = count + 1
f.write ( "};\n" )


f.close ()