# NOTE: rename as mtgC
from collections import OrderedDict
import re

#                    Name                             AppID
unsortedAppIDs = dict(Registration                   = 31,
                      Configuration                  = 32,
                      ConfigurationDiagnostics       = 33,
                      ChannelPing                    = 34,
                      GCL                            = 35,
                      TaskDeliveryApp                = 36,
                      DataLogger                     = 37,
                      Reprogramming                  = 38,
                      FTS                            = 39, # File Transfer Service
                      Diagnostics                    = 40,
                      PowerManagerAdapter            = 41,
                      CommServices                   = 128,
                      PowerManagement                = 129,
                      DebugLogs                      = 131,
                      Watchdog                       = 132,
                      GpsManager                     = 133,
                      AppStartup                     = 134,
                      GSM                            = 135,
                      Iridium                        = 136,
                      Ethernet                       = 137,
                      DiagnosticsAppStatus           = 138,
                      DiagnosticsAppReporting        = 139,
                      DebugLogLevelLimits            = 140,
                      LoggingRuntimeApplication      = 141,
                      TimeManager                    = 142,
                      DataloggerMonitor              = 143,
                      CPing                          = 144,
                      ConfigTool                     = 145,
                      Shutdown                       = 146,
                      HoursOfOperationApp            = 147,
                      HourMeter                      = 148,
                      DeletionApp                    = 149,
                      PlatformCANServiceApp          = 150,
                      TMActivityLog                  = 151,
                      QualcommLegacy                 = 152,
                      AppStartupAdapter              = 153,
                      GSMNetworkSimulator            = 154,
                      TopMon                         = 155,
                      OperatorAlertComponent         = 169,
                      SARUIApp                       = 170,
                      StartInstaller                 = 171,
                      BreadcrumbsApp                 = 172,
                      SMS                            = 173,
                      SAOnboardReprogrammingApp      = 174,
                      Start                          = 175,
                      DiagnosticBrain                = 176,
                      WiFiAdapter                    = 177,
                      MobileRTK                      = 178,
                      GreenstarDataManager           = 200,
                      RemoteScreenApp                = 201,
                      LicenseManagement              = 202,
                      ConnectedDeviceProxyApp        = 203,
                      SAO                            = 204,
                      DebugInterface                 = 205,
                      CropSense                      = 210,
                      FactoryDataMonitor             = 211,
                      TimberCare                     = 212,
                      GSixOTAUpdate                  = 213,
                      OSN                            = 214, # Onboard State Notification
                      CANWANControl                  = 217,
                     )

appIDs = OrderedDict(sorted(unsortedAppIDs.items(), key=lambda t: t[1]))

unsortedconfigDB = dict()

unsortedconfigDB['BreadcrumbsApp'] = \
         dict(EnableBreadcrumbFeature                             = {'ParamID' : 1,  'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'Enables / disables the breadcrumb feature.'},
              BreadcrumbTimeInterval                              = {'ParamID' : 2,  'DataType' : 'UINT16',  'Default' : 1800,  'Info' : r'**Seconds**Time in seconds since last breadcrumb point before another breadcrumb is logged automatically.'},
              MinimumDistance                                     = {'ParamID' : 3,  'DataType' : 'UINT16',  'Default' : 25,    'Info' : r'**Meters**A displacement by this distance or greater from last point is required for a breadcrumb point to be logged when at least bread crumb time interval has elapsed since the last bread crumb record.'},
              HeadingTrigger                                      = {'ParamID' : 4,  'DataType' : 'UINT8',   'Default' : 10,    'Info' : r'**Degrees**A change (+/-) in heading by this angle or greater will cause a breadcrumb point to be logged. See HeadingTriggerDelay below. Set to zero to disable heading change trigger.'},
              HeadingTriggerDelay                                 = {'ParamID' : 5,  'DataType' : 'UINT16',  'Default' : 3,     'Info' : r'**Seconds**Minimum time in seconds that the heading change must be above the limit to trigger a breadcrumb point.'},
              MachineStateTriggerEnabled                          = {'ParamID' : 6,  'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'If true, a point is logged when the machine state changes.'},
              LogFuelLevelInBreadcrumb                            = {'ParamID' : 7,  'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'If true, fuel level is logged in each breadcrumb.'},
              LogMachineStateInBreadcrumb                         = {'ParamID' : 8,  'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'If true, the machine state is logged in each breadcrumb.'},
              MaxAcceptableAgeOfGPSFix                            = {'ParamID' : 10, 'DataType' : 'UINT16',  'Default' : 10,    'Info' : r'**Seconds**If the GPS fix is older than this, it is taken as invalid for breadcrumb purposes.'},
              DistanceFromLastCourseThreshold                     = {'ParamID' : 11, 'DataType' : 'UINT16',  'Default' : 61,    'Info' : r'**Meters**'},
              MinElapsedTimeSinceLastBreadcrumbForHeadingTriggers = {'ParamID' : 12, 'DataType' : 'UINT16',  'Default' : 3,     'Info' : r'**Seconds**Minimum number of seconds that must pass since the last breadcrumb of any kind before triggering a breadcrumb based on heading.'},
              LocationHistoryReportPeriod                         = {'ParamID' : 13, 'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'**Seconds**Number of seconds to wait between automatically sending Location History Reports at sufficient routing level to cause the device to call in.'},
              LogCellularTechnologyInBreadcrumb                   = {'ParamID' : 14, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'If true, cell technology is logged in each breadcrumb.'},
              LogRSSIInBreadcrumb                                 = {'ParamID' : 15, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'If true, RSSI is logged in each breadcrumb.'},
             )

unsortedconfigDB['ChannelPing'] = \
         dict(PingNetworkID                         = {'ParamID' : 1,  'DataType' : 'UINT8',   'Default' : 255,   'Info' : r'**0=GTT, 1=Iridium, 2=GSM, 3=Ethernet, 4=WiFi, 255=NA**When sending a ping request, identifies the network on which to send the ping request to the host, and on which the host should send the response.'},
              InitiatePing                          = {'ParamID' : 4,  'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'Set this value to TRUE to initiate a ping. After queuing a ping to comm services, terminal will set the value back to 0.'},
              LastPingRequestFromMWGTimestamp       = {'ParamID' : 9,  'DataType' : 'INT64',   'Default' : 0,     'Info' : r'**UTC Time in Seconds**Timestamp at which MWG initiated a ping request.'},
              LastPingRequestFromMWGCorrelationID   = {'ParamID' : 10, 'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'CorrelationID of last MWG ping request sent.'},
              TimestampOfPingTurnaroundAtHost       = {'ParamID' : 11, 'DataType' : 'INT64',   'Default' : 0,     'Info' : r'**UTC Time in Seconds**When a ping response is received from the host, it contains the timestamp at which the host received the ping request from the MWG.'},
              LastPingResponseFromHostCorrelationID = {'ParamID' : 12, 'DataType' : 'UINT32',  'Default' : 3,     'Info' : r'Correlation ID of the last ping response received from the host.'},
              LastPingRequestRxFromHostTimestamp    = {'ParamID' : 13, 'DataType' : 'INT64',   'Default' : 0,     'Info' : r'**UTC Time in Seconds**Timestamp of the last receipt of a ping request from the host by the MWG.'},
              CorrelationIDOfLastPingReqFromHost    = {'ParamID' : 14, 'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'Correlation ID of the last ping request received from the host by the MWG.'},
             )

unsortedconfigDB['CommServices'] = \
         dict(CellCallInBaseTime                  = {'ParamID' : 1,  'DataType' : 'UINT16',  'Default' : 0,        'Info' : r'**Minutes**Daily call-in base time. Minutes since midnight UTC.'},
              CellCallInRepeatInterval            = {'ParamID' : 2,  'DataType' : 'UINT16',  'Default' : 0,        'Info' : r'**Minutes**Number of minutes between scheduled cellular call-in times (starting with CellCallInBaseTime).'},
              CellCallInDays                      = {'ParamID' : 3,  'DataType' : 'UINT8',   'Default' : 0x7F,     'Info' : r'Bit field indicating which days the cell call-in schedule will be applied. A "1" indicates to call-in on that day. Multiple days can be set.'},
              SatelliteCallInBaseTime             = {'ParamID' : 4,  'DataType' : 'UINT16',  'Default' : 0,        'Info' : r'**Minutes**Daily call-in base time. Minutes since midnight UTC.'},
              SatelliteCallInRepeatInterval       = {'ParamID' : 5,  'DataType' : 'UINT16',  'Default' : 0,        'Info' : r'**Minutes**Number of minutes between scheduled cellular call-in times (starting with CellCallInBaseTime).'},
              SatelliteCallInDays                 = {'ParamID' : 6,  'DataType' : 'UINT8',   'Default' : 0x7F,     'Info' : r'Bit field indicating which days the cell call-in schedule will be applied. A "1" indicates to call-in on that day. Multiple days can be set.'},
              CommDeviceID                        = {'ParamID' : 7,  'DataType' : 'UINT32',  'Default' : 0,        'Info' : r'Used by communications services as the unique address of this device. '},
              EnableEthernet                      = {'ParamID' : 8,  'DataType' : 'BOOLEAN', 'Default' : False,    'Info' : r'If true, allows messages to be sent on Ethernet adapter.'},
              EnableGSM                           = {'ParamID' : 9,  'DataType' : 'BOOLEAN', 'Default' : True,     'Info' : r'If true, allows messages to be routed on GSM adapter.'},
              EnableIridium                       = {'ParamID' : 10, 'DataType' : 'BOOLEAN', 'Default' : True,     'Info' : r'If true, allows messages to be routed on Iridium.'},
              ForceCall                           = {'ParamID' : 11, 'DataType' : 'BOOLEAN', 'Default' : False,    'Info' : r'When written to with a non-0 value, causes Comm Services to force a call. Comm Services sets the value back to 0 after the force call is recognized.'},
              SatelliteStayAwakePeriod            = {'ParamID' : 12, 'DataType' : 'UINT8',   'Default' : 3,        'Info' : r'**Minutes**This is the period of time that the satellite modem on the MWG will stay awake to listen for a ring alert.'},
              EnvironmentID                       = {'ParamID' : 13, 'DataType' : 'UINT8',   'Default' : 0,        'Info' : r'Environment ID of the host environment with which this MWG is communicating.'},
              AppIDOfMessagesToErase              = {'ParamID' : 14, 'DataType' : 'UINT16',  'Default' : 0,        'Info' : r'Set by Service Advisor prior to initiating an erase (cancel) of queued messages from the MWG.'},
              MessagesEraseCommand                = {'ParamID' : 15, 'DataType' : 'UINT8',   'Default' : 0,        'Info' : r'Set to 1 by Service Advisor to trigger the cancellation of messages having the AppID AppIDOfMessagesToErase.'},
              MaxOutboxSize                       = {'ParamID' : 16, 'DataType' : 'UINT32',  'Default' : 62914560, 'Info' : r'**Bytes**Maximum size of the outbox, in bytes (as computed according to the sum of all outbound payload sizes and the sum of all outbound file sizes).'},
              EnableSMS                           = {'ParamID' : 17, 'DataType' : 'BOOLEAN', 'Default' : True,     'Info' : r'If true, allows messages to be routed on SMS adapter.'},
              CarrierRegSatEscalationThreshold    = {'ParamID' : 18, 'DataType' : 'UINT16',  'Default' : 3600,     'Info' : r'**Seconds**If the device is not currently registered with the GSM carrier network, this parameter specifies the minimum number of seconds that must pass between the last registration or boot time (whichever is more recent) before a TM that is eligible to be sent over both GSM and Iridium may be escalated to Iridium.'},
              IncomingTransferExpirationThreshold = {'ParamID' : 19, 'DataType' : 'UINT32',  'Default' : 5184000,  'Info' : r'**Seconds**Specifies the amount of time in seconds comm services shall allow an incoming file transfer to remain idle (i.e. no TMs related to the transfer received) before cancelling the transfer.'},
              EnableFTSTransferModes              = {'ParamID' : 20, 'DataType' : 'UINT8',   'Default' : 1,        'Info' : r'**0=TPP Only, 1=Atomos with TPP fallback**Indicates which FTS transfer modes are enabled.'},
              EnableWiFi                          = {'ParamID' : 21, 'DataType' : 'BOOLEAN', 'Default' : False,    'Info' : r'If true, allows messages to be sent on WiFi adapter.'},
              NotifyCallStillOpenInterval         = {'ParamID' : 22, 'DataType' : 'UINT32',  'Default' : 3600,     'Info' : r'**Seconds**The amount of time to wait, in seconds, while a call is active, before sending a notification that the call is still active.'},
              InitiateBlackout                    = {'ParamID' : 23, 'DataType' : 'BOOLEAN', 'Default' : False,    'Info' : r'If TRUE, Comm Services must only send TMs with blackout override specified in their metadata.'},
              SatelliteEscalationTime             = {'ParamID' : 24, 'DataType' : 'UINT32',  'Default' : 7200,     'Info' : r'The amount of time to wait, in seconds, before a TM that can escalate to satellite due to age will do so.'},
             )

unsortedconfigDB['Configuration'] = \
         dict(MonitoredParamsOnCallInSatCapable              = {'ParamID' : 1,  'DataType' : 'BYTEARRAY', 'Default' : None,  'Info' : r'Content of the ByteArray is: UInt16: Number of parameters, Begin Repeat, UInt16 AppID, UInt16 ParamID, End Repeat'},
              MonitoredParamsOnCallInCellOnly                = {'ParamID' : 2,  'DataType' : 'BYTEARRAY', 'Default' : None,  'Info' : r'Content of the ByteArray is: UInt16: Number of parameters, Begin Repeat, UInt16 AppID, UInt16 ParamID, End Repeat'},
              MonitoredParamsOnChangeSatCapable              = {'ParamID' : 3,  'DataType' : 'BYTEARRAY', 'Default' : None,  'Info' : r'Content of the ByteArray is: UInt16: Number of parameters, Begin Repeat, UInt16 AppID, UInt16 ParamID, End Repeat'},
              MonitoredParamsOnChangeCellOnly                = {'ParamID' : 4,  'DataType' : 'BYTEARRAY', 'Default' : None,  'Info' : r'Content of the ByteArray is: UInt16: Number of parameters, Begin Repeat, UInt16 AppID, UInt16 ParamID, End Repeat'},
              MonitoredParamsAlwaysMonitorOnChangeSatCapable = {'ParamID' : 5,  'DataType' : 'BYTEARRAY', 'Default' : None,  'Info' : r'Content of the ByteArray is: UInt16: Number of parameters, Begin Repeat, UInt16 AppID, UInt16 ParamID, End Repeat'},
              FlushDirtyCache                                = {'ParamID' : 6,  'DataType' : 'BOOLEAN',   'Default' : False, 'Info' : r'Set to true to cause ConfigApp to flush cached values to the config DB.'},
             )

unsortedconfigDB['ConnectedDeviceProxyApp'] = \
         dict(CurrentlyConnectedDeviceSerialNumbers      = {'ParamID' : 1,  'DataType' : 'STRING',    'Default' : [],      'Info' : r'Serial number(s) of devices that are currently considered associated with the MTG.'},
              LastHostAckTimestamp                       = {'ParamID' : 2,  'DataType' : 'INT64',     'Default' : 0,       'Info' : r'Host generated timestamp picked up from the last accepted TM ConnectedDeviceAcknowledgement.'},
              ClearPersistedToDeviceTMs                  = {'ParamID' : 3,  'DataType' : 'BOOLEAN',   'Default' : False,   'Info' : r'When set to 1 (intended by OBD), it will initiate the clearing of all TMs stored in the MTG for delivery to the connected device(s).'},
              ForgetConnectedDeviceTimeout               = {'ParamID' : 4,  'DataType' : 'UINT32',    'Default' : 7200,    'Info' : r'**Seconds**When a connected device has not been seen by the MTG for this amount of key-on time, the MTG will remove any stored data related to that device, and the device will be no longer considered as connected to the MTG.'},
              AppIDStaticRegistrationList                = {'ParamID' : 5,  'DataType' : 'STRING',    'Default' : '200',   'Info' : r'**Comma separated list of decimal numbers**The Proxy App needs to register for certain AppIDs (ie. WDT) to ensure that TMs are stored even when there is no connected device.'},
              ForgetTMTimeout                            = {'ParamID' : 6,  'DataType' : 'UINT32',    'Default' : 7884000, 'Info' : r'**Seconds**This is a maximum number of seconds to wait for a persisted TM to be delivered.'},
              OSPLStarted                                = {'ParamID' : 7,  'DataType' : 'BOOLEAN',   'Default' : False,   'Info' : r'When set to true, ospl (DDS) has been started. False means DDS has not been started.'},
              StartDDS                                   = {'ParamID' : 8,  'DataType' : 'BOOLEAN',   'Default' : False,   'Info' : r'When set to true, the proxy app will signal to itself to start DDS.  (This should only occurs if the OSPL Started param (#7) is false.)'},
              MaxTMFileStorageSize                       = {'ParamID' : 9,  'DataType' : 'UINT32',    'Default' : 20000,   'Info' : r'**KBytes**Maximum amount of memory that the MTG will reserve for file transfers to/from host.'},
              WDTAllow                                   = {'ParamID' : 10, 'DataType' : 'BOOLEAN',   'Default' : False,   'Info' : r'Set to true when the host determines that Wireless Data Transfer is allowed via a Connected Device.'},
              RawNMEAForwarding                          = {'ParamID' : 11, 'DataType' : 'BOOLEAN',   'Default' : False,   'Info' : r'Set to true to activate forwarding of Raw NMEA sentences to the connected device.'},
              ConnectedDeviceSerialNumberDeviceDiscovery = {'ParamID' : 12, 'DataType' : 'STRING',    'Default' : '',      'Info' : r'Serial number of device(s) that are currently sending the DeviceDiscovery messages to MTG.'},
              ForgetConnectedDeviceTimeoutValue          = {'ParamID' : 13, 'DataType' : 'BYTEARRAY', 'Default' : None,    'Info' : r'When a connected device has not been seen by the MTG for the threshold time of Device Discovery (1 min), then the duration from then on for that device, is stored in this.'},
             )

unsortedconfigDB['DataLogger'] = \
         dict(CreateDetailedGranules                       = {'ParamID' : 1,  'DataType' : 'UINT8',   'Default' : 1,     'Info' : r'If 1, Datalogger will create the detailed granules and send these via cell.'},
              Create24HrSatGranules                        = {'ParamID' : 2,  'DataType' : 'UINT8',   'Default' : 1,     'Info' : r'If 1, Datalogger will create daily granules and send these with a routing class that also allows satellite transmission.'},
              Create25EngHrSatGranules                     = {'ParamID' : 3,  'DataType' : 'UINT8',   'Default' : 1,     'Info' : r'If 1, Datalogger will create granules at 25 engine hour boundaries and send these with a routing class that also allows satellite transmission.'},
              MaxAlertNotificationsPerAlertTypePerKeyCycle = {'ParamID' : 4,  'DataType' : 'UINT32',  'Default' : 100,   'Info' : r'The maximum number of times alert notifications are generated per key cycle per Alert/EventID.'},
              ConfigModelID                                = {'ParamID' : 5,  'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'Integer ID "ConfigModelID" in the config loaded by the datalogger.'},
              ConfigModel                                  = {'ParamID' : 6,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'ConfigModel string contained in the config.'},
              ConfigTimestamp                              = {'ParamID' : 7,  'DataType' : 'INT64',   'Default' : 0,     'Info' : r'**UTC Time in Seconds**Timestamp from the DataLoggerConfigSetup TM. Represents the dattime at which th host sent the config to the terminal.'},
              ConfigTypeId                                 = {'ParamID' : 8,  'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'**0=Unknown, 1=Default, 2=Default911, 3=Select, 4=ConfigWithoutCA, 5=ConfigWithCA**From XML config element'},
              UltimateOrHigherConfigAvailable              = {'ParamID' : 9,  'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'Filled in by datalogger at startup.'},
              SatelliteGranuleDuration                     = {'ParamID' : 10, 'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'**Seconds**Duration of a satellite granule in seconds. '},
              EngineHourGranuleDuration                    = {'ParamID' : 11, 'DataType' : 'UINT32',  'Default' : 25,    'Info' : r'**Hours**Duration of an engine hour granule in hours.'},
              EnableCropBasedGranule                       = {'ParamID' : 12, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'Enables logic in datalogger system executive that advances granules on crop change and puts the crop ID into the granule.'},
              ReportConfigActionOnStartup                  = {'ParamID' : 30, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'Set by app that changed the config files (datalogger or datalogger monitor).'},
              CorrelationIDToUseInConfigStatusTM           = {'ParamID' : 31, 'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'Set by datalogger on receipt of config from CS (except in the case that the received TM has an earlier timestamp than one already received).'},
              LastConfigChange                             = {'ParamID' : 32, 'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'**0=Unspecified, 1=Starting with default config, 2=Config from host, 3=Rollback to NonCA, 4=Rollback to 911, 5=Default due to loss of registration**See description of ReportConfigActionOnStartup.'},
              LastConfigChangeTimestamp                    = {'ParamID' : 33, 'DataType' : 'INT64',   'Default' : 0,     'Info' : r'See description of ReportConfigActionOnStartup'},
              ConfigLastLoadedDescription                  = {'ParamID' : 34, 'DataType' : 'STRING',  'Default' : '',    'Info' : r'Changed by datalogger on successful load of a config.'},
              ConfigLastLoadedTimestamp                    = {'ParamID' : 35, 'DataType' : 'INT64',   'Default' : 0,     'Info' : r'Updated by datalogger to the current system time on successful load of a config and on a wake/key on when a config has already been successfully loaded.'},
              DataloggerErrorCount                         = {'ParamID' : 37, 'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'Used to track the number of times Datalogger entered an error state during a single key cycle.'},
              SensorLowThreshold                           = {'ParamID' : 38, 'DataType' : 'UINT16',  'Default' : 25,    'Info' : r'**Units of 0.05 Volts**Threshold voltage below which input is regarded as low.'},
              SensorHighThreshold                          = {'ParamID' : 39, 'DataType' : 'UINT16',  'Default' : 50,    'Info' : r'**Units of 0.05 Volts**Threshold voltage above which input is regarded as high.'},
              SensorIgnitionDelayOnColdBoot                = {'ParamID' : 40, 'DataType' : 'UINT16',  'Default' : 60,    'Info' : r'**Seconds**Time duration to ignore sensor alerts on cold boot.'},
              SensorIgnitionDelayOnWakeFromSleep           = {'ParamID' : 41, 'DataType' : 'UINT16',  'Default' : 120,   'Info' : r'**Seconds**Time duration to ignore sensor alerts on warm start (wake from sleep).'},
             )

unsortedconfigDB['DataloggerMonitor'] = \
         dict(CPULimit        = {'ParamID' : 1, 'DataType' : 'UINT8',  'Default' : 50,  'Info' : r'**Percent**This is the ceiling on acceptable CPU usage by Datalogger before it is considered to be in a high CPU state.'},
              HighCPUDuration = {'ParamID' : 2, 'DataType' : 'UINT16', 'Default' : 120, 'Info' : r'**Seconds**This is the ceiling on the length of time Datalogger can be in a high CPU state before it triggers a shutdown by DataloggerMonitor.'},
              RAMLimit        = {'ParamID' : 3, 'DataType' : 'UINT8',  'Default' : 30,  'Info' : r'**Megabytes**This is the ceiling on acceptable RAM usage by Datalogger before it triggers a shutdown by DataloggerMonitor.'},
             )

unsortedconfigDB['DebugInterface'] = \
         dict(EnableDebugText             = {'ParamID' : 1, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'Enable/Disable all debug text being output.'},
              EnableDebugTextSocket       = {'ParamID' : 2, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'Enable the TCP Socket for debug text instead of RS-232.'},
              DebugTextPort               = {'ParamID' : 3, 'DataType' : 'UINT32',  'Default' : 6000,  'Info' : r'Set the TCP Socket port to communicate on for debug text.'},
              EnableHostCommSnifferSocket = {'ParamID' : 4, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'Enable the TCP Socket for Host Communication TPP Traffic in order to sniff it in real time.'},
              HostCommSnifferPort         = {'ParamID' : 5, 'DataType' : 'UINT32',  'Default' : 6001,  'Info' : r'Set the TCP Socket port to communicate on for Host Communication TPP Traffic.'},
             )

unsortedconfigDB['DebugLogs'] = \
         dict(DefaultLogLevelLimit                = {'ParamID' : 1,  'DataType' : 'UINT8',   'Default' : 9,     'Info' : r'**0=SystemDefault, 1=Reserved, 2=Reserved, 3=OpEvent_Modification, 4=OpEvent_CriticalEvent, 5=Diagnostic_Header, 6=Alert, 7=Warning, 8=Notice, 9=Debug, 10=Debug2**This default is used only if there is no source specific limit that applies to a particular log message, or the source-specific limit indicates to use the system-wide log level.'},
              PrintscreenLogLevelLimit            = {'ParamID' : 2,  'DataType' : 'UINT8',   'Default' : 6,     'Info' : r'**0=SystemDefault, 1=Reserved, 2=Reserved, 3=OpEvent_Modification, 4=OpEvent_CriticalEvent, 5=Diagnostic_Header, 6=Alert, 7=Warning, 8=Notice, 9=Debug, 10=Debug2**Any log entries equal to or more critical than this setting will be printed on screen.'},
              MaxLogFileSize                      = {'ParamID' : 3,  'DataType' : 'UINT32',  'Default' : 1,     'Info' : r'**Megabytes**Number of bytes required before the debug log advances to a new log file due to the reason of file size limit reached.'},
              MaxTotalSizeOfLogFilesOnDisk        = {'ParamID' : 4,  'DataType' : 'UINT32',  'Default' : 20,    'Info' : r'**Megabytes**Number of bytes collected into log files together on the terminal.'},
              DeleteLogFilesOnSuccessfulQueuing   = {'ParamID' : 5,  'DataType' : 'BOOLEAN', 'Default' : True,  'Info' : r'When responding to a log retrieval Telematics Message, delete the log file(s) that have been successfully queued.'},
              FlushQueueOnWarning                 = {'ParamID' : 6,  'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'NOT USED - Should the log runtime write the buffered entries to disk immediately if a warning is received.'},
              FlushQueueOnAlert                   = {'ParamID' : 7,  'DataType' : 'BOOLEAN', 'Default' : True,  'Info' : r'NOT USED - Should the log runtime write the buffered entries to disk immediately to disk if an a log entry with logtype = "alert" is found. '},
              LogBufferHighWatermark              = {'ParamID' : 8,  'DataType' : 'UINT32',  'Default' : 10,    'Info' : r'NOT USED - The count of log entries to cache before writing them to disk because there are too many in cache.'},
              KeepFileOpenBetweenWrites           = {'ParamID' : 9,  'DataType' : 'BOOLEAN', 'Default' : True,  'Info' : r'Should the logger keep the file open after a block of entries is written to disk. Keeping it open allows the OS to buffer the file, resulting in less flash wear. However, it is then prone to loss of data if there is a system crash. Applies to normal log file and alert only log file.'},
              MaxAgeOfLogBufferEntries            = {'ParamID' : 10, 'DataType' : 'UINT16',  'Default' : 60,    'Info' : r'NOT USED - **Seconds**If logging by applications is infrequent, the cache high watermark may not be reached for a long time. This param specifies the max duration between a file write operation and having unwritten log entries in the buffer. If this age is reached, the buffer is written to file.'},
              OBD_SendLastDebugLog                = {'ParamID' : 11, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'When set to 1, debugLogsOTA app takes a request to send the latest debug log file to the server and sets this param to 0.'},
              MaxEventLogNotificationsPerKeyCycle = {'ParamID' : 12, 'DataType' : 'UINT16',  'Default' : 10,    'Info' : r'The maximum event log notifications sent to the host per key cycle. Any more will be logged as debug log entries only. The count resets on transition to key on.'},
              AppIDCaptureToEventLog              = {'ParamID' : 13, 'DataType' : 'UINT16',  'Default' : 0,     'Info' : r'If non-zero, DebugLog entries for this AppID will be duplicated into EventLog.'},
             )

unsortedconfigDB['Diagnostics'] = \
         dict(DeviceStateReportOnCallEnabled = {'ParamID' : 1, 'DataType' : 'BOOLEAN', 'Default' : True,           'Info' : r'Indicates whether the Diagnostics App is enabled to send the Device State Report telematics message at each call-in.'},
              CallResultDataEnabled          = {'ParamID' : 2, 'DataType' : 'BOOLEAN', 'Default' : True,           'Info' : r'Indicates whether the Diagnostics App is enabled to send the Call Result Data telematics message for each cellular call attempt.'},
              CPUHighLimit                   = {'ParamID' : 3, 'DataType' : 'UINT8',   'Default' : 80,             'Info' : r'**Percent**If the CPU use is above this limit for more than 30 sec, the CPUOverLimit flag will be set and remains set for the key cycle.'},
              MemoryHighLimit                = {'ParamID' : 4, 'DataType' : 'UINT8',   'Default' : 80,             'Info' : r'**Percent**The total size of memory used in the sytem will be periodically checked. At any point, if memory used is greater than the limit, the MemoryOverLimit flag is set and will remain set for the key cycle.'},
              FlashFreeSizeLimit             = {'ParamID' : 5, 'DataType' : 'UINT16',  'Default' : 100,            'Info' : r'**Megabytes**Periodically, the available free space in the flash memory will be monitored. At any point, if it is less than the predefined limit, the FlashOverLimit param is set and remains set for the key cycle.'},
              SMSCarrierAlertAddress         = {'ParamID' : 6, 'DataType' : 'STRING',  'Default' : '+15333545938', 'Info' : r'MDN to which an SMS Carrier Alert message should be sent.'},
              RAMDiskFreeSizeLimit           = {'ParamID' : 7, 'DataType' : 'UINT16',  'Default' : 1,              'Info' : r'**Megabytes**Periodically, the available free space in the RAM disk root (/) will be monitored.'},
             )

unsortedconfigDB['DiagnosticsAppReporting'] = \
         dict(CellModemType                        = {'ParamID' : 1,   'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=modem absent, 1=Wavecom WMP-150 GSM modem**Presence and type of cell modem.'},
              CellSIMStatus                        = {'ParamID' : 2,   'DataType' : 'UINT8',   'Default' : 2,          'Info' : r'**0=present and ok, 1=not present, 2=SIM error**Presence and status of SIM.'},
              EngineHoursAvailableOnCAN            = {'ParamID' : 3,   'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'Whether Engine Hours is being reported from CAN.'},
              MiniGranuleCreationCount             = {'ParamID' : 4,   'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Count of mini granules created by datalogger (3 min intervals).'},
              GSMRegistrationState                 = {'ParamID' : 5,   'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'Whether registration is complete or pending for the GSM Modem.'},
              SatelliteRegistrationState           = {'ParamID' : 8,   'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'Whether registration is complete or pending for the satellite modem.'},
              EngineTurnOnCount                    = {'ParamID' : 11,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Increments each time engine transitions from off to on. (Includes cases where we come out of sleep / hibernate and see that engine is already on)'},
              KeyTurnOnCount                       = {'ParamID' : 12,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Increments each time key is turned on. (Includes cases where we come out of sleep / hibernate and see that key is already on)'},
              LastCAN1Status                       = {'ParamID' : 13,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=No CAN activity, 1=250kHz, 2=500kHz**Updated only when key is on.'},
              LastCAN2Status                       = {'ParamID' : 14,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=No CAN activity, 1=250kHz, 2=500kHz**Updated only when key is on.'},
              LastCAN3Status                       = {'ParamID' : 15,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=No CAN activity, 1=250kHz, 2=500kHz**Updated only when key is on.'},
              LastCAN4Status                       = {'ParamID' : 16,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=No CAN activity, 1=250kHz, 2=500kHz**Updated only when key is on.'},
              CPUOverLimit                         = {'ParamID' : 17,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'True if CPU use has been over a limit determined by engineering at any time since last key on.'},
              RAMUsageOverLimit                    = {'ParamID' : 18,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'True if total system memory use has been over a limit determined by engineering at anytime since last key on.'},
              FlashUsageOverLimit                  = {'ParamID' : 19,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'True if flash use in the system is over limit at any time since last key on. The limit is determined by engineering.'},
              LastPowerManagerState                = {'ParamID' : 20,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=Unknown, 1=Starting, 2=Running, 3=Shutting down, 4=Shutdown, 5=Hibernate**Power manager updates this at any time it changes state.'},
              LastPowerManagerShutdownGraceful     = {'ParamID' : 21,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'Set to True on startup if LastPowerManagerState was in (shutdown, hibernate).'},
              LastAppsstartState                   = {'ParamID' : 22,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=Unknown, 1=Starting, 2=Running, 3=Shutting down, 4=Shutdown, 5=Hibernate**Power manager updates this at any time it changes state.'},
              LastAppsstartShutdownGraceful        = {'ParamID' : 23,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'Set to True on startup if LastAppsstartState was in (shutdown, hibernate).'},
              RTCErrorAtStartup                    = {'ParamID' : 24,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'True if the RTC had not maintained the correct time at startup.'},
              RTCUnsynced                          = {'ParamID' : 25,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'True if RTC time at startup was suspect and there has been no time sync yet.'},
              KeyOnsSinceGoodFix                   = {'ParamID' : 26,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'Number of key ons since a "good fix". Good fix is currently defined as a 2D or 3D fix.'},
              RegistrationChangeReason             = {'ParamID' : 27,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=No change pending, 1=CAN change, 2=ServiceTool change**'},
              LastCountedCellFailureDay            = {'ParamID' : 28,  'DataType' : 'INT64',   'Default' : 0,          'Info' : r'When a cell call fails and results in incrementing the count of CellCommFailureDays, this timestamp is updated to today.'},
              CellCommFailureDays                  = {'ParamID' : 29,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Number of days that attempted cell calls have failed. Resets on successful send messages via cell, disabled cell.'},
              LastCountedSatFailureDay             = {'ParamID' : 30,  'DataType' : 'INT64',   'Default' : 0,          'Info' : r'When a sat data exchange fails and results in incrementing the count of SatCommFailureDays, this timestamp is updated to today.'},
              SatCommFailureDays                   = {'ParamID' : 31,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Number of days that attempted sat data exchanges have failed. Resets on successful send messages via sat, disabled sat.'},
              CellModemErrors                      = {'ParamID' : 32,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=No error or cell not enabled, 1=Modem unresponsive, 2=No SIM, 3=Network registration error, 4=Unable to establish call for 10+ attempts with sufficient RSSI**Error in cell modem.'},
              SatelliteModemErrors                 = {'ParamID' : 35,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=No error or sat not enabled, 1=Modem unresponsive, 2=Network registration error, 3=Unable to send for 10 or more attempts, with sufficient signal level, 4=Unable to retrieve message (which the sat says exists) for 10 or more attempts with sufficient signal level**'},
              SatelliteModemAntennaFailure         = {'ParamID' : 36,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'If true, there is a problem with the satellite antenna.'},
              GPSError                             = {'ParamID' : 38,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=No error, 1=GPS unresponsive, 2=engine on but no fix for 1 hour**Set if the GPS detects any errors'},
              GPSAntennaStatus                     = {'ParamID' : 39,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=Unknown, 1=OK, 2=Short, 3=Open**'},
              GSM_CallInProgress                   = {'ParamID' : 41,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r''},
              GSM_RSSIAtStart                      = {'ParamID' : 42,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r''},
              GSM_CallBeginTimestamp               = {'ParamID' : 43,  'DataType' : 'INT64',   'Default' : 0,          'Info' : r''},
              GSM_PositionAtStart_Latitude         = {'ParamID' : 44,  'DataType' : 'DOUBLE',  'Default' : 0.0,        'Info' : r'**Degrees**-90 to +90.'},
              GSM_PositionAtStart_Longitude        = {'ParamID' : 45,  'DataType' : 'DOUBLE',  'Default' : 0.0,        'Info' : r'**Degrees**-180 to +180 degrees: E is positive, W is negative.'},
              GSM_GPSTimestampAtStart              = {'ParamID' : 46,  'DataType' : 'INT64',   'Default' : 0,          'Info' : r'Last known GPS timestamp is stored on receipt of CallAttempt notification with notificationType = CallBegin/CallSkipped.'},
              GSM_AltitudeAtStart                  = {'ParamID' : 47,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'**Meters**Meters above / below sea level'},
              GSM_CallResult                       = {'ParamID' : 48,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**DWV**'},
              GSM_CallDuration                     = {'ParamID' : 49,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'**Seconds**'},
              SatelliteModemModelID                = {'ParamID' : 50,  'DataType' : 'STRING',  'Default' : '',         'Info' : r'Stored when the modem model ID is retrieved from the satellite modem; blanked if no modem present.'},
              SatelliteModemFirmwareVersion        = {'ParamID' : 51,  'DataType' : 'STRING',  'Default' : '',         'Info' : r'Stored when the modem firmware version is retrieved from the satellite modem; blanked if no modem present.'},
              CellularModemVersion                 = {'ParamID' : 52,  'DataType' : 'STRING',  'Default' : '',         'Info' : r'Stored when the modem version is retrieved from the cellular modem; blanked if no modem present.'},
              GSMSentKBytesLTD                     = {'ParamID' : 53,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes sent over GSM Network.'},
              GSMReceivedKBytesLTD                 = {'ParamID' : 54,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes received over GSM Network.'},
              IridiumSentKBytesLTD                 = {'ParamID' : 55,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes sent over Iridium Network.'},
              IridiumReceivedKBytesLTD             = {'ParamID' : 56,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes received over Iridium Network.'},
              EthernetSentKBytesLTD                = {'ParamID' : 57,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes sent over Ethernet Network.'},
              EthernetReceivedKBytesLTD            = {'ParamID' : 58,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes received over Ethernet Network.'},
              GSMSentPacketsLTD                    = {'ParamID' : 59,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets sent over GSM Network.'},
              GSMReceivedPacketsLTD                = {'ParamID' : 60,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets received over GSM Network.'},
              IridiumSentPacketsLTD                = {'ParamID' : 61,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets sent over Iridium Network.'},
              IridiumReceivedPacketsLTD            = {'ParamID' : 62,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets received over Iridium Network.'},
              EthernetSentPacketsLTD               = {'ParamID' : 63,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets sent over Ethernet Network.'},
              EthernetReceivedPacketsLTD           = {'ParamID' : 64,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets received over Ethernet Network.'},
              GSMFailedPacketsLTD                  = {'ParamID' : 65,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets failed over GSM Network.'},
              GSMFailedKBytesLTD                   = {'ParamID' : 66,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes failed over GSM Network.'},
              IridiumFailedPacketsLTD              = {'ParamID' : 67,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets failed over Iridium Network.'},
              IridiumFailedKBytesLTD               = {'ParamID' : 68,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes failed over Iridium Network.'},
              EthernetFailedPacketsLTD             = {'ParamID' : 69,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets failed over Ethernet Network.'},
              EthernetFailedKBytesLTD              = {'ParamID' : 70,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes failed over Ethernet Network.'},
              PowerOnKeyOnDurationLTD              = {'ParamID' : 71,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'**Seconds**Terminal life-to-date duration in Power-on-key-on power state.'},
              PowerOnKeyOffDurationLTD             = {'ParamID' : 72,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'**Seconds**Terminal life-to-date duration in Power-on-key-off power state.'},
              SleepDurationLTD                     = {'ParamID' : 73,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'**Seconds**Terminal life-to-date duration in Sleep power state.'},
              LastPowerStateEntered                = {'ParamID' : 74,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=Off, 1=Prestart, 2=On, 3=Polling for Sleep Readiness, 4=Preparing for Sleep, 5=Poll for Next Wake Time, 6=Sleep, 7=Polling for Hibernate Readiness, 8=Preparing To Hibernate, 9=Hibernate**Update on each power state transition.'},
              FlashDiskAvailable                   = {'ParamID' : 75,  'DataType' : 'UINT32',  'Default' : 0xFFFFFFFF, 'Info' : r'**KBytes**Total free flash space at last power state change.'},
              RAMDiskAvailable                     = {'ParamID' : 76,  'DataType' : 'UINT32',  'Default' : 0xFFFFFFFF, 'Info' : r'**KBytes**Total free RAM disk space at last power state change.'},
              RAMAvailable                         = {'ParamID' : 77,  'DataType' : 'UINT32',  'Default' : 0xFFFFFFFF, 'Info' : r'**KBytes**Total free RAM at last power state change.'},
              MaxCPUUtilization                    = {'ParamID' : 78,  'DataType' : 'UINT8',   'Default' : 0xFF,       'Info' : r'**Percent**Max CPU utilization over any 30 second period leading up to the last power state change.'},
              IgnitionVoltage                      = {'ParamID' : 79,  'DataType' : 'UINT16',  'Default' : 0,          'Info' : r'**Hundredths of a Volt**The last sample of Ignition Voltage Monitor.'},
              DataLoggerConfigGUID                 = {'ParamID' : 80,  'DataType' : 'STRING',  'Default' : '',         'Info' : r'GUID of config file in use. Updated when DataLogger loads a config file and parses Config GUID.'},
              ResetCount                           = {'ParamID' : 81,  'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Count of unexpected resets/powerups. Incremented at startup when Diagnostics App determines that the last shutdown was not graceful.'},
              BatteryVoltage                       = {'ParamID' : 82,  'DataType' : 'UINT16',  'Default' : 0,          'Info' : r'**Hundredths of a Volt**LastSample of Unswitched power supply voltage.'},
              CAN1ActiveStatus                     = {'ParamID' : 83,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r''},
              CAN2ActiveStatus                     = {'ParamID' : 84,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r''},
              CAN3ActiveStatus                     = {'ParamID' : 85,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r''},
              CAN4ActiveStatus                     = {'ParamID' : 86,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r''},
              CAN1HVoltage                         = {'ParamID' : 87,  'DataType' : 'UINT16',  'Default' : 0,          'Info' : r'**Hundredths of a Volt**Read at some convenient interval between 1 and 30 sec.'},
              CAN1LVoltage                         = {'ParamID' : 88,  'DataType' : 'UINT16',  'Default' : 0,          'Info' : r'**Hundredths of a Volt**Read at some convenient interval between 1 and 30 sec.'},
              CAN2HVoltage                         = {'ParamID' : 89,  'DataType' : 'UINT16',  'Default' : 0,          'Info' : r'**Hundredths of a Volt**Read at some convenient interval between 1 and 30 sec.'},
              CAN2LVoltage                         = {'ParamID' : 90,  'DataType' : 'UINT16',  'Default' : 0,          'Info' : r'**Hundredths of a Volt**Read at some convenient interval between 1 and 30 sec.'},
              CAN3HVoltage                         = {'ParamID' : 91,  'DataType' : 'UINT16',  'Default' : 0,          'Info' : r'**Hundredths of a Volt**Read at some convenient interval between 1 and 30 sec.'},
              CAN3LVoltage                         = {'ParamID' : 92,  'DataType' : 'UINT16',  'Default' : 0,          'Info' : r'**Hundredths of a Volt**Read at some convenient interval between 1 and 30 sec.'},
              UltimateDataSinceKeyOn               = {'ParamID' : 93,  'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'This is updated by DiagnosticsApp at some convenient interval between 1 and 30 sec (or could be on demand).'},
              FlashFreePercent                     = {'ParamID' : 94,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**Percent**Flash free percent at last power change.'},
              CPUFreePercent                       = {'ParamID' : 95,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**Percent**Free CPU computed at 30 sec intervals.'},
              RAMFreePercent                       = {'ParamID' : 96,  'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**Percent**Free RAM best computed on demand.'},
              CurrentSystemDateTime                = {'ParamID' : 97,  'DataType' : 'INT64',   'Default' : 0,          'Info' : r'**UTC Time in Seconds**Updated only in OBD mode.'},
              LastGPSTimestamp                     = {'ParamID' : 98,  'DataType' : 'INT64',   'Default' : 0,          'Info' : r'**UTC Time in Seconds**Timestamp of last good GPS fix. Updated once in 10 to 30 secs.'},
              GPSLatitude                          = {'ParamID' : 99,  'DataType' : 'DOUBLE',  'Default' : 0.0,        'Info' : r'**Degrees**Last good GPS fix. -90 to +90 degrees: N is positive, S is negative.'},
              GPSLongitude                         = {'ParamID' : 100, 'DataType' : 'DOUBLE',  'Default' : 0.0,        'Info' : r'**Degrees**Last good GPS fix. -180 to +180 degrees: E is positive, W is negative.'},
              IPAddressOfLastGPRSConnection        = {'ParamID' : 101, 'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'IP address assigned to the MWG by the network. Byte order: high order byte (0xFF000000) expresses the first octet of the IP address.'},
              DNSIPAddressOfLastGPRSConnection     = {'ParamID' : 102, 'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'IP address of the DNS server provided when the network connection is established. Byte order: high order byte (0xFF000000) expresses the first octet of the IP address.'},
              GatewayIPAddressOfLastGPRSConnection = {'ParamID' : 103, 'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'IP address of the default gateway proovided by the network at connection. Byte order: high order byte (0xFF000000) expresses the first octet of the IP address.'},
              SatelliteModemPresent                = {'ParamID' : 104, 'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'Set to true if any response is received from the satellite modem.'},
              SatelliteRegisteredSignal            = {'ParamID' : 105, 'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'Any signal > 0 is taken as registered signal. Updated when we get a new signal strength notification from the modem.'},
              SatelliteSBDRegistered               = {'ParamID' : 106, 'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'Must be updated whenever modem status is monitored, including at key on, at intervals, at transmit session begin/end, etc. May use unsolicited notifications from modem.'},
              SatelliteMessageIOTime               = {'ParamID' : 107, 'DataType' : 'INT64',   'Default' : 0,          'Info' : r'**UTC Time in Seconds**Timestamp of last packet received or last transmit confirmation (i.e. modem indicates successful handoff to satellite of a sent packet) using satellite modem.'},
              NextCellCallTime                     = {'ParamID' : 108, 'DataType' : 'INT64',   'Default' : 0,          'Info' : r'**UTC Time in Seconds**Updated when a next call time is calculated.'},
              NextSatCallTime                      = {'ParamID' : 109, 'DataType' : 'INT64',   'Default' : 0,          'Info' : r'**UTC Time in Seconds**Updated when a next call time is calculated.'},
              GSMAntennaType                       = {'ParamID' : 110, 'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=Unknown, 1=US, 2=EU, 3=Short circuit, 4=Open circuit**'},
              LastGCLConfigUpdateTimestamp         = {'ParamID' : 112, 'DataType' : 'INT64',   'Default' : 0,          'Info' : r'**UTC Time in Seconds**Last from-host timestamp of an accepted Movement or Boundary or Engine Start alert setup.'},
              MWGHardwarePartNumber                = {'ParamID' : 113, 'DataType' : 'STRING',  'Default' : '',         'Info' : r''},
              TPPPacketCount                       = {'ParamID' : 115, 'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'A count of TPP packets successfully sent or received over any channel.'},
              CAN4HVoltage                         = {'ParamID' : 116, 'DataType' : 'UINT16',  'Default' : 0,          'Info' : r'**Hundredths of a Volt**Read at some convenient interval between 1 and 30 sec.'},
              CAN4LVoltage                         = {'ParamID' : 117, 'DataType' : 'UINT16',  'Default' : 0,          'Info' : r'**Hundredths of a Volt**Read at some convenient interval between 1 and 30 sec.'},
              EngineRunFromCAN                     = {'ParamID' : 118, 'DataType' : 'BOOLEAN', 'Default' : False,      'Info' : r'Set to true on receiving CAN EngineRPM messages first time after each boot.'},
              GSMOperator                          = {'ParamID' : 119, 'DataType' : 'STRING',  'Default' : '---',      'Info' : r'Written any time an operator notification is received from the modem.'},
              GSM_RSSILastKnown                    = {'ParamID' : 120, 'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'Written any time an RSSI notification is received from the modem.'},
              RAMDiskRestartCounter                = {'ParamID' : 121, 'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Incremented any time a shutdown is requested by Diagnostics App due to lack of space on RAMDisk root.'},
              WiFiSentKBytesLTD                    = {'ParamID' : 122, 'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes sent over WiFi Network.'},
              WiFiReceivedKBytesLTD                = {'ParamID' : 123, 'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes received over WiFi Network.'},
              WiFiSentPacketsLTD                   = {'ParamID' : 124, 'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets sent over WiFi Network.'},
              WiFiReceivedPacketsLTD               = {'ParamID' : 125, 'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets received over WiFi Network.'},
              WiFiFailedPacketsLTD                 = {'ParamID' : 126, 'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date packets failed over WiFi Network.'},
              WiFiFailedKBytesLTD                  = {'ParamID' : 127, 'DataType' : 'UINT32',  'Default' : 0,          'Info' : r'Terminal life-to-date Kbytes failed over WiFi Network.'},
              CellularTechnology                   = {'ParamID' : 128, 'DataType' : 'UINT8',   'Default' : 0,          'Info' : r'**0=Not registered, 1=2G GPRS, 2=2G EDGE, 3=3G WCDMA, 4=3G HSDPA, 5=3G HSUPA, 6=3G HSDPA/HSUPA**This value represents the cellular service availability at the current location.'},
             )

unsortedconfigDB['Ethernet'] = \
         dict(EthernetHostAddr                     = {'ParamID' : 1,  'DataType' : 'STRING', 'Default' : '204.54.18.130', 'Info' : r'Host FQDN or IP address to which TPP packets are sent.'},
              EthernetHostPort                     = {'ParamID' : 2,  'DataType' : 'UINT16', 'Default' : 48999,           'Info' : r'UDP port to which TPP packets are sent.'},
              EthernetUDPPort                      = {'ParamID' : 3,  'DataType' : 'UINT16', 'Default' : 48999,           'Info' : r'Local UDP port on which MWG listens for TPP packets.'},
              EthernetMaxPacketSize                = {'ParamID' : 4,  'DataType' : 'UINT16', 'Default' : 1024,            'Info' : r'**Bytes**Max TPP packet size to send.'},
              EthernetWindowSize                   = {'ParamID' : 5,  'DataType' : 'UINT16', 'Default' : 10,              'Info' : r'The TPP Window allows a new packet to be sent when (number of unacked packets < window size) AND (PacketID distance from oldest unacked packet to next packet < 120).'},
              EthernetPacketTimeoutTime            = {'ParamID' : 7,  'DataType' : 'UINT32', 'Default' : 15000,           'Info' : r'**Milliseconds**Number of milliseconds after sending a TPP packet to wait for a TPP Packet Ack before considering the packet to have timed out.'},
              EthernetMaxConsecutivePacketTimeouts = {'ParamID' : 8,  'DataType' : 'UINT32', 'Default' : 30,              'Info' : r'The number of consecutive TPP packet timeouts that trigger TPP to give up on the communication session with the host.'},
              EthernetPacketAckCoalesceWaitTime    = {'ParamID' : 9,  'DataType' : 'UINT32', 'Default' : 1000,            'Info' : r'**Milliseconds**The maximum time in milliseconds to wait after receiving a TPP packet before triggering the sending of a TPP packet that can contain the packet ack(s).'},
              EthernetTMAckCoalesceWaitTime        = {'ParamID' : 10, 'DataType' : 'UINT32', 'Default' : 5000,            'Info' : r'**Milliseconds**The maximum time in milliseconds to wait after a received TM becomes acknowledgable before triggering the sending of a TPP packet that can contain the TM ack(s).'},
              EthernetReassemblyTimeout            = {'ParamID' : 11, 'DataType' : 'UINT32', 'Default' : 150000,          'Info' : r'**Milliseconds**The maximum time in milliseconds to retain received fragments for any single partially received TM in the expectation that the remaining fragments could still be received.'},
              EthernetMinimumFragmentSize          = {'ParamID' : 12, 'DataType' : 'UINT16', 'Default' : 128,             'Info' : r'**Bytes**The size of the smallest TM fragment that TPP is allowed to encode.'},
             )

unsortedconfigDB['GSM'] = \
         dict(GSMHostAddr                     = {'ParamID' : 1,  'DataType' : 'STRING',  'Default' : 'jdlinkcs.deere.com',   'Info' : r'Host FQDN or IP address to which TPP packets are sent.'},
              GSMHostPort                     = {'ParamID' : 2,  'DataType' : 'UINT16',  'Default' : 49000,                  'Info' : r'UDP port to which TPP packets are sent.'},
              GSMUDPPort                      = {'ParamID' : 3,  'DataType' : 'UINT16',  'Default' : 49000,                  'Info' : r'Local UDP port on which MWG listens for TPP packets.'},
              GSMMaxPacketSize                = {'ParamID' : 4,  'DataType' : 'UINT16',  'Default' : 1024,                   'Info' : r'**Bytes**Max TPP packet size to send.'},
              GSMWindowSize                   = {'ParamID' : 5,  'DataType' : 'UINT16',  'Default' : 15,                     'Info' : r'The TPP Window allows a new packet to be sent when (number of unacked packets < window size) AND (PacketID distance from oldest unacked packet to next packet < 120).'},
              GSMCallKeepAlive                = {'ParamID' : 6,  'DataType' : 'UINT32',  'Default' : 60,                     'Info' : r'**Seconds**Number of seconds of idle time during which to keep the GSM/GPRS data session open.'},
              GSMPacketTimeoutTime            = {'ParamID' : 7,  'DataType' : 'UINT32',  'Default' : 40000,                  'Info' : r'**Milliseconds**Number of milliseconds after sending a TPP packet to wait for a TPP Packet Ack before considering the packet to have timed out.'},
              GSMMaxConsecutivePacketTimeouts = {'ParamID' : 8,  'DataType' : 'UINT32',  'Default' : 16,                     'Info' : r'The number of consecutive TPP packet timeouts that trigger TPP to give up on the communication session with the host.'},
              GSMPacketAckCoalesceWaitTime    = {'ParamID' : 9,  'DataType' : 'UINT32',  'Default' : 2000,                   'Info' : r'**Milliseconds**The maximum time in milliseconds to wait after receiving a TPP packet before triggering the sending of a TPP packet that can contain the packet ack(s).'},
              GSMTMAckCoalesceWaitTime        = {'ParamID' : 10, 'DataType' : 'UINT32',  'Default' : 5000,                   'Info' : r'**Milliseconds**The maximum time in milliseconds to wait after a received TM becomes acknowledgable before triggering the sending of a TPP packet that can contain the TM ack(s).'},
              GSMReassemblyTimeout            = {'ParamID' : 11, 'DataType' : 'UINT32',  'Default' : 7200000,                'Info' : r'**Milliseconds**The maximum time in milliseconds to retain received fragments for any single partially received TM in the expectation that the remaining fragments could still be received.'},
              GSMMinimumFragmentSize          = {'ParamID' : 12, 'DataType' : 'UINT16',  'Default' : 128,                    'Info' : r'**Bytes**The size of the smallest TM fragment that TPP is allowed to encode.'},
              GSMAPN                          = {'ParamID' : 13, 'DataType' : 'STRING',  'Default' : '\"jdlink.deere.com\"', 'Info' : r'APN string for making GSM/GPRS connections. Must be a string including leading and trailing " characters.'},
              GSMModemBandSelection           = {'ParamID' : 15, 'DataType' : 'UINT8',   'Default' : 7,                      'Info' : r'**0=850 MHz mono-band, 1=900 MHz mono-band, 2=1800 MHz mono-band, 3=1900 MHz mono-band, 4=850/1900 MHz dual-band, 5=900/1800 MHz dual-band, 6=900/1900 MHz dual-band, 7=850/900/1800/1900 MHz quad-band**Frequency band to be used by the GSM modem.'},
              GSMUsername                     = {'ParamID' : 16, 'DataType' : 'STRING',  'Default' : '',                     'Info' : r'Username to be used for RasDial (PPP) authentication with the carrier.'},
              GSMPassword                     = {'ParamID' : 17, 'DataType' : 'STRING',  'Default' : '',                     'Info' : r'Password to be used for RasDial (PPP) authentication with the carrier.'},
              GSMCarrierBan                   = {'ParamID' : 18, 'DataType' : 'STRING',  'Default' : '',                     'Info' : r'String that identifies a single GSM carrier that should be placed on the SIM\'s \'forbidden PLNM\' list so that the GSM Modem won\'t attempt to establish connection with the specified carrier. Only a single banned carrier is supported at a time by the terminal (note: a SIM may support 4 or more forbidden PLNMs).'},
              GSMSessionIdleTime              = {'ParamID' : 19, 'DataType' : 'UINT32',  'Default' : 120,                    'Info' : r'**Seconds**While a GSM call is open, this is the amount of time (in seconds) to wait after the last TPP packet was sent or received before starting a new TPP session.'},
              GSMModemNumberSoftResets        = {'ParamID' : 20, 'DataType' : 'UINT32',  'Default' : 0,                      'Info' : r'The number of soft resets on the GSM modem.  This value is cumulative.'},
              GSMModemNumberHardResets        = {'ParamID' : 21, 'DataType' : 'UINT32',  'Default' : 0,                      'Info' : r'The number of hard resets on the GSM modem.  This value is cumulative.'},
              GSMModemRATSelection            = {'ParamID' : 22, 'DataType' : 'UINT8',   'Default' : 0,                      'Info' : r'**0=Dual mode 3G preferred, 1=Dual mode GSM preferred, 2=Single mode 3G, 3=Single mode GSM**Selection of the Radio Access Technology. This value is only used for the u-blox quad-band modem (ignored by the Sierra Wireless modem).'},
              GSMExternalSIMAPN               = {'ParamID' : 23, 'DataType' : 'STRING',  'Default' : '',                     'Info' : r'APN string for making GSM/GPRS connections with external SIM. Must be a string including leading and trailing " characters.'},
              GSMExternalSIMUsername          = {'ParamID' : 24, 'DataType' : 'STRING',  'Default' : '',                     'Info' : r'Username to be used for RasDial (PPP) authentication with the carrier when using external SIM.'},
              GSMExternalSIMPassword          = {'ParamID' : 25, 'DataType' : 'STRING',  'Default' : '',                     'Info' : r'Password to be used for RasDial (PPP) authentication with the carrier when using external SIM.'},
              GSMUseExternalSIM               = {'ParamID' : 26, 'DataType' : 'BOOLEAN', 'Default' : False,                  'Info' : r'If TRUE, Comm Services will attempt to use the external SIM versions for APN, Username, and Password. If FALSE, Comm Services will use the internal SIM versions.'},
              GSMExternalSIMHostPort          = {'ParamID' : 27, 'DataType' : 'UINT16',  'Default' : 49030,                  'Info' : r'The Port for the external SIM host.'},
              GSMSimulateModem                = {'ParamID' : 28, 'DataType' : 'BOOLEAN', 'Default' : False,                  'Info' : r'If TRUE, Comm Services will use the simulated modem Socket connection. If FALSE, Comm Services will use the real modem serial connection.'},
              GSMOverrideCountryCode          = {'ParamID' : 29, 'DataType' : 'BOOLEAN', 'Default' : False,                  'Info' : r'If TRUE, Comm Services will use the country code from the modem. If FALSE, the country code from the modem will be discarded for the current value in the DB.'},
              GSMAllowRegistration            = {'ParamID' : 30, 'DataType' : 'BOOLEAN', 'Default' : True,                   'Info' : r'If FALSE, Comm Services will prevent modem from registering with network. If TRUE, registration will be attempted.'},
             )

unsortedconfigDB['GSMNetworkSimulator'] = \
         dict(GSMNetworkSimEnable          = {'ParamID' : 1, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'Enable/Disable Simulated GSM'},
              RASDialFailurePercent        = {'ParamID' : 2, 'DataType' : 'UINT16',  'Default' : 0,     'Info' : r'**Percent**'},
              RASDialFailureSeconds        = {'ParamID' : 3, 'DataType' : 'UINT16',  'Default' : 0,     'Info' : r'**Seconds**'},
              RingAlertOccurPercent        = {'ParamID' : 4, 'DataType' : 'UINT16',  'Default' : 0,     'Info' : r'**Percent**'},
              RingAlertIntervalSeconds     = {'ParamID' : 5, 'DataType' : 'UINT16',  'Default' : 30,    'Info' : r'**Seconds**'},
              SignalStrengthFailurePercent = {'ParamID' : 6, 'DataType' : 'UINT16',  'Default' : 0,     'Info' : r'**Percent**'},
              SignalStrengthFailureSeconds = {'ParamID' : 7, 'DataType' : 'UINT16',  'Default' : 30,    'Info' : r'**Seconds**'},
              RSSIMean                     = {'ParamID' : 8, 'DataType' : 'UINT16',  'Default' : 15,    'Info' : r''},
              RSSIStandardDeviation        = {'ParamID' : 9, 'DataType' : 'UINT16',  'Default' : 5,     'Info' : r''},
             )

unsortedconfigDB['GCL'] = \
         dict(GCLWakeupIntervalMinutes = {'ParamID' : 1, 'DataType' : 'UINT16', 'Default' : 60, 'Info' : r'**Minutes**'},
             )

unsortedconfigDB['GpsManager'] = \
         dict(GPSMinimumFirmwareLevel = {'ParamID' : 1, 'DataType' : 'STRING',  'Default' : '',    'Info' : r'If this is non blank, then the firmware version of the GPS firmware is compared against this to determine whether the firmware in the GPS is too old.'},
              GPSSimulatorTCPSource   = {'ParamID' : 2, 'DataType' : 'STRING',  'Default' : '',    'Info' : r'If GPSSource is 1 during startup, GPS Manager will attempt to connect to a GPS Simulator using TCP/IP at the provided IP Address and Port (expected to be available over Ethernet). IP address and port of the GPS simulator, in the form: n.n.n.n:p.'},
              GPSSource               = {'ParamID' : 3, 'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'**0=internal I2C interface, 1=external TCP/IP source, 2=external COM port**Identifies the source port for GPS data.'},
              PublishOnVehicleBus     = {'ParamID' : 4, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'Determines if the MTG will publish GPS data on the vehicle CAN bus.'},
              PublishOnImplementBus   = {'ParamID' : 5, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'Determines if the MTG will publish GPS data on the implement CAN bus.'},
             )

unsortedconfigDB['HourMeter'] = \
         dict(EngineHoursIsAvailableOnCAN   = {'ParamID' : 1, 'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'**0=Unknown, 1=Yes, 2=No**Set by datalogger if the config has an Engine.Hours binary conversion.'},
              UserInputEngHoursInHundredths = {'ParamID' : 2, 'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'**Hundredths of Hour**Set by host via ConfigApp upon user input of new engine hours.'},
              HoursBeingCounted             = {'ParamID' : 3, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'When engine hour info is received from the datalogger, or the internal hour meter increases, remember the timestamp and set this parameter to true.'},
              LastEngineHoursInHundredths   = {'ParamID' : 4, 'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'Set by hour meter / service tool.'},
             )

unsortedconfigDB['Iridium'] = \
         dict(IridiumMaxPacketSize                = {'ParamID' : 4,  'DataType' : 'UINT16', 'Default' : 340,       'Info' : r'**Bytes**Max TPP packet size to send.'},
              IridiumWindowSize                   = {'ParamID' : 5,  'DataType' : 'UINT16', 'Default' : 100,       'Info' : r'The TPP Window allows a new packet to be sent when (number of unacked packets < window size) AND (PacketID distance from oldest unacked packet to next packet < 120).'},
              IridiumPacketTimeoutTime            = {'ParamID' : 7,  'DataType' : 'UINT32', 'Default' : 1200000,   'Info' : r'**Milliseconds**Number of milliseconds after sending a TPP packet to wait for a TPP Packet Ack before considering the packet to have timed out.'},
              IridiumMaxConsecutivePacketTimeouts = {'ParamID' : 8,  'DataType' : 'UINT32', 'Default' : 5,         'Info' : r'The number of consecutive TPP packet timeouts that trigger TPP to give up on the communication session with the host.'},
              IridiumPacketAckCoalesceWaitTime    = {'ParamID' : 9,  'DataType' : 'UINT32', 'Default' : 300000,    'Info' : r'**Milliseconds**The maximum time in milliseconds to wait after receiving a TPP packet before triggering the sending of a TPP packet that can contain the packet ack(s).'},
              IridiumTMAckCoalesceWaitTime        = {'ParamID' : 10, 'DataType' : 'UINT32', 'Default' : 300000,    'Info' : r'**Milliseconds**The maximum time in milliseconds to wait after a received TM becomes acknowledgable before triggering the sending of a TPP packet that can contain the TM ack(s).'},
              IridiumReassemblyTimeout            = {'ParamID' : 11, 'DataType' : 'UINT32', 'Default' : 435600000, 'Info' : r'**Milliseconds**The maximum time in milliseconds to retain received fragments for any single partially received TM in the expectation that the remaining fragments could still be received.'},
              IridiumMinimumFragmentSize          = {'ParamID' : 12, 'DataType' : 'UINT16', 'Default' : 128,       'Info' : r'**Bytes**The size of the smallest TM fragment that TPP is allowed to encode.'},
             )

unsortedconfigDB['PlatformCANServiceApp'] = \
         dict(OriginalVehiclePIN                    = {'ParamID' : 1, 'DataType' : 'STRING',  'Default' : '',    'Info' : r'The End of line tool at some factories will write this string via OBD. Later, the MWG will need to return the value using OBD when requested.'},
              CommandedAddressBus0                  = {'ParamID' : 2, 'DataType' : 'UINT8',   'Default' : 254,   'Info' : r'This value is written when a Commanded Address CAN message is received with a NAME matching that of the MTG on the vehicle bus.'},
              CommandedAddressBus1                  = {'ParamID' : 3, 'DataType' : 'UINT8',   'Default' : 254,   'Info' : r'This value is written when a Commanded Address CAN message is received with a NAME matching that of the MTG on the implement bus.'},
              DisableAutomaticMachineIdentification = {'ParamID' : 4, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'If set to true, the power-on identification of machine based on VIN, ESN will not take place.'},
              StartInhibit                          = {'ParamID' : 5, 'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'**0=No Inhibit, 1=Inhibit Level 1, 2=Inhibit Level 2**Set from the host to non-zero if the host wants to inhibit start of the machine according to the values listed. The startInhibit task will set a pattern in a regularly transmitted CAN message, based on the value of this parameter.'},
              ForceShutdown                         = {'ParamID' : 6, 'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'When set to true the PlatformCANService does an immediate shutdown of the MTG.'},
              ReportNetworkVandalism                = {'ParamID' : 7, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'If true, the Network Antenna bits (SPN 520649) in CAN message Machine Control (PGN 0xFFF8 Command Byte 0x54) will report Not Working Properly regardless of antenna or SIM status.'},
             )

unsortedconfigDB['PowerManagement'] = \
         dict(LastKeyOffTime                       = {'ParamID' : 1,  'DataType' : 'INT64',  'Default' : 0,     'Info' : r'**UTC Time in Seconds**'},
              HibernateAfterKeyOffPeriod           = {'ParamID' : 2,  'DataType' : 'UINT32', 'Default' : 0,     'Info' : r'**Seconds**Duration from the time of key off to when the MWG will attempt to hibernate (lowest power mode).'},
              StayAwakeAfterKeyOffPeriod           = {'ParamID' : 3,  'DataType' : 'UINT32', 'Default' : 10800, 'Info' : r'**Seconds**(Deprecated)Duration from the time of key off to when the MWG will attempt to sleep, assuming applications / services on the device have completed their own processing.'},
              LowVoltageHibernationThreshold       = {'ParamID' : 4,  'DataType' : 'UINT16', 'Default' : 0,     'Info' : r'**1/100ths of Volts**When the MWG senses an input voltage lower than this value for LowVoltageDuration, the MWG will attempt to hibernate if key is off.'},
              LowVoltageDuration                   = {'ParamID' : 5,  'DataType' : 'UINT16', 'Default' : 60,    'Info' : r'**Seconds**Low Voltage Duration range for both 12 and 24 volt systems should be between 1 and 999 seconds.'},
              SleepReadinessPollBailout            = {'ParamID' : 6,  'DataType' : 'UINT32', 'Default' : 15300, 'Info' : r'**Seconds**Max time to allow applications to push off transition to sleep.'},
              LongRunningOpLowVoltageThreshold_12V = {'ParamID' : 7,  'DataType' : 'UINT32', 'Default' : 1150,  'Info' : r'**1/100ths of Volts**The voltage below which long running operations such as controller reprogramming should not be started.'},
              LongRunningOpLowVoltageThreshold_24V = {'ParamID' : 8,  'DataType' : 'UINT32', 'Default' : 2150,  'Info' : r'**1/100ths of Volts**The voltage below which long running operations such as controller reprogramming should not be started.'},
              InferredVoltageSystem                = {'ParamID' : 9,  'DataType' : 'UINT8',  'Default' : 0,     'Info' : r'**0=Unknown, 12=12V system, 24=24V system**'},
              KeyState                             = {'ParamID' : 10, 'DataType' : 'UINT8',  'Default' : 0,     'Info' : r'**0=unknown, 1=off, 2=on**The state of the ignition, as broadcast to applications via IVS messaging.'},
              EngineState                          = {'ParamID' : 11, 'DataType' : 'UINT8',  'Default' : 0,     'Info' : r'**0=unknown, 1=off, 2=on**EngineDetection from PlatformCANSvc or analog voltage.'},
              RawKeyState                          = {'ParamID' : 12, 'DataType' : 'UINT8',  'Default' : 0,     'Info' : r'**0=unknown, 1=off, 2=on**The current state of the ignition as read from the BSP (no power manager hysteresis applied).'},
              StayAwakeAfterKeyOffPeriod2          = {'ParamID' : 13, 'DataType' : 'UINT32', 'Default' : 10800, 'Info' : r'**Seconds**Duration from the time of key off to when the MWG will attempt to sleep, assuming applications / services on the device have completed their own processing.'},
             )

unsortedconfigDB['QualcommLegacy'] = \
         dict(ServiceLevel       = {'ParamID' : 1, 'DataType' : 'UINT8',  'Default' : 1,  'Info' : r'**1=Select, 2=Advanced, 3=Ultimate**'},
              EngineSerialNumber = {'ParamID' : 2, 'DataType' : 'STRING', 'Default' : '', 'Info' : r'20 Chars Max'},
             )

unsortedconfigDB['Registration'] = \
         dict(MachineID                         = {'ParamID' : 1,   'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'The machine ID as assigned by the host during the registration process.'},
              TerminalSerialNumber              = {'ParamID' : 2,   'DataType' : 'STRING',  'Default' : '',    'Info' : r'The serial number of the terminal.'},
              RegistrationState                 = {'ParamID' : 9,   'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'**0=Unknown, 1=Unregistered, 2=Pending, 3=Registered**'},
              PIN                               = {'ParamID' : 10,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The PIN (VIN) obtained from the CAN bus.'},
              ESN                               = {'ParamID' : 11,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The engine serial number obtained from the CAN bus.'},
              CANDetectionComplete              = {'ParamID' : 19,  'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'If set to true, the PlatformCANService/MachineIdentifier has determined that VIN and ESN interrogation is complete and the VIN and ESN have been written to the config params.'},
              CommandedPIN                      = {'ParamID' : 20,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The PIN (VIN) as set by an external service tool.'},
              CommandedESN                      = {'ParamID' : 21,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The ESN as set by an external service tool.'},
              CommandedMachineName              = {'ParamID' : 22,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'**Unicode**The machine name as set by an external service tool.'},
              CommandedVoltageSystem            = {'ParamID' : 23,  'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'The voltage system (12V or 24V) as set by an external service tool.'},
              CommandedChangesComplete          = {'ParamID' : 29,  'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'**0=Nothing ever entered, 1=Values entered, 2=Registration in progress, 3=Registration complete**Set to 1 by the service tool after the other commanded parameters have been set to the values as specified by the service technician.'},
              ReportedPIN                       = {'ParamID' : 40,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The PIN sent by the host to acknowledge the PIN value obtained by the CAN bus and sent by the mobile.'},
              ReportedESN                       = {'ParamID' : 41,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The ESN sent by the host to acknowledge the ESN value obtained by the CAN bus and sent by the mobile.'},
              ValidatedPIN                      = {'ParamID' : 50,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The PIN (VIN) as determined by the host.'},
              RegisteredESN                     = {'ParamID' : 51,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The ESN as determined by the host.'},
              RegisteredMachineName             = {'ParamID' : 52,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'**Unicode**The machine name as determined by the host.'},
              RegisteredVoltageSystem           = {'ParamID' : 53,  'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'The voltage system as determined by the host.'},
              RegisteredMake                    = {'ParamID' : 54,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'**Unicode**The machine make as determined by the host.'},
              RegisteredModel                   = {'ParamID' : 55,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'**Unicode**The machine model as determined by the host.'},
              RegisteredType                    = {'ParamID' : 56,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'**Unicode**The machine type as determined by the host.'},
              GSM_IMEI                          = {'ParamID' : 70,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The IMEI acquired from the GSM modem.'},
              GSM_IMSI                          = {'ParamID' : 71,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The IMSI acquired from the GSM modem.'},
              GSM_MDN                           = {'ParamID' : 72,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The MDN acquired from the GSM modem.'},
              GSM_ICCID                         = {'ParamID' : 73,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The ICCID acquired from the GSM modem.'},
              RegisteredGSM_IMEI                = {'ParamID' : 80,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The GSM IMEI as echoed by the host.'},
              RegisteredGSM_IMSI                = {'ParamID' : 81,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The GSM IMSI as echoed by the host.'},
              RegisteredGSM_MDN                 = {'ParamID' : 82,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The GSM MDN as echoed by the host.'},
              RegisteredGSM_ICCID               = {'ParamID' : 83,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The GSM ICCID as echoed by the host.'},
              IridiumIMEI                       = {'ParamID' : 90,  'DataType' : 'STRING',  'Default' : '',    'Info' : r'The IMEI acquired from the Iridium modem.'},
              RegisteredIridium_IMEI            = {'ParamID' : 100, 'DataType' : 'STRING',  'Default' : '',    'Info' : r'The Iridium IMEI as echoed by the host.'},
              MachineRegistrationBlockTimestamp = {'ParamID' : 101, 'DataType' : 'INT64',   'Default' : 0,     'Info' : r'Timestamp of receipt of the machine registration block.'},
              RegistrationResultCode            = {'ParamID' : 102, 'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'Last registration code received from host.'},
              BestLicenseTypeAvailable          = {'ParamID' : 103, 'DataType' : 'STRING',  'Default' : '',    'Info' : r'Must be 31 chars or less'},
              LicenseTypePurchased              = {'ParamID' : 104, 'DataType' : 'STRING',  'Default' : '',    'Info' : r'Must be 31 chars or less'},
              ClearRegistration                 = {'ParamID' : 105, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'When set by OBD, it will clear registration information that had been received from the host.'},
              COS_Status                        = {'ParamID' : 110, 'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'**0=Internal SIM Card Required, 1=Registration Successful, 2=Registration Pending, 3=Setup Unsuccessful**'},
              MobileCountryCode                 = {'ParamID' : 111, 'DataType' : 'UINT16',  'Default' : 310,   'Info' : r'A 3 digit code indicating the country of operation for the device.'},
              COS_StatusConfirmed               = {'ParamID' : 112, 'DataType' : 'BOOLEAN', 'Default' : True,  'Info' : r'Set to FALSE when COS_Status or mobilecountry code changes. Set to TRUE when the device receives a COS status response from the host confirming the current COS_status'},
              COS_Commanded                     = {'ParamID' : 113, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r'If TRUE, the device has been commanded to attempt to use external SIM information. If FALSE, the device should use the internal SIM.'},
              GSM_ExternalSIM_MDN               = {'ParamID' : 114, 'DataType' : 'STRING',  'Default' : '',    'Info' : r'The MDN of the external SIM, used for COS. Needed so the host can send SMS to the device.'},
              COS_ErrorCode                     = {'ParamID' : 115, 'DataType' : 'UINT8',   'Default' : 0,     'Info' : r'**0=Success, 1=COS_ConfigMissingOrInvalid, 2=APN_Invalid, 3=MaxCallFailures, 4=SIM_Absent, 5=SIM_NotActivated, 6=SIM_Error, 7=SIM_PinRequired, 8=SIM_PukRequired, 9=SIM_Pin2Required, 10=SIM_Puk2Required, 11=PH_SIM_PinRequired, 12=SIM_IncorrectPassword**'},
             )

unsortedconfigDB['Reprogramming'] = \
         dict(SoftwareVersionMajor            = {'ParamID' : 1, 'DataType' : 'UINT16', 'Default' : 0,  'Info' : r'Set by Reprogramming app to the currently-running software version during startup.'},
              SoftwareVersionMinor            = {'ParamID' : 2, 'DataType' : 'UINT16', 'Default' : 0,  'Info' : r'Set by Reprogramming app to the currently-running software version during startup.'},
              BuildNumber                     = {'ParamID' : 3, 'DataType' : 'UINT32', 'Default' : 0,  'Info' : r'Set by Reprogramming app to the currently-running software version during startup.'},
              BuildDateTime                   = {'ParamID' : 4, 'DataType' : 'INT64',  'Default' : 0,  'Info' : r'**UTC Time in Seconds**Set by Reprogramming app to the currently-running software version during startup.'},
              LastReprogrammingState          = {'ParamID' : 5, 'DataType' : 'UINT8',  'Default' : 0,  'Info' : r'**0=Unknown, 1=ReprogrammingSuccessful, 2=PayloadTransferStarted, 3=PayloadProcessingStarted, 4=CorruptedPayload, 5=PayloadAuthenticationFailure, 6=WrongPayloadForDevice, 7=WrongPayloadForCurrentState, 8=PayloadExtractedRebootInitiated, 9=UnexpectedPayloadProcessingError**'},
              LastReprogrammingStateTimestamp = {'ParamID' : 6, 'DataType' : 'INT64',  'Default' : 0,  'Info' : r'**UTC Time in Seconds**Set by Reprogramming app to the currently-running software version during startup.'},
              ReprogrammingInfoString         = {'ParamID' : 7, 'DataType' : 'STRING', 'Default' : '', 'Info' : r'ASCII information about a reprogramming operaiton. Something that confirms to the user that if the reprogramming succeeded, the expectation is met. Can be blank.'},
             )

unsortedconfigDB['TaskDeliveryApp'] = \
         dict(WatchDogTimeout               = {'ParamID' : 1,  'DataType' : 'UINT32',  'Default' : 1800,            'Info' : r'**Seconds**The number of seconds to specify to watchdog when registering threads.'},
              MaximumRecordingSize          = {'ParamID' : 2,  'DataType' : 'UINT32',  'Default' : 1048000,         'Info' : r'**Bytes**The maximum size of a recording file, in bytes.'},
              ToolIdentity                  = {'ParamID' : 3,  'DataType' : 'STRING',  'Default' : '1F2F9A',        'Info' : r'The tool identity used by SAOnboard Diagnostics and Reprogramming.'},
              CalLogLevels                  = {'ParamID' : 4,  'DataType' : 'STRING',  'Default' : 'ERROR WARNING', 'Info' : r'The log levels that will be written to the CAL Logs..'},
              CalEcuAccessLevel             = {'ParamID' : 5,  'DataType' : 'UINT32',  'Default' : 1,               'Info' : r'The access level the CAL will request of the ECU on connection.'},
              CALEcuAccessLevelPassword     = {'ParamID' : 6,  'DataType' : 'STRING',  'Default' : '',              'Info' : r'The password to be used when requesting access to the ECU.'},
              CalSamplingRate               = {'ParamID' : 7,  'DataType' : 'UINT32',  'Default' : 250,             'Info' : r'**Milliseconds**The minimum period (in milliseconds) of time between data point updates (only for connections that support controlling this time)'},
              CalJDCommLoggingEnabled       = {'ParamID' : 8,  'DataType' : 'BOOLEAN', 'Default' : False,           'Info' : r'A flag indicating if JDComm logging is enabled for connections.'},
              PrimaryToolAddress            = {'ParamID' : 9,  'DataType' : 'UINT8',   'Default' : 0xF9,            'Info' : r'The tool address used by SAOnboard Diagnostics and Reprogramming.'},
              PrimaryToolFunctionInstance   = {'ParamID' : 10, 'DataType' : 'UINT16',  'Default' : 0,               'Info' : r'The tool function instance used by SAOnboard Diagnostics and Reprogramming.'},
              SecondaryToolAddress          = {'ParamID' : 11, 'DataType' : 'UINT8',   'Default' : 0xFA,            'Info' : r'The tool address used by SAOnboard Diagnostics for ECUs on CAN3 (the "PowerTrain Bus").'},
              SecondaryToolFunctionInstance = {'ParamID' : 12, 'DataType' : 'UINT16',  'Default' : 1,               'Info' : r'The function instance used by SAOnboard Diagnostics for ECUs on CAN3 (the "PowerTrain Bus").'},
              CalDtcUpdateTimer             = {'ParamID' : 13, 'DataType' : 'UINT32',  'Default' : 500,             'Info' : r'**Milliseconds**The period (in milliseconds) between DTC request timeout checks.'},
              CalDM1Timeout                 = {'ParamID' : 14, 'DataType' : 'UINT32',  'Default' : 3000,            'Info' : r'**Milliseconds**The number of milliseconds to wait for a broadcast DM1 message before requesting Active Codes.'},
              CalUniversalTimeout           = {'ParamID' : 15, 'DataType' : 'UINT32',  'Default' : 12000,           'Info' : r'**Milliseconds**The number of milliseconds to wait before a message is treated as timed out.'},
              CalEngineHourMultiplier       = {'ParamID' : 16, 'DataType' : 'UINT32',  'Default' : 50,              'Info' : r'The value by which the engine timestamp is multiplied to convert to milliseconds.'},
              CalIdmRecordingFrameLength    = {'ParamID' : 17, 'DataType' : 'UINT32',  'Default' : 1000,            'Info' : r'The default frame length used in a CAL recording for the IDM (not the IDM sampling rate).'},
              SuspendDelay                  = {'ParamID' : 18, 'DataType' : 'UINT32',  'Default' : 5000,            'Info' : r'**Milliseconds**The number of milliseconds to wait after an ignition off occurs to determine if processing should suspend.'},
              TMCommandVersion              = {'ParamID' : 19, 'DataType' : 'UINT32',  'Default' : 1,               'Info' : r'Current version of the SAOnboardCommand message.'},
              TMStatusVersion               = {'ParamID' : 20, 'DataType' : 'UINT32',  'Default' : 1,               'Info' : r'Current version of the SAOnboardStatus message.'},
              TMUploadDtcVersion            = {'ParamID' : 21, 'DataType' : 'UINT32',  'Default' : 1,               'Info' : r'Current version of the SAOnboardDTCUpload message.'},
              TMUploadRecordingVersion      = {'ParamID' : 22, 'DataType' : 'UINT32',  'Default' : 1,               'Info' : r'Current version of the SAOnboardRecordingUpload message.'},
              SARStatus                     = {'ParamID' : 36, 'DataType' : 'UINT32',  'Default' : 0,               'Info' : r'**0=no error, 1=CAL, 2=Reprogramming, 3=Power Manager, 4=Comm Services, 5=Watchdog, 6=Registration, 7=Platform CAN Service**Status of the SAOnboard Application.'},
             )

unsortedconfigDB['TimeManager'] = \
         dict(TZ_DaylightTimeStart  = {'ParamID' : 1,  'DataType' : 'INT64',   'Default' : 0,     'Info' : r'**UTC Time in Seconds**Date and time at which daylight time begins for the terminal.'},
              TZ_DaylightTimeEnd    = {'ParamID' : 2,  'DataType' : 'INT64',   'Default' : 0,     'Info' : r'**UTC Time in Seconds**Date and time at which daylight time ends for the terminal.'},
              TZ_DaylightOffsetMins = {'ParamID' : 3,  'DataType' : 'INT16',   'Default' : -300,  'Info' : r'**Minutes**Offset from UTC during daylight savings time.'},
              TZ_StandardOffsetMins = {'ParamID' : 4,  'DataType' : 'INT16',   'Default' : -360,  'Info' : r'**Minutes**Offset from UTC during standard time.'},
              LastTimeZoneOffset    = {'ParamID' : 5,  'DataType' : 'INT16',   'Default' : -360,  'Info' : r'**Minutes**Last known offset from UTC. Loaded at startup to speed up messaging in case of unknown time.'},
              LastMLT               = {'ParamID' : 6,  'DataType' : 'INT64',   'Default' : 0,     'Info' : r'**Tenths of a Second**MLT (from MIG Linear Time) runs when the processor is running. During registration, host will bring up MLT to the highest known value for the machine, if the MLT in the device is not already at a higher value.'},
              LastTLT               = {'ParamID' : 7,  'DataType' : 'INT64',   'Default' : 0,     'Info' : r'**Tenths of a Second**Terminal linear time. Runs when the processor is running. Continuously increases for the device.'},
              MLTTick               = {'ParamID' : 8,  'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'Tick count for the last MLT.'},
              TLTTick               = {'ParamID' : 9,  'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'Tick count for the last terminal linear time'},
              IsTimeValid           = {'ParamID' : 10, 'DataType' : 'BOOLEAN', 'Default' : False, 'Info' : r''},
              LastMLTInTenthsOfHour = {'ParamID' : 11, 'DataType' : 'UINT32',  'Default' : 0,     'Info' : r'Updated by time manager when LastMLT is updated by time manager in config store.'},
              LastKnownCorrection   = {'ParamID' : 12, 'DataType' : 'INT64',   'Default' : 0,     'Info' : r'When time correction is needed this value is set until the correction is applied.  This is not volatile since we may apply this correction at boot time in the case where updating the RTC failed before reboot.'},
             )

unsortedconfigDB['WiFiAdapter'] = \
         dict(WiFiHostAddr                     = {'ParamID' : 1,  'DataType' : 'STRING', 'Default' : '',             'Info' : r'Host FQDN or IP address to which TPP packets are sent.'},
              WiFiHostPort                     = {'ParamID' : 2,  'DataType' : 'UINT16', 'Default' : 0,              'Info' : r'UDP port to which TPP packets are sent.'},
              WiFiUDPPort                      = {'ParamID' : 3,  'DataType' : 'UINT16', 'Default' : 0,              'Info' : r'Local UDP port on which MWG listens for TPP packets.'},
              WiFiMaxPacketSize                = {'ParamID' : 4,  'DataType' : 'UINT16', 'Default' : 1024,           'Info' : r'**Bytes**Max TPP packet size to send.'},
              WiFiWindowSize                   = {'ParamID' : 5,  'DataType' : 'UINT16', 'Default' : 15,             'Info' : r'The TPP Window allows a new packet to be sent when (number of unacked packets < window size) AND (PacketID distance from oldest unacked packet to next packet < 120).'},
              WiFiPacketTimeoutTime            = {'ParamID' : 7,  'DataType' : 'UINT32', 'Default' : 40000,          'Info' : r'**Milliseconds**Number of milliseconds after sending a TPP packet to wait for a TPP Packet Ack before considering the packet to have timed out.'},
              WiFiMaxConsecutivePacketTimeouts = {'ParamID' : 8,  'DataType' : 'UINT32', 'Default' : 16,             'Info' : r'The number of consecutive TPP packet timeouts that trigger TPP to give up on the communication session with the host.'},
              WiFiPacketAckCoalesceWaitTime    = {'ParamID' : 9,  'DataType' : 'UINT32', 'Default' : 2000,           'Info' : r'**Milliseconds**The maximum time in milliseconds to wait after receiving a TPP packet before triggering the sending of a TPP packet that can contain the packet ack(s).'},
              WiFiTMAckCoalesceWaitTime        = {'ParamID' : 10, 'DataType' : 'UINT32', 'Default' : 5000,           'Info' : r'**Milliseconds**The maximum time in milliseconds to wait after a received TM becomes acknowledgable before triggering the sending of a TPP packet that can contain the TM ack(s).'},
              WiFiReassemblyTimeout            = {'ParamID' : 11, 'DataType' : 'UINT32', 'Default' : 7200000,        'Info' : r'**Milliseconds**The maximum time in milliseconds to retain received fragments for any single partially received TM in the expectation that the remaining fragments could still be received.'},
              WiFiMinimumFragmentSize          = {'ParamID' : 12, 'DataType' : 'UINT16', 'Default' : 128,            'Info' : r'**Bytes**The size of the smallest TM fragment that TPP is allowed to encode.'},
              WiFiGatewayAddr                  = {'ParamID' : 13, 'DataType' : 'STRING', 'Default' : '192.168.1.20', 'Info' : r'Used to specify the local address of the WiFi hardware that acts as a gateway to connect to WiFi hotspots.'},
              WiFiAccessPointSSID              = {'ParamID' : 14, 'DataType' : 'STRING', 'Default' : '',             'Info' : r'This is the SSID of the WiFi hotspot to connect to.'},
              WiFiAccessPointPassword          = {'ParamID' : 15, 'DataType' : 'STRING', 'Default' : '',             'Info' : r'This is the password of the WiFi hotspot to connect to.'},
             )

unsortedconfigDB['CANWANControl'] = \
         dict(EnableCANWANControl              = {'ParamID' : 1,  'DataType' : 'BOOLEAN', 'Default' : False,         'Info' : r' Upon being True (False), this parameter will enable (disable) the CANWAN service, so it could respond (ignore) the CAN message.'},
             )

configDB = OrderedDict()
for appName in appIDs:
   if appName in unsortedconfigDB:
      configDB[appName] = OrderedDict(sorted(unsortedconfigDB[appName].items(), key=lambda t: t[1]['ParamID']))

# MTG Regular Expressions

dbGet = r'GET:'
dbSet = r'SET:'
dbClear = r'CLEAR:'
dbDoesNotExist = r'.  No parameter type in the DB for'
dbReturnText = '(?P<type>(?:%s|%s|%s)|(?:%s)) +AppID=(?P<appID>\d+), ParamID=(?P<paramID>\d+)(?:,.+Value=(?P<value>.+))?' % (dbGet, dbSet, dbClear, dbDoesNotExist)
dbReturnTextCompiled = re.compile(dbReturnText)

mtgErrorMessages = ['criticalMessage', 'alertMessage', 'exception', 'queueFull']

mtgRegExpDict = dict(# Statuses
                     powerDownMessage  = 'POWER OFF',
                     powerOnMessage    = 'POWER ON',
                     startUpMessage    = 'Microsoft Windows CE Bootloader Common Library',
                     bootMenuDisplayed = 'Boot Loader Configuration:',
                     bootMenuFinished  = 'Reading NK image from NAND',
                     wceStartUpMessage = 'Launcher: Object Store size = \d+ bytes\, \d+ bytes free\.',
                     firmwareVersion   = '^(\\\\.*> )?(?P<version>\d+\.\d+\.\d+)\W*$',
                     cpuUsage          = 'CheckSystemLimitCPU.+CPU used=(?P<used>\d+) percent,.+Threshold=(?P<threshold>\d+)',
                     ramUsage          = 'CheckSystemLimitRAM.+RAM=(?P<used>\d+), Threshold=(?P<threshold>\d+)',
                     ethernetLink      = 'HandleCheckEthernetLink.+EthernetLink is (?P<value>\w+)',
                     cellStrength      = 'GSM Modem RSSI: -(?P<value>.+) dBm',
                     reprogramStarting = 'ReprogramApplication::CheckForUpdateFile.*Found update file',
                     reprogramFailed   = 'ReprogramApplication::DecryptTheFiles.*failed',
                     reprogramComplete = 'ReprogramApplication::DispatchAppstartMessage.*Waiting for update file',
                     dateTime          = '\^\^(?P<year>\d{4}):(?P<month>\d{2}):(?P<day>\d{2})\-(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}):(?P<secondf>\d{3}).+\^\^',
                     # Errors/Warnings
                     criticalMessage   = '~\+4~\+', # OpEvent_CriticalEvent
                     alertMessage      = '~\+6~\+', # immediate action required
                     exception         = 'Exception \'.+\'',
                     queueFull         = 'Message Queue .* Full',
                    )

regExpCompiledDict = {}
for i in mtgRegExpDict:
   regExpCompiledDict[i] = re.compile(mtgRegExpDict[i])

reprogramItemRegExCompiled = re.compile('(?P<text>(?:ReprogramApplication::.*)|(?:UncompressUsingAlone::.*)|(?:InstallApp::.*))\^\^\,\.\,')

# MTG Commands

cdTestFrameworkDict = dict(TriggerTM              = {'Command' : r'TriggerTM',              'InPlatform' : True, 'Info' : r'Send a dummy TM to the connected devices(s)'},
                           TriggerTMWithFile      = {'Command' : r'TriggerTMWithFile',      'InPlatform' : True, 'Info' : r'Send a dummy TM with file attachment to the connected device(s)'},
                           TriggerTMWithSetupFile = {'Command' : r'TriggerTMWithSetupFile', 'InPlatform' : True, 'Info' : r'Send a setup file using WDT (Setup.zip must exist in the NAND Flash directory)'},
                           TriggerTMOnCDInfoRecv  = {'Command' : r'TriggerTMOnCDInfoRecv',  'InPlatform' : True, 'Info' : r'Send a dummy TM to the connected device(s), when CDInfo received'},
                           TriggerRDA             = {'Command' : r'-rda',                   'InPlatform' : True, 'Info' : r'Send an RDA session request (Serial Number is optional)'},
                           TriggerLA              = {'Command' : r'-la',                    'InPlatform' : True, 'Info' : r'Send a License Activation TM to the connected device(s) (Serial Number and Activation Code are optional'},
                           CancelTM               = {'Command' : r'CancelTM',               'InPlatform' : True, 'Info' : r'Helps to Initiate a CANCEL TM request from CD'},
                           OfpEnableWdt           = {'Command' : r'OfpEnableWdt',           'InPlatform' : True, 'Info' : r'Send a Configuration(OFP WDT Status) TM to the connected device(s)'},
                           OfpDisableWdt          = {'Command' : r'OfpDisableWdt',          'InPlatform' : True, 'Info' : r'Send a Configuration(OFP WDT Status) TM to the connected device(s)'},
                           CGCenable              = {'Command' : r'CGC-enable',             'InPlatform' : True, 'Info' : r'Send CGC enable message to the connected device(s)'},
                           CGCdisable             = {'Command' : r'CGC-disable',            'InPlatform' : True, 'Info' : r'Send CGC disable message to the connected device(s)'},
                          )

miscCommandsDict = dict(getFirmwareVersion = {'Command' : r'type \"NAND Flash"\Version.txt', 'InPlatform' : False, 'Info' : r'Retrieves the current firmware version of the MTG'},
                        rollLatestLog      = {'Command' : r'logger -r',                      'InPlatform' : True,  'Info' : r'Closes the current log and creates a new one'},
                       )

mtgCommandsDict = OrderedDict()

for i in configDB:
   key = 'ConfigDB  ' + str(appIDs[i]) + '  '
   if appIDs[i] < 100:
      key = key + '  '
   key = key + i
   mtgCommandsDict[key] = { 'exeName' : r'', 'Dict' : configDB[i], 'ConfigTool' : True}

mtgCommandsDict['CDTestFramework'] = { 'exeName' : r'CDTestFramework', 'Dict' : cdTestFrameworkDict, 'ConfigTool' : False}
mtgCommandsDict['MISC_Commands']   = { 'exeName' : r'',                'Dict' : miscCommandsDict,    'ConfigTool' : False}
