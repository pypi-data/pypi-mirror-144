'''
This module contains several function which are used to initialize a certain experiment. 
Before using the functions in this module, an experiment() object needs to be created (typically by the main.pyw file), and a config file needs to be assigned to 
the experiment. After the experiment have been assigned a config file, the function set_up_experiment(exp) is called, where exp is the experiment() object.
'''
import PyQt5.QtWidgets as Qt# QApplication, QWidget, QMainWindow, QPushButton, QHBoxLayout
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import logging
import numpy as np
import importlib
from importlib.metadata import version  
import ergastirio.panels
import ergastirio.widgets
import ergastirio.utils

style1 = """{
            font: bold;
            border: 1px solid black;
            border-radius: 6px;
            margin-top: 6px;
        }
"""

style2 = """::title {
            subcontrol-origin: margin;
            left: 7px;
            padding: -4px 5px 0px 5px;
        }
        """

def setup(exp):
    if not set_up_experiment(exp):
        return False
    if not set_up_experiment_gui(exp):
        return False
    link_data_to_gui(exp)
    return True
  
def set_up_experiment(exp):
    '''
    This function initializes a certain experiment (passed as an input argument) based on the settings stored in the dictionary exp.config.
    It subsequently calls several functions to load instruments, initialize storage arrays, validate user configs
    '''

    if not load_general_settings(exp):
        return False
        
    if not load_instruments(exp):       #Load all instruments based on the strings specified in the list exp.config['Instruments']
        return False

    if not generate_data_headers(exp):  #Based on the loaded instruments, and on the data created by each instrument, it populates the list of strings exp.data_headers
        return False

    if not load_and_check_postprocessed_data(exp):
        return False

    initialize_storage_variable(exp)    #Create Storage variables
    initialize_temporary_variable(exp)
       
    if not validate_plots_settings(exp): #check if the plots settings specified in the .json file are valid (i.e. any quantity defined in 'x' and 'y' is a valid device data
        return False
    return True


def set_up_experiment_gui(exp):
    '''
    This function initializes the GUI of an experiment (passed as an input argument). It must be called after calling the function set_up_experiment()
    '''
    create_gui_table_data(exp,exp.parent.containers['tabledata']['container'])
    create_gui_plots(exp,exp.parent.containers['plots']['scrollarea'])
    if not create_gui_instruments(exp,exp.parent.containers['instruments']['container']): #Create GUIs for all loaded instruments 
        return False
    #
    if 'DefaultView' in exp.config.keys():
        QtCore.QTimer.singleShot(1, lambda : exp.mainwindow.set_view(exp.config['DefaultView']))

        
    return True



def load_general_settings(exp):
    if 'General_Settings' in exp.config.keys():
        exp.logger.info(f"Loading general settings...")
        if 'refresh_time_internal_trigger' in exp.config['General_Settings'].keys():
            exp.refresh_time_internal_trigger = exp.config['General_Settings']['refresh_time_internal_trigger']
        if 'refresh_time_multiple_acquisitions' in exp.config['General_Settings'].keys():
            exp.refresh_time_multiple_acquisitions = exp.config['General_Settings']['refresh_time_multiple_acquisitions']
        if 'average_acquisition' in exp.config['General_Settings'].keys():
            exp.average_acquisition = bool(exp.config['General_Settings']['average_acquisition'])
    #"continous_acquisition": 0,
    #"triggered_acquisition": 1,
    #"refresh_time_multiple_acquisitions": 0.2,
    #"average_acquisition": 1,
    #"trigger_delay": 0,
    #"trigger_instrument": "dev2_pyThorlabsPM100x"
    return True

def load_instruments(exp):
    ''' Loads all instruments defined in exp.config['Instruments'] and stores them in the list exp.instruments
        For each intruments, the respective interface object is also created, but not the gui.

        Returns true if all instruments were loaded correctly, false otherwise
    '''
    exp.logger.info(f"Loading all instruments specified in {exp.config_file}...")
    exp.instruments = []
    i=0
    for instrument in exp.config['Instruments']:
        IsValidPackage = importlib.util.find_spec(instrument) is not None
        if not(IsValidPackage):
            exp.logger.error(f"{instrument} is not a valid python package. Fix the error and restart this application")
            return False
        device_module =  importlib.import_module(instrument+'.main')
        if not(hasattr(device_module,'interface')):
            exp.logger.error(f"{instrument} is a valid package, but it does not contain an 'interface' class.")
            return False
        fullname = f"dev{i}_{instrument}"
        try:
            exp.instruments.append({'name':f"dev{i}",
                                        'fullname':fullname,
                                        'type':instrument,
                                        'interface_class':device_module.interface,
                                        'interface':  device_module.interface(  app=exp.app,
                                                                                mainwindow=exp.mainwindow,
                                                                                name_logger=fullname) #It might make more sense to create the interface objects in the load_instruments function instead
                                    }
                                    )
        except Exception as e:
            exp.logger.error(f"An error occurred while loading the instrument {instrument}: {e}")
            return False
        exp.logger.info(f"Instrument loaded: {exp.instruments[i]['name']} -> {exp.instruments[i]['type']}")
        i = i+1
    return True

def generate_data_headers(exp):
    ''' Generates a list of data headers for the experiment exp, based on the loaded instruments.
    For each instrument in exp.instruments, the list of output data is contained in the keys of the dictionary instrument.['interface_class'].output.
    The headers 'timestamp' and 'time' are also added at the beginning of the data headers.

    Returns True
    '''
    exp.logger.info(f"Preparing the data headers...")
    exp.data_headers =[]
    exp.data_headers.append('timestamp')
    exp.data_headers.append('time')
    for instrument in exp.instruments:
        if hasattr(instrument['interface_class'],'output'):
            for key in instrument['interface_class'].output.keys():
                exp.data_headers.append(instrument['name']+'.'+key)
        else:
            exp.logger.info(f"Instrument {instrument['fullname']} does not have an \'output\' dictionary defined. I wil assume that it does not produce data.")
    exp.logger.info(f"The following data will be acquired: {exp.data_headers}")
    return True

def load_and_check_postprocessed_data(exp):
    ''' Load the post-processed data defined in exp.config['PostProcessedData'] (if any is defined)
        and checks that each of them represents a valid formula.
        It apppen the name of each post-processed data to the list exp.data_headers.

        TO DO: check that no post-processed data has same name as another valid data.

        Returns true if all post-processed data are valid, false otherwhise.
    '''
    if ('PostProcessedData' in exp.config.keys()):
        exp.logger.info(f"Validating post-processed data...")
        for post_processed_data_name,post_processed_data in exp.config['PostProcessedData'].items():
            (msg,flag) = ergastirio.utils.check_list_is_valid_formula(post_processed_data,valid_variable_names=exp.data_headers)
            if not(flag==1):
                exp.logger.error(f"A problem occurred with the post-processed data: {msg}.")
                return False
            exp.data_headers.append(post_processed_data_name)

    return True
    

def initialize_storage_variable(exp):
    ''' Initialize all arrays for data storage. '''      
    exp.data = ergastirio.EnhancedList([]) #np.empty([0,len(exp.data_headers)]) 
    exp.data_std = ergastirio.EnhancedList([])
    return True
    
def initialize_temporary_variable(exp):
    ''' These variables will only be used as temporary arrays for averaging purposes. The number of columns in the storage matrices is given by the length of exp.data_headers. '''
    exp.numb_acq_to_average = 0 # This will contain the number of acquisitions to be averaged, chosen by the user
    exp.data_being_averaged = False #It's a flag which keeps track of whether data is being currently averaged
    exp.data_temp = np.empty([0,len(exp.data_headers)-2]) #The number of columns of expdata_temp is 2 less than the number of columns of exp.data
                                                                #because the first 2 columns of exp.data are for time and acquisition number
    return True

def validate_plots_settings(exp):
    '''
    This function looks at the content of exp.config['Plots'] and check that all settings specified by the user are valid
    '''
    exp.logger.info(f"Validating all plot settings...")
    exp.plots = []
    valid_data = exp.data_headers.copy()
    valid_data.append("acq#") #Need to implement this better
    for plotindex, plot in enumerate(exp.config['Plots']):
        if isinstance(plot,dict) and ('x' in plot.keys()) and ('y' in plot.keys()):
            if not plot['x'] in valid_data:
                exp.logger.error(f"Plot #{plotindex}: {plot['x']} is not a valid device data")
                return False
            if isinstance(plot['y'],str):
                plot['y'] = [plot['y']]
            for y_data in plot['y']:
                if not y_data in valid_data:
                    exp.logger.error(f"Plot #{plotindex}: {y_data} is not a valid device data")
                    return False            
        else:
            exp.logger.error(f"Each plot must be defined in the .json file as a dictionary containing an 'x' and a 'y' key.")
            return False
        exp.plots.append({'name':f"plot{plotindex}",
                            'x':plot['x'],
                            'y':plot['y']})
        exp.logger.info(f"Plot #{plotindex}, x = {plot['x']}, y = {plot['y']}")
    return True

def create_gui_logging(exp,container):
    '''
    Create GUIs for logger
    container
        QWidget which will contain the GUIs
    '''
    exp.logger.info(f"Creating GUI for logger...")
    box = Qt.QVBoxLayout()
    exp.logging_text_area = ergastirio.widgets.LoggerTextArea()
    exp.logging_text_area.add_logger(logger=logging.getLogger(exp.name_logger))
        
    box.addWidget(exp.logging_text_area)
    container.setLayout(box)

    return True

def create_gui_instruments(exp,container):
    '''
    Create GUIs for all loaded instruments, and for the acquisition control panel

    container
        QWidget which will contain the GUIs
    '''

    if ('Alignment_Instruments_Window' in exp.config.keys())  and exp.config['Alignment_Instruments_Window']=='H':
        box = Qt.QHBoxLayout()
    else: 
        box = Qt.QVBoxLayout()

    exp.logger.info(f"Creating GUI for all loaded instruments...")
    
    for i,instrument in enumerate(exp.instruments):
        exp.instruments[i]['frame'] = Qt.QGroupBox() # Qt.QWidget()
        exp.instruments[i]['frame'].setObjectName(exp.instruments[i]['name']+'_frame')
        string = "QGroupBox#"+ exp.instruments[i]['frame'].objectName()
        exp.instruments[i]['frame'].setStyleSheet(string + style1 + string + style2) #This line changes the style of ONLY this QWdiget

        exp.instruments[i]['frame'].setTitle(f"{exp.instruments[i]['name']} ({exp.instruments[i]['type']} v{version(exp.instruments[i]['type'])})")
        
        exp.logging_text_area.add_logger(logger=logging.getLogger(exp.instruments[i]['fullname'])) #Connect the logger of this instrument to the text area for logging in the GUI
        exp.instruments[i]['interface'].create_gui(parent=exp.instruments[i]['frame'])
        exp.instruments[i]['frame'].resize(exp.instruments[i]['frame'].sizeHint())
        box.addWidget(exp.instruments[i]['frame'] )
    box.addStretch(1)

    container.setLayout(box) #This line makes sure that all widgest defined so far are assigned to the widget defined in container
    exp.container_instruments = container
    exp.container_instruments.resize(exp.container_instruments.sizeHint())
    return True

def create_gui_plots(exp,container):
    '''
    Create GUIs for all plots

    container
        QWidget which will contain the GUIs
    '''
    exp.logger.info(f"Creating GUI for all plots...")

    container.mdi = Qt.QMdiArea()
    container.setWidget(container.mdi)
    for plotindex, plot in enumerate(exp.plots):
        exp.plots[plotindex]['subwindow'] = Qt.QMdiSubWindow()
        exp.plots[plotindex]['subwindow'].setWindowFlags(QtCore.Qt.FramelessWindowHint)
        exp.plots[plotindex]['subwindow'].setWindowTitle(exp.plots[plotindex]['name'])
        exp.plots[plotindex]['scrollarea'] = Qt.QScrollArea()
        exp.plots[plotindex]['widget'] = Qt.QWidget()
        exp.plots[plotindex]['subwindow'].setWidget(exp.plots[plotindex]['scrollarea'])
        exp.plots[plotindex]['scrollarea'].setWidget(exp.plots[plotindex]['widget'])
        exp.plots[plotindex]['scrollarea'].setWidgetResizable(True)
        container.mdi.addSubWindow(exp.plots[plotindex]['subwindow'])
        exp.plots[plotindex]['plotobject'] = ergastirio.widgets.PlotObject(exp.app, 
                                                                           exp.mainwindow, 
                                                                           exp.plots[plotindex]['widget'],
                                                                           data_headers = exp.data_headers,
                                                                           plot_config=exp.plots[plotindex])
        exp.plots[plotindex]['widget'].show()
    container.mdi.tileSubWindows()
    exp.container_plots = container
    return True

def create_gui_table_data(exp,container):
    '''
    Create GUIs for the table showing the currently stored data

    container
        QWidget which will contain the GUIs
    '''  
    exp.logger.info(f"Creating GUI for table...")

    layout = Qt.QVBoxLayout()

    ## CREATE ACQUISITION CONTROL PANEL
    exp.logger.info(f"Creating GUI for acquisition control panel...")
    exp.control_panel_container = Qt.QGroupBox() 
    exp.control_panel_container.setObjectName('acquisition_panel')
    string = 'QGroupBox#acquisition_panel'
    exp.control_panel_container.setStyleSheet(string + style1 + '\nQGroupBox' + style2) #This line changes the style of ONLY this QWdiget
    exp.control_panel_container.setTitle(f"Acquisition Panel")
    exp.control_panel = ergastirio.panels.acquisition_control(  exp.app,
                                                                exp.mainwindow,
                                                                exp.control_panel_container,
                                                                exp
                                                                )
    exp.control_panel.create_gui()
    ####

    ## CREATE DATA MANAGEMENT PANEL
    exp.data_management_panel_container = Qt.QGroupBox()
    exp.data_management_panel = ergastirio.panels.data_management(  exp.app,
                                                                    exp.mainwindow,
                                                                    exp.data_management_panel_container,
                                                                    exp)
    exp.data_management_panel.create_gui()
    exp.tabledata = ergastirio.widgets.Table()
    exp.tabledata.data_headers = exp.data_headers
    exp.tabledata.data = exp.data
    ####
    
    layout.addWidget(exp.control_panel_container)
    layout.addWidget(exp.data_management_panel_container)
    layout.addWidget(exp.tabledata,stretch=1)
    container.setLayout(layout)
    exp.container_tabledata = container
    return True

def link_data_to_gui(exp):
    '''
    The data collected in the experiment is stored in exp.data, which is an instance of the EnhancedList class.
    This is a 'dynamic' list, wich allows 'linked objects'. Whenever any data stored in an EnhancedList is changed, any linked
    object is notified, and a copy of the currently stored date is sent to the object.
    This is used as an elegant way to keep the table data and plots always syncronized with the stored data.
    To link an object, we use the method add_syncronized_objects defined in the EnhancedList class

    data.add_syncronized_objects([ InstanceOfTargetObject,  TargetClassProperty])

    Every time that the content of data is changed (e.g. a row is added to acquired data), the object data is also copied into
    the propery InstanceOfTargetObject.TargetClassProperty
    '''
    exp.data.add_syncronized_objects([  exp.tabledata,  ergastirio.widgets.Table.data])
    for plot in exp.plots:
        exp.data.add_syncronized_objects([  plot['plotobject'],  ergastirio.widgets.PlotObject.data])
