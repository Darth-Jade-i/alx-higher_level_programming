#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Create database engine
        engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost/{database_name}",
            pool_pre_ping=True)

        # Create tables based on defined models
        Base.metadata.create_all(engine)

        print("Tables created successfully.")

    except SQLAlchemyError as e:
        print(f"Error creating tables: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
