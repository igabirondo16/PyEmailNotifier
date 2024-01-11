
import io
import sys

class StdoutCapturer(list):
    """
    Python class that is used for storing all the
    standard output in a variable.
    """

    def __init__(self):
        super().__init__()
        self._stdout = None
        self._stringio = None

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = io.StringIO()
        return self

    def __exit__(self,*args):
        self.append(self._stringio.getvalue())
        del self._stringio
        sys.stdout = self._stdout
