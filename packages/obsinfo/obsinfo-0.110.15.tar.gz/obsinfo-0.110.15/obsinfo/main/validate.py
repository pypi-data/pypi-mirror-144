#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
     Main functions for obsinfo-validate. 
     
     obsinfo strongly follows the hierarchy of StationXML files.
       
     Module contains both class ValidateObsinfo and a main entry point for obsinfo-validate
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA @UnusedWildImport

import os
from pathlib import Path, PurePath
import glob
import inspect
import difflib
import re
import sys
from json.decoder import JSONDecodeError
from argparse import ArgumentParser
from ..misc.configuration import ObsinfoConfiguration

import logging
from logging.handlers import RotatingFileHandler


#Third party imports
from obspy.core.utcdatetime import UTCDateTime

# obsinfo imports
from obsinfo.obsMetadata.obsmetadata import (ObsMetadata)
from obsinfo.instrumentation import (Instrumentation, InstrumentComponent,
                                     Datalogger, Preamplifier, Sensor,
                                     ResponseStages, Stage, Filter, Location)
from obsinfo.network import (Station, Network)
from obsinfo.instrumentation.filter import (Filter, PolesZeros, FIR, Coefficients, ResponseList,
                     Analog, Digital, AD_Conversion)
from obsinfo.misc.printobs import  (PrintObs)
from obsinfo.misc.discoveryfiles import Datapath
import obsinfo 
from obsinfo.obsMetadata.obsmetadata import ObsMetadata
from obsinfo.misc.discoveryfiles import Datapath
from obsinfo.misc.const import *


class ValidateObsinfo():
    """
    Contains methods to validate each level of information files.
    
    Attributes:
        datapath (:class:`/.Datapath`): Store datapath list(s)
        verbose (bool): Prints progress messages
        remote (bool): Indicates file in command line argument is to be found
            using datapath 
        debug (bool): Print more detailed messages. 
    """
    
    def setUp(self, verbose=True, remote=False, debug=False):
        """
        Sets up status variables according to .obsinforc and command line arguments.
        
        Args:
            verbose (bool): Print several progress messages
            remote (bool): Find file in command line argument using datapath
            debug (bool): Print more detailed messages and enable traceback
                of exceptions
        Returns: self
        """
        dp = Datapath()
        self.datapath = dp
        self.datapath.infofiles_path = dp.datapath_list 
        self.datapath.validate_path = Path(obsinfo.__file__).parent.joinpath('data', 'schemas')
    
        self.verbose = verbose
        self.remote = remote
        self.debug = debug
        
        return self

    def assertTextFilesEqual(self, first, second, msg=None):
        """
        Compares two text files
        
        :param first: First file to compare
        :type first: str
        :param second: Second file to compare
        :type second: str
        :param msg: Message to print in case of failure
        :type msg: str
        """
        with open(first) as f:
            str_a = f.read()
        with open(second) as f:
            str_b = f.read()
        if str_a != str_b:
            first_lines = str_a.splitlines(True)
            second_lines = str_b.splitlines(True)
            delta = difflib.unified_diff(
                first_lines, second_lines,
                fromfile=first, tofile=second)
            message = ''.join(delta)
            if msg:
                message += " : " + msg
            self.fail("Multi-line strings are unequal:\n" + message)
        
    def validate_all_filters(self):
        """
         Validate all information files in <component>/responses/_filters" subdirectory, as given by datapath.

         If you wish to test individual files, use test_filter(file) with file an absolute or 
         relative file name.
        """
        for dir in self.datapath.infofiles_path:
            files_in_validate_dir = Path(dir).joinpath(
                "*rs", # includes sensors, preamplifiers and dataloggers
                "responses",
                "filters/*.yaml")
            
            filelist = glob.glob(str(files_in_validate_dir))
            for file in filelist:
                self.validate_filter(file)
        
    def validate_filters_in_directory(self, dir):
        """
        Validate all information files in filter directory.
        
        :param dir: directory where filter files reside 
        :type dir: str
        """
        if dir.is_dir():
            for file in dir.iterdir():
                self.validate_filter(file)     

    def validate_filter(self, info_file):
        """
        Validate a single filter file.

        :param info_file: filter info file to validate. No assumptions made about path.
        :type info_file: str
        """
        ret = ObsMetadata().validate(self.datapath.validate_path, info_file,
                                     self.remote, "yaml", "filter",
                                     self.verbose, "filter", False)            
        if self.verbose: 
            self._print_passed(f'Filter test for: {info_file}', ret)      
        
    def validate_all_stages(self):
        """
        Validate all information files in each responses subdirectory "<component>/responses/_filters"
        
        If you wish to test individual files, use test_stage(file) with file an absolute or 
        relative file name.
        """
        for dir in self.datapath.infofiles_path:
            files_in_validate_dir = Path(dir).joinpath(
                "*rs", # includes sensors, preamplifiers and dataloggers
                "responses/*.yaml"
                )
            filelist = glob.glob(str(files_in_validate_dir))
            for file in filelist:
                self.validate_stage(file)
        
    def validate_stages_in_directory(self, dir):
        """
        Validate all information files in stage directory as given by datapath.
        
        :param dir: directory where stage files reside 
        :type dir: str
        """              
        datalogger_dir_re = re.compile(".*/dataloggers")
        sensor_dir_re = re.compile(".*/sensors")
        exception_re = re.compile(".*/test-with")
        if re.match(datalogger_dir_re, str(dir)) or re.match(sensor_dir_re, str(dir)):
            for file in (Path(dir).joinpath("responses")).iterdir():
                if not file.is_dir() and re.match(exception_re, str(file)) == None: 
                    self.validate_stage(file)        
        
    def validate_stage(self, info_file):
        """
        Validate a single stage file.

        :param info_file: stage info file to validate. No assumptions made about path.
        :type info_file: str
        """   
        ret = ObsMetadata().validate(self.datapath.validate_path,
                                     info_file, self.remote, "yaml", "stage",
                                     self.verbose, "stage", False)         
        if self.verbose: 
            self._print_passed(f'Stage validate for: {info_file}', ret)      
            
        
    def validate_all_components(self):
        """
        Validate all information files in each components (sensor, preamplifier, datalogger) subdirectory
        as given by datapath
        """
        components_list = ["sensors",
                           "preamplifiers",
                           "dataloggers"]
        for dir in self.datapath.infofiles_path:
            for comp in components_list:
                # includes sensors, preamplifiers and dataloggers
                files_in_validate_dir = Path(dir).joinpath(comp, "*.yaml")
                filelist = glob.glob(str(files_in_validate_dir))
                for file in filelist:
                    ret = ObsMetadata().validate(self.datapath.validate_path,
                                                 file, self.remote, "yaml",
                                                 comp, self.verbose, comp[:-1],
                                                 False)
                    if self.verbose: 
                        self._print_passed(file, ret)  

    def validate_datalogger(self, info_file):
        """
        Validate a single datalogger file.

        :param info_file: datalogger info file to validate. No assumptions made about path.
        :type info_file: str
        """
        # OJO: no configuraton passed from above. No delay_correction either.
        ret = ObsMetadata().validate(self.datapath.validate_path, info_file,
                                     self.remote, "yaml", "datalogger",
                                     self.verbose, "datalogger", False)
        if self.verbose: 
            self._print_passed(info_file, ret)  
           
    def validate_sensor(self, info_file):
        """
        Validate single sensor instrument_component information file
        
        :param info_file: sensor info file to validate. No assumptions made about path.
        :type info_file: str
        """
        #OJO: no configuraton passed from above. No delay_correction either.
        ret = ObsMetadata().validate(self.datapath.validate_path, info_file,
                                     self.remote, "yaml", "sensor",
                                     self.verbose, "sensor", False)
        if self.verbose: 
            self._print_passed(info_file, ret)  
        
    def validate_preamplifier(self, info_file):
        """
        Validate single preamplifier instrument_component information file
        
        :param info_file: preamplifier info file to validate. No assumptions made about path.
        :type info_file: str
        """
        #OJO: no configuraton passed from above. No delay_correction either.
        ret = ObsMetadata().validate(self.datapath.validate_path, info_file,
                                     self.remote, "yaml", "preamplifier",
                                     self.verbose, "preamplifier", False)
        if self.verbose: 
            self._print_passed(info_file, ret)  
           
    def validate_all_instrumentations(self):
        """
        Validate all information files for instrumentations in a directory given by datapath
        
        If you want to validate a single instrumentation file use validate_instrumentation.
        """
        
        for dir in self.datapath.infofiles_path:
            # includes sensors, preamplifiers and dataloggers
            files_in_validate_dir = Path(dir).joinpath("instrumentation/*.yaml")
            filelist = glob.glob(str(files_in_validate_dir))
            for file in filelist:
                self.validate_instrumentation(file)      

    def validate_instrumentation(self, info_file):
        """
        Validate single instrumentation information file
        
        :param info_file: instrumentation info file to validate. No assumptions
            made about path.
        :type info_file: str
        """
        ret = ObsMetadata().validate(self.datapath.validate_path, info_file,
                                     self.remote, "yaml", "instrumentation",
                                     self.verbose,
                                     "instrumentation.schema.json", False)
        if self.verbose: 
            self._print_passed(info_file, ret)  
       
    @staticmethod 
    def _print_passed(text, passed):
        if passed:   
            print(f'{text}: PASSED')
        else:   
            print(f'{text}: FAILED')
                     
    def validate_station(self, info_file='TEST.station.yaml', level="all"):
        """
        Validate single station information file
        
        :param info_file: station info file to validate. No assumptions made about path.
        :type info_file: str
        """
        ret = ObsMetadata().validate(self.datapath.validate_path, info_file,
                                     self.remote, "yaml", "station",
                                     self.verbose, "station.yaml.json", False)   
        if self.verbose: 
            self._print_passed(f'Station validate for: {info_file}', ret)  

    def validate_all_networks(self):
        """
        Validate all network information files in a directory.given by datapath
        """
        
        for dir in self.datapath.infofiles_path:
            # includes sensors, preamplifiers and dataloggers
            files_in_validate_dir = Path(dir).joinpath("network/*.yaml")
            filelist = glob.glob(str(files_in_validate_dir))
            for file in filelist:
                self.validate_network(file)

    def validate_network(self, info_file):
        """
        Validate single network information file
        
        :param info_file: network info file to validate. No assumptions made about path.
        :type info_file: str
        """
        ret = ObsMetadata().validate(self.datapath.validate_path, info_file, "yaml", "network", self.remote, self.verbose, "network", False)
        if self.verbose: 
            self._print_passed(f'Network validate for: {info_file}', ret)  

  
def main():
    """
    Entry point for obsinfo-validate. 
     
     1) Setups status variables from command line arguments.
     2) Validates file according to file type contained in name
     3) Manages all uncaught exceptions
    """
    args = retrieve_arguments()
    input_filename = args.input_filename
    logger = init_logging()
    
    val = ValidateObsinfo()
    val.setUp(verbose=args.verbose, remote=args.remote, debug=args.debug)
    
    if args.schema:
        if is_valid_type(args.schema):
            type = args.schema
        else:
            raise ValueError(f'Unknown schema type: {args.schema}')
    else:
        type = ObsMetadata.get_information_file_type(input_filename)
         
    if args.verbose:
        print(f'Validating {type} file')
            
#     try:               
    if type == "filter":
        val.validate_filter(input_filename)
    elif type == "stage":
        val.validate_stage(input_filename)
    elif type == "datalogger":
        val.validate_datalogger(input_filename)
    elif type == "preamplifier":
        val.validate_preamplifier(input_filename)
    elif type == "sensor":
        val.validate_sensor(input_filename)
    elif type == "instrumentation":
        val.validate_instrumentation(input_filename)
    elif type == "station":
        val.validate_station(input_filename)
    elif type == "network":
        val.validate_network(input_filename)
                       
#     except TypeError as e:
#         print("TypeError:" + str(e))
#         logger.error("TypeError: Illegal format: fields may be missing or with wrong format in input file, or there is a programming error")
#         if args.debug:
#             raise
#         sys.exit(EXIT_DATAERR)
#     except (KeyError, IndexError) as e:
#         print("Illegal value in dictionary key or list index:" + str(e))
#         logger.error("KeyError, IndexError: Illegal value in dictionary key or list index")
#         if args.debug:
#             raise
#         sys.exit(EXIT_SOFTWARE)
#     except ValueError as e:
#         print("ValueError:" + str(e))
#         logger.error("ValueError: An illegal value was detected")
#         if args.debug:
#             raise
#         sys.exit(EXIT_DATAERR)
#     except FileNotFoundError as e:
#         if args.debug:
#             raise
#         print("File not found:" + str(e))
#         logger.error(f"FileNotFoundError: {str(e)}")
#         sys.exit(EXIT_NOINPUT)
#     except JSONDecodeError as e:
#         print("JSONDecodeError:" + str(e))
#         logger.error("JSONDecodeError: File and/or subfiles have an illegal format. Probably indentation or missing quotes/parentheses/brackets")
#         if args.debug:
#             raise 
#         sys.exit(EXIT_DATAERR)
#     except (IOError, OSError, LookupError) as e:
#         print("File could not be opened or read:" + str(e))
#         logger.error("IOError, OSError, LookupError: File could not be opened or read")
#         if args.debug:
#             raise
#         sys.exit(EXIT_UNAVAILABLE)
#     except AttributeError as e:
#         print("Attribute error: " + str(e))
#         logger.debug("AttributeError: Programming error: an object in code had a wrong attribute")
#         if args.debug:
#             raise
#         sys.exit(EXIT_SOFTWARE)
#     except:
#         print("General exception")
#         logger.debug("General exception:")
#         if args.debug:
#             raise
#         sys.exit(EXIT_FAILURE)
#    
    sys.exit(EXIT_SUCCESS)
     

def retrieve_arguments():
    """
    Retrieve arguments from command line. Setup several status variables and get information file name
      
    :returns: dictionary object with all status variables and information file name.
    """
    # Parse the arguments
    parser_args = ArgumentParser(prog="obsinfo-validate")
    
    #flags
    parser_args.add_argument(
        "-q", "--quiet", action='store_true', default=False,
        help="Quiet operation. Don't print informative messages") 
    parser_args.add_argument(
        "-s", "--schema", help="Force validation against given schema") 
    parser_args.add_argument(
        "-r", "--remote",  action='store_true', default=False,
        help="Search input_filename in the DATAPATH repositories")
    parser_args.add_argument(
        "-d", "--debug",  action='store_true', default=False,
        help="Print traceback for exceptions")  
    # positional arguments
    parser_args.add_argument("input_filename", type=str,
                             help="Information file to be validated.")
    
    args = parser_args.parse_args()
    args.verbose = not args.quiet
    
    if not Path(args.input_filename).is_absolute():
        args.input_filename = str(Path(os.getcwd()).joinpath(args.input_filename).resolve())
             
    return args  


def init_logging():
    """
    Create or open a rotating logging file and add it to ObsinfoConfiguration
    
    :returns: object of Logger class 
    """
    logfile = Path.home().joinpath('.obsinfo', 'obsinfolog-validate')
    
    logger = logging.getLogger("obsinfo")
    
    logger.setLevel(logging.DEBUG)
    # add a rotating handler with 200K (approx) files and just two files
    handler = RotatingFileHandler(logfile, maxBytes=200000,
                                  backupCount=2)
    frmt = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(frmt)
    logger.addHandler(handler)  
    
    return logger 

    
if __name__ == '__main__':
    main()
