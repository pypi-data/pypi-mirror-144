import pandas as pd
import pathlib
from pathlib import Path
import glob
import os, shutil
import time
from google.cloud import storage


class FileRegistry:
    filelist = ()
    ex = []

    def __init__(self, kind, name, ftype='csv', rootpath='', path=''):
        self.name = name
        
        if rootpath == '':
            self.rootpath = '/Volumes/GoogleDrive/My Drive/__Data/'
        else:
            self.rootpath = rootpath

        if kind == 'options':
            self.path = self.rootpath + 'Xignite/Options/' + path + '/'
        elif kind == 'options_main':
            self.path = self.rootpath + 'Xignite/OptionsMain/' + path + '/'
        elif kind == 'daily_price':
            self.path = self.rootpath + 'Xignite/DailyPrice/' + path + '/'
        elif kind == 'price_file_list':
            self.path = self.rootpath + 'Xignite/PriceFileList/' + path + '/'
        elif kind == 'xlsx':
            self.path = self.rootpath + 'Analysis/' + path + '/'
        elif kind == 'trades':
            self.path = self.rootpath + 'Analysis/' + path + '/'
        elif kind == 'graphs':
            self.path = self.rootpath + 'Analysis/' + kind + '/' + path + '/'
        elif kind == 'historic':
            self.path = self.rootpath + '__Premind/6. Product-Tech/14. FraudArb/HistoricData' + path + '/'
        elif kind == 'historic_ticker':
            self.path = self.rootpath + '__Premind/6. Product-Tech/14. FraudArb/Articles' + path + '/'
        elif kind == 'ticker':
            self.path = self.rootpath + '__Python/Premind_Light/Analytics/Analytics_Cloud/Analytics_Docker/data/FraudArb/Tickers' + path + '/'
        elif kind == 'TradingDates':
            self.path = self.rootpath + 'Core/' + kind + path + '/'
        elif kind == 'wordanalysis':
            self.path = self.rootpath + kind + path + '/'
        elif kind == 'Master':
            self.path = self.rootpath + 'Core/' + kind + path + '/'
        elif kind == 'Profile':
            self.path = self.rootpath + 'Core/' + kind + path + '/'
        elif kind == 'ISIN':
            self.path = self.rootpath + 'Core/' + kind + path + '/'
        elif kind == 'predictions':
            self.path = self.rootpath + 'live_testing/' + path + '/'
        elif kind == 'dashboard':
            self.path = self.rootpath + 'dashboard/' + path + '/'
        elif kind == 'generic':
            self.path = self.rootpath + path
        
        if ftype == "":
            self.fullpath = self.path + name
        else:
            self.fullpath = self.path + name + '.' + ftype

        flist = list(self.filelist)
        flist.append(self.name)
        self.filelist = tuple(flist)

    def file_exists(self):
        return Path(self.fullpath).is_file()

    def move_rename(self):
        downloads = '/Users/burakozkan/downloads/'
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)
        time.sleep(2)
        list_of_files = glob.glob(downloads + '/*.csv')  # * means all if need specific format then *.csv
        filename = max(list_of_files, key=os.path.getctime)
        shutil.move(os.path.join(downloads, filename), os.path.join(self.path, self.name))

    def just_move(self):
        new_path = '/Users/burakozkan/MarketData/xdaily'
        shutil.move(os.path.join(self.path, self.name), os.path.join(new_path, self.name))

    def get_data(self):
        if 'EURO' in self.name and 'static_data' in self.path:
            df = pd.read_csv(self.fullpath, sep=';', parse_dates=True, skiprows=[1, 2, 3])
            df = df.rename(columns={'Name': 'Name1', 'Symbol': 'Symbol1'})
            df.insert(1, 'Symbol', df['Symbol1'])
            df.insert(0, 'Name', df['Name1'])
            return df
        return pd.read_csv(self.fullpath, parse_dates=True)

    def export_data(self, data_list, append=False):
        if append and self.file_exists():
            pd.read_csv(self.fullpath).append(data_list).to_csv(self.fullpath, encoding='utf-8', index=False)
        else:
            pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)
            data_list.to_csv(self.fullpath, encoding='utf-8', index=False)

    def export_data_indexed(self, data_list):
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)
        data_list.to_csv(self.fullpath, encoding='utf-8', index=True)

    def is_file_empty(self):
        """ Check if file is empty by reading first character in it"""
        # open ile in read mode
        with open(self.fullpath, 'r') as read_obj:
            # read first character
            one_char = read_obj.read(1)
            # if not fetched then file is empty
            if not one_char:
                return True
        return False

    def get_iex_data(self):
        return pd.read_csv(self.fullpath, lineterminator='\n', quotechar='"', parse_dates=True)