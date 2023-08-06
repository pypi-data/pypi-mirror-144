import logging

from tensorflow.keras.callbacks import Callback

from graphsignal.profilers.tensorflow import profile_span

logger = logging.getLogger('graphsignal')


class GraphsignalCallback(Callback):
    __slots__ = [
        '_span'
    ]

    def __init__(self):
        self._span = None

    def _start_profiler(self, span_name, batch=None):
        if not self._span:
            self._span = profile_span(span_name=span_name)
            if batch is not None:
                self._span.add_metadata('batch', batch)

    def _stop_profiler(self):
        if self._span:
            self._span.stop()
            self._span = None

    def on_predict_begin(self, logs=None):
        self._start_profiler('Prediction')

    def on_predict_end(self, logs=None):
        self._stop_profiler()

    def on_train_batch_begin(self, batch, logs=None):
        self._start_profiler('Training batch', batch=batch)

    def on_train_batch_end(self, batch, logs=None):
        self._stop_profiler()

    def on_test_batch_begin(self, batch, logs=None):
        self._start_profiler('Test batch', batch=batch)

    def on_test_batch_end(self, batch, logs=None):
        self._stop_profiler()

    def on_predict_batch_begin(self, batch, logs=None):
        self._start_profiler('Prediction batch', batch=batch)

    def on_predict_batch_end(self, batch, logs=None):
        self._stop_profiler()
