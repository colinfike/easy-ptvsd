"""
Easy PTVSD Module.

Contains any decorators or convenience functions for PTVSD.
"""
import ptvsd


class wait_and_break:
    """
    Decorator to create ptvsd server, wait for attach, break into debugger, continue.

    This pattern of using a class to make a decorator cleans up the double nested
    functions needed to create a decorator that accepts arguments. Maybe a little hacky
    but I believe this definitely follows the zen of python more than a double nested
    decorator function.

    Essentially, when the decorator is evaluated it returns a new wait_and_break object
    that will be invoked with the decorated function as an argument and return the new
    wrapped function.
    """

    DEFAULT_SECRET = "my_secret"
    DEFAULT_ADDRESS = ("0.0.0.0", 3000)

    def __init__(self, secret=DEFAULT_SECRET, address=DEFAULT_ADDRESS):
        """Set default secret and address."""
        self.secret = secret
        self.address = address

    def __call__(self, function):
        """Run ptvsd code and continue with decorated function."""
        def wait_and_break_deco(*args, **kwargs):
            ptvsd.enable_attach(self.secret, address=self.address)
            ptvsd.wait_for_attach()
            ptvsd.break_into_debugger()
            function(*args, **kwargs)
        return wait_and_break_deco
