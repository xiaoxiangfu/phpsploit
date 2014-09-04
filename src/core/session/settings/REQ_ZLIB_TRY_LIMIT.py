import objects
import datatypes


class REQ_ZLIB_TRY_LIMIT:
    """
    This setting adjusts from what payload size
    the zlib compression feature is disabled.

    The framework requests engine looks for the best
    way to spread the payload with a minimum of http
    requests when payloads are large.
    Therefore, the compression feature is exponentially
    cpu greedy, so it is a good practice to set
    the limit according to the cpu capacity of your
    machine.
    """
    type = objects.settings.RandLineBuffer

    def setter(self, value):
        value = datatypes.ByteSize(value)
        if value < 1:
            raise ValueError("must be a positive bytes number")
        return value

    def default_value(self):
        raw_value = "20 MiB"
        return self.setter(raw_value)