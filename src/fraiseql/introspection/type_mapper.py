"""Type mapping utilities for AutoFraiseQL.
This module provides utilities to map PostgreSQL database types to Python types
for dynamic GraphQL type generation.
"""
from datetime import date, datetime
from decimal import Decimal
from typing import Any
from uuid import UUID

class TypeMapper:
    """Map PostgreSQL types to Python types."""

    # PostgreSQL -> Python type mapping
    PG_TO_PYTHON = {
        "uuid": UUID,
        "text": str,
        "character varying": str,
        "varchar": str,
        "char": str,
        "integer": int,
        "int": int,
        "int4": int,
        "bigint": int,
        "int8": int,
        "smallint": int,
        "int2": int,
        "boolean": bool,
        "bool": bool,
        "timestamp with time zone": datetime,
        "timestamptz": datetime,
        "timestamp without time zone": datetime,
        "timestamp": datetime,
        "date": date,
        "json": dict,
        "jsonb": dict,
        "numeric": Decimal,
        "decimal": Decimal,
        "real": float,
        "double precision": float,
        "float4": float,
        "float8": float,
    }

    def map_type(self, pg_type: str) -> Any:
        """Map a PostgreSQL type string to a Python type."""
        # Handle array types
        is_array = False
        if pg_type.startswith("_"):
            is_array = True
            base_type = pg_type[1:]
        elif pg_type.endswith("[]"):
            is_array = True
            base_type = pg_type[:-2]
        else:
            base_type = pg_type

        # Clean base type (remove length specifications like varchar(255))
        if "(" in base_type:
            base_type = base_type.split("(")[0].strip()

        python_type = self.PG_TO_PYTHON.get(base_type.lower(), Any)

        if is_array:
            return list[python_type]

        return python_type
