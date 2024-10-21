__version__ = '0.0.5'

from tinydataflow.core import TinyDataFlow
from tinydataflow.connectors.selectors import CSVLineReader, TxtFileReader, FileSelector
from tinydataflow.transformers import ListToDictTransformer, LineWriter, EmailSender