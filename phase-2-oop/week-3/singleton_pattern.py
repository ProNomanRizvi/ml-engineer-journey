class ConfigManager:
    _instance = None  # class-level attribute — instance nahi

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
# Task

class ConfigManagers:
    instance = None
    
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
   
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.config = {}
            self._initialized = True

if __name__ == "__main__":
    a = ConfigManagers()
    a.config["model"] = "ResNet50"  
    b = ConfigManagers()             
    print(b.config)                 # "ResNet50" 
    print(id(a) == id(b))          # True