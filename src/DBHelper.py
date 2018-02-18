from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ProcessData import ProcessData


import sqlite3

class DBHelper(object):
    Base = declarative_base()
    engine = create_engine('sqlite:///TimeTrack.db')
    projects = []
    tasks = []
    
    database_name = 'TimeTrack.db'
    
    current_process_data = ProcessData()
    
    def initialize_helper(self):
        self.Base.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
    
    def fetch_projects(self):
        self.projects = self.session.query(Project).all()
        
    def fetch_tasks(self):
        self.tasks = self.session.query(ProjectTask).all()

    def fetch_tasks_by_project(self, pid):
        self.tasks = self.session.query(ProjectTask).filter_by(project_id=pid)
    
    def populate_process_data(self, last_inserted_process):
        self.current_process_data.process_id = last_inserted_process[0]
        self.current_process_data.task_id = last_inserted_process[1]
        self.current_process_data.project_id = last_inserted_process[2]
        self.current_process_data.start_time = last_inserted_process[3]
        self.current_process_data.end_time = last_inserted_process[4]
        self.current_process_data.duration = last_inserted_process[5]
        self.current_process_data.weekend_id = last_inserted_process[6]
        self.current_process_data.user_id = 1
        
    
    def create_process(self,tid,pid,stime,etime,dur, weekid):
        self.current_process = Process(task_id=tid, project_id=pid, start_time=stime,end_time=etime,duration=dur,week_id = weekid)
        self.populate_process_data(self, self.current_process)
        
        self.session.add(self.current_process)
        self.session.commit()
        
        return self.current_process_data
        
    def create_process_without_orm(self, task_id, project_id, start_time, end_time, duration, week_id):
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()
        new_process = (task_id,project_id, start_time, end_time, duration, week_id,)
        cur.execute("INSERT INTO process(task_id, project_id, start_time, end_time, duration, week_id) VALUES (?,?,?,?,?,?)", new_process)
        
        self.current_process_id = cur.lastrowid
        
        process_id = (self.current_process_id,)
        
        cur.execute("SELECT * FROM process WHERE id = ?", process_id)
        
        last_inserted_process = cur.fetchone()
        
        self.populate_process_data(self, last_inserted_process)
        
        conn.commit()
        conn.close()
        
        return self.current_process_data
        
    #Updates duration
    def update_process(self, cur_process_data):
        self.current_process.duration = cur_process_data.duration
        self.session.commit()
        
        self.populate_process_data(self, self.current_process)
        
        return self.current_process_data
    
    def update_process_without_orm(self, cur_process_data):
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()
        
        cur.execute("UPDATE process set duration = ? WHERE id = ?", (cur_process_data.duration, self.current_process_id))
        
        process_id = (self.current_process_id,)
        
        cur.execute("SELECT * FROM process WHERE id = ?", process_id)
        
        last_inserted_process = cur.fetchone()
        
        self.populate_process_data(self, last_inserted_process)
        
        conn.commit()
        conn.close()
        
        
        return self.current_process_data
        

    def stop_process(self, cur_process_data):
        self.current_process.duration = cur_process_data.duration
        self.current_process.end_time = cur_process_data.end_time
        self.session.commit()
        
        self.populate_process_data(self, self.current_process)
        
        return self.current_process_data

    def stop_process_without_orm(self, cur_process_data):
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()
        
        cur.execute("UPDATE process set duration = ?, end_time = ? WHERE id = ?", (cur_process_data.duration, cur_process_data.end_time, self.current_process_id))

        process_id = (self.current_process_id,)
        
        cur.execute("SELECT * FROM process WHERE id = ?", process_id)
        
        last_inserted_process = cur.fetchone()
        
        self.populate_process_data(self, last_inserted_process)

        
        conn.commit()
        conn.close()
        
        return self.current_process_data
        
            
    def current_week(self, date_today):
        self.current_calendar_week = self.session.query(Calendar_Week).filter(Calendar_Week.start_date <= date_today).filter(Calendar_Week.end_date >= date_today)[0]
        
        

class Process(DBHelper.Base):
    __tablename__ = "Process"
    
    id = Column('id', Integer, primary_key=True)
    task_id = Column('task_id', Integer)
    project_id = Column('project_id', Integer)
    start_time = Column('start_time',Integer)
    end_time = Column('end_time', Integer)
    duration = Column('duration', String)
    week_id = Column('week_id', Integer)
    


class Project(DBHelper.Base):
    __tablename__ = "Project"
    
    id = Column('id', Integer, primary_key=True)
    project_name = Column('name',String(250))
    


class ProjectTask(DBHelper.Base):
    __tablename__ = "ProjectTask"
    
    id = Column('id', Integer, primary_key=True)
    project_id = Column('project_id', Integer)
    task_description = Column('name', String(250))
    
    
class Calendar_Week(DBHelper.Base):
    __tablename__ = "Calendar_Week"
    
    id = Column('id', Integer, primary_key=True)
    calendar_week = Column('calendar_week', Integer)
    start_date = Column('start_date', Integer)
    end_date = Column('end_date',Integer)
    calendar_year = Column('calendar_year', Integer)
