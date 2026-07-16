"""
    Case study:Food delivery application
    Imagine your developing a food delivery system
    The application can run in three environment
    Development
    Testing
    production
"""
#Define configuration classes
class DevConfig:
    database="sqlite.db"
    debug=True
class TestConfig:
    database="test.db"
    debug=True
class ProdConfig:
    database="mysql://food_app"
    debug=False

#Step2: Define a Configuration factory(callable)
def get_config(environment):
    if environment == "dev":
        return DevConfig()
    elif environment =="test":
        return TestConfig()
    else:
        return ProdConfig()
    
#Step3: Use the factory
env="dev"
config=get_config(env)

print(config.database)
print(config.debug)