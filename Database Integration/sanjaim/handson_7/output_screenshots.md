**Task 1: Set Up Alembic and Create a Baseline Migration**

```javascript
(venv) [sanjai@sanjai handson_7]$ alembic init migrations
  Creating directory /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/migrations ...  done
  Creating directory /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/migrations/versions ...  done
  Generating /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/migrations/script.py.mako ...  done
  Generating /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/alembic.ini ...  done
  Generating /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/migrations/env.py ...  done
  Generating /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/migrations/README ...  done
  Please edit configuration/connection/logging settings in /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/alembic.ini before proceeding.
(venv) [sanjai@sanjai handson_7]$ alembic revision --autogenerate -m "initial schema"
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.schemas
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.tables
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.types
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.constraints
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.defaults
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.comments
  Generating /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/migrations/versions/06c01391e4ef_initial_schema.py ...  done
(venv) [sanjai@sanjai handson_7]$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 06c01391e4ef, initial schema
(venv) [sanjai@sanjai handson_7]$
```

**Task 2: Add and Apply Incremental Migrations**

```javascript
(venv) [sanjai@sanjai handson_7]$ alembic revision --autogenerate -m 'add iis_active to students'
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.schemas
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.tables
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.types
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.constraints
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.defaults
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.comments
INFO  [alembic.autogenerate.compare.tables] Detected added column 'students.is_active'
  Generating /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/migrations/versions/0a7788ce2c93_add_iis_active_to_students.py ...  done
(venv) [sanjai@sanjai handson_7]$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 06c01391e4ef -> 0a7788ce2c93, add iis_active to students
(venv) [sanjai@sanjai handson_7]$ alembic revision --autogeneration -m 'added course model'
usage: alembic [-h] [--version] [-c CONFIG] [-n NAME] [-x X] [--raiseerr] [-q]
               {branches,check,current,downgrade,edit,ensure_version,heads,history,init,list_templates,merge,revision,show,stamp,upgrade} ...
alembic: error: unrecognized arguments: --autogeneration
(venv) [sanjai@sanjai handson_7]$ alembic revision --autogenerate -m 'added course model'
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.schemas
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.tables
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.types
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.constraints
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.defaults
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.comments
INFO  [alembic.autogenerate.compare.tables] Detected added table 'course_schedules'
  Generating /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/migrations/versions/296feb363211_added_course_model.py ...  done
(venv) [sanjai@sanjai handson_7]$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 0a7788ce2c93 -> 296feb363211, added course model
(venv) [sanjai@sanjai handson_7]$ alembic history --verbose
Rev: 296feb363211 (head)
Parent: 0a7788ce2c93
Path: /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/migrations/versions/296feb363211_added_course_model.py

    added course model

    Revision ID: 296feb363211
    Revises: 0a7788ce2c93
    Create Date: 2026-07-12 10:56:13.959991

Rev: 0a7788ce2c93
Parent: 06c01391e4ef
Path: /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/migrations/versions/0a7788ce2c93_add_iis_active_to_students.py

    add iis_active to students

    Revision ID: 0a7788ce2c93
    Revises: 06c01391e4ef
    Create Date: 2026-07-12 10:51:16.979456

Rev: 06c01391e4ef
Parent: <base>
Path: /home/sanjai/Desktop/cognizant/Database Integration/sanjaim/handson_7/migrations/versions/06c01391e4ef_initial_schema.py

    initial schema

    Revision ID: 06c01391e4ef
    Revises:
    Create Date: 2026-07-12 10:15:12.699704

(venv) [sanjai@sanjai handson_7]$
```

**Task 3: Rollback and Recovery**

```
(venv) [sanjai@sanjai handson_7]$ alembic current
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
296feb363211 (head)
(venv) [sanjai@sanjai handson_7]$ alembic downgrade -1
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running downgrade 296feb363211 -> 0a7788ce2c93, added course model
(venv) [sanjai@sanjai handson_7]$ alembic downgrade base
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running downgrade 0a7788ce2c93 -> 06c01391e4ef, add iis_active to students
INFO  [alembic.runtime.migration] Running downgrade 06c01391e4ef -> , initial schema
(venv) [sanjai@sanjai handson_7]$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 06c01391e4ef, initial schema
INFO  [alembic.runtime.migration] Running upgrade 06c01391e4ef -> 0a7788ce2c93, add iis_active to students
INFO  [alembic.runtime.migration] Running upgrade 0a7788ce2c93 -> 296feb363211, added course model
(venv) [sanjai@sanjai handson_7]$
```