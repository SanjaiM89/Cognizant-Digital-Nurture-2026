```
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