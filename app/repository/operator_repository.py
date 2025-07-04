from typing import List, Optional
from app.models.operator import Operator
from app.db.mssql import get_connection

def create_operator(data) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO operators (user_id, branch_id, role, is_active)
        VALUES (?, ?, ?, ?)
    """, (data.user_id, data.branch_id, data.role, data.is_active))
    conn.commit()
    operator_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return operator_id

def get_all_operators() -> List[Operator]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, user_id, branch_id, role, is_active FROM operators")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [Operator(*row) for row in rows]

def get_operator_by_id(operator_id: int) -> Optional[Operator]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, user_id, branch_id, role, is_active FROM operators WHERE id = ?", (operator_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return Operator(*row) if row else None

def update_operator(operator: Operator) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE operators SET user_id=?, branch_id=?, role=?, is_active=? WHERE id=?
    """, (operator.user_id, operator.branch_id, operator.role, operator.is_active, operator.id))
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()
    return affected > 0

def delete_operator(operator_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM operators WHERE id = ?", (operator_id,))
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()
    return affected > 0
