from threading import Thread

class ClientException(Exception):
    
    """Exception thrown when a method passed by the caller fails internally."""


def setup(**args):
    Thread(target=_setup, args=[args]).start()

def _setup(args):

    """ This function takes care of the module setup synchronously. Its arguments are:

        * `testImports`: function taking no parameters. Returns True if the environment is deemed adequate, else returns False.
        * `installList`: a list of tuples of the forḿ (`pip module as a string`, [`module names to import`])
        * `onSuccess`: callback when the modules are successfully loaded and installed. It is guaranteed that the environment has been cleared by `testImports`.
        * `onFail`: error callback. Gets an exception as a parameter."""

    # testImports, installList, onSuccess, onFail

    isOK = False

    try:

        isOK = args["testImports"]

    except Exception as e: # onFailed acts as an error handler.
        
        args["onFailed"](e)

    if not isOK:

        pass # The main part of this sorcery

    try:

        isOK = args["testImports"]()

    except Exception as e: # onFailed acts as an error handler

        args["onFailed"](e)

    if not isOK:

        args["onFailed"](ImportError("Couldn't import the required modules."))

    else:

        args["onSuccess"]()
