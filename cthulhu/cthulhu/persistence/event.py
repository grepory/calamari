from sqlalchemy import Column, Integer, Text, DateTime
from cthulhu.persistence import Base


CRITICAL = 1
ERROR = 2
WARNING = 3
RECOVERY = 4
INFO = 5

SEVERITIES = {
    CRITICAL: "CRITICAL",
    ERROR: "ERROR",
    WARNING: "WARNING",
    RECOVERY: "RECOVERY",
    INFO: "INFO"
}


def severity_str(severity):
    return SEVERITIES[severity]


class Event(Base):
    """
    Events generated by the Cthulhu Eventer.
    """
    __tablename__ = 'cthulhu_event'

    id = Column(Integer, autoincrement=True, primary_key=True)

    # Time at which event was synthesized by Eventer
    when = Column(DateTime(timezone=True))

    severity = Column(Integer)

    # Human readable message
    message = Column(Text)

    # Optionally associated with a cluster
    fsid = Column(Text, nullable=True)
    # Optionally associated with a server
    fqdn = Column(Text, nullable=True)
    # Optionally associated with a service type ('osd', 'mon', 'mds') (FSID must be set)
    service_type = Column(Text, nullable=True)
    # Optionally associate with a particular service (service_type must be set)
    service_id = Column(Text, nullable=True)

    def __repr__(self):
        return "<Event %s @ %s>" % (self.id, self.when)
