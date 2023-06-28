import configparser
# from configparser import ConfigParser
config=configparser.RawConfigParser()
# config=ConfigParser()
config.read('/Users/chenchuenay/PycharmProjects/Nop-Commerce_realtime_Project/Configurations/config.ini')
print(config.sections())
print(config.get('common info','baseurl'))
class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        # url =config.get('common info','baseurl')
        url = config.get('common info','baseurl')
        return url
    
    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username
    
    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

        
        
        
  