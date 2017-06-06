from tkinter import *


def showCofdmDataRate ():
    rate = str ( CalculateCofdmDataRate ( Constellation.get (), CodeRate.get (), GuardInterval.get (), Bandwidth.get () ) )
    list_rate = list ( rate )
    if ( len ( list_rate ) > 6 ):
        list_rate.insert ( -6, "," )
        list_rate.insert ( -3, "," )
    elif ( len ( rate ) > 3 ):
        list_rate.insert ( -3, "," )
    labelCofdmRate.config ( text = ''.join ( list_rate ) + " bps" )


def CalculateCofdmDataRate ( constellation, code_rate, guard_interval, bandwidth ):
    SYMBOL_QPSK_8MHZ = ( 12441177.50 / 8.0 )
    
    COFDM_CONSTELLATION_QPSK = 0
    COFDM_CONSTELLATION_16QAM = 1
    COFDM_CONSTELLATION_64QAM = 2
    
    COFDM_CODE_RATE_1_2 = 0
    COFDM_CODE_RATE_2_3 = 1
    COFDM_CODE_RATE_3_4 = 2
    COFDM_CODE_RATE_5_6 = 3
    COFDM_CODE_RATE_7_8 = 4
    
    COFDM_GUARD_INTERVAL_1_32 = 0
    COFDM_GUARD_INTERVAL_1_16 = 1
    COFDM_GUARD_INTERVAL_1_8 = 2
    COFDM_GUARD_INTERVAL_1_4 = 3
    
    # Calculate code rate
    if ( code_rate == COFDM_CODE_RATE_1_2 ):
        CR = 1.0 / 2.0
    elif ( code_rate == COFDM_CODE_RATE_2_3 ):
        CR = 2.0 / 3.0
    elif ( code_rate == COFDM_CODE_RATE_3_4 ):
        CR = 3.0 / 4.0
    elif ( code_rate == COFDM_CODE_RATE_5_6 ):
        CR = 5.0 / 6.0
    else:
        CR = 7.0 / 8.0

    # Calculate guard interval
    if ( guard_interval == COFDM_GUARD_INTERVAL_1_32 ):
        GI = 1.0 / 32.0
    elif ( guard_interval == COFDM_GUARD_INTERVAL_1_16 ):
        GI = 1.0 / 16.0
    elif ( guard_interval == COFDM_GUARD_INTERVAL_1_8 ):
        GI = 1.0 / 8.0
    else:
        GI = 1.0 / 4.0
        
    # Calculate Symbol under different constellation and bandwidth
    MOD  = 1.0
    MOD += constellation
    BW   = bandwidth / 8000.0
    data_rate  = SYMBOL_QPSK_8MHZ
    data_rate *= MOD
    data_rate *= BW

    # Calculate data rate under different Code Rate and Guard Interval
    data_rate *= ( CR / ( 1.0 + GI ) )
    data_rate  = ( data_rate + 0.5 ) * 8

    return (int)( data_rate )


def center_window ( width = 300, height = 200 ):
    # get screen width and height
    screen_width = mainWindow.winfo_screenwidth ()
    screen_height = mainWindow.winfo_screenheight ()

    # calculate position x and y coordinates
    x = ( screen_width  / 2 ) - ( width  / 2 )
    y = ( screen_height / 2 ) - ( height / 2 )
    mainWindow.geometry ( '%dx%d+%d+%d' % ( width, height, x, y ) )


# window
mainWindow = Tk ()

mainWindow.resizable ( width = False, height = False )
#mainWindow.geometry ( "720x140" )
center_window ( 720, 140 )
mainWindow.title ( "COFDM Rate Calculator" )
for i in range ( 1, 10 ):
    mainWindow.columnconfigure ( i, minsize = 60 )

# Constelllation
Constellation = IntVar ()
Constellation.set ( "0" )
labelConstellation = Label ( mainWindow, text = "Constellation:" )
labelConstellation.grid ( row = 0, sticky = E )
strConstellation = [ "QPSK", "16QAM", "64QAM" ]
for i in range ( 0, len ( strConstellation ) ):
    btnConstellation = Radiobutton ( mainWindow, text = strConstellation [ i ], variable = Constellation, value = i, command = showCofdmDataRate )
    btnConstellation.grid ( row = 0, column = i + 1, sticky = W )

# Code Rate
CodeRate = IntVar ()
CodeRate.set ( "0" )
labelCodeRate = Label ( mainWindow, text = "Code Rate:" )
labelCodeRate.grid ( row = 1, sticky = E )
strCodeRate = [ "1/2", "2/3", "3/4", "5/6", "7/8" ]
for i in range ( 0, len ( strCodeRate ) ):
    btnCodeRate = Radiobutton ( mainWindow, text = strCodeRate [ i ], variable = CodeRate, value = i, command = showCofdmDataRate )
    btnCodeRate.grid ( row = 1, column = i + 1, sticky = W )

# Guard Interval
GuardInterval = IntVar ()
GuardInterval.set ( "0" )
labelGuardInterval = Label ( mainWindow, text = "Guard Interval:" )
labelGuardInterval.grid ( row = 2, sticky = E )
strGuardInterval = [ "1/32", "1/16", "1/8", "1/4" ]
for i in range ( 0, len ( strGuardInterval ) ):
    btnGuardInterval = Radiobutton ( mainWindow, text = strGuardInterval [ i ], variable = GuardInterval, value = i, command = showCofdmDataRate )
    btnGuardInterval.grid ( row = 2, column = i + 1, sticky = W )

# Bandwidth
Bandwidth = IntVar ()
Bandwidth.set ( 1250 )
labelBandwidth = Label ( mainWindow, text = "Bandwidth:" )
labelBandwidth.grid ( row = 3, sticky = E )
strBandwidth = [ "1.25MHz", "1.5MHz", "2MHz", "2.5MHz", "3MHz", "4MHz", "5MHz", "6MHz", "7MHz", "8MHz" ]
intBandwidth = [ 1250, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000 ] 
for i in range ( 0, len ( strBandwidth ) ):
    btnBandwidth = Radiobutton ( mainWindow, text = strBandwidth [ i ], variable = Bandwidth, value = intBandwidth [ i ], command = showCofdmDataRate )
    btnBandwidth.grid ( row = 3, column = i + 1, sticky = W )


# Data Rate
labelDataRate = Label ( mainWindow, text = "Data Rate:" )
labelDataRate.grid ( row = 5, sticky = E )
labelCofdmRate = Label ( mainWindow, text = "942,517 bps" )
labelCofdmRate.grid ( row = 5, column = 1, columnspan = 4 )
labelCofdmRate.config ( font = ( "Courier", 18 ) )

mainWindow.mainloop()
