"""
This type stub file was generated by pyright.
"""

thread_local_data = ...
class Engine:
    """Wraps a SQLAlchemy engine.
    """
    def __init__(self, url) -> None:
        ...
    
    def get_transaction_connection(self): # -> Any | None:
        """
        :returns: A new connection with autocommit disabled (to be used for transactions).
        """
        ...
    
    def get_connection(self):
        """
        :returns: A new connection with autocommit enabled
        """
        ...
    
    def get_existing_transaction_connection(self): # -> Any | None:
        """
        :returns: The transaction connection bound to this Engine instance, if one exists, or None.
        """
        ...
    
    def close_transaction_connection(self): # -> None:
        """Closes the transaction connection bound to this Engine instance, if one exists and
        removes it.
        """
        ...
    
    def is_postgres(self): # -> bool:
        ...
    
    def __getattr__(self, attr): # -> Any:
        ...
    

