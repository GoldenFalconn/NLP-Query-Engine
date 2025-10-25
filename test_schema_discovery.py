import pytest
from backend.api.services.schema_discovery import SchemaDiscoveryService

def test_schema_discovery():
    """Test schema discovery service"""
    # Mock schema info
    schema_info = {
        "tables": [
            {
                "name": "employees",
                "columns": [
                    {"name": "id", "type": "INTEGER", "nullable": False},
                    {"name": "name", "type": "VARCHAR", "nullable": False},
                    {"name": "salary", "type": "DECIMAL", "nullable": True}
                ],
                "foreign_keys": []
            }
        ],
        "relationships": []
    }
    
    service = SchemaDiscoveryService(schema_info)
    
    # Test table finding
    table = service.find_table_by_context("employees")
    assert table == "employees"
    
    # Test column finding
    columns = service.find_columns_by_keywords(["salary"], "employees")
    assert len(columns) > 0

if __name__ == "__main__":
    pytest.main([__file__])
