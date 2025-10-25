import pytest
from backend.api.services.query_engine import QueryEngine
from backend.api.services.schema_discovery import SchemaDiscoveryService

def test_query_analysis():
    """Test query type analysis"""
    # Mock schema
    schema_info = {
        "tables": [
            {
                "name": "employees",
                "columns": [
                    {"name": "id", "type": "INTEGER", "nullable": False},
                    {"name": "name", "type": "VARCHAR", "nullable": False}
                ],
                "foreign_keys": []
            }
        ],
        "relationships": []
    }
    
    schema_service = SchemaDiscoveryService(schema_info)
    query_engine = QueryEngine(schema_service)
    
    # Test query type detection
    assert query_engine._analyze_query_type("count all employees") == "structured"
    assert query_engine._analyze_query_type("what is employee handbook?") == "document"

if __name__ == "__main__":
    pytest.main([__file__])
