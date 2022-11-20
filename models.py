from pydantic import BaseModel
from .database import Base
from sqlalchemy.sql.expression import null
from sqlalchemy import Column, String

class application_data(BaseModel):
    a_description: str
    a_ing_ci_monitored_by: str
    it_custodian_ck: str
    app_name: str
    itcustodian_name: str
    class_name: str
    app_id: str
    environment: str
    is_solution_descr: str
    server_name: str

class hierarchy_data(BaseModel):
    cn: str
    uid: str
    managers: str
    managers_id: str

class password_vault_requests(BaseModel):
    Time: str
    User: str
    Safe: str
    Action: str
    Server: str
    Request ID: str
    Reason: str
    Request number: str

class application_data(Base):
    __tablename__ = "application_data"
    a_description = Column(String, nullable = True)
    a_ing_ci_monitored_by = Column(String,  nullable = True)
    it_custodian_ck = Column(String,  nullable = False)
    app_name = Column(String,  nullable = False)
    itcustodian_name = Column(String, nullable = False)
    class_name = Column(String,  nullable = True)
    app_id = Column(String, nullable = False)
    environment = Column(String,  nullable = False)
    is_solution_descr = Column(String,  nullable = True)
    server_name = Column(String, primary_key = True, nullable = False)


