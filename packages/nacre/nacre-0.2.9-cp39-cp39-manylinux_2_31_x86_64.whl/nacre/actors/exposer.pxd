from nautilus_trader.common.actor cimport Actor
from nautilus_trader.common.component cimport Component
from nautilus_trader.common.logging cimport LogColor
from nautilus_trader.common.logging cimport Logger
from nautilus_trader.common.logging cimport LoggerAdapter
from nautilus_trader.core.correctness cimport Condition
from nautilus_trader.model.data.base cimport GenericData
from nautilus_trader.model.data.tick cimport QuoteTick
from nautilus_trader.model.data.tick cimport TradeTick
from nautilus_trader.trading.trader cimport Trader

from nacre.metrics.metric_manager cimport MetricManager
from nacre.model.data.tick cimport MarkTick
from nacre.model.report_position cimport ReportedAccount


cdef class AccessLoggerAdapter(LoggerAdapter):
    cpdef void info(self, str msg, LogColor color=*, dict extra=*) except *

cdef class Exposer(Actor):
    cdef object _loop
    cdef object _runner
    cdef readonly MetricManager _metric_manager
    cdef readonly Trader trader
    """The trader back reference.\n\n:returns: `Trader`"""

    cdef object _run_http_server_task

    cpdef void register_trader(self, Trader trader) except *

    cpdef void update_generic_data(self, GenericData data) except *
    cpdef void update_quote_tick(self, QuoteTick tick) except *
    cpdef void update_trade_tick(self, TradeTick tick) except *
    cpdef void update_report_position(self, ReportedAccount account) except *
